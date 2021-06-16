#!/bin/bash
echo 'lenri1078' | sudo -S sh -c "ip route del default via 192.168.1.1"
echo 'lenri1078' | sudo -S sh -c "ip route del default via 192.168.0.1"
ip route list
echo ' '
