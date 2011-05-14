#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, commands, os, os.path, pygtk, gtk

class MikunchApp:
    def __init__(self):
        # Set the Glade file
        self.gladefile = 'mikunchu.ui'
        self.wTree = gtk.Builder()
        self.wTree.add_from_file(os.path.join(os.path.dirname(__file__), self.gladefile))
        # Create our dictionary and connect it
        dic = { \
            "on_btnCancel_clicked" : self.on_btnCancel_clicked, \
            "on_btnOK_clicked" : self.on_btnOK_clicked,
            "on_TopLevel_destroy" : self.on_TopLevel_destroy \
            }
        self.wTree.connect_signals(dic)

        self.mainWindow = self.wTree.get_object("TopLevel")
        self.mainWindow.show_all()

    def on_TopLevel_destroy(self, widget):
        # ウィンドウを閉じてアプリケーションを終了する
        gtk.main_quit()

    def on_btnOK_clicked(self, widget):
        # ウィンドウを閉じてアプリケーションを終了する
        gtk.main_quit()

    def on_btnCancel_clicked(self,widget):
        # ウィンドウを閉じてアプリケーションを終了する
        gtk.main_quit()

if __name__ == "__main__":
    MikunchApp()
    gtk.main()
