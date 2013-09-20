#!/bin/bash

while true
do
  sleep 60
  rm -f serviceStatus.txt
  if wget http://www.mta.info/status/serviceStatus.txt
  then
      git commit -am "service status: `date`"
  else
      echo oops
  fi
done
