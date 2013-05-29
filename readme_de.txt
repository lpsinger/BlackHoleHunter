###### ApacheFriends XAMPPlite Version 1.7.0 ######

  + Apache 2..2.11
  + MySQL 5.1.30 (Community Server)
  + PHP 5.2.8
  + XAMPPlite Control Version 2.5 von www.nat32.com	
  + XAMPPlite Security 1.0	
  + SQLite 2.8.15
  + OpenSSL 0.9.8i
  + phpMyAdmin 3.1.1
  + Webalizer 2.01-10
  + Zend Optimizer 3.3.0
  + eAccelerator 0.9.5.3 für PHP 5.2.7 (comment in php.ini)

--------------------------------------------------------------- 

* System-Voraussetzungen:
  
  + 64 MB RAM (EMPFOHLEN)
  + 200 MB freier Speicherplatz
  + Windows 98, ME oder
  + Windows NT, 2000, XP (EMPFOHLEN)

* SCHNELLINSTALLATION:

[HINWEIS: Auf die obersten Hirachie eines beliebigen Laufwerks bzw. auf dem Wechseldatenträger des USB-Sticks entpacken => E:\ oder W:\. Es entsteht E:\XAMPPlite oder W:\XAMPPlite. Für den USB-Stick nicht die "setup_XAMPPlite.bat" nutzen, um ihn auch transportabel nutzen zu können!]

Schritt 1: Das Setup mit der Datei "setup_XAMPPlite.bat" im XAMPPlite-Verzeichnis starten. Bemerkung: XAMPPlite macht selbst keine Einträge in die Windows Registry und setzt auch keine Systemvariablen.

Schritt 2: Apache2 mit PHP4 starten mit => \XAMPPlite\apache_start.bat
Der Apache 2 wird durch einfaches schließen der Apache Kommandoforderung (CMD) heruntergefahren.

Schritt 3: MySQL starten der mit => \XAMPPlite\mysql_start.bat
Den MySQL regulär stoppen mit "mysql_stop.bat".

Schritt 4: Öffne deinen Browser und gebe http://127.0.0.1 oder http://localhost ein. Danach gelangst du zu den zahlreichen ApacheFriends-Beispielen auf deinem lokalen Server.

Schritt 5: Das Root-Verzeichnis (Hauptdokumente) für HTTP (oft HTML) ist => C:\XAMPPlite\htdocs. PHP kann die Endungen  *.php, *.php3, *.php4, *.phtml haben, *.shtml für SSI, *.cgi für CGI (z. B.: Perl).

Schritt 6: XAMPPlite DEINSTALLIEREN?
Einfach das "XAMPPlite"-Verzeichnis löschen. Vorher aber alle Server stoppen 
bzw. als Dienste deinstallieren.

---------------------------------------------------------------

* PASSWÖRTER:

1) MySQL:

   Benutzer: root
   Passwort:
   (also kein Passwort!)

2) FileZilla FTP:

   Benutzer: newuser
   Passwort: wampp 

   Benutzer: anonymous
   Passwort: some@mail.net

3) Mercury: 

   Postmaster: Postmaster (postmaster@localhost)
   Administrator: Admin (admin@localhost)

   TestUser: newuser  
   Passwort: wampp 

4) WEBDAV: 

   Benutzer: wampp
   Password: XAMPPlite 

---------------------------------------------------------------

* NUR FÜR NT-SYSTEME! (NT4 | Windows 2000 | Windows XP):

- \XAMPPlite\apache\apache_installservice.bat 
  ===> Installiert den Apache 2 als Dienst

- \XAMPPlite\apache\apache_uninstallservice.bat 
  ===> Deinstalliert den Apache 2 als Dienst

- \XAMPPlite\mysql\mysql_installservice.bat 
  ===> Installiert MySQL als Dienst

- \XAMPPlite\mysql\mysql_uninstallservice.bat 
  ===> Deinstalliert MySQL als Dienst

==> Nach allen De- / Installationen der Dienste, System unbedingt neustarten! 

---------------------------------------------------------------

* DAS THEMA SICHERHEIT:

Wie schon an anderer Stelle erwähnt ist XAMPPlite nicht für den Produktionseinsatz gedacht, sondern nur für Entwickler in Entwicklungsumgebungen. Das hat zur Folge, dass XAMPPlite absichtlich nicht restriktiv sondern im Gegenteil sehr offen vorkonfiguriert ist. Für einen Entwickler ist das ideal, da er so keine Grenzen vom System vorgeschrieben bekommt.
Für einen Produktionseinsatz ist das allerdings überhaupt nicht geeignet!
Hier eine Liste, der Dinge, die an XAMPPlite absichtlich (!) unsicher sind:

