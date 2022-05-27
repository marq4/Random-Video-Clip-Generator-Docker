#!/bin/sh

LOGFILE=.installation.log

echo
echo 'Installing programs... '
apt-get update -y  >$LOGFILE 2>&1
echo

echo 'Installing python3... '
apt-get install -y python3  >$LOGFILE 2>&1
python3 --version
echo

echo 'Installing ffmpeg... '
apt-get install -y ffmpeg   >$LOGFILE 2>&1
ffmpeg -version | head -1
echo

echo 'Installing ffmpeg... '
apt-get install -y vim   >$LOGFILE 2>&1
vim --version | head -1
echo

echo 'Program installation finished. '

exit $?
