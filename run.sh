#!/bin/bash
fname=`basename $1`
while true
do
        python pokecli.py -cf /home/ubuntu/$1 >> logs/log-$fname.log 2>> /logs/error-$fname.log;
        echo ">Bot crashed. Restarting...";
        sleep 5;
done