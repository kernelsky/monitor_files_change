# coding=gbk
import hashlib
import os
import datetime

def GetFileMd5(filename):
    if not os.path.isfile(filename):
        return
    myhash = hashlib.md5()
    f = open(filename,'rb')
    while True:
        b = f.read(8096)
        if not b :
            break
        myhash.update(b)
    f.close()
    return myhash.hexdigest()

filepath = "D:\python\monitor_files\���Ŀ¼\B\�жȲ���20200514.docx"
# ����ļ���md5ֵ�Լ���¼����ʱ��
starttime = datetime.datetime.now()
print(GetFileMd5(filepath))
endtime = datetime.datetime.now()
print('����ʱ�䣺%ds'%((endtime-starttime).seconds))