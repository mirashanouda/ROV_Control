#! /bin/bash 

echo "Executing commands"
gnome-terminal -- bash joy.sh &&
gnome-terminal -- rostopic echo joy &&
gnome-terminal -- bash map.sh &&
gnome-terminal -- bash serial.sh;
