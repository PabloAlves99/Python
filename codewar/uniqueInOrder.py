def unique_in_order(sequence):
    list = []
    x = ''
    for i in sequence:
        if i == x:
            continue
        else:
            list.append(i)
        x = i
    return list

print(unique_in_order('ABCabcABCabc'))