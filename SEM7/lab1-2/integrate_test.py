from main import integrate, integrate_async


def test_integrate_func():
    assert callable(integrate)


def test_integate_type():
    import math
    result = integrate(math.cos, 1, 5)
    assert type(result) is float


def test_integrate_range():
    import math
    result = integrate(math.sin, 1, 1, n_iter=150)
    assert result == 0


def test_integrate_1():
    f = lambda x: x ** 2 + 3 * x + 5
    result = integrate(f, 5, 10)
    assert result == 429.1666875


def test_integrate_2():
    import math
    result = integrate(math.sin, 1, 5, n_iter=1000)
    assert result == 0.25663978


def test_integrate_3():
    f = lambda x: x ** 3 + 1.5 * x
    result = integrate(f, 2, 12, n_iter=100)
    assert result == 5285.35


def test_integrate_async_1():
    f = lambda x: x ** 2 + 3 * x + 5
    result = integrate_async(f, 1, 10)
    assert result == 526.5001215


def test_integrate_async_2():
    import math
    result = integrate_async(math.sin, 1, 5, n_iter=1000)
    assert result == 0.25663978


def test_integrate_async_3():
    f = lambda x: x ** 3 + 1.5 * x
    result = integrate_async(f, 2, 12, n_iter=100)
    assert result == 5285.35

