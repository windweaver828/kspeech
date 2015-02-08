import ctypes, subprocess, pyperclip

import time, sys, os, speech, time, webbrowser, win32api, win32con

def Function(command):

    def isCommand(command, args):
        '''For reference this the expected argument format
        Think of each level of the list as alternating between and and or
        starting with and. So for instance:
        args = [['power', 'shut', 'send'], ["off", "down", ["to", "hell"]], ["computer"]]
        means (power or shut) and (off or down or (to and hell)) and computer in command
        so "jarvis send the computer to hell please" is just as valid as "jarvis power off the computer"
        '''
        
        for arg in args:
            isin = False
            for argument in arg:
                if isinstance(argument, list):
                    isin = True
                    for ar in argument:
                        if not ar in command: isin = False
                elif argument in command: isin = True
                if not isin: return False
        return True

##    def isCommand(command, args):
##        for arg in args:
##            if isinstance(arg, list):
##                if not orCommand(command, arg): return False 
##            elif not arg in command: return False
##        return True
##
##    def orCommand(command, args):
##        for arg in args:
##            if isinstance(arg, list):
##                if not isCommand(command, arg): return False
##            elif not arg in command: return False
##        return True

    if isCommand(command, [['text']]):
        text = command.replace("text", "")
        pyperclip.setcb(text)
        PressKey(ctrl), PressKey(V)
        ReleaseKey(ctrl), ReleaseKey(V)
        PressKey(enter)
        ReleaseKey(enter)

    elif isCommand(command, [["new"],["folder", "directory"]]):
        PressKey(ctrl), PressKey(shift), PressKey(N)
        ReleaseKey(ctrl), ReleaseKey(shift), ReleaseKey(N)

    elif isCommand(command, [["save"]]):
        PressKey(ctrl), PressKey(S)
        ReleaseKey(ctrl), ReleaseKey(S)

    elif isCommand(command, [["cut"], ["selected", "clip", "text"]]):
        PressKey(ctrl), PressKey(X)
        ReleaseKey(ctrl), ReleaseKey(X)

    elif isCommand(command, [["copy"], ["selected", "clip", "text"]]):
        PressKey(ctrl), PressKey(C)
        ReleaseKey(ctrl), ReleaseKey(C)

    elif isCommand(command, [["insert", "paste"]]):
        PressKey(ctrl), PressKey(V)
        ReleaseKey(ctrl), ReleaseKey(V)

    elif isCommand(command, [["undid", "undo"]]):
        PressKey(ctrl), PressKey(Z)
        ReleaseKey(ctrl), ReleaseKey(Z)

    elif isCommand(command, [['rename', ["change", "name"]]]):
        PressKey(F2)
        ReleaseKey(F2)        

    elif isCommand(command, [["select"], ["all"]]):
        PressKey(ctrl), PressKey(A)
        ReleaseKey(ctrl), ReleaseKey(A)

    elif isCommand(command, [["properties"]]):
        PressKey(alt), PressKey(enter)
        ReleaseKey(alt), ReleaseKey(enter)

    elif isCommand(command, [["help"], ["menu"]]):
        PressKey(F1)
        ReleaseKey(F1)

    elif isCommand(command, [["minimize"], ["all"]]):
        PressKey(windows), PressKey(M)
        ReleaseKey(windows), ReleaseKey(M)

    elif isCommand(command, [["send", "move"], ["left"], ["monitor", "screen"]]):
        PressKey(windows), PressKey(shift), PressKey(left)
        ReleaseKey(windows), ReleaseKey(shift), ReleaseKey(left)

    elif isCommand(command, [["send", "move"], ["right"], ["monitor", "screen"]]):
        PressKey(windows), PressKey(shift), PressKey(up)
        ReleaseKey(windows), ReleaseKey(shift), ReleaseKey(up)

    elif isCommand(command, [["rotate"], ["right"]]):
        PressKey(ctrl), PressKey(0xBE)
        ReleaseKey(ctrl), ReleaseKey(0xBE)

    elif isCommand(command, [["rotate"], ["left"]]):
        PressKey(alt), PressKey(0xBC)
        ReleaseKey(alt), ReleaseKey(0xBC)

    elif isCommand(command, [["three"], ["tabs"]]):
        PressKey(windows), PressKey(ctrl), PressKey(tab)
        ReleaseKey(windows), ReleaseKey(ctrl), ReleaseKey(tab)

    elif isCommand(command, [["full"], ["left"]]):
        PressKey(windows), PressKey(left)
        ReleaseKey(windows), ReleaseKey(left)

    elif isCommand(command, [["full"], ["right"]]):
        PressKey(windows), PressKey(right)
        ReleaseKey(windows), ReleaseKey(right)

    elif isCommand(command, [["shrink"], ["window"]]):
        PressKey(windows), PressKey(down)
        ReleaseKey(windows), ReleaseKey(down)

    elif isCommand(command, [["go"], ["right"]]):
        PressKey(right)
        ReleaseKey(right)

    elif isCommand(command, [["go"], ["left"]]):
        PressKey(left)
        ReleaseKey(left)

    elif isCommand(command, [["close"], ["window"]]):
        PressKey(alt), PressKey(F4)
        ReleaseKey(alt), ReleaseKey(F4)

    elif isCommand(command, [["full"], ["screen"]]):
        PressKey(F11)
        ReleaseKey(F11)

    elif isCommand(command, [["recycle"], ["bin"]]):
        if isCommand(command, [["show", "open"]]):
            os.popen("start shell:RecycleBinFolder")
        else: os.popen('python "c:\\users\\james\\documents\\speech macros\\pyscripts\\EmptyRecycleBin.pyw"')

    elif isCommand(command, [["movie"], ["list"]]):
        os.popen('python "c:\\users\\james\\documents\\speech macros\\pyscripts\\listmovienames.pyw"')
        os.popen('notepad "c:\\users\\james\\documents\\speech macros\\pyscripts\\movielist.txt"')

    elif isCommand(command, [["task"], ["manager"]]):
        PressKey(shift), PressKey(ctrl), PressKey(escape)
        ReleaseKey(shift), ReleaseKey(ctrl), ReleaseKey(escape)

    elif isCommand(command, [["restart", "reboot", ["power", "off"], \
                              ["shut", "down"]], ["abort", "cancel", "stop"]]):
        os.popen("shutdown -a")

    elif isCommand(command, [['power', 'shut'], ["off", "down"], ["pc", "computer"]]):
        speech.say("shutting down computer in one minute")
        os.popen("shutdown -s -t 60")

    elif isCommand(command, [["reboot", "restart"], ["pc", "computer"]]):
        speech.say("rebooting computer in one minute")
        os.popen("shutdown -r -t 60")

    elif isCommand(command, [["secure", "lock"], ["pc", "computer"]]):
        os.popen('Rundll32.exe User32.dll,LockWorkStation')

    elif isCommand(command, [["what", "tell"], ["time"]]):
        hour = time.localtime().tm_hour
        minute = time.localtime().tm_min
        seconds = time.localtime().tm_sec
        day_night = "A M"
        if hour > 12:
            if hour != 12:
                hour = hour - 12
            day_night = "P  M"
        if hour == 0:
            hour = 12
        if minute < 10:
            minute = str("o")+str(minute)
        if minute == "o0":
            minute = "O clock "
        speech.say(" Current time is " + str(hour) +" " + str(minute) + day_night)
    elif isCommand(command, [["speech"], ["macro"]]):
        os.popen('start explorer "c:\\users\\james\\documents\\Speech Macros"')
                   
    elif isCommand(command, [["my", "show", "open"], ["document"]]):
        os.popen('start explorer "c:\\users\\james\\documents"')

    elif isCommand(command, [["my", "show", "open"], ["download"]]):
        os.popen('start explorer "c:\\users\\james\\downloads"')

    elif isCommand(command, [["movie"], ["folder"]]):
        os.popen('start explorer "\\\\WINDSERV\\ExternalDrive 2 TB\\Videos"')

    elif isCommand(command, [["kid"], ["folder"]]):
        os.popen('start explorer "\\\\WINDSERV\\ExternalDrive 1.5 TB\\Lyndas Movies"')

    elif isCommand(command, [["tv"], ["folder"]]):
        os.popen('start explorer "\\\\WINDSERV\\ExternalDrive 2 TB\\TV Episodes"')

    elif isCommand(command, [["hide"], ["rainmeter", "interface"]]):
        os.chdir("C:\\Program Files\\Rainmeter\\")
        os.popen('rainmeter.exe !settransparency "255"')

    elif isCommand(command, [["show", "unhide", "restore"], ["rainmeter", "interface"]]):
        os.chdir("C:\\Program Files\\Rainmeter\\")
        os.popen('rainmeter.exe !settransparency "0"')

    elif isCommand(command, [["edit", "alter", "add", "change"], ["notes", "memo"]]):
        os.popen('notepad "c:\\users\\james\\documents\\speech macros\\pyscripts\\Ironmanbackup.txt"')

    elif isCommand(command, [["stop"], ["listening"]]) or \
         isCommand(command, [["speech"], ["off"]]):
        PressKey(windows), PressKey(ctrl)
        ReleaseKey(windows), ReleaseKey(ctrl)
        os.popen("c:\\users\\james\\downloads\\vox\\voxshort.lnk")

    elif isCommand(command, [["scroll"], ["up", "left"]]):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,win32con.WHEEL_DELTA*3)

    elif isCommand(command, [["scroll"], ["down", "right"]]):
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-win32con.WHEEL_DELTA*3)

    elif isCommand(command, [["switch", "swap", "change"], ["window", "application"]]):
        PressKey(alt), PressKey(shift), PressKey(0x9)
        ReleaseKey(alt), ReleaseKey(shift), ReleaseKey(0x9)
        
    elif isCommand(command, [["drop"], ["box"]]):
        os.popen(r'start explorer "C:\Users\James\Dropbox"')

    
