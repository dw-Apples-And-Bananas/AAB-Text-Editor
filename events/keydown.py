import wx
import json
import os



with open("./keybinds.json") as file:
    keybinds = json.load(file)


def KeyDown(panel, event):
    char = chr(event.GetKeyCode()).lower()
    syntax = {
        "cmd": event.CmdDown(),
        "ctrl": event.ControlDown(),
        "shift": event.ShiftDown()
    }

    skipped = False
    for bind in keybinds:
        if char == bind.split("+")[-1]:
            for key in bind.split("+"):
                try:
                    if not syntax[key]:
                        skipped = True
                        break
                except KeyError:
                    pass
            if not skipped:
                eval(keybinds[bind])
                break

    event.Skip()



def Save(panel):
    with open(panel.currFile, "w") as file:
        file.write(panel.GetValue())



def OpenFile(panel):
    with wx.FileDialog(panel, style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
        if fileDialog.ShowModal() == wx.ID_CANCEL:
            return

        pathname = fileDialog.GetPath()
        panel.currFile = pathname
        try:
            with open(pathname) as file:
                panel.write(file.read())
        except:
            print("Error")



def Run(panel):
    Save(panel)
    os.system(f"python3 {panel.currFile}")
