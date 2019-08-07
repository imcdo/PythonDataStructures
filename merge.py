from collections.abc import Iterable # import the iterable type


def star(*l, **kv):
    print('tuple', l)
    print('values: ', *l)
    print(kv)
    print(kv.items())

    for k,v in kv.items():
        pass
    # dict = {*kv}

def merge_sorted_list(l1: Iterable, l2: Iterable) -> list:
    l = []
    i1 = i2 = 0

    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] <= l2[i2]:
            l.append(l1[i1])
            i1 += 1
        else:
            l.append(l2[i2])
            i2 += 1
    
    # one is empty so this is definitly sorted
    l.extend([*l1[i1:], *l2[i2:]])
    return l

def merge_sort_rec(l: Iterable) -> list:
    if len(l) == 1:
        return l 
    else:
        return merge_sorted_list(merge_sort_rec(l[:len(l)//2]), \
                                 merge_sort_rec(l[len(l)//2:]))


# print(merge_sort_rec([1,3,2,10,4,5,20,14]))
star(1,2,3,4,45,5,5,6,7, key=2, w=[1,2,3,4])