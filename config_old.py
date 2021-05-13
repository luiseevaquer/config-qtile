try:
    from libqtile.manager import Key, Group, Click, Drag, Screen, Match
except ImportError:
    from libqtile.config import Key, Group, Click, Drag, Screen, Match
from libqtile.command import lazy
from libqtile.layout.base import Layout
from libqtile import layout, bar, widget, hook

import platform
import sys
import subprocess
import os


mod = "mod4"
modkey = mod

count_screen = os.popen("xrandr | grep '*'").read().count('\n')

# global font options
# widget_defaults = dict(
#     font = 'Anonymous Pro',
#     fontsize = 18,
#     padding = 3,
# )

class Battery(widget.Battery):
	def _get_text(self):
		info = self._get_info()
		if info is False:
			return '---'
		if info['full']:
			no = int(info['now'] / info['full'] * 9.999)
		else:
			no = 0
		if info['stat'] == 'Discharging':
			char = self.discharge_char
			if no < 2:
				self.layout.colour = self.low_foreground
			else:
				self.layout.colour = self.foreground
		elif info['stat'] == 'Charging':
			char = self.charge_char
		#elif info['stat'] == 'Unknown':
		else:
			char = '■'
		return '{}{}{}'.format(char, no, 'B')#chr(0x1F506))

if count_screen == 2:
    screens = [
        Screen(
            bottom=bar.Bar([
                widget.TaskList(highlight_method='block',),
                widget.KeyboardLayout(configured_keyboards=['us', 'latam', 'es']),
                widget.DF(visible_on_warn=False, measure='G', warn_space=5, format=' {uf}{m} | {r:.0f}% '),
                widget.ThermalSensor(),
                widget.BatteryIcon(),
                widget.Battery(fontsize=10),
                ], 24,),
            top = bar.Bar([
                widget.GroupBox(
                    urgent_alert_method='text',
                    highlight_method='block',
                    inactive='999999'),
                widget.Prompt(
                    prompt="run: ",
                ),
                #widget.WindowName(foreground='00FFFF'),
                widget.Spacer(),
                widget.CapsNumLockIndicator(),
                widget.Systray(),
                #widget.Volume(update_interval=0.2, cardid=1, emoji=True),
                widget.Clock(format='|| %a %b %d || %H:%M'),
                widget.TextBox(text=" "),
                ], 24,),
        ),
        Screen(
            bottom=bar.Bar([
                widget.TaskList(highlight_method='block',),
                #widget.Mpris2(objname='org.mpris.MediaPlayer2.spotify', name='spotify'),
                widget.BatteryIcon(),
                widget.Battery(fontsize=10),
                ], 24,),
            top = bar.Bar([
                widget.GroupBox(
                    urgent_alert_method='text',
                    highlight_method='block',
                    inactive='999999'),
                widget.Spacer(),
                #widget.WindowName(foreground='00FFFF'),
                widget.Notify(foreground="FF0000", fontsize=12, font="Anonymous Pro"),
                widget.Clock(format=' %a %b %d || %H:%M'),
                #widget.Clock('%Y-%m-%d %a %H:%M %p'),
                ], 24,),
        ),
    ]
else:
    # 1 screen
    screens = [
        Screen(top = bar.Bar([
                widget.GroupBox(urgent_alert_method='text'),
                widget.Prompt(
                    prompt="run: ",
                ),
                widget.WindowName(foreground='00FFFF'),
                widget.Notify(foreground="FF0000", fontsize=12, font="Anonymous Pro"),
                widget.CapsNumLockIndicator(),
                widget.KeyboardLayout(configured_keyboards=['us', 'latam', 'es']),
                widget.Systray(),
                widget.Clock(format='%a %b %d, %H:%M'),
                widget.TextBox(text=" "),
                widget.BatteryIcon(),
                widget.Battery(fontsize=10),
            ], 24,),
        )
    ]

