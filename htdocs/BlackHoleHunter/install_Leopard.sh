#!/bin/sh
dir="`echo $PWD/$0 | sed 's%/[^/]*$%/public_html%;s%.*//%/%'`"
cd /Library/WebServer || exit

test -r /etc/apache2/httpd.conf.bhhbak && echo /etc/apache2/httpd.conf.bhhbak exists && exit
test -r Documents.bhhbak && echo /Library/WebServer/Documents.bhhbak exists && exit
test -r CGI-Executables.bhhbak && echo /Library/WebServer/CGI-Executables.bhhbak exists && exit

sudo mv Documents Documents.bhhbak
sudo mv CGI-Executables CGI-Executables.bhhbak
sudo cp -R "$dir" Documents
sudo ln -s Documents/cgi-bin CGI-Executables

sudo mv /etc/apache2/httpd.conf /etc/apache2/httpd.conf.bhhbak
sudo awk '{print};/AddHandler *cgi-script/{print "     AddHandler cgi-script .py\n     AddHandler cgi-script .pl"}' /etc/apache2/httpd.conf.bhhbak > /tmp/httpd.conf
sudo mv /tmp/httpd.conf /etc/apache2

sudo apachectl restart
