from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

import os
import json
import time

# Update These Data
folder_to_track = "/Users/coachrye/Desktop/TrackMe"
folder_destination = "/Users/coachrye/Desktop/SendMe"
# "/Users/coachrye/Documents/_Desktop Cleanup"
sub_images = "/Images"
sub_others = "/Others"
sub_pdfles = "/PDFs"
sub_videos = "/Videos"

class MyHandler(FileSystemEventHandler):

    # def on_created(self, event):
    #     print(f"hey, {event.src_path} has been created!")

    # def on_deleted(self, event):
    #     print(f"what the f**k! Someone deleted {event.src_path}!")

    # # def on_modified(self, event):
    # #     print(f"hey buddy, {event.src_path} has been modified")

    # def on_moved(self, event):
    #     print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
    
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            new_name = filename
            # TODO: Check filetype and update folder_destination
            file_exists = os.path.isfile(folder_destination + "/" + new_name)
            while file_exists:
                # new_name = name-only + newname + extension-only
                new_name = os.path.splitext(filename)[0] + "-" + str(i) + os.path.splitext(filename)[1]
                file_exists = os.path.isfile(folder_destination + "/" + new_name)
                i += 1
            
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + new_name
            os.rename(src, new_destination)

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
