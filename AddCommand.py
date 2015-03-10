import os, wx

config_file = os.path.expanduser("~/.config/kspeech/commands.conf")
command_file = os.path.expanduser("~/Projects/kspeech/Commands.py")

def getDefs():
    with open(command_file) as cf:
        for line in cf.readlines():
            if 'def ' in line:
                if '=' in line:
                    pass
                else:
                    a = line.split("def ")[-1]
                    yield(a.split("(")[0], a.split('(')[1].split(")")[0])

def test():
    for definition, args in getDefs():
        print("{}({})".format(definition, args))

##class InputFrame(wx.Frame):
##    def __init__(self, defs):
##        wx.Frame.__init__(self, defs):
##            self.defs = getDefs()
##                       

if __name__ == "__main__":
    test()
    ##    app = wx.App()
    ##    app.MainLoop()
