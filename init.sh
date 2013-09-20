#!/bin/bash

wget http://www.mta.info/status/serviceStatus.txt
git init
git add serviceStatus.txt
git commit -m "initial commit"
