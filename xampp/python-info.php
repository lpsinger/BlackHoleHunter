<html>
<head>
<meta name="author" content="Kay Vogelgesang, Kai Oswald Seidler">
<link href="xampp.css" rel="stylesheet" type="text/css">
</head>

<body>
<? 
include("lang/".file_get_contents("lang.tmp").".php"); 
include ("where.php");
?>

&nbsp;<br>
<h1>PYTHON</h1>

<table border="0">


<tr>
<td width="100"><?=$TEXT['info-module']?>:</td>
<td width="10">&nbsp;</td>
<td width="*">Python/2.3.5</td>
</tr>
<tr>
<td width="100"><?=$TEXT['info-extension']?>:</td>
<td width="10">&nbsp;</td>
<td width="*">.py</td>
</tr>
<tr>
<td width="100"><?=$TEXT['info-docdir']?>:</td>
<td width="10">&nbsp;</td>
<td width="*"><? echo $partwampp."\htdocs\\python\\";?></td>
</tr>
<tr>
<td width="100"><?=$TEXT['info-conf']?>:</td>
<td width="10">&nbsp;</td>
<td width="*"><? echo $partwampp."\apache\\conf\\python.conf";?></td>
</tr>
<tr>
<td width="100"><?=$TEXT['info-examples']?>:</td>
<td width="10">&nbsp;</td>
<td width="*"><? echo $partwampp."\htdocs\\python\\index.py";?> | Alias: <a target=content href=/python/index.py>http://localhost/python/index.py</a></td>
</tr>
<tr>
<td width="100">&nbsp;</td>
<td width="10">&nbsp;</td>
<td width="*">&nbsp;</td>
</tr>
<tr>
<td width="100"><?=$TEXT['info-extension']?>:</td>
<td width="10">&nbsp;</td>
<td width="*">.cgi</td>
</tr>
<tr>
<td width="100"><?=$TEXT['info-docdir']?>:</td>
<td width="10">&nbsp;</td>
<td width="*"><? echo $partwampp."\cgi-bin\\";?> &amp; <? echo $partwampp."\htdocs\\";?></td>
</tr>
<tr>
<td width="100"><?=$TEXT['info-conf']?>:</td>
<td width="10">&nbsp;</td>
<td width="*"><? echo $partwampp."\apache\\conf\\python.conf";?></td>
</tr>
<tr>
<td width="100"><?=$TEXT['info-examples']?>:</td>
<td width="10">&nbsp;</td>
<td width="*"><? echo $partwampp."\cgi-bin\\python.cgi";?> | Alias: <a target=content href=/cgi-bin/python.cgi>http://localhost/cgi-bin/python.cgi</a></td>
</tr>

<tr>
<td width="100">&nbsp;</td>
<td width="10">&nbsp;</td>
<td width="*">&nbsp;</td>
</tr>
<tr>
<td width="100"><?=$TEXT['info-extension']?>:</td>
<td width="10">&nbsp;</td>
<td width="*">.spy => Spyce 2.0.3</td>
</tr>
<tr>
<td width="100"><?=$TEXT['info-docdir']?>:</td>
<td width="10">&nbsp;</td>
<td width="*"><? echo $partwampp."\htdocs\\python\\";?></td>
</tr>
<tr>
<td width="100"><?=$TEXT['info-conf']?>:</td>
<td width="10">&nbsp;</td>
<td width="*"><? echo $partwampp."\apache\\conf\\python.conf";?></td>
</tr>
<tr>
<td width="100"><?=$TEXT['info-examples']?>:</td>
<td width="10">&nbsp;</td>
<td width="*"><? echo $partwampp."\htdocs\\python\\info.spy";?> | Alias: <a target=content href=/python/info.spy>http://localhost/python/info.spy</a></td>
</tr>

<tr>
<td width="100">&nbsp;</td>
<td width="10">&nbsp;</td>
<td width="*">&nbsp;</td>
</tr>
<tr>
<td width="100">Homepage:</td>
<td width="10">&nbsp;</td>
<td width="*"><A HREF="http://www.python.org" target="_new">http://www.python.org</A></td>
</tr>
<tr>
<td width="100">&nbsp;</td>
<td width="10">&nbsp;</td>
<td width="*">&nbsp;</td>
</tr>
</table>
<p>


</body>
</html>
