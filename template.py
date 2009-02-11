import traceback

def standard(values):
  return ["\n".join(
    doctype(values) +
    surround('html',
      surround('head',title(values)+stylesheet(values)) +
      body(values)
    )
  )]

def title(values):
  return surround('title',values['title'])
  
def doctype(values):
  return ['<!doctype html>']
  
def stylesheet(values):
  return ['<link rel="stylesheet" href="/style/base.css" type="text/css" media="all" />']

def body(values):
  return surround('body',values['body'])
  
def surround(tag,content):
  if isinstance(content,str):
    inner = [content]
  else:
    inner = content
  return ['<%s>'%tag] + inner + ['</%s>'%tag]

def error(exception):
  return ["\n".join([repr(exception),str(exception)]+traceback.format_tb(exception.__traceback__))]

def not_found(exception):
  return ["resource not found: %s" % exception.filename]
