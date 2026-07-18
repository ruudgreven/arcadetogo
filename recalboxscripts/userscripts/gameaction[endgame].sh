#!/bin/ash
cat /tmp/es_state.inf | mosquitto_pub -h localhost -p 1883 -t /BruudtArcade/endgame -s