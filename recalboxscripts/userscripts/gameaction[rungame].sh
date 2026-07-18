#!/bin/ash
echo "`cat /tmp/es_state.inf | grep ImagePath | cut -d= -f2`" | sed 's;\ ;\\ ;g' | xargs base64 > /tmp/additional.inf
echo "`cat /tmp/es_state.inf | grep GamePath | cut -d= -f2`" | sed -r 's/(.*\.).*/\1ini/' | sed 's;\ ;\\ ;g' | xargs cat > /tmp/keys.inf

cat /tmp/es_state.inf | mosquitto_pub -h localhost -p 1883 -t /BruudtArcade/rungame -s
cat /tmp/additional.inf | mosquitto_pub -h localhost -p 1883 -t /BruudtArcade/currentimage -s
cat /tmp/keys.inf | mosquitto_pub -h localhost -p 1883 -t /BruudtArcade/currentconfig -s