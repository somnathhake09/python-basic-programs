#process scanning
import psutil
import time

def scan_processes(lmit=5):
    process_list = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'cpu_percent','create_time']):
        try:
            i=proc.as_dict(attrs=['pid', 'name', 'cpu_percent','create_time'])
            i['create_time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(i['create_time']))
            process_list.append(i)

            if len(process_list) == lmit:
                break
        except Exception as e:
            print(f"Error occurred while processing process: {e}")
    return process_list