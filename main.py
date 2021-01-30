#!/usr/bin/env python3

import sys

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio

from MainWindow import MainWindow

class Uygulama(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,
            application_id="tr.org.pardus.ornek-uygulama",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
            **kwargs)
    
    def do_activate(self): # do_active metodu program açıldığında çalışır.
        self.window = MainWindow(self) # MainWindow nesnemizi oluşturduk.
        # Burada sadece oluşturmamız yeterli çünkü göstermeyi MainWindow'un içinde yaptık.

# Uygulama nesnemizi olusturup calistiralim.
app = Uygulama()
app.run(sys.argv)
