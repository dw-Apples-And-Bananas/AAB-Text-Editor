import wx
import wx.stc as stc
import events



class TextPanel(stc.StyledTextCtrl):
    def __init__(self, app):
        stc.StyledTextCtrl.__init__(self, app, size=app.Size)

        self.app = app


        self.SetMarginType(1, wx.stc.STC_MARGIN_NUMBER)
        self.SetMarginMask(1, 0)
        self.SetMarginWidth(1, 26)
        self.StyleSetSpec(wx.stc.STC_STYLE_LINENUMBER,'fore:#909090,back:#FFFFFF')


        self.Bind(wx.EVT_KEY_DOWN, lambda event: events.KeyDown(self, event))
        self.Bind(wx.EVT_UPDATE_UI, self.UpdateUi)



    def UpdateUi(self, event):
        self.SetPosition((0,0))
        self.SetSize(self.app.Size)
