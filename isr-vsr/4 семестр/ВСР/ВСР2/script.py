def checktime(function):
    def wrapper(*args, **kwargs):
        import time
        t1 = time.time()
        value = function(*args, **kwargs)
        t2 = time.time()
        t = t2 - t1
        print('Время выполнения функции {}: {}'.format(function.__name__, t))
        return value

    return wrapper


@checktime
def test_function():
    import time
    time.sleep(0.5)
    
    
test_function()