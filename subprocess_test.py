import time
import subprocess
from subprocess import PIPE
import numpy

# subprocessの入れ子はうまく動かない

def sub():
    time.sleep(3)
    print('ok')
    # process()
    print('done')

def process():
    proc = subprocess.run(['venv/Scripts/python', 'multiprocess_module_test.py'], stdout=PIPE, stderr=PIPE)
    print(proc.stdout.decode('utf-8').split('\r\n'))
    print(proc.stderr.decode('utf-8').split('\n'))
    out = proc.stdout.decode('utf-8').split('\r\n')
    print(f'{out}:{type(out)}')
    
if __name__ == '__main__':
    sub()