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
            try :
                with open( file, 'w' ) as f :
                    f.seek( 0, 0 )
                    f.close()
            except IOError :
                wx.LogError( "Could not open file '%s'" % file)

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
                    f.seek( 0, 0 )
                    while True:
                        line = f.readline()
                        if line.startswith('[') or line.startswith('\n') or not line :
                            print("Passing line '%s'" % line)
                        else :
                            break
                    print("First line: %s" % line)
                    f.close()
            except IOError :
                wx.LogError( "Could not open file '%s'" % file)

if __name__ == "__main__" :
    app = wx.App( redirect=False )
    locale = wx.Locale(wx.LANGUAGE_ENGLISH)
    window = window( None )
    window.Show( True )
    app.MainLoop()
