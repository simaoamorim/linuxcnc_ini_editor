#!/usr/bin/env python3
import sys
import os
import wx
import fb.GUI as GUI
import configparser

class terminal ( GUI.terminal_frame ) :
    def __init__ ( self, parent ) :
        GUI.terminal_frame.__init__( self, parent )

    def write( self, text ) :
        self.m_output.WriteText( text )

    def flush( self ) :
        pass

    def onClose( self, event ) :
        self.m_output.SetValue('')
        self.Hide()

class window ( GUI.MainFrame ) :
    def __init__ ( self, parent ) :
        GUI.MainFrame.__init__( self, parent )
        self.log = terminal( None )
        self.config = configparser.ConfigParser()
        with open("res/struct.ini", 'r') as conf :
            try :
                self.config.read_file( f = conf )
            except Exception as e :
                wx.LogError( "Error occured: %s" % e )
            finally :
                conf.close()

    def print_config( self, event ) :
        self.log.Show( True )
        for section in self.config.sections() :
            print('[%s]' % section, file=self.log )
            for option in self.config.options( section ) :
                print('\t%s = %s' % ( option, self.config.get( section, option ) ), file=self.log )

    def event_close ( self, event ) :
        self.log.Destroy()
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
        self.config.set( section = 'DISPLAY', option = 'display',
                        value = self.display_choice.GetString(
                            self.display_choice.GetSelection() ).lower() )

    def chose_pos_offset( self, event ) :
        self.config.set( section = 'DISPLAY', option = 'position_offset',
                        value = self.pos_offset_choice.GetString(
                            self.pos_offset_choice.GetSelection() ).lower() )

    def chose_pos_fb( self, event ) :
        self.config.set( section = 'DISPLAY', option = 'position_feedback',
                        value = self.pos_fb_choice.GetValue() )

if __name__ == "__main__" :
    app = wx.App( redirect=False )
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    window = window( None )
    window.Show( True )
    app.MainLoop()
