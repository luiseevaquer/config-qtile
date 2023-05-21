#!/bin/bash
echo 'lenri1078' | sudo -S -k sudo brightnessctl set 0%
/home/lescobarvx/.config/hass/service_hass.sh homeassistant turn_off input_boolean.monitor_laptop
