import sys
import time
import random
import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir  = "C:/Users/Luís Felipe"

class File_event_handler(FileSystemEventHandler):
    
    def on_created(self, event):
        print(f"olá, {event.src_path} foi criado")
        
    def on_deleted(self, event):
        print(f"opa, alguém excluiu {event.src_path}")
        
    def on_modified(self, event):
        print(f"olá, {event.src_path} foi modificado")
        
    def on_moved(self, event):
        print(f"alguém moveu {event.src_path} para {event.dest_path}")           
        
event_handler = File_event_handler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive = True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("executando")
except KeyboardInterrupt:
    print("interrompido")
    observer.stop()                 