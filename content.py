from slog import template

import os.path

class StaticPublisher:
  def __init__(self, doc_root):
    self.doc_root = doc_root

  def __call__(self, environ, start_response):
    self.environ = environ
    try:
      with open(self.path_from_request()) as doc:
        values = {'title': 'test title'}
        values['body'] = doc.read() + "\n" + self.show_environ()
        response = template.standard(values)
        start_response('200 OK', [('Content-Type','text/html;charset=utf-8')])
        return response
    except Exception as e:
      start_response('404 Not Found', [('Content-Type', 'text/plain')])
      return template.error(e)

  def show_environ(self):
    return "<dl>%s</dl>" % "\n".join("<dt>%s</dt><dd>%s</dd>" % (k,v) for k,v in self.environ.items())

  def path_from_request(self):
    path = "%s.doc" % os.path.normpath(self.environ.get('PATH_INFO'))[1:]
    return os.path.join(self.doc_root,path)
