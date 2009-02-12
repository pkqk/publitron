import traceback

def standard(environ, attrs, content):
  return StandardTemplate(environ,attrs,content).render()

class StandardTemplate:
  def __init__(self,environ,attrs,content):
    self.environ = environ
    self.attrs = attrs
    self.content = content

  def title(self):
    return self.surround('title',self.attrs['title'])
  
  def prelude(self):
    return ['<!doctype html>']
  
  def stylesheet(self):
    return ['<link rel="stylesheet" href="/style/base.css" type="text/css" media="all" />']

  def body(self):
    return self.surround('body', self.content)
    # return self.surround('body', self.content + self.show_environ())
  
  def surround(self,tag,content):
    if isinstance(content,str):
      inner = [content]
    else:
      inner = content
    return ['<%s>'%tag] + inner + ['</%s>'%tag]
    
  def show_environ(self):
    return "<dl>%s</dl>" % "\n".join("<dt>%s</dt><dd>%s</dd>" % (k,v) for k,v in self.environ.items())
  
  def render(self):
    return ["\n".join(
      self.prelude() +
      self.surround('html',
        self.surround('head',self.title()+self.stylesheet()) +
        self.body()
      )
    )]

def error(exception):
  return ["\n".join([repr(exception),str(exception)]+traceback.format_tb(exception.__traceback__))]

def not_found(exception):
  return ["resource not found: %s" % exception.filename]
