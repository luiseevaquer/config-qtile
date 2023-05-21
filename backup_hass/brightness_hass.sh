#!/bin/bash
APIKEY=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJlYTEyNzUyYmNkMTM0ZWEyOGFkNTM1ZGU2ZDM1OTQyNiIsImlhdCI6MTY1MDM5NDAzOCwiZXhwIjoxOTY1NzU0MDM4fQ.75d9E1eGgboXGEqpRiP08rCe9eFKucy6CLtyX9Gh2rY
APIKEY=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI2OGM1ODdiMjRhMGE0YjI2YWNhYjAwNDUzNjk3ZjE4MyIsImlhdCI6MTY1MTgwMzQ3MCwiZXhwIjoxOTY3MTYzNDcwfQ.QsonGfNpc9is5Er9yKA31r-i2plxbVTeJbNL7C50TfU # RASPBERRY
SERVER=192.168.1.6
set -x
clear
while read l; do line=$l; done < /home/lescobarvx/.config/qtile/bulb_name.txt
if [ "$1" == "step" ]
  then
	curl -X POST \
	-H "Authorization: Bearer ${APIKEY}" \
	-H "Content-Type: application/json" \
	-d "{\"entity_id\": \"$line\", \"brightness_step\": \"$2\"}" \
	http://${SERVER}:8123/api/services/light/turn_on
else
	curl -X POST \
	-H "Authorization: Bearer ${APIKEY}" \
	-H "Content-Type: application/json" \
	-d "{\"entity_id\": \"$line\", \"brightness\": \"$2\"}" \
	http://${SERVER}:8123/api/services/light/turn_on
fi
