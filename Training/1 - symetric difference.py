def content(set1, set2, args):
    for a in set1:
        if a not in set2:
            args.append(a)

def binary_sym(set1, set2):
    args = []
    content(set1, set2, args)
    content(set2, set1, args)
    print(args)
    return args

def sym(*args):
    set1 = args.pop(0)
    set2 = args.pop(1)
    args.add(binary_sym(set1, set2))
    if (args.sizeof != 1):
        sym(*args)
    else:
        return args[0]
        
sym([1, 2, 3], [5, 2, 1, 4,])