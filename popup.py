#!/usr/bin/python

import wx, sys, Process, os, time
from subprocess import Popen, PIPE

##try:
##    Popen('killall pop-up', shell=True)
##except: pass
##time.sleep(0.5)
##Process.chgProcessName("pop-up")

class PopUp(wx.Frame):
    def __init__(self, text):
        self.app = wx.App()
        wx.Frame.__init__ ( self, None, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 300,200 ), style = wx.DEFAULT_DIALOG_STYLE )
        self.SetSizeHintsSz( wx.Size( 300,-1 ), wx.DefaultSize )
        self.text = text
        fgSizer = wx.FlexGridSizer( 2, 1, 0, 0 )
        fgSizer.AddGrowableCol( 0 )
        fgSizer.AddGrowableRow( 0 )
        fgSizer.SetFlexibleDirection( wx.BOTH )
        fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
        self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL )
        gSizer = wx.GridSizer( 1, 1, 0, 0 )
        self.m_staticText = wx.StaticText( self.m_panel, wx.ID_ANY, u'Test', wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText.Wrap( 10 )
        gSizer.Add(self.m_staticText, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        self.m_panel.SetSizer(gSizer)
        self.m_panel.Layout()
        gSizer.Fit(self.m_panel)
        fgSizer.Add(self.m_panel, 1, wx.EXPAND |wx.ALL, 5)
        m_sdbSizer = wx.StdDialogButtonSizer()
        self.m_sdbSizerOK = wx.Button(self, wx.ID_OK)
        self.m_sdbSizerOK.Bind(wx.EVT_BUTTON, self.onClose)
        m_sdbSizer.AddButton(self.m_sdbSizerOK)
##        self.m_sdbSizerCancel = wx.Button(self, wx.ID_CANCEL)
##        m_sdbSizer.AddButton(self.m_sdbSizerCancel)
        m_sdbSizer.Realize()
        fgSizer.Add(m_sdbSizer, 1, wx.ALL|wx.EXPAND, 5 )
        self.SetSizer(fgSizer)
        self.Layout()
        self.Centre(wx.BOTH )
        self.setMessageLine(10)
##        wx.CallLater(2000, self.onClose, True)
        self.Show()
        self.app.MainLoop()
        print('What up bitches')

    def setMessageLine(self, messageLine):
##        message = sys.argv[1:]
        self.m_staticText.SetLabel(self.text)
        self.Fit()

    def onClose(self, event):
        self.Close()
    
##if __name__ == '__main__':
##    app = wx.App()
PopUp('Howdy')
##    app.MainLoop()
