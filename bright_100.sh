#!/bin/bash
/home/lescobarvx/.config/hass/service_hass.sh switch turn_on switch.enchufe_monitor
echo 'lenri1078' | sudo -S -k sudo brightnessctl set 100%
/home/lescobarvx/.config/hass/service_hass.sh homeassistant turn_on input_boolean.monitor_laptop
