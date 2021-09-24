
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
#Installler librairie watchdog avec pip install 

import os
import time

class MyHandler(FileSystemEventHandler): 
    i = 1
    def on_modified(self, event):
        new_name = "Image" + str(self.i) + ".PNG"
        for filename in os.listdir(folder_to_track):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_exists = os.path.isfile(folder_destination + "/" + new_name)
                while file_exists:
                    self.i += 1
                    new_name = "Image" + str(self.i) + ".PNG"
                    file_exists = os.path.isfile(folder_destination + "/" + new_name)

            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + new_name
            os.rename(src, new_destination)

folder_to_track = "path/to/yourInitialFolder"
folder_destination = "path/to/your/Destination"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start() 


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
