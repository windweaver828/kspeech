import os, wx

config_file = os.path.expanduser("~/.config/kspeech/commands.conf")
command_file = os.path.expanduser("~/Projects/kspeech/Commands.py")

def getDefs():
    with open(command_file) as cf:
        lines = cf.readlines()
        for line in lines:
            if 'def ' in line:
                if '=' in line:
                    pass
                else:
                    a = line.split("def ")[-1]
                    defs = a.split("(")[0]
                    args = a.split('(')[1].split(")")[0]
                    print 'defs = '+defs
                    print 'args = '+args

##class InputFrame(wx.Frame):
##    def __init__(self, defs):
##        wx.Frame.__init__(self, defs):
##            self.defs = getDefs()
##                       

if __name__ == "__main__":
    getDefs()
    ##    app = wx.App()
    ##    app.MainLoop()
