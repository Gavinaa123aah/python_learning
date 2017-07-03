
def application(environ,start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return 'hello world!{0}---{1}'.format(environ['PATH_INFO'][1:],888)


