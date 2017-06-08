#!/bin/bash

UNIT_FILE="actuator-bigsea.service"

echo "--- Download actuator ---"
git clone https://github.com/bigsea-ufcg/actuator-service.git
mv -f actuator-service /opt/
mv /opt/actuator-service /opt/actuator-bigsea
pushd /opt/actuator-bigsea/install

echo "--- Installation ---"
echo "1. cp -v \"$UNIT_FILE\" \"/etc/systemd/system/\""
cp -v "$UNIT_FILE" "/etc/systemd/system/"
echo "2. systemctl enable $UNIT_FILE"
systemctl enable $UNIT_FILE
echo "3. systemctl daemon-reload"
systemctl daemon-reload
echo "4. systemctl restart $UNIT_FILE"
systemctl restart $UNIT_FILE
