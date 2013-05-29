#!C:/xampplite/python/python.exe
import random

def html_header_standard():
  htmlOutput = html_header_top() + html_header_bottom()
  return htmlOutput


def html_header_flash(waveSound,signalSound):
  htmlOutput = html_header_top() + html_header_flashscript(waveSound,signalSound) + html_header_bottom()
  return htmlOutput

def html_header_top():
  htmlOutput = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
      "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-gb">
<head>
	<meta name="Author" content="Cardiff University Relativity Group"/>
	<meta name="copyright" content="Copyright Cardiff University"/>
	<meta name="Description" content="Black Hole Hunter Website "/>
	<meta name="keywords" content="Black Hole Hunter, Relativity Group, Cardiff University, Cardiff, Wales, United Kingdom"/>
	<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
	<title>Black Hole Hunter</title>
	<style type="text/css" media="all"> @import "/styles-site.css"; </style>
	<link rel="alternate stylesheet" type="text/css" media="all" title="large" href="/large.css"/>
	<link rel="alternate stylesheet" type="text/css" media="all" title="small" href="/small.css"/>
	<link rel="stylesheet" type="text/css" media="all" href="/css/yui/container.css"/>
	<script type="text/javascript" src="/scripts/styleswitcher.js"></script>
	<script type="text/javascript" src="/scripts/popup.js"></script>
	<script src="/js/yui/yahoo-dom-event.js" type="text/javascript"></script>
    <script src="/js/yui/dragdrop-min.js" type="text/javascript"></script>
    <script src="/js/yui/container-min.js" type="text/javascript"></script>
    <script src="/js/yui/popups.js" type="text/javascript"></script>
"""
  return htmlOutput


def html_header_bottom():
  htmlOutput = """</head>

<body>
<div id="wrap">
	<div id="header">
		<span><a href="http://localhost/"><img src="/images/logo2.jpg" alt="Black Hole Hunter" title="Black Hole Hunter" height="62" width="452" /></a></span>
		<div id="right">
			Text size: 
			<a href="#" onclick="setActiveStyleSheet('small'); return false;">Small</a>
			 / 
			<a href="#" onclick="setActiveStyleSheet('medium'); return false;">Medium</a>
			 / 
			<a href="#" onclick="setActiveStyleSheet('large'); return false;">Large</a>
			<br />
                  Click <a href="http://localhost/index.html"><b>here</b></a> to restart game.
                  <br />
<!--
			<br/>

			<a href="http://jigsaw.w3.org/css-validator/validator?uri=http://www.blackholehunter.org/" rel="external"><img style="border:0;width:80px;height:15px" src="/images/css.gif" alt="Valid CSS!" title="Valid CSS!"/></a>
			<a href="http://validator.w3.org/check?uri=referer" rel="external"><img src="/images/xhtml0.gif" alt="Valid XHTML 1.0" title="Valid XHTML 1.0" height="15" width="80" /></a>
-->
		</div>
	</div>
"""
  return htmlOutput

def html_header_flashscript(waveSound,signalSound):
  htmlOutput = """	<script type="text/javascript" src="/soundmanager/script/soundmanager2-nodebug-jsmin.js"></script>
	<script type="text/javascript">
		soundManager.url = '/soundmanager/soundmanager2.swf'; // override default SWF url
		soundManager.debugMode = true;
		soundManager.consoleOnly = false;
		soundManager.onload = function() {
//			soundManager is initialised, ready to use. Create a sound for this demo page.
			soundManager.createSound({
				id:'signal',
				url: '""" + signalSound + """'
			});
			soundManager.createSound({
				id:'sound0',
				url: '""" + waveSound[0] + """'
			});
			soundManager.createSound({
				id:'sound1',
				url: '""" + waveSound[1] + """'
			});
			soundManager.createSound({
				id:'sound2',
				url: '""" + waveSound[2] + """'
			});
			soundManager.createSound({
				id:'sound3',
				url: '""" + waveSound[3] + """'
			});
			soundManager.createSound({
				id:'chirp',
				url: '/eo/chirp1.mp3'
			});
			soundManager.createSound({
				id:'BHNS',
				url: '/eo/BHNS.mp3'
			});
			soundManager.createSound({
				id:'GEO',
				url: '/eo/GEO.mp3'
			});
		}
	</script>
"""
  return htmlOutput

def error_form_reading():
  htmlOutput = """<div id="contentgame"> 
