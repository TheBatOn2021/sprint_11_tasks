n, k = input().split()
n = int(n)
k = 10 ** int(k)
fibPrev = 0
fib = 1
cached = [fibPrev, fib]

for curr in range(n):
    fibOld = fib
    fib = (fib + fibPrev) % k
    fibPrev = fibOld

    if fibPrev == 0 and fib == 1:
        cached.pop()
        break
    else:
        cached.append(fib)

offset = (n+1) % len(cached)
print(cached[offset])
