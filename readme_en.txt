###### ApacheFriends XAMPPlite Version 1.7.0 ######

  + Apache 2..2.11
  + MySQL 5.1.30 (Community Server)
  + PHP 5.2.8
  + XAMPPlite Control Version 2.5 from www.nat32.com	
  + XAMPPlite Security 1.0	
  + SQLite 2.8.15
  + OpenSSL 0.9.8i
  + phpMyAdmin 3.1.1
  + Webalizer 2.01-10
  + Zend Optimizer 3.3.0
  + eAccelerator 0.9.5.3 for PHP 5.2.7 (comment in php.ini)
 
* System Requirements:
 
  + 64 MB RAM (RECOMMENDED)
  + 200 MB free fixed disk 
  + Windows 98, ME
  + Windows NT, 2000, XP (RECOMMENDED)

---------------------------------------------------------------

* QUICK INSTALLATION:

[NOTE: Unpack the package to your USB stick or a partition of your choice.
There it must be on the highest level like E:\ or W:\. It will 
build E:\XAMPPlite or W:\XAMPPlite or something like this. Please do not use the "setup_XAMPPlite.bat" for an USB stick installation!]   

Step 1: Unpack the package into a directory of your choice. Please start the 
"setup_XAMPPlite.bat" and beginning the installation. Note: XAMPPlite makes no entries in the windows registry and no settings for the system variables.

Step 2: If installation ends successfully, start the Apache 2 with 
"apache_start".bat", MySQL with "mysql_start".bat". Stop the MySQL Server with "mysql_stop.bat". For shutdown the Apache HTTPD, only close the Apache Command (CMD).

Step 3: Start your browser and type http://127.0.0.1 or http://localhost in the location bar. You should see our pre-made
start page with certain examples and test screens.

Step 4: PHP (with mod_php, as *.php, *.php3, *.php4, *.phtml), Perl by default with *.cgi, SSI with *.shtml are all located in => C:\XAMPPlite\htdocs\.
Examples:
- C:\XAMPPlite\htdocs\test.php => http://localhost/test.php
- C:\XAMPPlite\myhome\test.php => http://localhost/myhome/test.php

Step 5: XAMPPlite UNINSTALL? Simply remove the "XAMPPlite" Directory.
But before please shutdown the apache and mysql.

---------------------------------------------------------------

* PASSWORDS:

1) MySQL:

   User: root
   Password:
   (means no password!)

2) FileZilla FTP:

   User: newuser
   Password: wampp 

   User: anonymous
   Password: some@mail.net

3) Mercury: 

   Postmaster: postmaster (postmaster@localhost)
   Administrator: Admin (admin@localhost)

   TestUser: newuser  
   Password: wampp

4) WEBDAV:

   User: wampp
   Password: XAMPPlite

---------------------------------------------------------------

* ONLY FOR NT SYSTEMS! (NT4 | Windows 2000 | Windows XP):

- \XAMPPlite\apache\apache_installservice.bat 
  ===> Install Apache 2 as service

- \XAMPPlite\apache\apache_uninstallservice.bat 
  ===> Uninstall Apache 2 as service

- \XAMPPlite\mysql\mysql_installservice.bat 
  ===> Install MySQL as service

- \XAMPPlite\mysql\mysql_uninstallservice.bat 
  ===> Uninstall MySQL as service

==> After all un- / installations of services, better restart system!

----------------------------------------------------------------

A matter of security (A MUST READ!)

As mentioned before, XAMPPlite is not meant for production use but only for developers in a development environment. The way XAMPPlite is configured is to be open as possible and allowing the developer anything he/she wants. For development environments this is great but in a production environment it could be fatal. Here a list of missing security 
in XAMPPlite:

- The MySQL administrator (root) has no password.
- The MySQL daemon is accessible via network.
- phpMyAdmin is accessible via network.
- Examples are accessible via network.

To fix most of the security weaknesses simply call the following URL:

	http://localhost/security/

The root password for MySQL and phpMyAdmin, and also a XAMPPlite directory protection can being established here.

---------------------------------------------------------------

* Apache Notes:

(1) In contrast of apache 1.x, you can not stop the apache 2.x with the command "apache -k shutdown". These functions only for an installations as service by NT systems. So, simply close
the Apache START command for shutdown.
  
(2) To use the experimental version of mod_auth_mysql remove the # in the httpd.conf. Detailed information about this topic can be found on the left menu of XAMPPlite, once you started it.

(3) To use Mod_Dav load the Modules mod_dav.so + mod_dav_fs.so in the "httpd.conf" by removing the # on 
the beginning of their lines. Then try http://127.0.0.1:81 (NOT for Microsoft Frontpage, but for Adobe Dreamweaver!)

---------------------------------------------------------------

* MYSQL NOTES:

(1) The MySQL server can be started by double-clicking (executing) mysql_start.bat. This file can be found in the same folder you installed XAMPPlite in, most likely this will be C:\XAMPPlite\.
The exact path to this file is X:\XAMPPlite\mysql_start.bat, where "X" indicates the letter of the drive you unpacked XAMPPlite into. This batch file starts the MySQL server in console mode. The first intialization might take a few minutes.
Do not close the DOS window or you'll crash the server!
To stop the server, please use mysql_shutdown.bat, which is located in the same directory.

(2) To use the MySQL Daemon with "innodb" for better performance, please edit the "my" (or "my.cnf") file in the C:\XAMPPlite\mysql\bin directory or for services the c:\my.cnf for windows NT/2000/XP. In there, activate the "innodb_data_file_path=ibdata1:30M" statement. Attention, "innodb" is not recommended for 95/98/ME.
To use MySQL as Service for NT / 2000 / XP, simply copy the "my" / "my.cnf" file to "C:\my", or "C:\my.cnf". Please note that this file has to be placed in C:\ (root), other locations are not permitted. Then execute the "mysql_installservice.bat" in the mysql folder.

(3) MySQL starts with standard values for the user id and the password. The preset user id is "root", the password is "" (= no password). To access MySQL via PHP with the preset values, you'll have to use the following syntax:

	mysql_connect("localhost", "root", "");

If you want to set a password for MySQL access, please use of MySQL Admin.
To set the passwort "secret" for the user "root", type the following:

	C:\XAMPPlite\mysql\bin\mysqladmin.exe -u root -p secret
    
After changing the password you'll have to reconfigure phpMyAdmin to use the new password, otherwise it won't be able to access the databases. To do that, open the file config.inc.php in \XAMPPlite\phpmyadmin\ and edit the following lines:

	$cfg['Servers'][$i]['user']            = 'root';   // MySQL User
	$cfg['Servers'][$i]['auth_type']       = 'http';   // HTTP authentification

So first the 'root' password is queried by the MySQL server, before phpMyAdmin may access.
  	    	
---------------------------------------------------------------    

		Have a lot of fun! | Viel Spa�! | Bonne Chance!
