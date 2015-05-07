import os, wx

config_file = os.path.expanduser("~/.config/kspeech/commands.conf")
command_file = os.path.expanduser("~/Projects/kspeech/Commands.py")
writefile = os.path.expanduser("~/Desktop/test.txt")

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

white = (101,250,85)

class InputFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, (200, 350), wx.Size(350, 350))#, style=wx.NO_BORDER)
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour(white)
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.defs = {}
        self.funcs = []
        for definition, args in getDefs():
            self.funcs.append(definition)
            self.defs[definition]=args        
        self.listBox = wx.ListBox(panel, -1, (25,10), (125,100), self.funcs)
        self.Bind(wx.EVT_LISTBOX, self.changeArgs)
        self.label = wx.StaticText(panel, -1, 'This is the Required Argument', (25, 110))
        self.argText = wx.StaticText(panel, -1, "None", (25, 130))
        self.inputLabel = wx.StaticText(panel, -1, 'Enter the command to listen for', (25, 150))
        self.input1 = wx.TextCtrl(panel, -1, pos=(25, 170), size=(300, 30), value = "[['this', 'this], ['this']]")
        self.inputLabel = wx.StaticText(panel, -1, 'Enter the required args space separated', (25, 200))
        self.input2 = wx.TextCtrl(panel, -1, pos=(25, 220), size=(300, 30))
        m_close = wx.Button(panel, wx.ID_CLOSE, "Close", pos=(150,300))
        m_close.Bind(wx.EVT_BUTTON, self.OnClose)
        m_ok = wx.Button(panel, wx.ID_OK, "OK", pos=(250,300))
        m_ok.Bind(wx.EVT_BUTTON, self.OnOk)

    def OnOk(self, event):
        commands = self.input1.GetValue()
        function_call = self.listBox.GetStringSelection()
        args = self.input2.GetValue()
        if len(commands) < 3:
            self.Destroy()
        else:
            self.Config(commands, function_call, args)
            self.Destroy()

    def changeArgs(self, event):
        function_call = self.listBox.GetStringSelection()
        if len(self.defs[function_call]) < 3:
            self.argText.SetLabel('None')
        else: self.argText.SetLabel(self.defs[function_call])

    def Config(self, command, function, args): # I really don't like this function.. lol
        newlines = []
        f = open(writefile, "w")
        with open(command_file, 'r') as orig:
            newlines = orig.readlines()
        wline = 'commdef = [{}]\n'.format(command)
        wline += 'func = {}\n'.format(function)
        wline += "args = ['{}\n']".format(args)
        wline += 'commfunc = [func, args]\ncommands[commdef] = commfunc\n'
        if not len(command) <2:
            newlines.insert(-74, wline)
        for line in newlines:
            f.write(line)
        f.close()
        
    def OnClose(self, event):
        self.Destroy()
        
if __name__ == "__main__":
    test()
    app = wx.App()
    frame = InputFrame(None, -1, 'Add Voice Commmand')
    frame.Show()
    app.MainLoop()
