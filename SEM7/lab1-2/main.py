import concurrent.futures as ftres

def integrate(f, a: float, b: float, *, n_iter: int = 1000):
    if a == b:
        return 0

    # вычисление по методу трапеций
    h = (b - a) / n_iter
    s = (f(a) + f(b)) / 2
    x = a + h
    
    for i in range(int(n_iter)-1):
        s += f(x + i*h)
    
    result = h * s
    return float(round(result, 8))


def integrate_async(f, a: float, b: float, *, n_jobs: int = 2, n_iter: int = 1000):
    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs) # потоки
    step = (b - a) / n_jobs # шаг вычисления интеграла, кол-во частей равно кол-ву потоков

    fs = [(a + i * step, a + (i + 1) * step) for i in range(n_jobs)] # интервалы для каждого потока
    spawn_lst = [executor.submit(integrate, f, *interval, n_iter=n_iter // n_jobs) for interval in fs] # запуск вычислений в потоках, кол-во итераций n_iter делится на кол-во потоков
    s = [r.result() for r in ftres.as_completed(spawn_lst)] # сохранение значений интерграла на интервалах
    
    return sum(s) # значение интеграла - сумма значений на каждом интервале, вычисленном в отдельном потоке


if __name__ == '__main__':
    import math
    print(integrate(math.atan, 0, math.pi, n_iter=10**6))
    print(integrate_async(math.atan, 0, math.pi, n_iter=10**6))
