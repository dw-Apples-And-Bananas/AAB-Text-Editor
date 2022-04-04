import wx



if __name__ == "__main__":
    from gui.application import Application
    main = wx.App()
    application = Application(main)
    application.Show()
    main.MainLoop()
