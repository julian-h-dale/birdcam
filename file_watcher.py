from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Watcher:
    DIRECTORY_TO_WATCH = "./pics"

    def __init__(self):
        self.observer = Observer()
    
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("error")
        self.observer.join()
        
class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event): 
        if event.is_directory:
            print("directory event")
        elif event.event_type == 'created':
            print("file created " + event.src_path)
        elif event.event_type == 'modified':
            print("file modified " + event.src_path)

if __name__ == '__main__': 
    print("starting program")
    w = Watcher()
    w.run()