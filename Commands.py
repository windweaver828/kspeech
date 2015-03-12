#!/usr/bin/env python

# Examples to help under the if name == main clause down below

import sys
from CommandsDict import CommandsDict

# ------------------------------------------------------- #
# Add functions to call here                              #

def helloworld():
	print("Hello, World!")


def helloname(name):
	print("Hello, {name}!".format(name=name))


def xdo(key):
    if 'keydown' in key:
        cmd = 'xdotool '+key
    else:
        cmd = "xdotool "+ send_key +" "+key
        os.popen(cmd)

def numToWords(num,join=True):
    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']
    thousands = ['','thousand','million','billion','trillion','quadrillion', \
                 'quintillion','sextillion','septillion','octillion', \
                 'nonillion','decillion','undecillion','duodecillion', \
                 'tredecillion','quattuordecillion','sexdecillion', \
                 'septendecillion','octodecillion','novemdecillion', \
                 'vigintillion']
    words = []
    if num==0: words.append('zero')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = (numStrLen+2)/3
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = groups-(i/3+1)
            if h>=1:
                words.append(units[h])
                words.append('hundred')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g]+',')
    if join: return ' '.join(words)
    return words

def dbusremote(server, var):
    cmd = "/home/pi/bin/dbuscontrol "
    if var == 'status':
        cmd += "status"
    elif var == 'stop':
        cmd += "stop"
    elif var == 'pause':
        cmd += "pause"
    elif var == 'seek':
        cmd += "seek"
    elif var == 'vol down':
        cmd += "volumedown"
    elif var == 'vol up':
        cmd += "volumeup"
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(server, port=22, username='pi', password='pi')
    except: print('Can not connect to : {server}').format(server=server)
    stdin, stdout, stderr = client.exec_command(cmd)
    a = (stdout.read().strip())
    duration = a.split(':')[1].split("\n")[0]
    position = a.split(':')[2].split("\n")[0]
    timecorrect(duration, position)

def timecorrect(dur, pos):
    duration = datetime.timedelta(microseconds = int(dur))
    position = datetime.timedelta(microseconds = int(pos))
    timeremaining = duration - position
    print("Duration:  "+str(duration)[0:7])
    print("Position:  "+str(position)[0:7])
    print("Remaining: "+str(timeremaining)[0:7])
    percent_remaining= int((float(pos)/float(dur))*100)
    print("Completed: "+str(percent_remaining)+"%")
    remain = str(timeremaining).split(':')
    hours = remain[0]
    mins = remain[1]
    cmd = "There, are, "+str(hours)+", hour, and, "+numToWords(int(mins))+"minutes, remaining!"
    speak_init()
    speak(cmd)
   
def execterminal(cmd):
    cmd = 'gnome-terminal -e "'+cmd+'"'
    os.popen(cmd)        

def internet(address):
    os.popen("google-chrome "+address)                 

def nemo(path):
    os.popen("nemo "+path)
    
def vnc(client):
    os.popen('vncviewer '+client+"Pi &")

def ssh(client):
    cmd = "/home/james/bin/ssh"+client
    execterminal(cmd)

def reboot():
    subprocess.Popen('python /home/james/bin/rboot', shell=True)

def binconfig():
    subprocess.Popen('python /home/james/bin/binconfig', shell=True)

def mousegrid():
    child = subprocess.Popen('python /home/james/bin/kmousegrid.py', shell=True)
                
def speak_init():
    os.popen('echo "aah" | festival --tts').readlines()

def speak(sentence):
    os.popen('echo , "'+sentence+'" | festival --tts')

def numpress(num):
    xdo(num)
    
def runProg(cmd):
    subprocess.Popen(cmd, shell=True)

commands = CommandsDict()
# ------------------------------------------------------- #
# Add command definitions here                            #

