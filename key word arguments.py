def hello(**kargs):
    for k,v in kargs.items():
        print(k,v)

d = {str(k):v for k in range(10)
     for v in range(10)}

hello(**d)

def hello_list(name, *args, **kwargs):
    for c in args:
        print(c)
    print(name)

    for k,v in kwargs.items():
        print(k,v)

hello_list('Andrew', (5,5,5,5,5), **d)
