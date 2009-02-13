from . import template

import os.path
import json

class StaticPublisher:
  def __init__(self, doc_root):
    self.doc_root = doc_root

  def __call__(self, environ, start_response):
    self.environ = environ
    try:
      with open(self.path_from_request(),encoding='utf8') as doc:
        attrs, content = self.load_document(doc.read())
        response = template.standard(environ, attrs, content)
        start_response('200 OK', [self.content_type('html')])
        return response
    except IOError as e:
      start_response('404 Not Found', [self.content_type('plain')])
      return template.not_found(e)
    except Exception as e:
      start_response('500 Internal Server Error', [self.content_type('plain')])
      return template.error(e)

  def path_from_request(self):
    path = os.path.normpath(self.environ.get('PATH_INFO'))[1:]
    if path == '':
      path = 'index'
    return os.path.join(self.doc_root, '%s.doc' % path)
    
  def content_type(self,type):
    return ('Content-Type','text/%s;charset=utf-8' % type)
    
  def load_document(self,data):
    decoder = json.JSONDecoder()
    attrs, idx = decoder.raw_decode(data)
    content = data[idx:].strip()
    return attrs, content
