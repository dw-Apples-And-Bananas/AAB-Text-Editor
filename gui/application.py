import wx
from gui.textpanel import TextPanel



class Application(wx.Frame):
    def __init__(self, main):
        wx.Frame.__init__(self, None, title="AAB Text Editor", size=(800,530))
        self.Centre()


        self.textPanel = TextPanel(self)
