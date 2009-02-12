import traceback

def standard(attrs, content):
  return ["\n".join(
    prelude(attrs) +
    surround('html',
      surround('head',title(attrs)+stylesheet(attrs)) +
      body(attrs, content)
    )
  )]

def title(attrs):
  return surround('title',attrs['title'])
  
def prelude(attrs):
  return ['<!doctype html>']
  
def stylesheet(attrs):
  return ['<link rel="stylesheet" href="/style/base.css" type="text/css" media="all" />']

def body(attrs, content):
  return surround('body', content)
  
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
