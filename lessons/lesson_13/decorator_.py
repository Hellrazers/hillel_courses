
def fn_1():
    return 'Hello'

def fn_2(fn):
    print(fn, 'word')


fn_value = fn_1

fn_2(fn_value())



def first_deco(fn):
    def wrapper(*args, **kwargs):
        print('--' * 80)
        print('Before')
        value_fn = fn(*args, **kwargs)
        print('--' * 80)
        print('value_fn:', value_fn)
        return value_fn
    return wrapper


@first_deco
def fn_3():
    return 'Hello'


fn_3()

@first_deco
def fn_4():
    pass

fn_4()

@first_deco
def fn_5(*args):
    print(args)
    return sum(args)

list_values = list(range(1,4))

fn_5(*list_values)