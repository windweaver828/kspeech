import ctypes, subprocess, pyperclip

import time, sys, os, speech, time, webbrowser, win32api, win32con

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actual Functions
leftmouse = 0X01
rightmouse = 0x02
backspace = 0x08
tab = 0x09
enter = 0x0D
shift = 0x10
ctrl = 0x11
alt = 0x12
escape = 0x1B
space = 0x20
pageup = 0x21
pagedown = 0x22
end = 0x23
home = 0x24
left = 0x25
up = 0x26
right = 0x27
down = 0x28
windows = 0x5B
F1 = 0x70
F2 = 0x71
F3 = 0x72
F4 = 0x73
F5 = 0x74
F6 = 0x75
F7 = 0x76
F8 = 0x77
F9 = 0x78
F10 = 0x79
F11 = 0x7A
F12 = 0x7B
KP0 = 0x30
KP1 = 0x31
KP2 = 0x32
KP3 = 0x33
KP4 = 0x34
KP5 = 0x35
KP6 = 0x36
KP7 = 0x37
KP8 = 0x38
KP9 = 0x39
A = 0x41
B = 0x42
C = 0x43
D = 0x44
E = 0x45
F = 0x46
G = 0x47
H = 0x48
I = 0x49
J = 0x4A
K = 0x4B
L = 0x4C
M = 0x4D
N = 0x4E
O = 0x4F
P = 0x50
Q = 0x51
R = 0x52
S = 0x53
T = 0x54
U = 0x55
V = 0x56
W = 0x57
X = 0x58
Y = 0x59
Z = 0x5A


LBUTTON = 0x01               # Left mouse button
RBUTTON = 0x02               # Right mouse button
CANCEL = 0x03                # Control-break processing
MBUTTON = 0x04               # Middle mouse button (three-button mouse)
XBUTTON1 = 0x05              # X1 mouse button
XBUTTON2 = 0x06              # X2 mouse button
BACK = 0x08                  # BACKSPACE key
TAB = 0x09                   # TAB key
CLEAR = 0x0C                 # CLEAR key
RETURN = 0x0D                # ENTER key
SHIFT = 0x10                 # SHIFT key
CONTROL = 0x11               # CTRL key
MENU = 0x12                  # ALT key
PAUSE = 0x13                 # PAUSE key
CAPITAL = 0x14               # CAPS LOCK key
KANA = 0x15                  # IME Kana mode
HANGUL = 0x15                # IME Hangul mode
JUNJA = 0x17                 # IME Junja mode
FINAL = 0x18                 # IME final mode
HANJA = 0x19                 # IME Hanja mode
KANJI = 0x19                 # IME Kanji mode
ESCAPE = 0x1B                # ESC key
CONVERT = 0x1C               # IME convert
NONCONVERT = 0x1D            # IME nonconvert
ACCEPT = 0x1E                # IME accept
MODECHANGE = 0x1F            # IME mode change request
SPACE = 0x20                 # SPACEBAR
PRIOR = 0x21                 # PAGE UP key
NEXT = 0x22                  # PAGE DOWN key
END = 0x23                   # END key
HOME = 0x24                  # HOME key
LEFT = 0x25                  # LEFT ARROW key
UP = 0x26                    # UP ARROW key
RIGHT = 0x27                 # RIGHT ARROW key
DOWN = 0x28                  # DOWN ARROW key
SELECT = 0x29                # SELECT key
PRINT = 0x2A                 # PRINT key
EXECUTE = 0x2B               # EXECUTE key
SNAPSHOT = 0x2C              # PRINT SCREEN key
INSERT = 0x2D                # INS key
DELETE = 0x2E                # DEL key
HELP = 0x2F                  # HELP key
LWIN = 0x5B                  # Left Windows key (Natural keyboard)
RWIN = 0x5C                  # Right Windows key (Natural keyboard)
APPS = 0x5D                  # Applications key (Natural keyboard)
SLEEP = 0x5F                 # Computer Sleep key
NUMPAD0 = 0x60               # Numeric keypad 0 key
NUMPAD1 = 0x61               # Numeric keypad 1 key
NUMPAD2 = 0x62               # Numeric keypad 2 key
NUMPAD3 = 0x63               # Numeric keypad 3 key
NUMPAD4 = 0x64               # Numeric keypad 4 key
NUMPAD5 = 0x65               # Numeric keypad 5 key
NUMPAD6 = 0x66               # Numeric keypad 6 key
NUMPAD7 = 0x67               # Numeric keypad 7 key
NUMPAD8 = 0x68               # Numeric keypad 8 key
NUMPAD9 = 0x69               # Numeric keypad 9 key
MULTIPLY = 0x6A              # Multiply key
ADD = 0x6B                   # Add key
SEPARATOR = 0x6C             # Separator key
SUBTRACT = 0x6D              # Subtract key
DECIMAL = 0x6E               # Decimal key
DIVIDE = 0x6F                # Divide key
F1 = 0x70                    # F1 key
F2 = 0x71                    # F2 key
F3 = 0x72                    # F3 key
F4 = 0x73                    # F4 key
F5 = 0x74                    # F5 key
F6 = 0x75                    # F6 key
F7 = 0x76                    # F7 key
F8 = 0x77                    # F8 key
F9 = 0x78                    # F9 key
F10 = 0x79                   # F10 key
F11 = 0x7A                   # F11 key
F12 = 0x7B                   # F12 key
F13 = 0x7C                   # F13 key
F14 = 0x7D                   # F14 key
F15 = 0x7E                   # F15 key
F16 = 0x7F                   # F16 key
F17 = 0x80                   # F17 key
F18 = 0x81                   # F18 key
F19 = 0x82                   # F19 key
F20 = 0x83                   # F20 key
F21 = 0x84                   # F21 key
F22 = 0x85                   # F22 key
F23 = 0x86                   # F23 key
F24 = 0x87                   # F24 key
NUMLOCK = 0x90               # NUM LOCK key
SCROLL = 0x91                # SCROLL LOCK key
LSHIFT = 0xA0                # Left SHIFT key
RSHIFT = 0xA1                # Right SHIFT key
LCONTROL = 0xA2              # Left CONTROL key
RCONTROL = 0xA3              # Right CONTROL key

def Function(command):
    def PressKey(hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def ReleaseKey(hexKeyCode):
        extra = ctypes.c_ulong(0)
        ii_ = Input_I()
        ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
        x = Input( ctypes.c_ulong(1), ii_ )
        SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    MOUSE_SPEED = .6 #seconds 
    def mouse_glide_to(x,y):
        x1,y1 = win32api.GetCursorPos()
        smooth_glide_mouse(x1,y1, x, y, MOUSE_SPEED, 50)
     
    def smooth_glide_mouse(x1,y1,x2,y2, t, intervals):
        distance_x = x2-x1
        distance_y = y2-y1
        for n in range(0, intervals+1):
            win32api.SetCursorPos((x1 + n * (distance_x/intervals), y1 + n * (distance_y/intervals)))
            time.sleep(t*1.0/intervals)

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
