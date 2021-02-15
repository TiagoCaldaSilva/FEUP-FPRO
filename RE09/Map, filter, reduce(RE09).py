from functools import reduce


def reduce_map_filter(args):
    if type(args[2]) != tuple:
        if args[0] == "map":
            return list(map(args[1], args[2]))
        elif args[0] == "reduce":
            return reduce(args[1], args[2])
        elif args[0] == "filter":
            return list(filter(args[1], args[2]))
    else:
        return reduce_map_filter((args[0], args[1], reduce_map_filter(args[2])))
