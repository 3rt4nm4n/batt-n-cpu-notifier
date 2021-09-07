import psutil
from win10toast import ToastNotifier
battery = psutil.sensors_battery()
cpu=psutil.cpu_percent()
percent = battery.percent
notify = ToastNotifier()
notify.show_toast("Remaining Battery Percentage and CPU Usage", "Battery: "+str(percent)+"\nCPU:"+str(cpu),icon_path=None,duration=10)
#show_toast(title,message,icon,duration)

