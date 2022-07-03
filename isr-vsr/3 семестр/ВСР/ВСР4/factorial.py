def factorial(n):
    
    if type(n) is not int:
        raise TypeError('n должно быть целым числом')
    
    if n < 0:
        raise ValueError('n должно быть больше или равно 0')
    
    result = 1
    
    for n in range(1, n + 1):
        result *= n
    
    return result
