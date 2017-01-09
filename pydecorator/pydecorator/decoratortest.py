#/usr/bin/python
#encoding:utf-8

def log(text=None):
    if text==None:
        def decorator(func):
            def wrapper(*args, **kw):
                print 'begin call'
                re = func(*args,**kw)
                print 'end call'
                return re
            return wrapper
        return decorator
    else:
        def decorator(func):
            def wrapper(*args, **kw):
                print 'begin call'
                print text
                re = func(*args,**kw)
                print 'end call'
                return re
            return wrapper
        return decorator


@log()
def now():
    print 'now'

if __name__ == '__main__':
    now()
