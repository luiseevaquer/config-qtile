#!/bin/bash
echo 'lenri1078' | sudo -S -k sync 
echo 'lenri1078' | sudo -S -k sysctl -w vm.drop_caches=3 
