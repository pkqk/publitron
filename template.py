import traceback

def standard(values):
  layout = """<!doctype html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<title>%(title)s</title>
</head>
<body>
%(body)s
</body>
</html>"""
  return [layout % values]
  
def meta(extra=[]):
  return """<link rel="stylesheet" href="/style/base.css" type="text/css" media="all" />"""

def error(exception):
  return [str(exception),"\n"] + traceback.format_tb(exception.__traceback__)
