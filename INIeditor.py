#!/usr/bin/env python3
import sys
import os
import wx
import fb.GUI as GUI
import configparser

class window ( GUI.MainFrame ) :
    def __init__ ( self, parent ) :
        GUI.MainFrame.__init__( self, parent )
        self.logWindow = wx.LogWindow( pParent=self, szTitle='Log', show=False )
        self.config = configparser.ConfigParser()
        with open("res/struct.ini", 'r') as conf :
            try :
                self.config.read_file( f = conf )
            except Exception as e :
                wx.LogError( "Error occured: %s" % e )
            finally :
                conf.close()

    def show_about( self, event ) :
        event.Skip()

    def hide_about( self, event ) :
        evvent.Skip()

    def show_log( self, event ) :
        self.logWindow.Show()

    def event_close ( self, event ) :
        self.Destroy()
        raise SystemExit

    def event_save_as( self, event ) :
        with wx.FileDialog( parent = self, message = "Select file",
                           wildcard = "*.ini",
                           style = wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT ) as fileDialog :
            if fileDialog.ShowModal() == wx.ID_CANCEL :
                return
            file = fileDialog.GetPath()
            with open( file, 'w' ) as f :
                try :
                    self.config.write( fp = f, space_around_delimiters = True )
                    f.close()
                except IOError :
                    wx.LogError( "Could not open file '%s'" % file)

    def set_interface( self ) :
        self.display_choice.SetSelection(
            self.display_choice.FindString(
                self.config.get( 'DISPLAY', 'display' )
            )
        )
        self.pos_offset_choice.SetSelection(
            self.pos_offset_choice.FindString(
                self.config.get( 'DISPLAY', 'position_offset' ) ) )
        self.pos_fb_choice.SetSelection(
            self.pos_fb_choice.FindString(
                self.config.get( 'DISPLAY', 'position_feedback' )
            )
        )


    def event_open( self, event ) :
        with wx.FileDialog( parent = self,
                           message = "Open File",
                           wildcard = "*.ini",
                           style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST ) as fileDialog :
            if fileDialog.ShowModal() == wx.ID_CANCEL :
                return
            file = fileDialog.GetPath()
            try :
                with open( file, 'r' ) as f :
                    self.config.read_file( f = f )
                    f.close()
                    self.set_interface()
            except IOError :
                wx.LogError( "Could not open file '%s'" % file)


    def chose_display( self, event ) :
        item = self.display_choice.GetString(
                self.display_choice.GetSelection()
            ).lower()
        self.config.set( section = 'DISPLAY',
                         option = 'display',
                         value = item )
        wx.LogDebug( "'DISPLAY'.'display' set to '%s'" % item )

    def chose_pos_offset( self, event ) :
        item = self.pos_offset_choice.GetString(
                self.pos_offset_choice.GetSelection()
            ).lower()
        self.config.set( section = 'DISPLAY',
                         option = 'position_offset',
                         value = item )
        wx.LogDebug( "'DISPLAY'.'position_offset' set to '%s'" % item )

    def chose_pos_fb( self, event ) :
        item = self.pos_fb_choice.GetString(
                self.pos_fb_choice.GetSelection()
            ).lower()
        self.config.set( section = 'DISPLAY',
                         option = 'position_feedback',
                         value = item )
        wx.LogDebug( "'DISPLAY'.'position_feedback' set to '%s'" % item )

if __name__ == "__main__" :
    app = wx.App( redirect=False )
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    window = window( None )
    window.Show( True )
    app.MainLoop()
