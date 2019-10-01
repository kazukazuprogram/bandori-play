#!/usr/bin/env python3
# coding: utf-8
import wx
import wx.adv

appname = "BanG Dream Music Player"
TRAY_ICON = 'icon.ico'


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.AppendItem(item)
    return item


def open_site():
    print("open site.")


class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        self.frame = frame
        super(TaskBarIcon, self).__init__()
        self.set_icon(TRAY_ICON)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.dclick)
        self.Bind(wx.adv.EVT_TASKBAR_MOVE, self.move)

    def move(self, event):
        print(event)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Open Site', self.on_open_site)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def dclick(self, event):
        print("double click")

    def set_icon(self, path):
        icon = wx.Icon(wx.Bitmap(path))
        self.SetIcon(icon, appname)

    def on_open_site(self, event):
        print("Open site")

    def on_exit(self, event):
        print('exit')
        wx.CallAfter(self.Destroy)
        self.frame.Close()


class App(wx.App):

    def OnInit(self):
        frame = wx.Frame(None)
        self.SetTopWindow(frame)
        TaskBarIcon(frame)
        return True


if __name__ == '__main__':
    app = App(False)
    app.MainLoop()
