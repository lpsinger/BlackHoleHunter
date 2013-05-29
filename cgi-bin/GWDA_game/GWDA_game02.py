#!/usr/bin/env python

def general_error (exception):
  htmlOutput = "<html>\n"
  htmlOutput += "<Body>\n"
  htmlOutput += "Error in running GWDA_game. Error message follows: \n"
  htmlOutput += "<br />"
  htmlOutput += "<br />"
  htmlOutput += "\n"
  htmlOutput += str(exception)
  htmlOutput += "\n"
  htmlOutput += "<br />"
  htmlOutput += "<br />"
  htmlOutput += """<form method="POST" action="/cgi-bin/GWDA_game/GWDA_game.html">
<input type="submit" value="Try again.">
</form>"""
  htmlOutput += "</body>\n</html>"
  return htmlOutput

print "Content-type: text/html\n\n"

try:
  import GWDA_game_code
  htmlOutput = GWDA_game_code.GWDA_game_results()
  print htmlOutput
except Exception, exception:
  htmlOutput = general_error (exception)
  print htmlOutput
  raise
