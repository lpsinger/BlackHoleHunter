#!/bin/sh
bak=bhhbak
items="/etc/httpd.conf /Library/WebServer/Documents /Library/WebServer/CGI-Executables"
for i in $items; do
  if test -r $i.$bak ; then
    :
  else
    echo "can't uninstall - $i.$bak missing"
    exit
  fi
done
for i in $items; do
  sudo rm -rf $i
  sudo mv $i.$bak $i
done
