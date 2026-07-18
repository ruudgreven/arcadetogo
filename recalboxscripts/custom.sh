#!/bin/sh
echo "Setting up network"
ifconfig eth0 <ip recalbox internal> netmask 255.255.255.0 up
ip route add <ip secondscreen> via <ip recalbox internal>