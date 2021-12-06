def mars_age(age: int) -> int:
    a = age * 365
    rez = a // 687
    return rez


print(mars_age(1000))
