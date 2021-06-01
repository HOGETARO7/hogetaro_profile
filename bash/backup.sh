#!/bin/bash

DATE=`date +%Y%m%d`
TIME=`date +%H%M`
DIR=/work/BACKUP_$DATE-$TIME
LIST=/work/level1_9-3.list

if [ $# -ne 1 ]; then
   echo "[ERROR] the count of argument is not 1"
   exit 255
else
   echo "[SUCCESS] the count of argument is 1"
fi

if [ ! -f $LIST ]; then
   echo "[ERROR] the list dosen't exist"
   exit 255
else
   echo "[SUCCESS] the list exists"
fi

if [ ! -d $DIR ]; then
   echo "[ERROR] the directory dosen't exist"
   exit 255
else
   echo "[SUCCESS] the directory exists"
fi