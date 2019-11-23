import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(800,600))

        self.InitUI()
        self.Centre()

    def InitUI(self):

        self.panel = wx.Panel(self)

        self.panel.SetBackgroundColour("gray")

        self.LoadImages()

        self.futurama1.SetPosition((20,20))
        self.futurama2.SetPosition((200,200))
        self.futurama3.SetPosition((300,300))

    def LoadImages(self):

        self.futurama1 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("img/futurama1.jpg", wx.BITMAP_TYPE_ANY))
        self.futurama2 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("img/futurama2.jpg", wx.BITMAP_TYPE_ANY))
        self.futurama3 = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("img/futurama3.jpg", wx.BITMAP_TYPE_ANY))

def main():
    app = wx.App()
    ex = Example(None, title="Absolute Positioning")
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
