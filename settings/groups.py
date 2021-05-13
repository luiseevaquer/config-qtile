# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Qtile workspaces

from libqtile import layout
from libqtile.config import Key, Group, Match, ScratchPad, DropDown
from libqtile.command import lazy
from settings.keys import mod, keys

groups_dict = {
    'command': {'label': "   ", 'pos': 1,},
    'browser': {'label': "   ",'pos': 2,},
    'terminal': {'label': "  ", 'pos': 3,},
    'code': {'label': "   ", 'pos': 4,},
    'multimedia': {'label': "   ", 'pos': 5,},
    'explorer': {'label': "   ", 'pos': 6,},
    'stack': {'label': "   ", 'pos': 7,},
    'tools': {'label': "   ", 'pos': 8,},
    'scratchpad': {'label': " x  ", 'pos': 9,},
}

groups = []

for i in groups_dict.keys():
    if i == 'command':
        groups.append(Group(i, label=groups_dict[i]['label'], position=groups_dict[i]['pos'], exclusive=True,
            spawn=[
            'urxvt -letsp 1 -rv +sb -e htop', 
            'urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/pping.sh google.com',
            # 'urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/mtr --displaymode 2  9.9.9.9',
            'urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/pping.sh raditz.vauxoo.com', 
            'urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/pping.sh 9.9.9.9'], layout='monadwide'))
    elif i == 'browser':
        groups.append(Group(i, label=groups_dict[i]['label'], position=groups_dict[i]['pos'], exclusive=True, 
            matches=[Match(wm_class=['Firefox', 'Firefox Developer Edition', 'TorBrowser', 'google-chrome', 'Google-chrome', 'epiphany', 'epiphany-browser', 'Epiphany'])]))
    elif i == 'terminal':
        groups.append(Group(i, label=groups_dict[i]['label'], position=groups_dict[i]['pos'], exclusive=True,
            matches=[Match(wm_class=['terminator', 'Terminator', 'urxvt', 'URxvt'])]))
    elif i == 'code':
        groups.append(Group(i, label=groups_dict[i]['label'], position=groups_dict[i]['pos'], exclusive=True,
            matches=[Match(wm_class=['code', 'VSCode', 'vscode', 'geany', 'Geany', 'gedit'])]))
    elif i == 'explorer':
        groups.append(Group(i, label=groups_dict[i]['label'], position=groups_dict[i]['pos'], exclusive=True,
            matches=[Match(wm_class=['nautilus','Nautilus', 'gnome-calculator', 'Calculadora', 'Calculator'])]))
    elif i == 'scratchpad':
        groups.append(ScratchPad(i, [
                DropDown("show_ip", "urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/show_ip.sh", on_focus_lost_hide=False),
                DropDown("switch_pns", "urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/switch_pns.sh", on_focus_lost_hide=False),
                DropDown("switch_inter", "urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/switch_inter.sh", on_focus_lost_hide=False),
                DropDown("speedtest", "urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/speedtest.sh", on_focus_lost_hide=False),
                DropDown("change_network", "urxvt -letsp 1 -rv +sb -e /home/lescobarvx/.config/qtile/change_network.sh", on_focus_lost_hide=False, width=0.7, height=0.8),
                DropDown("telegram-desktop", "telegram-desktop", on_focus_lost_hide=False),
                DropDown("spotify", "spotify", on_focus_lost_hide=False, width=0.9, height=0.9),
                DropDown("gnome-calculator", "gnome-calculator", on_focus_lost_hide=False, width=0.9, height=0.9),
                DropDown("pavucontrol", "pavucontrol", on_focus_lost_hide=False, width=0.9, height=0.9),
            ], position=groups_dict[i]['pos']))
    elif i == 'multimedia':
        groups.append(Group(i, label=groups_dict[i]['label'], position=groups_dict[i]['pos'], exclusive=True,
            matches=[
                Match(title=['Spotify', 'Kodi']),
                Match(wm_class=['zoom', 'kodi-bin', 'kodi', 'Totem', 'spotify', '/snap/spotify/42/usr/share/spotify/spotify']),
            ]))
    elif i == 'tools':
        groups.append(Group(i, label=groups_dict[i]['label'], position=groups_dict[i]['pos'], exclusive=True,
            matches=[Match(wm_class=['Shutter', 'pavucontrol', 'Control de Volumen'])]))
    elif i == 'stack':
        groups.append(Group(i, label=groups_dict[i]['label'], position=groups_dict[i]['pos'],
            matches=[
                Match(wm_class=['', 'Unnamed', 'transmission-gtk', 'soffice', 'libreoffice', 'wps', 'et', 
                                'libreoffice-calc', 'telegram-desktop', 'TelegramDesktop']), ]))
    else:
        groups.append(Group(i, label=groups_dict[i]['label'], position=groups_dict[i]['pos'],))

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "mod1"], actual_key, lazy.window.togroup(group.name))
    ])
keys.extend([
    Key([], 'F1', lazy.group['scratchpad'].dropdown_toggle('show_ip')),
    Key([mod, "mod1"], "XF86Launch5", lazy.group['scratchpad'].dropdown_toggle('switch_pns')),
    Key([mod, "mod1"], "XF86Launch6", lazy.group['scratchpad'].dropdown_toggle('switch_inter')),
    Key([mod, "mod1"], "XF86Launch9", lazy.group['scratchpad'].dropdown_toggle('speedtest')),
    Key([mod, "mod1"], "F1", lazy.group['scratchpad'].dropdown_toggle('switch_pns')),
    Key([mod, "mod1"], "F2", lazy.group['scratchpad'].dropdown_toggle('switch_inter')),
    Key([mod, "mod1"], "F3", lazy.group['scratchpad'].dropdown_toggle('speedtest')),
    Key([mod], "XF86Favorites",  lazy.group['scratchpad'].dropdown_toggle('change_network')),
    Key([], "XF86Messenger", lazy.group['scratchpad'].dropdown_toggle('telegram-desktop')), 
    Key([], "XF86Tools", lazy.group['scratchpad'].dropdown_toggle('spotify')),
    Key([], "XF86Calculator", lazy.group['scratchpad'].dropdown_toggle('gnome-calculator')),
    Key( [mod], "XF86AudioMute", lazy.group['scratchpad'].dropdown_toggle('pavucontrol')),
    ])
