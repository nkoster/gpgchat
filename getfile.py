import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class GetFile(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Choose a File")

        origin = os.path.dirname(os.path.realpath(__file__))

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.progressbar = Gtk.ProgressBar()
        vbox.pack_start(self.progressbar, True, True, 0)

        image = Gtk.Image.new_from_file(origin + '/upload.png')
        vbox.add(image)

        self.timeout_id = GObject.timeout_add(5, self.on_timeout, None)
        self.activity_mode = False

        self.label1 = Gtk.Label('<No file selected>')
        vbox.add(self.label1)

        button1 = Gtk.Button("Choose File")
        button1.connect("clicked", self.on_file_clicked)
        vbox.add(button1)

        self.t = 0.0005
        self.forward = True
        
    def on_timeout(self, user_data):
        if self.activity_mode:
            self.progressbar.pulse()
        else:
            new_value = self.progressbar.get_fraction() + self.t
            if new_value > 1:
                self.t = -0.0005
                if self.forward:
                    self.progressbar.set_inverted(True)
                    self.forward = False
                else:
                    self.progressbar.set_inverted(False)
                    self.forward = True
            if new_value < 0:
                self.t = 0.0005
            #self.progressbar.pulse()
            self.progressbar.set_fraction(new_value)
        return True

    def on_file_clicked(self, data):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        self.add_filters(dialog)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            #print("Open clicked")
            print(dialog.get_filename())
            self.label1.set_text(dialog.get_filename())
            Gtk.main_quit()
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()

    def add_filters(self, dialog):
        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

win = GetFile()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

