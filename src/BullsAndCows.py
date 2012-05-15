'''
Created on 18.04.2012

@author: kapitan Nemo
'''

import wx
import random

class Tablo(wx.Panel):
    def __init__(self, *args, **kwargs):
        super(Tablo, self).__init__(*args, **kwargs)
        tbl = wx.Panel(self, wx.ID_ANY)
        

class MainWindow(wx.Frame):
    TurnCounter = 0
    myval = 0
    
    def __init__(self, *argc, **kwargc):
        super(MainWindow, self).__init__(*argc, **kwargc)
        mb = wx.MenuBar()
        menu = wx.Menu()
        mi_new = menu.Append(wx.ID_NEW, "New Gm")
        menu.Append(wx.ID_SEPARATOR)
        mi_quit = menu.Append(wx.ID_EXIT, "&Quit")
        mb.Append(menu, "New Gm")
        
        self.TurnCounter = 0
        self.myval = 0
        
        self.SetMenuBar(mb)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, mi_quit)
        self.Bind(wx.EVT_MENU, self.OnNewGm, mi_new)
        
        self.myArbiter = Arbiter()
        
        self.btn1 = wx.Button(self, wx.ID_ANY, label = "1", size = (30, 30), pos = (30, 30))
        self.btn2 = wx.Button(self, wx.ID_ANY, label = "2", size = (30, 30), pos = (60, 30))
        self.btn3 = wx.Button(self, wx.ID_ANY, label = "3", size = (30, 30), pos = (90, 30))
        self.btn4 = wx.Button(self, wx.ID_ANY, label = "4", size = (30, 30), pos = (30, 60))
        self.btn5 = wx.Button(self, wx.ID_ANY, label = "5", size = (30, 30), pos = (60, 60))
        self.btn6 = wx.Button(self, wx.ID_ANY, label = "6", size = (30, 30), pos = (90, 60))
        self.btn7 = wx.Button(self, wx.ID_ANY, label = "7", size = (30, 30), pos = (30, 90))
        self.btn8 = wx.Button(self, wx.ID_ANY, label = "8", size = (30, 30), pos = (60, 90))
        self.btn9 = wx.Button(self, wx.ID_ANY, label = "9", size = (30, 30), pos = (90, 90))
        
        self.Bind(wx.EVT_BUTTON, self.OnBtn, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.OnBtn, self.btn2)
        self.Bind(wx.EVT_BUTTON, self.OnBtn, self.btn3)
        self.Bind(wx.EVT_BUTTON, self.OnBtn, self.btn4)
        self.Bind(wx.EVT_BUTTON, self.OnBtn, self.btn5)
        self.Bind(wx.EVT_BUTTON, self.OnBtn, self.btn6)
        self.Bind(wx.EVT_BUTTON, self.OnBtn, self.btn7)
        self.Bind(wx.EVT_BUTTON, self.OnBtn, self.btn8)
        self.Bind(wx.EVT_BUTTON, self.OnBtn, self.btn9)
        
        self.sw  = wx.ScrolledWindow(self, wx.ID_ANY, pos = (130, 30), size = (180, 90), style = wx.VSCROLL)
        self.tbl = wx.StaticText(self.sw, wx.ID_ANY)
        
        self.Show()
        
        self.myArbiter.newGame()
        
    def OnQuit(self, e):
        self.Close()
        
    def OnNewGm(self, e):
        self.myArbiter.newGame()
        
    def OnBtn(self, e):
        e.GetEventObject().Disable()
        self.myval = (self.myval*10)+int(e.GetEventObject().GetLabel())
        self.TurnCounter += 1
        if (self.TurnCounter == 4):
            ##print self.myval
            self.myArbiter.makeTurn(self.myval)
            self.TurnCounter = 0
            self.myval = 0
            self.btn1.Enable()
            self.btn2.Enable()
            self.btn3.Enable()
            self.btn4.Enable()
            self.btn5.Enable()
            self.btn6.Enable()
            self.btn7.Enable()
            self.btn8.Enable()
            self.btn9.Enable()
        

class Arbiter():
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0
    
    def __init_(self):
        self.v1 = 0
        self.v2 = 0
        self.v3 = 0
        self.v4 = 0
    
    def newGame(self):
        self.v1 = random.randint(1, 9)
        
        self.v2 = random.randint(1, 9)
        while self.v2 == self.v1:
            self.v2 = random.randint(1, 9)
            
        self.v3 = random.randint(1, 9)
        while ((self.v3==self.v1)|(self.v3==self.v2)):
            self.v3 = random.randint(1, 9)
            
        self.v4 = random.randint(1, 9)
        while ((self.v4==self.v1)|(self.v4==self.v2)|(self.v4==self.v3)):
            self.v4 = random.randint(1, 9)
            
        ##print "New Game"
        ##print "Value maked"
        ##print str(self.v1) + str(self.v2) + str(self.v3) + str(self.v4)
    
    def makeTurn(self, val):
        Bulls = 0
        Cows = 0
        if (val == (((self.v1*10)+self.v2)*10+self.v3)*10+self.v4):
            pass
            #print "Success"
            #print "I am making " + str(val)
        else:
            my_v1 = int((val/1000))
            my_v2 = int((val - my_v1*1000)/100)
            my_v3 = int((val - my_v1*1000 - my_v2*100)/10)
            my_v4 = int((val - my_v1*1000 - my_v2*100 - my_v3*10))
            
            if ((my_v1==self.v2)|(my_v1==self.v3)|(my_v1==self.v4)): Bulls += 1
            if ((my_v2==self.v2)|(my_v2==self.v3)|(my_v2==self.v4)): Bulls += 1
            if ((my_v3==self.v2)|(my_v3==self.v3)|(my_v3==self.v4)): Bulls += 1
            if ((my_v4==self.v2)|(my_v4==self.v3)|(my_v4==self.v4)): Bulls += 1
        
            if (my_v1==self.v1):
                Bulls += 1
                Cows  += 1
                 
            if (my_v2==self.v2):
                Bulls += 1
                Cows  += 1
                
            if (my_v3==self.v3):
                Bulls += 1
                Cows  += 1
                
            if (my_v4==self.v4):
                Bulls += 1
                Cows  += 1
                
            #print str(Bulls) + str(Cows)
            
            
class History():
    turns   = []
    results = []
    def __init__(self):
        pass
    
    def push(self, turn, res):
        self.turns.append(turn)
        self.results.append(res)
    
    def pop(self):
        string_result = ""
        for i in range(5):
            string_result += self.turns[len(self.turns) - 5 - i] + ": " + self.results[len(self.results) - 5 - i] + "\n"
        return string_result
        
if __name__ == '__main__':
    MainApp = wx.App()
    MainWindow = MainWindow(None, title = "Bulls and Cows", size = (600, 600), pos = (200, 200),style = wx.DEFAULT_FRAME_STYLE & ~wx.MAXIMIZE_BOX & ~wx.MINIMIZE_BOX & ~wx.RESIZE_BORDER)
    MainApp = MainApp.MainLoop()


