#!/bin/bash
echo 'lenri1078' | sudo -S -k sudo brightnessctl set 100%
/home/lescobarvx/.config/hass/service_hass.sh homeassistant turn_on input_boolean.monitor_laptop
