import os
import sys
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)
import shutil
from tkinter import *
file='C:\Windows\System32\drivers\etc\hosts'
suc=''
def end():
    bye.destroy()
def reboot():
    os.system("shutdown -r -t 1")
def block():
    shutil.copy(file, "host.txt")
    f = open(file, 'a')
    text="\n127.0.0.1 "+url.get()
    f.write(text)
    f.close()
    window.destroy()
    global suc
    suc='y'
def release():
    f = open("host.txt", 'r')
    s = f.read()
    f.close()
    f = open(file, 'w')
    f.write(s)
    f.close()
    window.destroy()
    global suc
    suc='n'
window=Tk()
window.title('block_site')
window.geometry("640x400+100+100")
label=Label(window, text="특정 사이트 접속 차단 프로그램입니다. 차단을 원하는 사이트의 주소를 입력해주세요.")
label.pack()
url=Entry(window)
url.pack()
block=Button(window, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100, text="차단", command=block)
block.pack()
release=Button(window, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100, text="해제", command=release)
release.pack()
window.mainloop()
if suc=='y':
    bye=Tk()
    bye.geometry("320x200+100+100")
    bye.title('block_site')
    message=Label(bye, text="재부팅이 필요합니다. 지금 다시 시작하시겠습니까?")
    message.pack()
    yes = Button(bye, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100, text="예", command=reboot)
    yes.pack()
    no = Button(bye, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100, text="아니오", command=end)
    no.pack()
    bye.mainloop()
if suc=='n':
    bye=Tk()
    bye.geometry("320x200+100+100")
    bye.title('block_site')
    message=Label(bye, text="성공하였습니다!")
    message.pack()
    ok = Button(bye, overrelief="solid", width=15, repeatdelay=1000, repeatinterval=100, text="확인", command=end)
    ok.pack()
    bye.mainloop()
