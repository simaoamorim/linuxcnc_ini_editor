#!/usr/bin/env python3
import sys
import os
import wx
import fb.GUI as GUI

class window ( GUI.MainFrame ) :
    def __init__ ( self, parent ) :
        GUI.MainFrame.__init__( self, parent )

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
            try :
                with open( file, 'w' ) as f :
                    f.seek( 0, 0 )
                    f.write("[DISPLAY]\n\n")
                    f.write("DISPLAY = %s\n" % self.display_choice.GetString( self.display_choice.GetSelection() ).lower() )
                    f.write("POSITION_OFFSET = %s\n" % self.pos_offset_choice.GetString( self.pos_offset_choice.GetSelection() ).lower() )
                    f.write("POSITION_FEEDBACK = %s\n" % self.pos_fb_choice.GetString( self.pos_fb_choice.GetSelection() ).lower() )
                    f.flush()
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
