import tkinter as tk
import time
import threading
import math
import itertools
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

alive = False
started = threading.Event()
t = None

# When windows is closed.
def _destroy_window():
    global t
    global started
    global alive
    alive = False
    started.set()
    t.join()
    root.quit()
    root.destroy()

def stop():
    global started
    global alive
    alive = False
    print('Threading was stopped ')
    started.clear()

def start():
    global started
    global alive
    alive = True
    print('THreading starts')
    started.set()

# Tkinter Class
root = tk.Tk()
root.withdraw()
root.title('Waveform Animation')
root.protocol('WM_DELETE_WINDOW', _destroy_window)  # When you close the tkinter window.
button_start = tk.Button(text='START', command=start)
button_start.pack()
button_stop = tk.Button(text='STOP', command=stop)
button_stop.pack()
button_close = tk.Button(text='CLOSE', command=_destroy_window)
button_close.pack()

def _redraw(_, x, y):
    """グラフを再描画するための関数"""
    # 現在のグラフを消去する
    plt.cla()
    # 折れ線グラフを再描画する
    plt.ylim(-1.2, 1.2)
    plt.plot(x, y)

i = 100

def main():
    # 描画領域
    fig = plt.figure(figsize=(10, 6))
    # 描画するデータ (最初は空)
    x = [j for j in range(100)]
    y = [0.0] * 100

    def _update():
        """データを一定間隔で追加するスレッドの処理"""
        global i
        global started
        global alive
        started.wait()
        iterater_y = 0
        while alive:
#        for frame in itertools.count(0, 0.1):
            x.pop(0)
            x.append(i)
            i += 1
            # x.append(frame)
            y.pop(0)
            y.append(math.sin(iterater_y))
            iterater_y += 0.1
            # データを追加する間隔 (100ms)
            time.sleep(0.2)
            started.wait()

    def _init():
        """データを一定間隔で追加するためのスレッドを起動する"""
        global alive
        global t
        alive = True
        t = threading.Thread(target=_update)
        t.daemon = True
        t.start()

    params = {
        'fig': fig,
        'func': _redraw,  # グラフを更新する関数
        'init_func': _init,  # グラフ初期化用の関数 (今回はデータ更新用スレッドの起動)
        'fargs': (x, y),  # 関数の引数 (フレーム番号を除く)
        'interval': 200,  # グラフを更新する間隔 (ミリ秒)
    }
    anime = animation.FuncAnimation(**params)

# Canvas
    canvas = FigureCanvasTkAgg(fig, master=root)  # Generate canvas instance, Embedding fig in root
    canvas.draw()
    canvas.get_tk_widget().pack()

# root
    root.update()
    root.deiconify()
    root.mainloop()

main()

# if __name__ == '__main__':
#    main()