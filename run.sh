#!/bin/bash
fname=`basename $1`

if [ -e "conf/"$1".json" ]
then
    echo "Found User"
    while true
    do
        python pokecli.py -cf conf/$1".json" >> logs/log-$fname.log 2>> logs/error-$fname.log;
        echo ">Bot crashed. Restarting...";
        sleep 5;
    done
else

    echo "No such User exist";
    echo  conf/$1".json"
fi
