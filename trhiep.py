import subprocess
import time

def start_bot(file_name):
    return subprocess.Popen(['python', file_name])

def monitor_bots(bots):
    while True:
        for name, process in bots.items():
            retcode = process.poll()
            if retcode is not None:
                current_time = time.strftime("%Y-%m-%d %H:%M:%S")
                print(f"\u001b[38;2;255;101;101m\n{name} đã dừng với mã thoát {retcode}.\nĐang khởi động lại...")
                bots[name] = start_bot(name)
                print(f'\n{current_time}\n')
                print(f"\u001b[38;2;134;182;245m🤡🤡{name} đã được khởi động lại🤡🤡\n")
        time.sleep(5)

if __name__ == "__main__":
    bots = {
        'freedasua.py': start_bot('freedasua.py'),
        #"tbao_nv_va_buff.py": start_bot("tbao_nv_va_buff.py")
    }
    monitor_bots(bots)
