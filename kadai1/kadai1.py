#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, pygtk, gtk

class Kadai1:
    def __init__(self):
        self.gladefile = "kadai1.ui"
        self.wTree = gtk.Builder()
        self.wTree.add_from_file(os.path.join(os.path.dirname(__file__), self.gladefile))
        dic = {"on_TopLevel_destroy" : self.on_TopLevel_destroy}
        self.wTree.connect_signals(dic)
        self.mainWindow = self.wTree.get_object("TopLevel")
        self.mainWindow.show_all()

    def on_TopLevel_destroy(self, widget):
        gtk.main_quit()

if __name__ == '__main__':
    Kadai1()
    gtk.main()
