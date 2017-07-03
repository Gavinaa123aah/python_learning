def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

def application1(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    #return [b'<h1>Hello,ttttt!</h1>']
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'])
    print environ['PATH_INFO']
    return [body.encode('utf-8')]

def application3(environ, start_response):
    path = environ['PATH_INFO']
    start_response('200 ok', [('Content_Type', 'text/html')])
    if path == '/':
        return '<h1>index</h1>'
    elif path == '/signin':
        return '<h1>login</h1>'

from wsgiref.simple_server import make_server

#httpd = make_server('', 8001, application)
#print('Serving HTTP on port 8001...')
httpd2 = make_server('',8002,application3)
print('Serving HTTP on port 8002...')
#httpd.serve_forever()
httpd2.serve_forever()