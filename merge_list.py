def merge_list(a, b):
    c = []
    N = len(a)
    M = len(b)

    i,j = 0,0

    while i < N and j < M:
        if a[i] <= b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j +=1

    c+=a[i:]+b[j:]
    return c


def split_and_merge_list(a):
    N1 = len(a)//2
    a1 = a[:N1]
    a2 = a[N1:]

    if len(a1) > 1:
        a1 = split_and_merge_list(a1)
    if len(a2) > 1:
        a2 = split_and_merge_list(a2)

    return merge_list(a1,a2)


if __name__ == "__main__":
    pass