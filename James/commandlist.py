import wx, itertools, random
import wx.richtext as rt
from subprocess import Popen, PIPE
from Commands import commands
from commandtools import isCommand

ignore = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def gentests(command):
    return itertools.product(*command)

def get_commands():
    passed = list()
    fails = list()
    for command in commands:
        for test in gentests(command):
            test = " ".join(test)
            if isCommand(test, command):
                passed.append(test)
            else:
                pass
    return passed    
##    pipe = Popen('python /home/james/Projects/kspeech/commandlisttest.py', stdout=PIPE, shell=True)
##    text = pipe.communicate()
##    return text
 
def show_commands():
    results = get_commands()
    mylist = [str(x) for x in results]
    tf = RichTextFrame(mylist, None)

class RichTextFrame(wx.Frame):
    def __init__(self, lines, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.rtc = rt.RichTextCtrl(self, style=wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.TE_READONLY)
        wx.CallAfter(self.rtc.SetFocus)
        self.rtc.Freeze()
        for line in lines:
            line.strip()
            if line == "None" or line in ignore:
                pass
            else:
                self.rtc.WriteText(line)
                self.rtc.Newline()
        self.rtc.Bind(wx.EVT_CLOSE, self.close)
        self.rtc.Thaw()
        self.Show()

    def close(self):
        self.Close()

if __name__ == "__main__":
    app = wx.App()
    show_commands()
    app.MainLoop()
