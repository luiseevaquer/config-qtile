# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Multimonitor support

from libqtile.config import Screen
from libqtile import bar
from settings.widgets import primary_widgets, secondary_widgets, pbottom_widgets, sbottom_widgets
from settings.monitors import connected_monitors
import subprocess


status_bar = lambda widgets: bar.Bar(widgets, 24, opacity=1)

screens = [Screen(
            top=status_bar(primary_widgets),
            bottom=status_bar(pbottom_widgets), 
            wallpaper='~/.config/qtile/background.jpg', 
            wallpaper_mode='stretch',)]

#connected_monitors = subprocess.run(
#    "xrandr | grep 'connected' | cut -d ' ' -f 2",
#    shell=True,
#    stdout=subprocess.PIPE
#).stdout.decode("UTF-8").split("\n")[:-1].count("connected")

if connected_monitors > 1:
    for i in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets),bottom=status_bar(sbottom_widgets)))
