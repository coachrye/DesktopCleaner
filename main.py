from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        new_name = "new_file_" + str(self.i) + ".txt"
        print("111")
        for filename in os.listdir(folder_to_track):
            print("222")
            file_exists = os.path.isfile(folder_destination + "/" + new_name)
            while file_exists:
                print("333")
                self.i += 1
                new_name = "new_file_" + str(self.i) + ".txt"
                file_exists = os.path.isfile(folder_destination + "/" + new_name)
            
            print("444")
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + new_name
            os.rename(src, new_destination)

print("555")
folder_to_track = "/Users/coachrye/Desktop"
folder_destination = "/Users/coachrye/Documents/_Desktop Cleanup"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
