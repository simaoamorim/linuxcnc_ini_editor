# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"INI Editor"), pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 400,400 ), wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel5 = wx.Panel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self.m_panel5, wx.ID_ANY, _(u"[DISPLAY]"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetToolTip( _(u"Display Section") )

        bSizer10.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.m_staticline1 = wx.StaticLine( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer10.Add( self.m_staticline1, 1, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer9.Add( bSizer10, 0, wx.EXPAND, 5 )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.st_interface = wx.StaticText( self.m_panel5, wx.ID_ANY, _(u"Display:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.st_interface.SetLabelMarkup( _(u"Display:") )
        self.st_interface.Wrap( -1 )

        self.st_interface.SetToolTip( _(u"User interface to use") )
        self.st_interface.SetMinSize( wx.Size( 50,-1 ) )

        bSizer8.Add( self.st_interface, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        display_choiceChoices = [ wx.EmptyString, _(u"Axis"), _(u"Gmoccapy"), _(u"Touchy"), _(u"Gscreen"), _(u"keystick"), _(u"tklinuxcnc"), _(u"xemc") ]
        self.display_choice = wx.Choice( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, display_choiceChoices, 0 )
        self.display_choice.SetSelection( 0 )
        bSizer8.Add( self.display_choice, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer9.Add( bSizer8, 0, wx.EXPAND, 5 )

        bSizer81 = wx.BoxSizer( wx.HORIZONTAL )

        self.st_interface1 = wx.StaticText( self.m_panel5, wx.ID_ANY, _(u"Coordinate Type:"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.st_interface1.SetLabelMarkup( _(u"Coordinate Type:") )
        self.st_interface1.Wrap( -1 )

        self.st_interface1.SetToolTip( _(u"Coordinate system to show on the DRO") )

        bSizer81.Add( self.st_interface1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        pos_offset_choiceChoices = [ wx.EmptyString, _(u"Relative"), _(u"Machine") ]
        self.pos_offset_choice = wx.Choice( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pos_offset_choiceChoices, 0 )
        self.pos_offset_choice.SetSelection( 0 )
        bSizer81.Add( self.pos_offset_choice, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        pos_fb_choiceChoices = [ wx.EmptyString, _(u"Commanded"), _(u"Actual") ]
        self.pos_fb_choice = wx.Choice( self.m_panel5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, pos_fb_choiceChoices, 0 )
        self.pos_fb_choice.SetSelection( 0 )
        bSizer81.Add( self.pos_fb_choice, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


        bSizer9.Add( bSizer81, 0, wx.EXPAND, 5 )


        self.m_panel5.SetSizer( bSizer9 )
        self.m_panel5.Layout()
        bSizer9.Fit( self.m_panel5 )
        bSizer6.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer4.Add( bSizer6, 1, wx.EXPAND, 5 )


        self.m_scrolledWindow1.SetSizer( bSizer4 )
        self.m_scrolledWindow1.Layout()
        bSizer4.Fit( self.m_scrolledWindow1 )
        bSizer2.Add( self.m_scrolledWindow1, 1, wx.ALL|wx.EXPAND, 0 )


        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )


        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_menubar1 = wx.MenuBar( 0 )
        self.m_file = wx.Menu()
        self.m_open = wx.MenuItem( self.m_file, wx.ID_ANY, _(u"Open")+ u"\t" + u"CTRL+O", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_open.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_MENU ) )
        self.m_file.Append( self.m_open )

        self.m_saveas = wx.MenuItem( self.m_file, wx.ID_ANY, _(u"Save As")+ u"\t" + u"CTRL+SHIFT+S", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_saveas.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FILE_SAVE_AS, wx.ART_MENU ) )
        self.m_file.Append( self.m_saveas )

        self.m_exit = wx.MenuItem( self.m_file, wx.ID_ANY, _(u"Exit")+ u"\t" + u"CTRL+Q", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_exit.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_QUIT, wx.ART_MENU ) )
        self.m_file.Append( self.m_exit )

        self.m_menubar1.Append( self.m_file, _(u"File") )

        self.m_help = wx.Menu()
        self.m_show_layout = wx.MenuItem( self.m_help, wx.ID_ANY, _(u"Show configuration layout"), wx.EmptyString, wx.ITEM_NORMAL )
        self.m_show_layout.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_HELP_BOOK, wx.ART_MENU ) )
        self.m_help.Append( self.m_show_layout )

        self.m_menubar1.Append( self.m_help, _(u"Help") )

        self.SetMenuBar( self.m_menubar1 )


        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.event_close )
        self.display_choice.Bind( wx.EVT_CHOICE, self.chose_display )
        self.pos_offset_choice.Bind( wx.EVT_CHOICE, self.chose_pos_offset )
        self.pos_fb_choice.Bind( wx.EVT_CHOICE, self.chose_pos_fb )
        self.Bind( wx.EVT_MENU, self.event_open, id = self.m_open.GetId() )
        self.Bind( wx.EVT_MENU, self.event_save_as, id = self.m_saveas.GetId() )
        self.Bind( wx.EVT_MENU, self.event_close, id = self.m_exit.GetId() )
        self.Bind( wx.EVT_MENU, self.print_config, id = self.m_show_layout.GetId() )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def event_close( self, event ):
        event.Skip()

    def chose_display( self, event ):
        event.Skip()

    def chose_pos_offset( self, event ):
        event.Skip()

    def chose_pos_fb( self, event ):
        event.Skip()

    def event_open( self, event ):
        event.Skip()

    def event_save_as( self, event ):
        event.Skip()


    def print_config( self, event ):
        event.Skip()


###########################################################################
## Class terminal_frame
###########################################################################

class terminal_frame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Terminal"), pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer9 = wx.BoxSizer( wx.VERTICAL )

        bSizer10 = wx.BoxSizer( wx.VERTICAL )

        self.m_output = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY )
        bSizer10.Add( self.m_output, 1, wx.ALL|wx.EXPAND, 0 )


        bSizer9.Add( bSizer10, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer9 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.onClose )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def onClose( self, event ):
        event.Skip()


