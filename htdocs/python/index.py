from mod_python import apache
def handler(req):
        req.content_type = "text/html"
        req.write("<html><head><link href=\"../xampp/xampp.css\" rel=\"stylesheet\" type=\"text/css\"></head><body>")
	req.write("&nbsp;<p><h1>Python is running with mod_python ...</h1>")
	req.write("<b>... that is all ...</b><br><br><br>")
        return apache.OK