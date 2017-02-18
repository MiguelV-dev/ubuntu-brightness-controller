import os
import signal
import subprocess

from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

PATH = os.path.dirname(os.path.abspath(__file__)) + "/"

APPINDICATOR_ID = 'indicator-brightnesscontroller'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath(PATH + 'sun.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()


def build_menu():
    menu = gtk.Menu()
	
    value = 10
    while value <= 100:
        item_myapp = gtk.MenuItem("%3d%%" % value)
        item_myapp.connect('activate', brightness, (float(value) / 100))
        menu.append(item_myapp)
        value += 10 
    
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)

    menu.show_all()
    return menu
    
def brightness(self, value):
    command = 'xrandr --listmonitors | grep -o "[[:alnum:]_-]*$" | tail -n +2'
    result = subprocess.check_output(command, shell=True)
    monitors = filter(None, result.split('\n'))
    for monitor in monitors:
        os.system("xrandr --output " + monitor + " --brightness " + str(value))
    return brightness

def quit():
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()


