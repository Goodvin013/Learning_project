def get_unit_trans(x, s=1024):
    d_units = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3,
               1: 'B', 2: 'KB', 3: 'MB', 4: 'GB'}
    for i in range(1, 5):
        if x > s: x /= s
        else: break
    return str(round(x)), d_units[i]

def size(byt: int):
    d = {1024 ** 3: 'GB', 1024 ** 2: 'MB', 1024: 'KB', 1: 'B'}
    for key, val in d.items():
        if byt > key:
            return round(byt / key), val

def hr_size(n, k = 0):
    return f"{round(n)} {['B', 'KB', 'MB', 'GB', 'TB'][k]}" if n < 1024 else hr_size(n / 1024, k + 1)

def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'