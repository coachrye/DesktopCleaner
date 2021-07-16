from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    i = 1
    # def on_created(self, event):
    #     print(f"hey, {event.src_path} has been created!")

    # def on_deleted(self, event):
    #     print(f"what the f**k! Someone deleted {event.src_path}!")

    # # def on_modified(self, event):
    # #     print(f"hey buddy, {event.src_path} has been modified")

    # def on_moved(self, event):
    #     print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
    
    def on_modified(self, event):
        new_name = "new_file_" + str(self.i) + ".txt"
        for filename in os.listdir(folder_to_track):
            file_exists = os.path.isfile(folder_destination + "/" + new_name)
            while file_exists:
                self.i += 1
                new_name = "new_file_" + str(self.i) + ".txt"
                file_exists = os.path.isfile(folder_destination + "/" + new_name)
            
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + new_name
            os.rename(src, new_destination)

folder_to_track = "/Users/coachrye/Desktop/TrackMe"
folder_destination = "/Users/coachrye/Desktop/SendMe"
# "/Users/coachrye/Documents/_Desktop Cleanup"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

observer.start()

try:
    while True:
        print("Watching path.")
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
print("\n\n\nFinished observing path")