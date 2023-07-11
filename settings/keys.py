# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile keybindings

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"
shift = "shift"
alt = "mod1"
control = "control"

# EMBY VARIABLES
SERVER = "http://192.168.1.10"
PORT = "8096"
API = "aa5a3636ba5540099f001e81d3122619"
SESSION = "11f0b585ab09be1d51a70079d77d1c15"
HEADER = '-H "accept: */*" -H "Content-Type: application/json"'
#HEADER = '-H "accept: */*" -H "Content-Type: application/json" -d "{\"Command\":\"PlayPause\",\"SeekPositionTicks\":0,\"ControllingUserId\":\"string\"}"'

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
    Key([mod], "e",              lazy.spawn("sunflower")),
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
    Key([mod], "F2",             lazy.spawn("flatpak run org.wezfurlong.wezterm")),
    Key([], "XF86Mail",       lazy.spawn("/home/lescobarvx/Descargas/beeper-3.62.20.AppImage")), 
    Key([mod], "XF86Mail",       lazy.spawn("/home/lescobarvx/Descargas/beeper-3.62.20.AppImage")), 
    Key([mod, "control"], "XF86Mail",       lazy.spawn("killall wezterm-gui")), 
    #Key([mod, "control"], "F1",     lazy.spawn("killall /usr/lib/firefox/firefox")),
    Key([mod, "control"], "F2",     lazy.spawn("killall wezterm-gui")),
    Key([mod, "control"], "XF86Calculator",            lazy.spawn("killall gnome-calculator")),
    #Key([mod], "Music",              lazy.function(app_or_group("music", "spotify"))),
    Key([mod, "shift"], "t",             lazy.spawn("urxvt -letsp 1 -rv +sb")),
    Key([mod], "Print",         lazy.spawn("flameshot gui")),
    Key([mod, "control"], "Print",         lazy.spawn("flameshot screen -r")),
    Key(["control"], "space",         lazy.spawn("rofi -show drun")),

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

    Key([], "XF86Launch5", lazy.spawn("/opt/firefox/firefox")), # Buttom 1 
    Key([mod, "control"], "XF86Launch5", lazy.spawn("killall /opt/firefox/firefox-bin")), # Buttom 1 FIREFOX DEV
        Key([mod, "control", "shift"], "F2", lazy.spawn("killall /opt/firefox/firefox-bin")), # Buttom 1 FIREFOX DEV
    Key([], "XF86Launch6", lazy.spawn("google-chrome")), # Buttom 2 
    Key([mod, "control"], "XF86Launch6", lazy.spawn("killall chrome")), # Buttom 2 
    Key([], "XF86Launch7", lazy.spawn("wcm")), # Buttom 3 
    Key([mod, "control"], "XF86Launch7", lazy.spawn("killall wcm")), # Buttom 3 
    Key([], "XF86Launch8", lazy.spawn("onlyoffice-desktopeditors")), # Buttom 4 
    Key([], "XF86Launch9", lazy.spawn("/home/lescobarvx/.config/qtile/freeram.sh")), # Buttom 5 
    Key([mod, "control", "shift"], "F5", lazy.spawn("/home/lescobarvx/.config/qtile/freeram.sh")), # Buttom 5 
    
    # CONFIGURACION DE TECLAS PARA CONTROL DE LUCES ################################################################################################################################################

    Key(["control", "shift"], "XF86Launch5", lazy.spawn("/home/lescobarvx/.config/hass/service_hass.sh light toggle light.bulb_sala")), # Buttom 1 BOMBILLO SALA
    Key(["control", "shift"], "XF86Launch6", lazy.spawn("/home/lescobarvx/.config/hass/service_hass.sh light toggle light.bombillo_deborah")), # Buttom 2 BOMBILLO DEBORAH
    Key(["control", "shift"], "XF86Launch7", lazy.spawn("/home/lescobarvx/.config/hass/service_hass.sh light toggle light.cuarto_principal")), # Buttom 3 BOMBILLO SHAILL
    Key(["control", "shift"], "XF86Favorites", lazy.spawn("/home/lescobarvx/.config/hass/service_hass.sh light toggle light.luces_hogar")), # Buttom 3 BOMBILLO SHAILL

    Key([mod, "control", "shift"], "XF86AudioPlay", lazy.spawn("/home/lescobarvx/.config/hass/service_hass.sh light turn_on")), # ENCENDER TODOS LOS BOMBILLOS 
    Key([mod, "control", "shift"], "XF86AudioStop", lazy.spawn("/home/lescobarvx/.config/hass/service_hass.sh light turn_off")), # APAGAR TODOS LOS BOMBILLOS 
 
    Key([mod, "control", "shift"], "XF86Launch5", lazy.spawn("/home/lescobarvx/.config/hass/set_bulb_hass.sh light.bulb_sala")), 
    Key([mod, "control", "shift"], "XF86Launch6", lazy.spawn("/home/lescobarvx/.config/hass/set_bulb_hass.sh light.bombillo_deborah")), 
    Key([mod, "control", "shift"], "XF86Launch7", lazy.spawn("/home/lescobarvx/.config/hass/set_bulb_hass.sh light.cuarto_principal")), 
    Key([mod, "control", "shift"], "XF86Favorites", lazy.spawn("/home/lescobarvx/.config/hass/set_bulb_hass.sh light.luces_hogar")), 

    Key([mod, "control", "shift"], "w", lazy.spawn("/home/lescobarvx/.config/hass/light_hass.sh turn_on white 6500 100")), # ENCENDER TODOS LOS BOMBILLOS COLD WHITE
    Key([mod, "control", "shift"], "r", lazy.spawn("/home/lescobarvx/.config/hass/light_hass.sh turn_on red 100")), # ENCENDER TODOS LOS BOMBILLOS RED
    Key([mod, "control", "shift"], "b", lazy.spawn("/home/lescobarvx/.config/hass/light_hass.sh turn_on blue 100")), # ENCENDER TODOS LOS BOMBILLOS BLUE
    Key([mod, "control", "shift"], "g", lazy.spawn("/home/lescobarvx/.config/hass/light_hass.sh turn_on green 100")), # ENCENDER TODOS LOS BOMBILLOS GREEN
    Key([mod, "control", "shift"], "y", lazy.spawn("/home/lescobarvx/.config/hass/light_hass.sh turn_on yellow 100")), # ENCENDER TODOS LOS BOMBILLOS YELLOW
    Key([mod, "control", "shift"], "m", lazy.spawn("/home/lescobarvx/.config/hass/light_hass.sh turn_on magenta 100")), # ENCENDER TODOS LOS BOMBILLOS MAGENTA
    Key([mod, "control", "shift"], "c", lazy.spawn("/home/lescobarvx/.config/hass/light_hass.sh turn_on cyan 100")), # ENCENDER TODOS LOS BOMBILLOS CYAN
    Key([mod, "control", "shift"], "o", lazy.spawn("/home/lescobarvx/.config/hass/light_hass.sh turn_on orange 100")), # ENCENDER TODOS LOS BOMBILLOS ORANGE
    Key([mod, "control", "shift"], "p", lazy.spawn("/home/lescobarvx/.config/hass/light_hass.sh turn_on purple 100")), # ENCENDER TODOS LOS BOMBILLOS PURPLE
    Key([mod, "control", "shift"], "f", lazy.spawn("/home/lescobarvx/.config/hass/efect_light_hass.sh Beautiful")), # ENCENDER TODOS LOS BOMBILLOS EFECTO BEAUTIFUL
    Key([mod, "control", "shift"], "a", lazy.spawn("/home/lescobarvx/.config/hass/efect_light_hass.sh Rainbow")), # ENCENDER TODOS LOS BOMBILLOS EFECTO BEAUTIFUL
    
    Key([mod, "control", "shift"], "XF86AudioRaiseVolume", lazy.spawn("/home/lescobarvx/.config/hass/brightness_hass.sh step +10")), 
    Key([mod, "control", "shift"], "XF86AudioLowerVolume", lazy.spawn("/home/lescobarvx/.config/hass/brightness_hass.sh step -10")), 

    Key([mod, "control", "shift"], "XF86AudioNext", lazy.spawn("/home/lescobarvx/.config/hass/brightness_hass.sh fixed 255")), 
    Key([mod, "control", "shift"], "XF86AudioPrev", lazy.spawn("/home/lescobarvx/.config/hass/brightness_hass.sh fixed 1")), 

    # ################################################################################################################################################################################################

    Key([], "XF86AudioPlay", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")),

    Key([], "XF86AudioNext", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")),
    Key([], "XF86AudioPrev", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")),

    Key([mod], "XF86AudioPlay", lazy.spawn('curl -X POST "%s:%s/emby/Sessions/%s/Playing/PlayPause?api_key=%s" -H "accept: */*" -H "Content-Type: application/json" -d "{\"Command\":\"PlayPause\",\"SeekPositionTicks\":0,\"ControllingUserId\":\"string\"}"' % (SERVER, PORT, SESSION, API))),
    Key([mod], "XF86AudioNext", lazy.spawn('curl -X POST "%s:%s/emby/Sessions/%s/Playing/NextTrack?api_key=%s" -H "accept: */*" -H "Content-Type: application/json" -d "{\"Command\":\"NextTrack\",\"SeekPositionTicks\":0,\"ControllingUserId\":\"string\"}"' % (SERVER, PORT, SESSION, API))),
    Key([mod], "XF86AudioPrev", lazy.spawn('curl -X POST "%s:%s/emby/Sessions/%s/Playing/PreviousTrack?api_key=%s" -H "accept: */*" -H "Content-Type: application/json" -d "{\"Command\":\"PreviousTrack\",\"SeekPositionTicks\":0,\"ControllingUserId\":\"string\"}"' % (SERVER, PORT, SESSION, API))),
    Key([mod], "XF86AudioStop", lazy.spawn('curl -X POST "%s:%s/emby/Sessions/%s/Command/GoHome?api_key=%s" -H "accept: */*" -H "Content-Type: application/json" -d "{\"Command\":\"GoHome\"}"' % (SERVER, PORT, SESSION, API))),
    Key([mod, "control"], "XF86AudioStop", lazy.spawn('curl -X POST "%s:%s/emby/Sessions/%s/Command/GoToSettings?api_key=%s" -H "accept: */*" -H "Content-Type: application/json" -d "{\"Command\":\"GoToSettings\"}"' % (SERVER, PORT, SESSION, API))),
    #Key([], "XF86AudioNext", lazy.spawn('curl -X POST "{}:{}/emby/Sessions/{}/Playing/NextTrack?api_key={}" {} -d "{\"Command\":\"NextTrack\"}"'.format(SERVER, PORT, SESSION, API, HEADER))),
    #Key([], "XF86AudioPrev", lazy.spawn('curl -X POST "{}:{}/emby/Sessions/{}/Playing/PreviousTrack?api_key={}" {} -d "{\"Command\":\"PreviousTrack\"}"'.format(SERVER, PORT, SESSION, API, HEADER))),
    #Key([], "XF86AudioStop", lazy.spawn('curl -X POST "{}:{}/emby/Sessions/{}/Command/ToggleOsdMenu?api_key={}" {} -d "{\"Command\":\"ToggleOsdMenu\"}"'.format(SERVER, PORT, SESSION, API, HEADER))),
    Key([mod, "mod1"], "XF86AudioStop", lazy.spawn("ssh tecnodomotik@192.168.1.16 \"/home/tecnodomotik/.config/qtile/shutdown.sh\"")),

    Key([mod, "control"], "XF86HomePage",     lazy.spawn("killall /usr/lib/firefox/firefox")),
    Key([], "XF86Favorites",     lazy.spawn("kodi")),

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
