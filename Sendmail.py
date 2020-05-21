# -- coding:UTF-8 --
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime
import hashlib
import os

def Sendmail(orgmail,filename,big_ver,sml_ver,file_path):
    fromaddr = 'xxxx@qq.com'
    password = 'xxxx'
    #orgmail = ['xxxx@qq.com']
    emaildate = datetime.datetime.now().strftime("%d/%m/%Y")
    if not os.path.isfile(file_path):
        return
    myhash = hashlib.md5()
    f = open(file_path, 'rb')
    while True:
        b = f.read(8096)
        if not b:
            break
        myhash.update(b)
    f.close()
    file_md5 = myhash.hexdigest()
    content = '%s\nDear Customer,\nThe following package has been uploaded to FTP server:ftp://ftp.cambricon.com. Please connect with FTP protocol.\n\nDecryption passcode will be sent to you in another mail with subject "You will need it for decryption"\nthe login ID and passcode are as below:\nID:%s\nPasscode:%s\n\nRelease Notes:\n1. XXX\n2. XXX\nFTP Location: %s\nPackage MD5: %s\nPackage Content:\nXXX\nXXX\nXXX\n\n\nCambricon, Inc.\nCopyright 2020. All Rights Reserved\n\nFor this product delivery, if you have any problems downloading the package,\nplease contact your Cambricon customer support contacts.\nThank you for choosing Cambricon.\nhttp://www.cambricon.com/ ' %(emaildate,big_ver,sml_ver,filename,file_md5)

    textApart = MIMEText(content)


    #TextFile = 'compare_ip.txt'
    #textApart = MIMEApplication(open(TextFile, 'rb').read())
    #textApart.add_header('Content-Disposition', 'attachment', filename=TextFile)


    m = MIMEMultipart()
    m.attach(textApart)
    m['Subject'] = 'Ftp server file was change , please check it ! .'
    try:
        server = smtplib.SMTP('smtp.qq.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, orgmail, m.as_string())
        pass
        print("email yes")
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误