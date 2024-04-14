import re


def alphanumeric(password):
    return bool(re.match(r'^[a-zA-Z0-9]+$', password))


if __name__ == '__main__':
    print(alphanumeric("hello world "))
    print(alphanumeric("PassW0rd"))
    print(alphanumeric("       "))
    print(alphanumeric(""))
    print(alphanumeric("VXg_YSNitPMR7zujLnco"))