## STAYS AT BOTTOM
    elif isCommand(command, [["netflix"]]):
        webbrowser.open("http://www.netflix.com")

    elif isCommand(command, [["supernatural"]]):
        webbrowser.open("http://www.cwtv.com/cw-video/supernatural/full-episodes")

    elif isCommand(command, [["facebook"]]):
        webbrowser.open("http://www.facebook.com")

    elif isCommand(command, [["drag"], ["mouse"]]):
        ctypes.windll.user32.SetCursorPos(30,30)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,30,30,0,0)
        time.sleep(0.4)
        mouse_glide_to(600, 600)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,600,600,0,0)
   
    elif isCommand(command, [["open"]]):
        PressKey(ctrl), PressKey(0x4F)
        ReleaseKey(ctrl), ReleaseKey(0x4F)

    elif isCommand(command, [["show"], ["desktop"]]):
        PressKey(windows), PressKey(D)
        ReleaseKey(windows), ReleaseKey(D)

    elif isCommand(command, [["cancel", "abort"]]):
        PressKey(escape)
        ReleaseKey(escape)

    elif isCommand(command, [["search", "find"]]):
        PressKey(ctrl), PressKey(F)
        ReleaseKey(ctrl), ReleaseKey(F)
        


if __name__ =="__main__":
    sys.argv = "./shortcuts jarvis three d tabs please".split(' ')
    command = ""
    for arg in sys.argv[1:]:
        if arg.lower() == 'jarvis': continue
        command += arg+ " "
    commands = command.strip().lower().split(" next ")
    for comm in commands:
        print command
        Function(comm)