<p>
Error in processing form data. Please return to the previous page and try again.
</p>
<form action="/index.html" method="post">
<p>
<input name="submit" value="Try again" id="submit" type="submit"/>
</p>
</form> 
</div>
</div>
</body>

</html>
"""
  return htmlOutput

def no_signal_set():
  htmlOutput = """<div id="contentgame"> /n"""
  htmlOutput += "Error: no signal has been chosen. If you are seeing this message please contact the developers.\n"
  htmlOutput +=  "Please return to the previous page and try again.\n"
  htmlOutput += """<form method="post" action="/index.html">
<p>
<input type="submit" value="Try again." />
</p>
</form> \n"""
  htmlOutput += "</div></div></body></html \n>"
  return htmlOutput

def game_main_html(numBoxes,waveSound,wavePicture,signalSound,signalPicture, \
                   sigNoisePicture,signalType,signalMass1,\
                   signalMass2,signalInclination,\
                   signalLocation,userScore,difficultyLevel,glitchFlag,\
                   numPlays,numLives):
  htmlOutput = """<div id="contentgame">"""
  htmlOutput += """<p class="intro" style="border-right: 1px solid #000000">\n"""
  htmlOutput += "Your mission, should you choose to accept it, is to find the gravitational wave signal from "
  if float(signalMass1) > 3 and float(signalMass2) > 3:
    htmlOutput += """the merger of two black holes"""
  elif float(signalMass1) < 3 and float(signalMass2) < 3:
    htmlOutput += """the merger of two neutron stars"""
  else:
    htmlOutput += """the merger of a black hole and a neutron star"""
  htmlOutput += " with masses " + signalMass2 + " and " + signalMass1
  htmlOutput += """ Solar masses in the noisy output of a gravitational wave detector.\n"""
  htmlOutput += "</p>\n<p class=\"intro\">\n"
  htmlOutput += "You can listen to this source by clicking on the images below. Then look at, and listen to, the four detector outputs. One of them will contain this signal; you must decide which one!\n"
  htmlOutput += "</p>\n\n"


  if glitchFlag:
    htmlOutput += """<p class="warning">
