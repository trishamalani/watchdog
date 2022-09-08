from ast import While
import os
import shutil
import time
from  watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source="C:/Users/trish/Downloads"
destination="C:/Users/trish/Downloads"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovement(FileSystemEventHandler):
    def on_created(self,event):
        print(event)
        name,ext=os.path.splitext(event.src_path)
        time.sleep(1)
        for key,value in dir_tree.items():
            time.sleep(1)
            if ext in value :
                filename=os.path.basename(event.src_path)
                print("dowloaded "+filename)

                path1=source+"/"+filename
                path2=destination+"/"+key
                path3=destination+"/"+key+"/"+filename

                if os.path.exists(path2):
                    print("moving "+filename+"......")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                    print("making folder....")
                    os.makedirs(path2)
                    print("moving "+filename+"......")
                    shutil.move(path1,path3)
                    time.sleep(1)
                    




event=FileMovement()
observe=Observer()
observe.schedule(event,source,recursive=True)
observe.start()

try:
    while True :
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observe.stop()