from mod_python import apache
def handler(req):
        req.content_type = "text/html"
        req.write("OK")	
        return apache.OK