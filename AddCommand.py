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

class InputFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, (200, 350), wx.Size(350, 350))
        panel = wx.Panel(self, -1)
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
        self.inputLabel = wx.StaticText(panel, -1, 'Enter the command to listen for format ["this", "or"]', (25, 150))
        self.input1 = wx.TextCtrl(panel, -1, pos=(25, 170), size=(300, 30))
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
        self.Config(commands, function_call, args)
        self.Destroy()

    def changeArgs(self, event):
        function_call = self.listBox.GetStringSelection()
        self.argText.SetLabel(self.defs[function_call])

    def Config(self, command, function, args): # I really don't like this function.. lol
        newlines = []
        with open(command_file, 'r') as orig:
            newlines = orig.readlines()
        wline = 'commdef = [{}]\n'.format(command)
        ## thought about trying to input as straight text
        ## this or this or this and this or this and this
        ## then split on the or/and but that will be harder
        ## than trying to remember the input format hehe
        wline += 'func = {}\n'.format(function)
        wline += "args = ['{}\n']".format(args)
        wline += 'commfunc = [func, args]\ncommands[commdef] = commfunc\n'
        #if len(command) <2:
        #This is a check in case you exit the addcommand without inputting anything it just overwrites commands.py
        #with the original lines...
        #    pass # why cehck for if we gonna pass anyway?
        else: newlines.insert(-74, wline) # -74!!! Wha tha Fuckk you tryin ta accomplish??
        ## newlines[-74] is the number of lines from the bottom to the top of the if name == __main__
        ## less chance that we are going to add something to the bottom of the file...
        ## this means that the new command will always be the last command in the list...
        ## without indexing the list of lines it is VERY difficult to insert into a file in a place
        ## where you are sure it will be where you intend it to go unless you count the lines and have
        ## a marker where you always want to insert the new lines either before or after if that makes sense.
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
