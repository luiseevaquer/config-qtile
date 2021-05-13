#!/bin/bash
echo 'lenri1078' | sudo -S sh -c "ip route del default via 192.168.1.1"
echo 'lenri1078' | sudo -S sh -c "ip route del default via 192.168.0.1"
echo 'lenri1078' | sudo -S sh -c "ip route add default via 192.168.1.1 dev eno1 proto dhcp metric 100"
ip route list
echo ' '
echo "IP Publica: "
curl https://ipinfo.io/ip
read -t 3 -n 1
