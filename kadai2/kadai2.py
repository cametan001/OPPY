#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os, os.path, pygtk, gtk, glib

imgs = ["img/miku-%d.png" % (i + 1) for i in range(39)]

class Kadai2:
    def __init__(self):
        self.gladefile = 'kadai2.ui'
        self.wTree = gtk.Builder()
        self.wTree.add_from_file(os.path.join(os.path.dirname (__file__), self.gladefile))
        dict = { 'on_TopLevel_destroy' : self.on_TopLevel_destroy }
        self.slide = self.wTree.get_object("Slide")
        self.wTree.connect_signals(dict)

        self.mainWindow = self.wTree.get_object('TopLevel')
        self.mainWindow.show_all()
        self.timeout = glib.timeout_add_seconds(1, self._timeout, self)

    def _timeout(self, event):
        self.slide = self.wTree.get_object('Slide')
        pixbuf = gtk.gdk.pixbuf_new_from_file(os.path.join(os.path.dirname(__file__), imgs.pop(0)))
        self.slide.set_from_pixbuf(pixbuf)
        return True

    def on_TopLevel_destroy(self, widget):
        gtk.main_quit()

if __name__ == '__main__':
    Kadai2()
    gtk.main()
