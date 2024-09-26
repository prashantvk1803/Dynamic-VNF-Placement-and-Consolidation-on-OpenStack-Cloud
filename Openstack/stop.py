import psutil
import os

def send_keyboard_interrupt(process_names):
    for process_name in process_names:
        for process in psutil.process_iter(['pid', 'name', 'cmdline']):
            if process_name in process.info['cmdline']:
                print(f"Sending SIGINT to process {process.info['pid']} ({process.info['name']})")
                try:
                    os.kill(process.info['pid'], 2) 
                except psutil.NoSuchProcess:
                    pass  

if __name__ == "__main__":
    # Replace 'datac1.py' and 'datac2.py' with your actual process names
    process_names_to_interrupt = ['python3', 'datac1.py', 'datac2.py']

    send_keyboard_interrupt(process_names_to_interrupt)