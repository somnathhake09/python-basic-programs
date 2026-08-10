import os
import time
import psutil
import sys
import schedule
from email.message import EmailMessage
import smtplib

DEFALT_MAIL_SENDER ="random@example.com"
DEFALT_MAIL_PASSWORD =""
DEFALT_RECEIVER = "shmaratha@gmail.com"
def sendMail(logFilePath):
    sender = DEFALT_MAIL_SENDER
    password = DEFALT_MAIL_PASSWORD
    receiver = DEFALT_RECEIVER

    smtp_server = "smtp.gmail.com"
    smtp_port = "465"

    if not sender or not password or not receiver:
        print("Mail Config missing...")
        return False
    
    if not os.path.exists(logFilePath):
        print("unamble to send mail. log file not found!")
        return False
    
    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "System Surveillance Log Fil:%s"%time.strftime("%Y-%m-%d %H:%M:%S")
    msg.set_content("Please find the attached log file for system surveillance.")

    with open(logFilePath,"rb") as f:
        file_data = f.read()

    msg.add_attachment(
        file_data,
        maintype ="text",
        subtype ="plain",
        filename = os.path.basename(logFilePath)
    )    

    try:
        with smtplib.SMTP_SSL(smtp_server,smtp_port) as server:
            server.login(sender,password)
            server.send_message(msg)

        print("log file emaild successfully to :",sender) 
        return True
    except Exception as e:
        print("Failed to send email:")
        return False   

def createlog(FolderName):
    border = "-"*40
    Ret = False
    Ret = os.path.exists(FolderName)
    if(Ret):
        Ret = os.path.isdir(FolderName)
        if not Ret:
            print("unable to create Folder")
            return
        
    else:
        os.mkdir(FolderName)
        print("Folder created successfully")

    timestamp =time.strftime("%Y-%m-%d_%H-%M-%S")
    Filename = os.path.join(FolderName, "%s.log"%timestamp)
    print("Log File Created:",Filename)

    f =open(Filename,"w")
    f.write(border + "\n")  
    f.write("\t\tSystem Survillance Script\n")
    f.write("Log Created at :" + time.ctime()+"\n")
    f.write(border + "\n\n")

    f.write("--------------System Information----------------\n")
    
    f.write("CPU Usage:%s %%\n"%psutil.cpu_percent())
    f.write(border + "\n")
    
    mem = psutil.virtual_memory()
    f.write("Ram Usage:%s %%\n"%mem.percent)
    
    f.write("Disk usage Report:\n")

    f.write(border + "\n")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            f.write("%s -> %s %% \n"%(part.mountpoint,usage.percent))
        except:
            pass

    f.write(border + "\n")
    
    net = psutil.net_io_counters()
    f.write("\nNetwork Usage Report:\n")

    f.write("Sent : %.2f MB\n"%(net.bytes_sent / (1024*1024)))
    f.write("Recv : %.2f MB\n"%(net.bytes_recv / (1024*1024)))
    f.write(border+ "\n\n")

    #process Logging

    Data = processScan()
    for i in Data:
        f.write("PID : %s\n"%i.get("pid"))
        f.write("Name : %s\n"%i.get("name"))
        f.write("UserName : %s\n"%i.get("username"))
        f.write("Status : %s\n"%i.get("status"))
        f.write("Start Time : %s\n"%i.get("create_time"))
        f.write("CPU : %s\n"%i.get("cpu_percent"))
        f.write("Memory : %s\n"%i.get("memory_percent"))
        f.write(border + "\n")

    f.write(border + "\n")
    f.write("\t\tEnd of the log file")
    f.write(border + "\n")

    f.close()    

def processScan():
    listprocesses =[]

    #warm up for cpu percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.3)

    for proc in psutil.process_iter():
        try:
            i = proc.as_dict(attrs=["pid","name","username","status","create_time"])
            try:
                i["create_time"] =time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["create_time"]))
            except:
                i["create_time"] ="NA"

            i["cpu_percent"] = proc.cpu_percent(None)
            i["memory_percent"] = proc.memory_percent()

            listprocesses.append(i)

        except:
            pass  
    return listprocesses          
def main():
    border ="-"*40

    print(border)
    print("\tsystem surveillance")
    print(border)

    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("this  script is used to:")
            print("1. create Automatic logs")
            print("2. Executes Periodically")
            print("3. send mail with the log")
            print("4. store information about processes")
            print("5 :store information about CPU")
            print("6 :store information about Ram Usage")
            print("7 :store information about secondary Storage")

        elif (sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use The Automation Script as follows : ")
            print("scriptname.py TimeInterval LogDirectoryName")
            print("TimeIntrval : Time interval in minutes for perodic scheduling")
            print("LogDirectoryName : the directory name to create  auto logs")

        else:
            print("Invalid argument")
            print("Use --h or --H for help and --u or --U for usage")

    elif (len(sys.argv) == 3):
        schedule.every(float(sys.argv[1])).minutes.do(createlog,sys.argv[2])

        print("Platform Surveillance Script started successfully...")
        print("Directory Created with name :", sys.argv[2])
        print("Time interval in minutes :", sys.argv[1])
        print("press Ctrl + c to stop execution")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Unable to proceed as thre is no such options")
        print("Please use --h or --u to get more details")

    print(border)
    print("\t Thank you for using the Script")
    print(border)     

main()