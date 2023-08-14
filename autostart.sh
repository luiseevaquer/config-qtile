#!/bin/sh
#ulauncher &
barrier &
megasync &
#dropbox start &
shutter --min_at_startup &
blueman-applet &
xscreensaver -nosplash &
triggercmdagent &
/usr/lib/policykit-1-gnome/polkit-gnome-authentication-agent-1 &