<b>Warning!</b><br/>
Real detectors do not give perfect output. Some of the data streams below may contain short, noisy glitches. Do not be fooled by these!
</p>
\n
"""


  htmlOutput += """<br style="clear: both" />\n\n"""
  htmlOutput += """<div class="signal"> \n"""
  htmlOutput += """<br />\n"""
  htmlOutput +="<p><b>Click on the image below to hear the sound.</b></p>\n\n"

  htmlOutput += """<img onclick="soundManager.play('signal')" style="width: 380px; height: 274px;" src=" """ + signalPicture  + """ " alt="The True Signal" title="The True Signal"/>\n"""  
  htmlOutput +="<p><b>This is the gravitational wave signal you are hunting for.</b></p>\n"
  htmlOutput +="""<br />\n"""

  if float(signalMass1) > 3 and float(signalMass2) > 3:
    signalPiccy = random.randrange(0,3,1)
    if signalPiccy == 0:
      htmlOutput +="""<img onclick="soundManager.play('signal')" style="width: 263px; height: 274px;" src="/images/bbh.jpg" alt="Ein Doppelsternsystem aus zwei schwarzen L&ouml;chern" title="A binary black hole system"/>\n"""
    if signalPiccy == 1:
      htmlOutput +="""<img onclick="soundManager.play('signal')" style="width: 365px; height: 274px;" src="/images/ORBHOLE7.jpg" alt="A binary black hole system." title="A binary black hole system"/>\n"""
    if signalPiccy == 2:
      htmlOutput +="""<img onclick="soundManager.play('signal')" style="width: 368px; height: 274px;" src="/images/bhCoal1.gif" alt="A binary black hole system." title="A binary black hole system"/>\n"""
  elif float(signalMass1) < 3 and float(signalMass2) < 3:
    signalPiccy = random.randrange(0,2,1)
    if signalPiccy == 0:
      htmlOutput +="""<img onclick="soundManager.play('signal')" style="width: 343px; height: 274px;" src="/images/bns.jpg" alt="A binary neutron star system." title="A binary neutron star system."/>\n"""
    if signalPiccy == 1:
      htmlOutput +="""<img onclick="soundManager.play('signal')" style="width: 365px; height: 274px;" src="/images/still1.jpg" alt="A binary neutron star system." title="A binary neutron star system."/>\n"""
  else:
    signalPiccy = random.randrange(0,2,1)
    if signalPiccy == 0:
      htmlOutput +="""<img onclick="soundManager.play('signal')" style="width: 281px; height: 274px;" src="/images/nsbh.jpeg " alt="A neutron star, black hole system." title="A neutron star, black hole system" />\n"""
    if signalPiccy == 1:
      htmlOutput +="""<img onclick="soundManager.play('signal')" style="width: 292px; height: 274px;" src="/images/Neutron4Lunch_1.jpg " alt="A neutron star, black hole system." title="A neutron star, black hole system" />\n"""


  htmlOutput +="<p><b>This is the waveform you are listening for.</b></p>\n"
  htmlOutput +="</div>\n\n"

  htmlOutput += """<div class = "outputs">\n"""
  htmlOutput += """<br />\n"""
  htmlOutput += "<p><b>Scroll down, and click on the picture to hear the corresponding sounds.</b></p> \n"
  htmlOutput += """<br />\n"""
  htmlOutput += """<div id="stream1">\n"""
  htmlOutput += """<br />\n"""
  htmlOutput += "<p><b>Data Stream 1</b></p>\n"
  htmlOutput += """<img onclick="soundManager.play('sound0')" style="width: 342px; height: 246px; align: left;" src=" """ + wavePicture[0] + """ " alt="Is the signal in here?" title="Is the signal in here?" />\n"""
  htmlOutput += "</div>\n"

  htmlOutput += """<div id="stream2">\n"""
  htmlOutput += """<br />\n"""
  htmlOutput += "<p><b>Data Stream 2</b></p>\n"
  htmlOutput += """<img onclick="soundManager.play('sound1')" style="width: 342px; height: 246px; align: left;" src=" """ + wavePicture[1] + """ " alt="Is the signal in here?" title="Is the signal in here?" />\n"""
  htmlOutput += "</div>\n"

  htmlOutput += """<div id="stream3">\n"""
  htmlOutput += """<br />\n"""
  htmlOutput += "<p><b>Data Stream 3</b></p>\n"
  htmlOutput += """<img onclick="soundManager.play('sound2')" style="width: 342px; height: 246px; align: left;" src=" """ + wavePicture[2] + """ " alt="Is the signal in here?" title="Is the signal in here?" />\n"""
  htmlOutput += "</div>\n"

  htmlOutput += """<div id="stream4">\n"""
  htmlOutput += """<br />\n"""
  htmlOutput += "<p><b>Data Stream 4</b></p>\n"
  htmlOutput += """<img onclick="soundManager.play('sound3')" style="width: 342px; height: 246px; align: left;" src=" """ + wavePicture[3] + """ " alt="Is the signal in here?" title="Is the signal in here?" />\n"""
  htmlOutput += "</div>"
  htmlOutput += """<br />\n"""

  htmlOutput += """<div id="select">\n"""
  htmlOutput += """<br />\n"""
  htmlOutput += """<br />\n"""
  htmlOutput += """<form method="post" action="/cgi-bin/GWDA_game/GWDA_game02.py">\n"""
  htmlOutput += """<p>Select which example contains the signal:&nbsp;&nbsp;\n"""
  htmlOutput += """<input name="submit" value="Proceed" id="submit" type="submit"/><br/></p> \n"""  
  htmlOutput += """<p><input name="answer" id="answer" value="1" type="radio" checked="checked"/>Data Stream 1 \n"""
  htmlOutput += """&nbsp;&nbsp;&nbsp;&nbsp; \n"""
  htmlOutput += """<input name="answer" value="2" type="radio"/>Data Stream 2 \n"""
  htmlOutput += """&nbsp;&nbsp;&nbsp;&nbsp; \n"""
  htmlOutput += """&nbsp;&nbsp;&nbsp;&nbsp; <br/> \n"""
  htmlOutput += """<input name="answer" value="3" type="radio"/>Data Stream 3 \n"""
  htmlOutput += """&nbsp;&nbsp;&nbsp;&nbsp; \n"""  
  htmlOutput += """<input name="answer" value="4" type="radio"/>Data Stream 4 \n"""  

  htmlOutput += """<input type="hidden" name="asfdghti" value=""" + "\""  + str(signalLocation) + "\"" + """/>
<input type="hidden" name="userscore" value=" """ + str(userScore) + """ "/>
<input type="hidden" name="difficulty" value=" """ + str(difficultyLevel) + """ "/>
<input type="hidden" name="numplays" value=" """ + str(numPlays) + """ "/>
<input type="hidden" name="numlives" value=" """ + str(numLives) + """ "/>
<input type="hidden" name="signalpic" value=" """ + sigNoisePicture + """ "/>
<input type="hidden" name="wavepic1" value=" """ + wavePicture[0] + """ "/>
<input type="hidden" name="wavepic2" value=" """ + wavePicture[1] + """ "/>
<input type="hidden" name="wavepic3" value=" """ + wavePicture[2] + """ "/>
<input type="hidden" name="wavepic4" value=" """ + wavePicture[3] + """ "/>
<input type="hidden" name="wavesound1" value=" """ + waveSound[0] + """ "/>
<input type="hidden" name="wavesound2" value=" """ + waveSound[1] + """ "/>
<input type="hidden" name="wavesound3" value=" """ + waveSound[2] + """ "/>
<input type="hidden" name="wavesound4" value=" """ + waveSound[3] + """ "/>   
"""
  htmlOutput += "<br />\n</p>\n</form>\n</div>\n</div>\n</div>\n</div>\n</body>\n</html>"""
  return htmlOutput

