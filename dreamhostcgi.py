import sys, os
from wsgiref.handlers import BaseCGIHandler

class DreamhostCGIHandler(BaseCGIHandler):
  wsgi_run_once = True

  def __init__(self):
    environ = dict(os.environ.items())
    if not 'PATH_INFO' in environ:
      environ['PATH_INFO'] = environ['SCRIPT_URL']
    BaseCGIHandler.__init__(
      self, sys.stdin, sys.stdout.buffer, sys.stderr, environ,
      multithread=False, multiprocess=True
    )