- Der MySQL-Administrator (root) hat kein Passwort.
- Der MySQL-Daemon ist übers Netzwerk erreichbar.
- phpMyAdmin ist über das Netzwerk erreichbar.
- In dem XAMPPlite-Demo-Seiten (die man unter http://localhost/ findet) gibt es den Punkt "Sicherheitscheck".
  Dort kann man sich den aktuellen Sicherheitszustand seiner XAMPPlite-Installation anzeigen lassen.

Will man XAMPPlite in einem Netzwerk betreiben, so dass der XAMPPlite-Server auch von anderen erreichbar ist, dann sollte man unbedingt die folgende URL aufrufen, mit dem man diese Unsicherheiten einschränken kann:

	http://localhost/security/

Hier kann das Root-Passwort für MySQL und phpMyAdmin und auch ein Verzeichnisschutz für die 
XAMPPlite-Seiten eingerichtet werden.

---------------------------------------------------------------

* Apache-Hinweise:

(1) Im Gegensatz zu dem Apache 1.x kann der Apache 2.x bei einen manuellen Start nicht mit "apache -k shutdown" gestoppt
werden. Das funktioniert nur als Dienstinstallation unter NT-Systemen. Also die Apache START Eingabeforderungen zum stoppen 
einfach schließen.

(2) Für mod_auth_mysql experimentell. Das Modul ebenfalls einfach in der "httpd.conf" auskomentieren. Weitere Hinweise zu diesem Modul findet ihr auf der Hauptseite dieses XAMPPlite-Pakets.

(3) Zum Laden von WebDAV, nur die Module mod_dav.so + mod_dav_fs.so in der "httpd.conf" auskommentieren (# entfernen). Dann für http://127.0.0.1:81 einrichten und testen! (NICHT für Microsoft Frontpage, einzig für Adobe Dreamweaver!)

---------------------------------------------------------------

* MYSQL-Hinweise:

(1) Um den MySQL-Daemon zu starten bitte Doppelklick auf \XAMPPlite\mysql_start.bat.
Der MySQL Server startet dann im Konsolen-Modus. Das dazu gehörige Konsolenfenster muss offen bleiben (!!) Zum Stop bitte die mysql_shutdown.bat benutzen!

(2) Um den MySQL-Daemon von diesem Paket mit "innodb" für bessere Performance zu
nutzen, editiert bitte die "my" bzw."my.cnf" im Verzeichnis "/XAMPPlite/mysql/bin" bzw. als Dienst die C:\my.cnf unter NT / 2000 / XP. Dort aktiviert ihr dann die Zeile "innodb_data_file_path=ibdata1:30M". Achtung, "innodb" kann ich derzeit nicht
für 95 / 98 / ME empfehlen, da es hier immmer wieder zu blockierenden Systemen kam. Also nur NT / 2000 / XP!
Wer MySQL als Dienst unter NT / 2000 / XP benutzen möchte, muss unbedingt (!) vorher die "my" bzw."my.cnf unter C:\ (also C:\my.cnf) implementieren. Danach die "mysql_installservice.bat" im Ordner "mysql" aktivieren.

(3) Der MySQL-Server startet ohne Passwort für MySQl-Administrator "root".
Für eine Zugriff in PHP sähe das also aus:

	mysql_connect("localhost", "root", "");

Ein Passwort für "root" könnt ihr über den MySQL-Admin in der Eingabeaufforderung
setzen. Z. B.: 

	C:\XAMPPlite\mysql\bin\mysqladmin.exe -u root -p geheim

Wichtig: Nach dem Einsetzen eines neuen Passwortes für Root muss auch phpMyAdmin informiert werden! Das geschieht über die Datei "config.inc.php"; zu finden als C:\XAMPPlite\phpmyadmin\config.inc.php. Dort also folgenden 
Zeilen editieren:
   
	$cfg['Servers'][$i]['user']            = 'root';   // MySQL User
	$cfg['Servers'][$i]['auth_type']       = 'http';   // HTTP-Authentifzierung

So wird zuerst das "root"-Passwort vom MySQL-Server abgefragt, bevor phpMyAdmin zugreifen darf.
    
---------------------------------------------------------------	
    
		Have a lot of fun! | Viel Spaß! | Bonne Chance!