keys = [
    # Log out; note that this doesn't use mod3: that's intentional in case mod3
    # gets hosed (which happens if you unplug and replug your usb keyboard
    # sometimes, or on ubuntu upgrades). This way you can still log back out
    # and in gracefully.

    Key([modkey], "h", lazy.layout.left()),
    Key([modkey], "l", lazy.layout.right()),
    Key([modkey, "shift"], "h", lazy.layout.swap_left()),
    Key([modkey, "shift"], "l", lazy.layout.swap_right()),
    Key([modkey, "shift"], "j", lazy.layout.shuffle_down()),
    Key([modkey, "shift"], "k", lazy.layout.shuffle_up()),
    Key([modkey], "i", lazy.layout.grow()),
    Key([modkey], "m", lazy.layout.shrink()),
    Key([modkey], "n", lazy.layout.normalize()),
    Key([modkey], "o", lazy.layout.maximize()),
    Key([modkey, "shift"], "space", lazy.layout.flip()),

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

    # interact with prompts
    Key([mod], "r",              lazy.spawncmd()),
    Key([mod], "g",              lazy.switchgroup()),

    # Control the notify widget
    Key([mod], "y",              lazy.widget['notify'].toggle()),
    Key([mod, "mod1"], "y",         lazy.widget['notify'].prev()),
    Key([mod, "mod1"], "u",         lazy.widget['notify'].next()),

    # start specific apps
    Key([mod, "control"], "F1",             lazy.spawn("firefox")),
    Key([mod, "control"], "F2",             lazy.spawn("terminator")),
    Key([], "XF86Calculator",            lazy.spawn("gnome-calculator")),
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
    Key(
        [mod], "XF86AudioMute",
        lazy.spawn("pavucontrol")
    ),

    Key([mod], "XF86Mail", lazy.spawn("terminator")), 
    Key([], "XF86HomePage",              lazy.spawn("firefox")),
    Key([], "XF86Messenger", lazy.spawn("zoom")),
    Key([], "XF86Tools", lazy.spawn("spotify")),
    Key([mod], "XF86Tools", lazy.spawn("kodi")),

    Key([], "XF86Launch5", lazy.spawn("firefox-dev")), # Buttom 1 
    Key([mod, "control"], "XF86Launch5", lazy.spawn("killall /opt/firefox-dev/firefox-bin")), # Buttom 1 
    Key([mod, "control", "shift"], "F2", lazy.spawn("killall /opt/firefox-dev/firefox-bin")), # Buttom 1 
    Key([], "XF86Launch6", lazy.spawn("google-chrome")), # Buttom 2 
    Key([mod, "control"], "XF86Launch6", lazy.spawn("killall chrome")), # Buttom 2 
    Key([], "XF86Launch7", lazy.spawn("epiphany-browser")), # Buttom 3 
    Key([mod, "control"], "XF86Launch7", lazy.spawn("killall epiphany-browser")), # Buttom 3 
    Key([], "XF86Launch8", lazy.spawn("libreoffice --calc")), # Buttom 4 
    Key([], "XF86Launch9", lazy.spawn("/home/lescobarvx/.config/qtile/freeram.sh")), # Buttom 5 
    Key([mod, "control", "shift"], "F5", lazy.spawn("/home/lescobarvx/.config/qtile/freeram.sh")), # Buttom 5 

    Key([], "XF86AudioPlay", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause")),
    Key([], "XF86AudioNext", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next")),
    Key([], "XF86AudioPrev", lazy.spawn("dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous")),

    Key([mod, "mod1"], "F1",     lazy.spawn("killall /usr/lib/firefox/firefox")),
    Key([mod, "control"], "XF86HomePage",     lazy.spawn("killall /usr/lib/firefox/firefox")),
    Key([mod, "control", "shift"], "F1",     lazy.spawn("killall /usr/lib/firefox/firefox")),
    Key([mod], "XF86Favorites",     lazy.spawn("xscreensaver-command --restart")),

    #Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("/home/lescobarvx/.config/qtile/bright_up.sh")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("/home/lescobarvx/.config/qtile/bright_down.sh")),
    Key(["control"], "XF86MonBrightnessUp", lazy.spawn("/home/lescobarvx/.config/qtile/bright_100.sh")),
    Key(["control"], "XF86MonBrightnessDown", lazy.spawn("/home/lescobarvx/.config/qtile/bright_0.sh")),
    Key([mod], "XF86AudioNext", lazy.spawn("/home/lescobarvx/.config/qtile/bright_up.sh")),
    Key([mod], "XF86AudioPrev", lazy.spawn("/home/lescobarvx/.config/qtile/bright_down.sh")),
    Key([mod, "control"], "XF86AudioNext", lazy.spawn("/home/lescobarvx/.config/qtile/bright_100.sh")),
    Key([mod, "control"], "XF86AudioPrev", lazy.spawn("/home/lescobarvx/.config/qtile/bright_0.sh")),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# Next, we specify group names, and use the group name list to generate an appropriate
# set of bindings for group switching.
groups = []

# throwaway groups for random stuff
for i in ['a', 's', 'd', 'f', 'g', 'h']:
    if i == 'a':
        groups.append(Group(i, spawn='urxvt -letsp 1 -rv +sb -e htop', layout='monadwide'))
        groups.append(Group(i, spawn='urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/pping.sh  9.9.9.9', layout='monadwide'))
        groups.append(Group(i, spawn='urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/pping.sh google.com', layout='monadwide'))
        groups.append(Group(i, spawn='urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/pping.sh 64.6.64.6', layout='monadwide'))
        groups.append(Group(i, spawn='urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/pping.sh 84.200.69.80', layout='monadwide'))
        #groups.append(Group(i, spawn='urxvt -letsp 1 -rv +sb -e cmatrix -a -b -C blue', layout='monadwide'))
        #groups.append(Group(i, spawn='urxvt -letsp 1 -rv +sb -e neofetch', layout='stack'))
    elif i in ['s', 'd']:
        groups.append(Group(i, layout='stack'))
    else:
        groups.append(Group(i, layout='max'))
    keys.append(
        Key([mod], i, lazy.group[i].toscreen())
    )
    keys.append(
        Key([mod, "mod1"], i, lazy.window.togroup(i))
    )

# groups with special jobs. I usually navigate to these via my app_or_group
# function.
groups.extend([
    Group('tools', layout='max', persist=False, init=False,
          matches=[Match(wm_class=['nautilus','Nautilus', 'gnome-calculator', 'Calculadora', 'Calculator', 'pavucontrol', 'Control de Volumen'])]),
    Group('music', layout='max', persist=False, init=False,
          matches=[Match(wm_class=['/snap/spotify/41/usr/share/spotify/spotify'])]),
    Group('video', layout='max', persist=False, init=False,
          matches=[Match(wm_class=['kodi-bin', 'kodi', 'Kodi'])]),
    Group('meet', layout='max', persist=False, init=False,
          matches=[Match(wm_class=['zoom', 'meeting'])]),
    Group('www', layout='max', persist=False, init=False,
          matches=[Match(wm_class=['Firefox', 'Firefox Developer Edition', 'TorBrowser', 'google-chrome', 'Google-chrome', 'epiphany', 'epiphany-browser', 'Epiphany'])]),
    Group('dev', persist=False, layout='max', init=False,
          matches=[Match(wm_class=['code', 'VSCode', 'vscode', 'geany'])]),
    Group('term', persist=False, layout='verticaltile', init=False,
          matches=[Match(wm_class=['terminator', 'Terminator'])]),
    Group('others', layout='verticaltile', persist=False, init=False,
          matches=[Match(wm_class=['shutter'])]),
    Group('ssavers', layout='max', persist=False, init=False,
          matches=[Match(wm_class=['cmatrix'])]),
    Group('office', layout='verticaltile', persist=False, init=False,
          matches=[Match(wm_class=['libreoffice', 'libreoffice-calc'])]),
])

esp_groups = {
   'w': 'www',
   't': 'tools',
   'x': 'dev', 
   'm': 'music', 
   'v': 'video', 
   'q': 'term',
   'l': 'office',
   'o': 'others',
}

for i in ['w', 't', 'x', 'm', 'q', 'l', 'o', 'v']:
    keys.append(
        Key([mod], i, lazy.group[esp_groups[i]].toscreen())
    )
    keys.append(
        Key([mod, "mod1"], i, lazy.window.togroup(esp_groups[i]))
    )
 
border_args = dict(
    border_width=1,
)

layouts = [
    layout.Stack(stacks=2, **border_args),
    layout.MonadTall(),
    layout.MonadWide(max_ratio=0.50,border_focus='#000000'),
    layout.VerticalTile(),
    layout.Tile(),
    layout.Max(),
    layout.Matrix(),

#    # a layout just for gimp
#    layout.Slice('left', 192, name='gimp', role='gimp-toolbox',
#         fallback=layout.Slice('right', 256, role='gimp-dock',
#         fallback=layout.Stack(stacks=1, **border_args))),
# 
#    # a layout for pidgin
#    layout.Slice('right', 256, name='pidgin', role='buddy_list',
#         fallback=layout.Stack(stacks=1, **border_args)),
]

# Automatically float these types. This overrides the default behavior (which
# is to also float utility types), but the default behavior breaks our fancy
# gimp slice layout specified later on.
floating_layout = layout.Floating(auto_float_types=[
  "notification",
  "toolbar",
  "splash",
  "dialog",
])

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])
