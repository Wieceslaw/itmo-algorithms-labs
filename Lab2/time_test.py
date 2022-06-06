from time import perf_counter


def time_test(func):
    def wrapper(*args, **kwargs):
        try:
            t_start = perf_counter()
            result = func(*args, **kwargs)
            print('Время работы: ' + str(perf_counter() - t_start) + ' секунд')
            return result
        except Exception as e:
            return f'Error: {e}' + help()
    return wrapper