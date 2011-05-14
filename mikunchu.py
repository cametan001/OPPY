#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys, commands, os, os.path, pygtk, gtk

## インストールコマンド群
installCommands = (
    ("gksudo add-apt-repository ppa:khf03353/ppa-kaorin",
     "gksudo apt-get update",
     'gksudo "apt-get -y install mikutube"'), # 一つ目のチェックボックスのコマンド群
    ("gksudo add-apt-repository ppa:khf03353/ppa-kaorin",
     "gksudo apt-get update",
     'gksudo "apt-get -y install mikukabe"'), # 二つ目のチェックボックスのコマンド群
    ("gksudo add-apt-repository ppa:khf03353/ppa-kaorin",
     "gksudo apt-get update",
     'gksudo "apt-get -y install mikukabe"') # 三つ目以降は、このように増やしていく
    )

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
        self.chkMikutube = self.wTree.get_object("chkMikutube")
        self.chkMikukabe = self.wTree.get_object("chkMikukabe")
        self.wTree.connect_signals(dic)

        self.mainWindow = self.wTree.get_object("TopLevel")
        self.mainWindow.show_all()

    def on_TopLevel_destroy(self, widget):
        # ウィンドウを閉じてアプリケーションを終了する
        gtk.main_quit()

    def on_btnOK_clicked(self, widget):
        # 適用を行ってアプリケーションを終了する
        if self.chkMikutube.get_active:
            # みくつべ♪インストールコマンドを実行
            [self.execCommand(cmd) for cmd in installCommands[0]]
        if self.chkMikutube.get_active:
            # みくかべ♪インストールコマンドを実行
            [self.execCommand(cmd) for cmd in installCommands[1]]
        # ウィンドウを閉じてアプリケーションを終了する
        gtk.main_quit()

    def on_btnCancel_clicked(self,widget):
        # ウィンドウを閉じてアプリケーションを終了する
        gtk.main_quit()

    def execCommand(self, command):
        print command                   # 受け渡されたコマンドのデバッグ用プリント
        ret = commands.getoutput(command)
        print ret                       # 実行結果のデバッグ用プリント
        return ret

if __name__ == "__main__":
    MikunchApp()
    gtk.main()
