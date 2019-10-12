import wx
import wx.xrc

import gettext
_ = gettext.gettext


class MainFrame (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=_(u"INI Editor"), pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.Size(400, 400), wx.DefaultSize)

        b_sizer1 = wx.BoxSizer(wx.VERTICAL)
        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        b_sizer2 = wx.BoxSizer(wx.VERTICAL)
        self.m_scrolledWindow1 = wx.ScrolledWindow(self.m_panel1, wx.ID_ANY, wx.DefaultPosition,
                                                   wx.DefaultSize, wx.HSCROLL | wx.VSCROLL)
        self.m_scrolledWindow1.SetScrollRate(5, 5)
        b_sizer4 = wx.BoxSizer(wx.VERTICAL)
        b_sizer6 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel5 = wx.Panel(self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition,
                                 wx.DefaultSize, wx.TAB_TRAVERSAL)
        b_sizer9 = wx.BoxSizer(wx.VERTICAL)
        b_sizer10 = wx.BoxSizer(wx.HORIZONTAL)
        self.m_staticText2 = wx.StaticText(self.m_panel5, wx.ID_ANY, _(u"[DISPLAY]"),
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetToolTip(_(u"Display Section"))
        b_sizer10.Add(self.m_staticText2, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.m_staticline1 = wx.StaticLine(self.m_panel5, wx.ID_ANY, wx.DefaultPosition,
                                           wx.DefaultSize, wx.LI_HORIZONTAL)
        b_sizer10.Add(self.m_staticline1, 1, wx.ALIGN_CENTER | wx.ALL, 5)
        b_sizer9.Add(b_sizer10, 0, wx.EXPAND, 5)
        b_sizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.st_interface = wx.StaticText(self.m_panel5, wx.ID_ANY, _(u"Display:"),
                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_interface.SetLabelMarkup(_(u"Display:"))
        self.st_interface.Wrap(-1)

        self.st_interface.SetToolTip(_(u"User interface to use"))
        self.st_interface.SetMinSize(wx.Size(50, -1))

        b_sizer8.Add(self.st_interface, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        display_choice_choices = [wx.EmptyString, u"Axis", u"Gmoccapy", u"Touchy", u"Gscreen",
                                  u"keystick", u"tklinuxcnc", u"xemc"]
        self.display_choice = wx.Choice(self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        display_choice_choices, 0)
        self.display_choice.SetSelection(0)
        b_sizer8.Add(self.display_choice, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        b_sizer9.Add(b_sizer8, 0, wx.EXPAND, 5)

        b_sizer81 = wx.BoxSizer(wx.HORIZONTAL)

        self.st_interface1 = wx.StaticText(self.m_panel5, wx.ID_ANY, _(u"Coordinate Type:"),
                                           wx.DefaultPosition, wx.DefaultSize, 0)
        self.st_interface1.SetLabelMarkup(_(u"Coordinate Type:"))
        self.st_interface1.Wrap(-1)
        self.st_interface1.SetToolTip(_(u"Coordinate system to show on the DRO"))

        b_sizer81.Add(self.st_interface1, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        pos_offset_choice_choices = [wx.EmptyString, u"Relative", u"Machine"]
        self.pos_offset_choice = wx.Choice(self.m_panel5, wx.ID_ANY, wx.DefaultPosition,
                                           wx.DefaultSize, pos_offset_choice_choices, 0)
        self.pos_offset_choice.SetSelection(0)
        b_sizer81.Add(self.pos_offset_choice, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        pos_fb_choice_choices = [wx.EmptyString, u"Commanded", u"Actual"]
        self.pos_fb_choice = wx.Choice(self.m_panel5, wx.ID_ANY, wx.DefaultPosition,
                                       wx.DefaultSize, pos_fb_choice_choices, 0)
        self.pos_fb_choice.SetSelection(0)
        b_sizer81.Add(self.pos_fb_choice, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        b_sizer9.Add(b_sizer81, 0, wx.EXPAND, 5)

        self.m_panel5.SetSizer(b_sizer9)
        self.m_panel5.Layout()
        b_sizer9.Fit(self.m_panel5)
        b_sizer6.Add(self.m_panel5, 1, wx.EXPAND | wx.ALL, 5)

        b_sizer4.Add(b_sizer6, 1, wx.EXPAND, 5)

        self.m_scrolledWindow1.SetSizer(b_sizer4)
        self.m_scrolledWindow1.Layout()
        b_sizer4.Fit(self.m_scrolledWindow1)
        b_sizer2.Add(self.m_scrolledWindow1, 1, wx.ALL | wx.EXPAND, 0)

        self.m_panel1.SetSizer(b_sizer2)
        self.m_panel1.Layout()
        b_sizer2.Fit(self.m_panel1)
        b_sizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 0)

        self.SetSizer(b_sizer1)
        self.Layout()
        self.m_menubar1 = wx.MenuBar(0)
        self.m_file = wx.Menu()
        self.m_open = wx.MenuItem(self.m_file, wx.ID_ANY, _(u"Open") + u"\t" + u"CTRL+O",
                                  wx.EmptyString, wx.ITEM_NORMAL)
        self.m_open.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_MENU))
        self.m_file.Append(self.m_open)

        self.m_saveas = wx.MenuItem(self.m_file, wx.ID_ANY, _(u"Save As") + u"\t" + u"CTRL+SHIFT+S",
                                    wx.EmptyString, wx.ITEM_NORMAL)
        self.m_saveas.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_MENU))
        self.m_file.Append(self.m_saveas)

        self.m_exit = wx.MenuItem(self.m_file, wx.ID_ANY, _(u"Exit") + u"\t" + u"CTRL+Q",
                                  wx.EmptyString, wx.ITEM_NORMAL)
        self.m_exit.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_QUIT, wx.ART_MENU))
        self.m_file.Append(self.m_exit)

        self.m_menubar1.Append(self.m_file, _(u"File"))

        self.m_help = wx.Menu()
        self.m_show_log = wx.MenuItem(self.m_help, wx.ID_ANY, _(u"Show Log"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_show_log.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_HELP_PAGE, wx.ART_MENU))
        self.m_help.Append(self.m_show_log)

        self.m_about = wx.MenuItem(self.m_help, wx.ID_ANY, _(u"About"), wx.EmptyString, wx.ITEM_NORMAL)
        self.m_about.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_TIP, wx.ART_MENU))
        self.m_help.Append(self.m_about)

        self.m_menubar1.Append(self.m_help, _(u"Help"))

        self.SetMenuBar(self.m_menubar1)

        self.m_statusBar1 = self.CreateStatusBar(1, 0, wx.ID_ANY)

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.event_close)
        self.display_choice.Bind(wx.EVT_CHOICE, self.chose_display)
        self.pos_offset_choice.Bind(wx.EVT_CHOICE, self.chose_pos_offset)
        self.pos_fb_choice.Bind(wx.EVT_CHOICE, self.chose_pos_fb)
        self.Bind(wx.EVT_MENU, self.event_open, id=self.m_open.GetId())
        self.Bind(wx.EVT_MENU, self.event_save_as, id=self.m_saveas.GetId())
        self.Bind(wx.EVT_MENU, self.event_close, id=self.m_exit.GetId())
        self.Bind(wx.EVT_MENU, self.show_log, id=self.m_show_log.GetId())
        self.Bind(wx.EVT_MENU, self.show_about, id=self.m_about.GetId())

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def event_close(self, event):
        event.Skip()

    def chose_display(self, event):
        event.Skip()

    def chose_pos_offset(self, event):
        event.Skip()

    def chose_pos_fb(self, event):
        event.Skip()

    def event_open(self, event):
        event.Skip()

    def event_save_as(self, event):
        event.Skip()

    def show_log(self, event):
        event.Skip()

    def show_about(self, event):
        event.Skip()
