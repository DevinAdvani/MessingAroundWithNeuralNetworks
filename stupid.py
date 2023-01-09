from itertools import chain, combinations
def f(k,n):
    if k%2 == 0:
        c = 0
    else:
        c = (2)**(n/k)
    return 1/k * (2**n + (k-1)*c)


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def g(k,n):
    nums = set([])
    for i in range(1,n+1):
        nums.add(i)
    numbers = list(powerset(nums))
    count = 0
    for i in numbers:
        if sum(i)%k==0:
            count += 1
    return count

print(f(2,2),g(2,2))