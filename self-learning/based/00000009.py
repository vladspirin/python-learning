hobbies_Adam = ('reading', ('jogging', 'boxing', 'yoga'), 'movies')
# 1
def unpack(input_tuple):
    unpacked = []
    for i in input_tuple:
        if isinstance(i, tuple):
            unpacked.extend(i)
        else:
            unpacked.append(i)
    return tuple(unpacked)
# 2
def unpack(input_tuple):
    unpacked = ()
    for x in input_tuple:
        unpacked += x if isinstance(x, tuple) else (x,)
    return unpacked

