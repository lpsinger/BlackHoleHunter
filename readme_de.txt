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
  + eAccelerator 0.9.5.3 f�r PHP 5.2.7 (comment in php.ini)

--------------------------------------------------------------- 

* System-Voraussetzungen:
  
  + 64 MB RAM (EMPFOHLEN)
  + 200 MB freier Speicherplatz
  + Windows 98, ME oder
  + Windows NT, 2000, XP (EMPFOHLEN)

* SCHNELLINSTALLATION:

[HINWEIS: Auf die obersten Hirachie eines beliebigen Laufwerks bzw. auf dem Wechseldatentr�ger des USB-Sticks entpacken => E:\ oder W:\. Es entsteht E:\XAMPPlite oder W:\XAMPPlite. F�r den USB-Stick nicht die "setup_XAMPPlite.bat" nutzen, um ihn auch transportabel nutzen zu k�nnen!]

Schritt 1: Das Setup mit der Datei "setup_XAMPPlite.bat" im XAMPPlite-Verzeichnis starten. Bemerkung: XAMPPlite macht selbst keine Eintr�ge in die Windows Registry und setzt auch keine Systemvariablen.

Schritt 2: Apache2 mit PHP4 starten mit => \XAMPPlite\apache_start.bat
Der Apache 2 wird durch einfaches schlie�en der Apache Kommandoforderung (CMD) heruntergefahren.

Schritt 3: MySQL starten der mit => \XAMPPlite\mysql_start.bat
Den MySQL regul�r stoppen mit "mysql_stop.bat".

Schritt 4: �ffne deinen Browser und gebe http://127.0.0.1 oder http://localhost ein. Danach gelangst du zu den zahlreichen ApacheFriends-Beispielen auf deinem lokalen Server.

Schritt 5: Das Root-Verzeichnis (Hauptdokumente) f�r HTTP (oft HTML) ist => C:\XAMPPlite\htdocs. PHP kann die Endungen  *.php, *.php3, *.php4, *.phtml haben, *.shtml f�r SSI, *.cgi f�r CGI (z. B.: Perl).

Schritt 6: XAMPPlite DEINSTALLIEREN?
Einfach das "XAMPPlite"-Verzeichnis l�schen. Vorher aber alle Server stoppen 
bzw. als Dienste deinstallieren.

---------------------------------------------------------------

* PASSW�RTER:

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

* NUR F�R NT-SYSTEME! (NT4 | Windows 2000 | Windows XP):

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

Wie schon an anderer Stelle erw�hnt ist XAMPPlite nicht f�r den Produktionseinsatz gedacht, sondern nur f�r Entwickler in Entwicklungsumgebungen. Das hat zur Folge, dass XAMPPlite absichtlich nicht restriktiv sondern im Gegenteil sehr offen vorkonfiguriert ist. F�r einen Entwickler ist das ideal, da er so keine Grenzen vom System vorgeschrieben bekommt.
F�r einen Produktionseinsatz ist das allerdings �berhaupt nicht geeignet!
Hier eine Liste, der Dinge, die an XAMPPlite absichtlich (!) unsicher sind:

- Der MySQL-Administrator (root) hat kein Passwort.
- Der MySQL-Daemon ist �bers Netzwerk erreichbar.
- phpMyAdmin ist �ber das Netzwerk erreichbar.
- In dem XAMPPlite-Demo-Seiten (die man unter http://localhost/ findet) gibt es den Punkt "Sicherheitscheck".
  Dort kann man sich den aktuellen Sicherheitszustand seiner XAMPPlite-Installation anzeigen lassen.

Will man XAMPPlite in einem Netzwerk betreiben, so dass der XAMPPlite-Server auch von anderen erreichbar ist, dann sollte man unbedingt die folgende URL aufrufen, mit dem man diese Unsicherheiten einschr�nken kann:

	http://localhost/security/

Hier kann das Root-Passwort f�r MySQL und phpMyAdmin und auch ein Verzeichnisschutz f�r die 
XAMPPlite-Seiten eingerichtet werden.

---------------------------------------------------------------

* Apache-Hinweise:

(1) Im Gegensatz zu dem Apache 1.x kann der Apache 2.x bei einen manuellen Start nicht mit "apache -k shutdown" gestoppt
werden. Das funktioniert nur als Dienstinstallation unter NT-Systemen. Also die Apache START Eingabeforderungen zum stoppen 
einfach schlie�en.

(2) F�r mod_auth_mysql experimentell. Das Modul ebenfalls einfach in der "httpd.conf" auskomentieren. Weitere Hinweise zu diesem Modul findet ihr auf der Hauptseite dieses XAMPPlite-Pakets.

(3) Zum Laden von WebDAV, nur die Module mod_dav.so + mod_dav_fs.so in der "httpd.conf" auskommentieren (# entfernen). Dann f�r http://127.0.0.1:81 einrichten und testen! (NICHT f�r Microsoft Frontpage, einzig f�r Adobe Dreamweaver!)

---------------------------------------------------------------

* MYSQL-Hinweise:

(1) Um den MySQL-Daemon zu starten bitte Doppelklick auf \XAMPPlite\mysql_start.bat.
Der MySQL Server startet dann im Konsolen-Modus. Das dazu geh�rige Konsolenfenster muss offen bleiben (!!) Zum Stop bitte die mysql_shutdown.bat benutzen!

(2) Um den MySQL-Daemon von diesem Paket mit "innodb" f�r bessere Performance zu
nutzen, editiert bitte die "my" bzw."my.cnf" im Verzeichnis "/XAMPPlite/mysql/bin" bzw. als Dienst die C:\my.cnf unter NT / 2000 / XP. Dort aktiviert ihr dann die Zeile "innodb_data_file_path=ibdata1:30M". Achtung, "innodb" kann ich derzeit nicht
f�r 95 / 98 / ME empfehlen, da es hier immmer wieder zu blockierenden Systemen kam. Also nur NT / 2000 / XP!
Wer MySQL als Dienst unter NT / 2000 / XP benutzen m�chte, muss unbedingt (!) vorher die "my" bzw."my.cnf unter C:\ (also C:\my.cnf) implementieren. Danach die "mysql_installservice.bat" im Ordner "mysql" aktivieren.

(3) Der MySQL-Server startet ohne Passwort f�r MySQl-Administrator "root".
F�r eine Zugriff in PHP s�he das also aus:

	mysql_connect("localhost", "root", "");

Ein Passwort f�r "root" k�nnt ihr �ber den MySQL-Admin in der Eingabeaufforderung
setzen. Z. B.: 

	C:\XAMPPlite\mysql\bin\mysqladmin.exe -u root -p geheim

Wichtig: Nach dem Einsetzen eines neuen Passwortes f�r Root muss auch phpMyAdmin informiert werden! Das geschieht �ber die Datei "config.inc.php"; zu finden als C:\XAMPPlite\phpmyadmin\config.inc.php. Dort also folgenden 
Zeilen editieren:
   
	$cfg['Servers'][$i]['user']            = 'root';   // MySQL User
	$cfg['Servers'][$i]['auth_type']       = 'http';   // HTTP-Authentifzierung

So wird zuerst das "root"-Passwort vom MySQL-Server abgefragt, bevor phpMyAdmin zugreifen darf.
    
---------------------------------------------------------------	
    
		Have a lot of fun! | Viel Spa�! | Bonne Chance!
