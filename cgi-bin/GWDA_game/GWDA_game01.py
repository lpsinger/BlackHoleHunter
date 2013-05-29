#!/usr/bin/env python

def general_error (exception):
  htmlOutput = "<html>\n"
  htmlOutput += "<body>\n"
  htmlOutput += "Error in running GWDA_game. Error message follows: \n"
  htmlOutput += "<br />"
  htmlOutput += "<br />"
  htmlOutput += str(exception)
  htmlOutput += "\n"
  htmlOutput += "<br />"
  htmlOutput += "<br />"
  htmlOutput += """<form method="POST" action="http://localhost/">
<input type="submit" value="Try again.">
</form>"""
  htmlOutput += "</body>\n</html>"
  return htmlOutput

print "Content-type: text/html\n\n"

try:
  import GWDA_game_code
  htmlOutput = GWDA_game_code.GWDA_game_main()
  print htmlOutput
except Exception, exception:
  htmlOutput = general_error (exception)
  print htmlOutput
  raise
