from libqtile import widget
from settings.theme import colors
from settings.monitors import connected_monitors
import subprocess
import subprocess

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def whatismyip():
    return '   ' + subprocess.check_output(['curl', 'ifconfig.me']).decode('utf-8').strip()  + ' '

def airpod_battery():
    return subprocess.check_output(['bluetooth_battery', '41:42:6E:FF:7C:57', '   ', '   ', '']).decode('utf-8').strip()  + ' '

base = lambda fg='text', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}

separator = lambda: widget.Sep(**base(), linewidth=0, padding=5)

icon = lambda fg='text', bg='dark', fontsize=16, text="?": widget.TextBox(
    **base(fg, bg),
    fontsize=fontsize,
    text=text,
    padding=3
)

glyphs = {
    'g_halfcircle': " ",
    'g_trapezoid': "",
    'g_flame': " ",
    'g_invertflame': " ",
    'g_triangle': "",
    'g_lowertriangle': " ",
    'g_pixelated': " ",
    'g_micropixelated': " ",
}

powerline = lambda fg="light", bg="dark", g='g_flame': widget.TextBox(
   **base(fg, bg),
    text=glyphs[g] if g in glyphs else g,
    fontsize=37,
    padding=-2
)

workspaces = lambda: [
    separator(),
    widget.GroupBox(
        **base(fg='light'),
        font='UbuntuMono Nerd Font',
        fontsize=19,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=0,
        borderwidth=0,
        active=colors['active'],
        inactive=colors['inactive'],
        rounded=False,
        highlight_method='block',
        urgent_alert_method='block',
        urgent_border=colors['urgent'],
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['grey'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark'],
        disable_drag=True
    ),
    widget.Spacer(**base(fg='focus')),
    #widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
    #separator(),
]

notif_gen = widget.Notify(**base(bg='dark'), fontsize=10, font="UbuntuMono Nerd Font Bold")
notif_01 = widget.TextBox(text="")
notif_02 = widget.TextBox(text="")

if connected_monitors == 1:
    notif_01 = notif_gen 
else:
    notif_02 = notif_gen

primary_widgets = [
    *workspaces(),

    separator(),

    widget.Prompt(**base(bg='dark'), prompt="run: "),

    notif_01,

    powerline('color3', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color3'), scale=0.65),

    widget.CurrentLayout(**base(bg='color3'), padding=5),

    powerline('color2', 'color3'),

    #widget.GenPollText(**base(bg='color2'), func=airpod_battery, update_interval=300),
    icon(bg="color2", text=' '), # Icon: nf-fa-download
    widget.ThermalSensor(**base(bg='color2')), # sudo apt install lm-sensors

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

]

secondary_widgets = [
    *workspaces(),

    separator(),

    notif_02,

    powerline('color4', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color4'), scale=0.65),

    widget.CurrentLayout(**base(bg='color4'), padding=5),

    powerline('color2', 'color4'),

    widget.GenPollText(**base(bg='color2'), func=whatismyip),
]

pbottom_widgets = [
    widget.TaskList(background=colors['dark'], highlight_method='block', font='UbuntuMono Nerd Font Bold', fontsize=10),
    separator(),

    #powerline('color4', 'dark'),

    #icon(bg="color4", text=' '),  # Icon: nf-fa-feed
    #widget.KeyboardLayout(**base(bg='color4'), configured_keyboards=['us', 'latam', 'es']),

    powerline('color3', 'dark'),

    icon(bg="color3", text=' '), # Icon: nf-fa-download
    
    widget.DF(**base(bg='color3'), visible_on_warn=False, measure='G', warn_space=5, format=' Free:{uf}{m}/{s}{m}  Used:{r:.0f}% '),
    #icon(bg="color3", text=' '), # Icon: nf-fa-download
    #widget.ThermalSensor(**base(bg='color3')), # sudo apt install lm-sensors

    powerline('color2', 'color3'),

    icon(bg="color2", text=' '),  # Icon: nf-fa-feed
    widget.Battery(**base(bg='color2')),

    powerline('dark', 'color2'),

    widget.Systray(background=colors['dark'], padding=5),
    icon(bg="dark", text=' '),
]

sbottom_widgets = [
    widget.TaskList(background=colors['dark'], highlight_method='block', font='UbuntuMono Nerd Font Bold', fontsize=10),
    powerline('color2', 'dark'),

    icon(bg="color2", text=' '),  # Icon: nf-fa-feed
    widget.KeyboardLayout(**base(bg='color2'), configured_keyboards=['us', 'latam', 'es']),

    powerline('color3', 'color2'),

    icon(bg="color3", text=' '),  # Icon: nf-fa-feed
    widget.Memory(**base(bg='color3')),

    powerline('color2', 'color3'),

    icon(bg="color2", text='  '),  # Icon: nf-fa-feed
    widget.Wlan(**base(bg='color2'), interface='wlp2s0'),  ## Missing iwlib - No se puede instalar

    powerline('color3', 'color2'),

    icon(bg="color3", text='  '),  # Icon: nf-fa-feed
    widget.Net(**base(bg='color3'), format='{down} ↓↑ {up}', interface='eno1'),

    powerline('dark', 'color3'),

    icon(bg="dark", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='dark'), format='%d/%m/%Y - %H:%M '),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
