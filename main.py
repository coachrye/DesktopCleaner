from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

import os
import json
import time

FOLDER_TO_TRACK = "/Users/coachrye/Desktop/TrackMe"
FOLDER_DESTINATION = "/Users/coachrye/Desktop/SendMe"

# Update These Data
folder_to_track = FOLDER_TO_TRACK
folder_destination = FOLDER_DESTINATION

# "/Users/coachrye/Documents/_Desktop Cleanup"
sub_images = "/Images"
sub_dcmnts = "/Documents"
sub_videos = "/Videos"
sub_audios = "/Audios"
sub_others = "/Others"

class MyHandler(FileSystemEventHandler): 

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            new_name = filename
            # TODO: Check and process differently if it's a directory / folder. 
            # Check https://stackoverflow.com/questions/22207936/how-to-find-files-and-skip-directories-in-os-listdir
            
            # Check filetype and update folder_destination
            global folder_destination
            file_extension = os.path.splitext(filename)[1]

            if (file_extension == ".png") or (file_extension == ".jpg") or (file_extension == ".bmp"):
                folder_destination = folder_destination + sub_images
            elif (file_extension == ".txt") or (file_extension == ".pdf") or (file_extension == ".doc") or (file_extension == ".docx"):
                folder_destination = folder_destination + sub_dcmnts
            elif (file_extension == ".mp4") or (file_extension == ".mov") or (file_extension == ".mkv"):
                folder_destination = folder_destination + sub_videos
            elif (file_extension == ".mp3") or (file_extension == ".m4a"):
                folder_destination = folder_destination + sub_audios
            else:
                folder_destination = folder_destination + sub_others

            file_exists = os.path.isfile(folder_destination + "/" + new_name)
            while file_exists:
                # new_name = name-only + newname + extension-only
                new_name = os.path.splitext(filename)[0] + "-" + str(i) + file_extension
                file_exists = os.path.isfile(folder_destination + "/" + new_name)
                i += 1
            
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + new_name
            os.rename(src, new_destination)
            folder_destination = FOLDER_DESTINATION

    # def on_created(self, event):
    #     print(f"hey, {event.src_path} has been created!")

    # def on_deleted(self, event):
    #     print(f"what the f**k! Someone deleted {event.src_path}!")

    # # def on_modified(self, event):
    # #     print(f"hey buddy, {event.src_path} has been modified")

    # def on_moved(self, event):
    #     print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)

observer.start()

try:
    while True:
        print(f"Watching path: {folder_to_track}")
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()

observer.join()
print("\n\n\nFinished observing path")
