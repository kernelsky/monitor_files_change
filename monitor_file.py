#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import asyncio
import base64
import logging
import os
import shutil
import sys
import hashlib
from datetime import datetime
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import Sendmail

WATCH_PATH = 'D:\\python\\monitor_files\\监控目录\\'  # 监控目录


class FileMonitorHandler(FileSystemEventHandler):
    def __init__(self, **kwargs):
        super(FileMonitorHandler, self).__init__(**kwargs)
        # 监控目录 目录下面以device_id为目录存放各自的图片
        self._watch_path = WATCH_PATH

    # 重写文件改变函数，文件改变都会触发文件夹变化
    def on_modified(self, event):
        if not event.is_directory:  # 文件改变都会触发文件夹变化
            file_path = event.src_path
            print("文件改变: %s " % file_path)

    def on_created(self, event):
        if not event.is_directory:  # 文件改变都会触发文件夹变化
            file_path = str(event.src_path)
            file_name = file_path.replace(WATCH_PATH, "")
            file_name = file_name.replace(".html", "")
            print("文件改变: %s " % file_path)
            print("文件改变: %s " % file_name)
            org = file_path.split("\\")[4]
            ver = file_path.split("\\")[-1]

            self.org_mate(org,file_name,ver,file_path)

    def org_mate(self,org,file_name,ver,file_path):
        with open("D:\python\monitor_files\org.txt", mode='r', encoding='utf-8') as f:
            orglist = f.readlines()
        with open("D:\\python\\monitor_files\\version.txt", mode='r', encoding='utf-8') as g:
            verlist = g.readlines()
            #print(ftextlist)
            for org_list in orglist:
                org_list = org_list.split(" ")
                for ver_list in verlist:
                    ver_list = ver_list.split(" ")
                    print(org_list[0],org,ver_list[0],ver)
                    if org_list[0] == org and ver_list[0] == ver:
                        orgmail = org_list[2]
                        big_ver = ver_list[1]
                        sml_ver = ver_list[2]
                        Sendmail.Sendmail(orgmail,file_name,big_ver,sml_ver,file_path)
                        print(orgmail)
                        print(file_name)
                    else:
                        pass

if __name__ == "__main__":
    event_handler = FileMonitorHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_PATH, recursive=True)  # recursive递归的
    observer.start()
    observer.join()