def answer_given(answerCorrect,wavePicture,userScore,quoteText,quoteLink,quoteID,quoteDivId,quoteSrc,quoteHd,\
                 difficultyLevel,numPlays,numLives):
  htmlOutput = """	<div id="contentgame"> \n"""
  htmlOutput += """<div id="result">\n"""

  if answerCorrect:
    htmlOutput += "<p><b>Well done!</b></p>\n"
  if not answerCorrect:
    htmlOutput += "<p><b>I'm sorry!</b></p>\n"
  if answerCorrect:
    htmlOutput += "<p>That was the correct answer!</p><p>On the right you can see the signal, shown in red, embedded in the noise of the correct data stream.</p>\n"
  if not answerCorrect:
    htmlOutput += "<p>That was the wrong answer.</p> <p>On the right you can see the signal, shown in red, embedded in the noise of the correct data stream.</p>\n"
  htmlOutput += """<p><b>Current score: """ + str(userScore) + """&nbsp;&nbsp;&nbsp;&nbsp; Current lives: """ + str(numLives) + """</b></p>\n"""
  htmlOutput += """<form method="post" action="/cgi-bin/GWDA_game/GWDA_game01.py"> \n"""
  htmlOutput += """<p>\n"""
  htmlOutput += """<input type="hidden" name="quotetext" value=""" + "\"" + str(quoteText) + "\"" + """ />\n"""
  htmlOutput += """<input type="hidden" name="quotelink" value=""" + "\"" + str(quoteLink) + "\"" + """ />\n"""
  htmlOutput += """<input type="hidden" name="userscore" value=""" + "\"" + str(userScore) + "\"" + """ />
<input type="hidden" name="difficulty" value=""" + "\"" + str(difficultyLevel) + "\"" + """ />
<input type="hidden" name="numplays" value=""" + "\"" + str(numPlays) + "\"" + """ />
<input type="hidden" name="numlives" value=""" + "\"" + str(numLives) + "\"" + """ />
"""
  if numLives < 1:
    htmlOutput += """<input type="submit" value="Click for your final score. "/>\n"""
  elif numPlays > 5:
    htmlOutput += """<input type="submit" value="Click for your final score. "/>\n"""
  elif answerCorrect:
    htmlOutput += """<input type="submit" value="Continue to level """ + str(difficultyLevel) + """ "/>\n"""
  else:
    htmlOutput += """<input type="submit" value="Try level """ + str(difficultyLevel) + """ again"/>\n"""
  
  htmlOutput += "</p>\n"
  htmlOutput += """</form>\n<br />\n"""

  htmlOutput +="""<div class="didyouknow">
<p><b>Did you know?</b></p>
<p>
""" + quoteText + """
</p>
"""
  if quoteLink:
    htmlOutput +="""
        <script type="text/javascript">
    	function """ + quoteDivId + """Insert() {
    		var req = new XMLHttpRequest();
    		req.open("GET",""" + '"' + quoteSrc + '"' + """,true);
    		req.onreadystatechange = function() {
    			if(req.readyState==4) {
    				if(req.status==200) {
    					var d = document.getElementById(""" + '"' + quoteDivId + """Body")
    					d.innerHTML = req.responseText;
    				}
    			}
    		}
    		req.send(null);
    	}
    </script>"""
    htmlOutput += """<p>\n<a href="javascript:""" + quoteDivId + 'Insert()"' + """id="quote""" + quoteID + """" title="Mehr lesen" rel="external">Mehr lesen ...</a>\n</p>\n</div>\n"""
    htmlOutput += """<div class="yui-skin-sam">
<div id=""" + '"' + quoteDivId + '"' + """>
<div class="hd">""" + quoteHd + """</div>
<div class="bd" id=""" + '"' + quoteDivId + 'Body"' + """></div>
<div class="ft">&copy; http://www.einstein-online.info</div>
</div>
"""

  htmlOutput += """</div>\n</div>\n"""
  htmlOutput += """<div class="outputs" style="border: none; padding-top: 20px">\n"""
  htmlOutput += """<div id="stream1">\n"""
  htmlOutput += """<br />\n"""
  htmlOutput += "<p><b>Data Stream 1</b></p>\n"
  htmlOutput += """<img onclick="soundManager.play('sound0')" style="width: 342px; height: 246px;" src=" """ + wavePicture[0] + """ " alt="Data with signal (if present) shown." title="Data with signal (if present) shown." />\n"""
  htmlOutput += """</div>\n"""
  htmlOutput += """<div id="stream2">\n"""
  htmlOutput += """<br />\n"""
  htmlOutput += "<p><b>Data Stream 2</b></p>\n"
  htmlOutput += """<img onclick="soundManager.play('sound1')" style="width: 342px; height: 246px;" src=" """ + wavePicture[1] + """ " alt="Data with signal (if present) shown." title="Data with signal (if present) shown."/>\n"""
  htmlOutput += """</div>\n"""
  htmlOutput += """<div id="stream3">\n"""
  htmlOutput += """<br />\n"""
  htmlOutput += "<p><b>Data Stream 3</b></p>\n"
  htmlOutput += """<img onclick="soundManager.play('sound2')" style="width: 342px; height: 246px;" src=" """ + wavePicture[2] + """ " alt="Data with signal (if present) shown." title="Data with signal (if present) shown."/>\n"""
  htmlOutput += """</div>\n"""
  htmlOutput += """<div id="stream4">\n"""
  htmlOutput += """<br />\n"""
  htmlOutput += "<p><b>Data Stream 4</b></p>\n"
  htmlOutput += """<img onclick="soundManager.play('sound3')" style="width: 342px; height: 246px;" src=" """ + wavePicture[3] + """ " alt="Data with signal (if present) shown." title="Data with signal (if present) shown."/>\n"""
  htmlOutput += """</div>\n"""
  htmlOutput += """</div>\n</div>\n</div>\n</body>\n</html>"""
  return htmlOutput

