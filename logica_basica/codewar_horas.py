def make_readable(seconds):
    return f'{seconds // 3600:02}:{seconds // 60 % 60:02}:{seconds % 60:02}'


if __name__ == '__main__':
    print(make_readable(0))
    print(make_readable(59))
    print(make_readable(60))
    print(make_readable(3599))
    print(make_readable(3600))
    print(make_readable(86399))
    print(make_readable(86400))
    print(make_readable(359999))
