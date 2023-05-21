#!/bin/bash
# APIKEY=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJlYTEyNzUyYmNkMTM0ZWEyOGFkNTM1ZGU2ZDM1OTQyNiIsImlhdCI6MTY1MDM5NDAzOCwiZXhwIjoxOTY1NzU0MDM4fQ.75d9E1eGgboXGEqpRiP08rCe9eFKucy6CLtyX9Gh2rY # 192.168.1.16
# APIKEY=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI2OGM1ODdiMjRhMGE0YjI2YWNhYjAwNDUzNjk3ZjE4MyIsImlhdCI6MTY1MTgwMzQ3MCwiZXhwIjoxOTY3MTYzNDcwfQ.QsonGfNpc9is5Er9yKA31r-i2plxbVTeJbNL7C50TfU # RASPBERRY
# SERVER=192.168.1.6
source ./config_hass.sh
set -x
clear
while read l; do line=$l; done < /home/lescobarvx/.config/qtile/bulb_name.txt
curl -X POST \
-H "Authorization: Bearer ${APIKEY}" \
-H "Content-Type: application/json" \
-d "{\"entity_id\": \"$line\", \"color_name\": \"$2\"}" \
http://${SERVER}:8123/api/services/light/$1
sleep .5
if [ "$2" == "white" ]
then
	sleep .5
	curl -X POST \
	-H "Authorization: Bearer ${APIKEY}" \
	-H "Content-Type: application/json" \
	-d "{\"entity_id\": \"$line\", \"kelvin\": \"$3\"}" \
	http://${SERVER}:8123/api/services/light/$1
	sleep .5
	if [ ! -z $4 ]
	then
		curl -X POST \
		-H "Authorization: Bearer ${APIKEY}" \
		-H "Content-Type: application/json" \
		-d "{\"entity_id\": \"$line\", \"brightness_pct\": \"$4\"}" \
		http://${SERVER}:8123/api/services/light/$1
		sleep .5
	fi
else 
	if [ ! -z $3 ]
	then
		curl -X POST \
		-H "Authorization: Bearer ${APIKEY}" \
		-H "Content-Type: application/json" \
		-d "{\"entity_id\": \"$line\", \"brightness_pct\": \"$3\"}" \
		http://${SERVER}:8123/api/services/light/$1
	fi
fi 
