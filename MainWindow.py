import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, Gio


class MainWindow:
	def __init__(self, app):
		# Gtk Builder nesnesini oluşturduk
		self.builder = Gtk.Builder()

		# Builder'a glade'de hazırladığımız arayüzümüzü verdik
		self.builder.add_from_file("Example.glade")
		self.builder.connect_signals(self) # Signals kısmındaki metodlar bu sınıfın içine yazılacak.

		# Window
		self.window = self.builder.get_object("window") # Pencere elemanımıza eriştik
		self.dialog_about = self.builder.get_object("hakkinda")
		self.merhaba = self.builder.get_object("merhaba")
		self.window.set_application(app) # Penceremizin uygulamasını main.py'den aldığımız Gtk.Application'a ayarladık
        
		# Ekranı göster
		self.window.show_all()
    
	def on_tikla_clicked(self, button):
		self.merhaba.run()
		self.merhaba.hide()
	def on_kapat_clicked(self, button):
		self.window.get_application().quit()
	def on_about_clicked(self, button):
		self.dialog_about.run()
		self.dialog_about.hide()
