def in_array(array1, array2):
    r = set()
    for _a1 in array1:
        for _a2 in array2:
            if _a1 in _a2:
                r.add(_a1)
    return [*r]


a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1, a2))