commdef = [['jayme'], ['status']]
func = dbusremote
args = ['jaymepi', 'status']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['ryann'], ['status']]
func = dbusremote
args = ['ryannpi', 'status']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['kill'],['voice']]
func = runProg
args = ['killall, kspeech']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['left'], ['click']]
func = xdo 
args = ['l']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['right'], ['click']]
func = xdo 
args = ['r']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['double'], ['click']]
func = xdo 
args = ['d']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['mouse']]
func = mousegrid
args = False
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['open', 'show'], ['terminal']]
func = xdo
args = ['keydown ctrl keydown alt key t keyup ctrl keyup alt']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['one']]
func = numpress
args = ['1']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['two']]
func = numpress
args = ['2']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['three']]
func = numpress
args = ['3']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['four']]
func = numpress
args = ['4']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['five']]
func = numpress
args = ['5']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['six']]
func = numpress
args = ['6']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['seven']]
func = numpress
args = ['7']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['eight']]
func = numpress
args = ['8']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['nine']]
func = numpress
args = ['9']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['vnc'], ['ryann']]
func = vnc
args = ['ryann']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['vnc'], ['jayme']]
func = vnc
args = ['jayme']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['new'], ['folder', 'directory']]
func = xdo
args = ['keydown', 'ctrl', 'keydown', 'shift', 'key', 'n', 'keyup', 'ctrl', 'keyup', 'shift']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['save']]
func = xdo
args = ['keydown', 'ctrl', 'key', 's', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['what'], ['time']]
func =  runProg
args = ['date', '+%I:%M%p', '|', 'festival', '--tts']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['cut'], ['selected', 'clip', 'text']]
func = xdo 
args = ['keydown', 'ctrl', 'key', 'x', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['send', 'move'], ['right'], ['monitor', 'screen']]
func = xdo
args = ['keydown', 'ctrl', 'keydown', 'shift', 'key', 'Right', 'keyup', 'ctrl', 'keyup', 'shift']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['send', 'move'], ['left'], ['monitor', 'screen']]
func = xdo
args = ['keydown', 'ctrl', 'keydown', 'shift', 'key', 'Left', 'keyup', 'ctrl', 'keyup', 'shift']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['left'], ['side']]
func = xdo
args = ['keydown', 'Super', 'key', 'Left', 'Keyup', 'Super']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['right'], ['side']]
func = xdo
args = ['keydown', 'Super', 'key', 'Right', 'keyup', 'Super']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['go'], ['right']]
func = xdo
args = ['key', 'Right']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['go'], ['left']]
func = xdo
args = ['key', 'Left']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['window'], ['bottom']]
func = xdo
args = ['keydown', 'Super', 'key', 'Down', 'keyup', 'Super']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['close'], ['window']]
func = xdo
args = ['keydown', 'alt', 'key', 'F4', 'keyup', 'alt']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['full'], ['screen']]
func = xdo
args = ['key', 'F11']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['open', 'show'], ['recycle', 'trash']]
func = xdo
args = ['keydown', 'ctrl', 'keydown', 'shift', 'key', 't', 'keyup', 'ctrl', 'keyup', 'shift']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['empty'], ['trash']]
func = runProg
args = ['sudo', 'rm', '-rf', '~/.local/share/Trash/files/*', '~/.local/share/Trash/info/*']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['my', 'show', 'open'], ['document','documents']]
func = nemo
args = ['/home/james/Documents']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['my', 'open', 'show'], ['download', 'downloads']]
func = nemo
args = ['/home/james/Downloads']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['show', 'open'], ['movie', 'movies'], ['folder', 'directory']]
func = nemo
args = ['/media/External-4.0/Media/Movies']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['show', 'open'], ['kid', 'kids'], ['folder', 'directory']]
func = nemo
args = ['/media/External-4.0/Media/Lyndas']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['open', 'show'], ['tv', 't v'], ['folder', 'directory']]
func = nemo
args = ['/media/External-4.0/Media/TV']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['open', 'show'], ['project', 'projects']]
func = nemo
args = ['/home/james/Projects']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['scroll'], ['up', 'left']]
func = xdo
args = ['click', '--repeat', '5', '4']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['scroll'], ['down', 'right']]
func = xdo
args = ['click', '--repeat', '5', '5']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['switch', 'swap', 'change'], ['window', 'application']]
func = xdo 
args = ['keydown', 'alt', 'key', 'Tab', 'keyup', 'alt']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['copy'], ['selected', 'clip', 'text']]
func = xdo
args = ['keydown', 'ctrl', 'key', 'c', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['insert', 'paste']]
func = xdo
args = ['keydown', 'ctrl', 'key', 'v', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['undo']]
func = xdo
args = ['keydown', 'ctrl', 'key', 'z', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['rename'], ['change', 'name']]
func = xdo
args = ['key', 'F2']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['select'], ['all']]
func = xdo
args = ['keydown', 'ctrl', 'key', 'a', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['help', 'menu']]
func = xdo
args = ['key', 'F1']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['minimize', 'show'], ['all', 'desktop']]
func = xdo
args = ['keydown', 'Super', 'key', 'd', 'keyup', 'Super']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['maximize']]
func = xdo
args = ['keydown', 'Super', 'key', 'Up', 'keyup', 'Super', 'keydown', 'Super', 'key', 'Up', 'keyup', 'Super']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['show', 'all']]
func = xdo
args = ['keydown', 'ctrl', 'keydown', 'alt', 'key', 'Up', 'keyup', 'ctrl', 'keyup', 'alt']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['netflix']]
func = internet
args = ['www.netflix.com']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['facebook']]
func = internet
args = ['www.facebook.com']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['school', 'college']]
func = internet
args = ['www.mgccc.edu']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['ice'], ['films']]
func = internet
args = ['www.icefilms.info']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['close'], ['tab']]
func = xdo
args = ['keydown', 'ctrl', 'key', 'F4', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['tab'], ['one']]
func = xdo
args = ['keydown', 'ctrl', 'key', '1', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['tab'], ['two']]
func = xdo
args = ['keydown', 'ctrl', 'key', '2', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['tab'], ['three']]
func = xdo
args = ['keydown', 'ctrl', 'key', '3', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['tab'], ['four']]
func = xdo
args = ['keydown', 'ctrl', 'key', '4', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['tab'], ['five']]
func = xdo
args = ['keydown', 'ctrl', 'key', '5', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['tab'], ['six']]
func = xdo
args = ['keydown', 'ctrl', 'key', '6', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['tab'], ['seven']]
func = xdo
args = ['keydown', 'ctrl', 'key', '7', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['tab'], ['eight']]
func = xdo
args = ['keydown', 'ctrl', 'key', '8', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['tab'], ['nine']]
func = xdo
args = ['keydown', 'ctrl', 'key', '9', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['open']]
func = xdo
args = ['keydown', 'ctrl', 'key', 'o', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['print']]
func = xdo
args = ['keydown', 'ctrl', 'key', 'p', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['delete']]
func = xdo
args = ['key', 'Delete']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['select', 'enter']]
func = xdo
args = ['key', 'Return']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['search', 'find']]
func = xdo 
args = ['keydown', 'ctrl', 'key', 'f', 'keyup', 'ctrl']
commfunc = [func, args]
commands[commdef] = commfunc

commdef = [['show', 'commands'], ['commands', 'list']]
func = runProg
args = ['python', '/home/james/Projects/kspeech/commandslist.py']
commfunc = [func, args]
commands[commdef] = commfunc

#Tests dont support 3+d lists
##commdef = [['power', 'shut', 'send'], ["off", "down", ["to", "hell"]], ["computer"]]
##func = reboot
##args = False
##commfunc = [func, args]
##commands[commdef] = commfunc
