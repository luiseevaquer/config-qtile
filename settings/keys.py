# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [
    # Log out; note that this doesn't use mod3: that's intentional in case mod3
    # gets hosed (which happens if you unplug and replug your usb keyboard
    # sometimes, or on ubuntu upgrades). This way you can still log back out
    # and in gracefully.

    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    Key([mod, "shift"], "h", lazy.layout.swap_left()),
    Key([mod, "shift"], "l", lazy.layout.swap_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "shift"], "space", lazy.layout.flip()),

    Key([mod], "k",              lazy.layout.down()),
    Key([mod], "j",              lazy.layout.up()),
    Key([mod], "space",          lazy.window.toggle_fullscreen()),
    Key([mod, "shift"], "Return",lazy.layout.toggle_split()),
    Key(["mod1"], "Tab",         lazy.nextlayout()),
    Key([mod, "mod1"], "h",      lazy.to_screen(0)),
    Key([mod, "mod1"], "l",      lazy.to_screen(1)),
    Key([mod, "control"], "x",   lazy.window.kill()),
    Key([mod], "e",              lazy.spawn("nautilus")),
    Key([mod, "control"], "r",   lazy.restart()),
    Key([mod, "shift"], "r",   lazy.restart()),
    Key([mod, "mod1"], "r",   lazy.restart()),
    Key([mod, "control"], "q",   lazy.shutdown()),
    Key(["shift", "mod1"], "q",  lazy.shutdown()),
    #Key([mod, "shift"], "p",  lazy.window.qtile.delete_group(lazy.window.qtile.current_group.name)),
    #Key([mod, "shift"], "p",  lazy.spawncmd()),

    # interact with prompts
    Key([mod], "r",              lazy.spawncmd()),
    Key([mod], "g",              lazy.switchgroup()),

    # Control the notify widget
    Key([mod], "y",              lazy.widget['notify'].toggle()),
    Key([mod, "mod1"], "y",         lazy.widget['notify'].prev()),
    Key([mod, "mod1"], "u",         lazy.widget['notify'].next()),

    # start specific apps
    Key([mod], "F1",             lazy.spawn("firefox")),
    Key([mod], "F2",             lazy.spawn("terminator")),
    Key([mod], "XF86Mail",       lazy.spawn("terminator")), 
    Key([mod, "control"], "XF86Mail",       lazy.spawn("killall terminator")), 
    #Key([mod, "control"], "F1",     lazy.spawn("killall /usr/lib/firefox/firefox")),
    Key([mod, "control"], "F2",     lazy.spawn("killall terminator")),
    Key([mod, "control"], "XF86Calculator",            lazy.spawn("killall gnome-calculator")),
    #Key([mod], "Music",              lazy.function(app_or_group("music", "spotify"))),
    Key([mod, "shift"], "t",             lazy.spawn("urxvt -letsp 1 -rv +sb")),
    Key([mod], "Print",         lazy.spawn("shutter")),

    # Change the volume if our keyboard has keys
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -c 1 set Headphone 5%+")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer -c 1 set Headphone 5%-")
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")
    ),

    Key([], "XF86HomePage",              lazy.spawn("firefox")),
    Key([mod], "XF86Messenger", lazy.spawn("zoom")),
    Key([mod], "XF86Tools", lazy.spawn("kodi")),

    Key([], "XF86Launch5", lazy.spawn("firefox-dev")), # Buttom 1 
    Key([mod, "control"], "XF86Launch5", lazy.spawn("killall /opt/firefox-dev/firefox-bin")), # Buttom 1 
    Key([mod, "control", "shift"], "F2", lazy.spawn("killall /opt/firefox-dev/firefox-bin")), # Buttom 1 
    Key([], "XF86Launch6", lazy.spawn("google-chrome")), # Buttom 2 
    Key([mod, "control"], "XF86Launch6", lazy.spawn("killall chrome")), # Buttom 2 
    Key([], "XF86Launch7", lazy.spawn("geany")), # Buttom 3 
    Key([mod, "control"], "XF86Launch7", lazy.spawn("killall geany")), # Buttom 3 
    Key([], "XF86Launch8", lazy.spawn("onlyoffice-desktopeditors")), # Buttom 4 
    Key([], "XF86Launch9", lazy.spawn("/home/lescobarvx/.config/qtile/freeram.sh")), # Buttom 5 
    Key([mod, "control", "shift"], "F5", lazy.spawn("/home/lescobarvx/.config/qtile/freeram.sh")), # Buttom 5 

    Key([], "XF86AudioPlay", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")),
    Key([], "XF86AudioNext", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")),
    Key([], "XF86AudioPrev", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")),

    Key([mod, "control"], "XF86HomePage",     lazy.spawn("killall /usr/lib/firefox/firefox")),
    Key([], "XF86Favorites",     lazy.spawn("code")),

    #Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("/home/lescobarvx/.config/qtile/bright_up.sh")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("/home/lescobarvx/.config/qtile/bright_down.sh")),
    Key(["control"], "XF86MonBrightnessUp", lazy.spawn("/home/lescobarvx/.config/qtile/bright_100.sh")),
    Key(["control"], "XF86MonBrightnessDown", lazy.spawn("/home/lescobarvx/.config/qtile/bright_0.sh")),
    Key([mod], "XF86AudioNext", lazy.spawn("/home/lescobarvx/.config/qtile/bright_up.sh")),
    Key([mod], "XF86AudioPrev", lazy.spawn("/home/lescobarvx/.config/qtile/bright_down.sh")),
    Key([mod, "control"], "XF86AudioNext", lazy.spawn("/home/lescobarvx/.config/qtile/bright_100.sh")),
    Key([mod, "control"], "XF86AudioPrev", lazy.spawn("/home/lescobarvx/.config/qtile/bright_0.sh")),
    Key([mod, "mod1"], "F12", lazy.spawn("/home/lescobarvx/.config/qtile/code_acer.sh")),
    Key([mod, "mod1"], "F11", lazy.spawn("/home/lescobarvx/.config/qtile/code_raditz.sh")),
]
