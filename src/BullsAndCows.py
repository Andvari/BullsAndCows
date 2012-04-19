'''
Created on 18.04.2012

@author: kapitan Nemo
'''

import wx
import random

class MainWindow(wx.Frame):
    def __init__(self, *argc, **kwargc):
        super(MainWindow, self).__init__(*argc, **kwargc)
        mb = wx.MenuBar()
        menu = wx.Menu()
        mi_new = menu.Append(wx.ID_NEW, "New Gm")
        menu.Append(wx.ID_SEPARATOR)
        mi_quit = menu.Append(wx.ID_EXIT, "&Quit")
        mb.Append(menu, "New Gm")
        self.SetMenuBar(mb)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, mi_quit)
        self.Bind(wx.EVT_MENU, self.OnNewGm, mi_new)
        
        self.Show()
        
    def OnQuit(self, e):
        self.Close()
        
    def OnNewGm(self, e):
        gm_field = GmField(self, wx.ID_ANY, size = (600, 600), pos = (0, 0))
        
class GmField(wx.Panel):
    def __init__(self, *argc, **kwargc):
        super(GmField, self).__init__(*argc, **kwargc)
        bull = []
        
        left_field  = wx.Panel(self, wx.ID_ANY, pos = (0, 0),   size = (300, 600), style = wx.SUNKEN_BORDER)
        right_field = wx.Panel(self, wx.ID_ANY, pos = (300, 0), size = (300, 600), style = wx.SUNKEN_BORDER)
        
        border = wx.StaticBox(left_field, wx.ID_ANY, label = "Make The Turn", pos = (20, 20), size = (260, 50))
        attempt_field = wx.TextCtrl(left_field, wx.ID_ANY, pos = (30, 40), size = (115, 20))
        attempt_btn   = wx.Button(left_field, wx.ID_ANY, label = "Is It Right?", pos = (155, 40), size = (115, 20))
        
        attempt_btn.Bind(wx.EVT_BUTTON, self.OnClick)
        self.Update()

    def OnClick(self, e):
        print e

    def generateBull(self):
        self.bull[0] = random.randint(1,9)
        
        self.bull[1] = random.randint(1,9)
        while (self.bull[1] == self.bull[0]):
            self.bull[1] = random.randint(1,9)
        
        self.bull[2] = random.randint(1,9)
        while ((self.bull[2] == self.bull[0])|(self.bull[2] == self.bull[1])):
            self.bull[2] = random.randint(1,9)
        
        self.bull[3] = random.randint(1,9)
        while ((self.bull[3] == self.bull[0])|(self.bull[3] == self.bull[1])|(self.bull[3] == self.bull[2])):
            self.bull[3] = random.randint(1,9)

if __name__ == '__main__':
    MainApp = wx.App()
    MainWindow = MainWindow(None, title = "Bulls and Cows", size = (600, 600), pos = (200, 200),style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX & ~wx.MINIMIZE_BOX & ~wx.RESIZE_BORDER)
    MainApp = MainApp.MainLoop()
    