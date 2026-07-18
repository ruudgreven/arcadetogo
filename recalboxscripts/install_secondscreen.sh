echo "Download new sources"
rm /recalbox/share/system/main.zip
wget https://github.com/ruudgreven/arcadetogo/archive/refs/heads/main.zip -O /recalbox/share/system/main.zip
rm -rf /recalbox/share/system/arcadetogo-main
unzip /recalbox/share/system/main.zip -d /recalbox/share/system

scp -r /recalbox/share/system/arcadetogo-main ruud@<second display ip>:~ -i /recalbox/share/system/.ssh/id_rsa
ssh ruud@<second display ip> -i /recalbox/share/system/.ssh/id_rsa '/sbin/reboot'