def game_over(finishFlag,userScore):
  htmlOutput ="""<div id="sidelinks">

<ul id="sidelist">

<li>
The Black Hole Hunter game was developed as a part of the Royal Society
Summer Exhibition 2008, <i>Can you hear black holes collide?</i>
presented by Cardiff University, Universities of Birmingham, Glasgow
and Southampton in the UK in collaboration with the Albert Einstein
Institute and Milde Marketing in Germany.<br/>
<br/>

Copyright &copy; Cardiff University
</li>

<li><hr/></li>

<li>
<img src="/images/logos2go/GWDA_logos_vert_final.jpg" alt="" title="" height="392" width="222" id="maps" usemap="#links" />
</li>

</ul>
</div>
"""
  htmlOutput += """<div id="content"> \n"""
  htmlOutput += """<p>
<img class="float" title="Two merging black holes" src="/images/main_wav2.jpg" width="200" height="209" alt="Two merging black holes"/>
</p> \n"""
  htmlOutput += """<p>"""
  if finishFlag:
    htmlOutput += """<b> Congratulations! </b></p> \n <p> You have completed <i>Black Hole Hunter</i>. We hope you enjoyed it!</p>"""
  else:
  	htmlOutput += """<b> Game Over! </b></p> \n <p>\n I'm sorry, you have run out of lives.</p> <p>Thank you for playing <i>Black Hole Hunter</i>. We hope you enjoyed it!\n</p>\n<p>\n</p>"""
  	htmlOutput += """<p><b> Your final score was: """ + str(userScore) + """</b></p>"""
  if finishFlag:
    htmlOutput += """<p> Why not play again with a harder starting level? </p>"""
  else:
    htmlOutput += """<p> Would you like to try again? </p>"""
  htmlOutput += """
<form method="post" action="/index.html">
<p> <input type="submit" value="Restart Game"/>
</p>
</form>

</div>
</div>
</div>
</div>
</body>

</html>
"""
  return htmlOutput 


