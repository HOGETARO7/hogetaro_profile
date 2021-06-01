#!/bin/bash

#変数設定
FILE=$1
DIRNAME=`dirname $1`
TIME=`date + %Y%m%d`

###################################
#前処理
###################################
#引数チェック
if [ $# -ne 1 ]; then
 echo "[ERROR] the count of argument is not one"
 echo `date`
 exit 255
else
 echo "[SUCCESS] the count of argument is one"
fi

#ファイル存在チェック
if [ ! -f $FILE ]; then
 echo "[ERROR] the file dosen't exist"
 echo `date`
 exit 255
else
 echo "[SUCCESS] the file exists"
fi

#初回チェック
test -s $FILE
if [ $? -ne 0 ]; then
 echo "[ERROR] log rotation have already done"
 exit 255
else
 echo "[SUCCESS] log rotation is begining"
fi

#既にログファイルが空でないか確認する
test -s $FILE
if [ $? -ne 0 ]; then
 echo "[ERROR] log rotation have already done"
 exit 0
fi

####################################
#主処理
####################################
#ファイルをコピーする
cp -ap $FILE $FILE.$TIME
if [ $? -ne 0 ]; then
 echo "[ERROR] failured to copy the file"
 exit 255
else
 echo "[SUCCESS] success to copy the file"
fi

#####################################
#後処理
#####################################
#ファイルを空にする
cat /dev/null > $FILE
if [ $? -ne 0 ]; then
 echo "[ERROR] making the original empty was failured"
 exit 255
else
 echo "[SUCCESS] making the original empty was successed"
fi

#古いログファイルを消去する
find $LOGDIR -mtime +7 -name "20*.log" | xargs rm -f
if [ $? -ne 0 ]; then
 echo "[ERROR] deleting old file was failured"
 exit 255
else
 echo "[SUCCESS] deleting logfile was successed, so rotaion was completed"
fi