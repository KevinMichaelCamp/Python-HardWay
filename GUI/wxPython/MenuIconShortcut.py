import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        # Create MenuBar
        menubar = wx.MenuBar()
        # File Menu
        fileMenu = wx.Menu()

        # New
        newItem = wx.MenuItem(fileMenu, wx.ID_NEW, '&New\tCtrl+N')
        newItem.SetBitmap(wx.Bitmap('img/new.png'))
        fileMenu.Append(newItem)
        # Open
        openItem = wx.MenuItem(fileMenu, wx.ID_OPEN, '&Open\tCtrl+O')
        openItem.SetBitmap(wx.Bitmap('img/open.png'))
        fileMenu.Append(openItem)
        # Save
        saveItem = wx.MenuItem(fileMenu, wx.ID_SAVE, '&Save\tCtrl+S')
        saveItem.SetBitmap(wx.Bitmap('img/save.png'))
        fileMenu.Append(saveItem)

        fileMenu.AppendSeparator()

        # Exit
        exitItem = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q')
        exitItem.SetBitmap(wx.Bitmap('img/quit.png'))
        fileMenu.Append(exitItem)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        # 
        self.Bind(wx.EVT_MENU, self.OnQuit, exitItem)

        self.SetSize((300, 200))
        self.SetTitle('Simple menu')
        self.Centre()

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
