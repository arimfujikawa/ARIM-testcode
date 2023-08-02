import tkinter as tk
import tkinter.messagebox as messagebox

root = tk.Tk()
root.attributes('-topmost', True)
root.withdraw()
root.lift()
root.focus_force()
messagebox.showinfo('メッセージ', '処理が完了しました。')
# root.lift()