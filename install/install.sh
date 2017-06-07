#!/bin/bash

INIT_FILE="actuator-bigsea"
UNIT_FILE="actuator-bigsea.service"

echo "--- Download actuator ---"
git clone https://github.com/bigsea-ufcg/actuator-service.git
mv -f actuator-service /opt/
mv /opt/actuator-service /opt/actuator-bigsea

echo "--- Installation ---"
echo "1. cp -f \"$INIT_FILE\" \"/etc/init.d/\""
cp -v "$INIT_FILE" "/etc/init.d/"
echo "2. cp -f \"$UNIT_FILE\" \"/etc/systemd/system/multi-user.target.wants/\""
cp -v "$UNIT_FILE" "/etc/systemd/system/multi-user.target.wants/"
echo "3. systemctl enable $UNIT_FILE"
systemctl enable $UNIT_FILE
echo "4. systemctl daemon-reload"
systemctl daemon-reload
echo "5. systemctl restart $UNIT_FILE"
systemctl restart $UNIT_FILE
