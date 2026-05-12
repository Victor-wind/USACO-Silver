# pass tests 3-5 within 3000+ MS, tests 6-20 take over 20 sec for 25M loops
# Line 50 and after provide better math solution, all tests pass within 600 MS

import sys
import time

start = time.time()

N, M = map(int, sys.stdin.readline().split())

a = [0]*(M+1)
b = [0]*(M+1)

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    a[x] += 1
    b[y] += 1

a_lst = [0]*(2*M+1)
b_lst = [0]*(2*M+1)

a_vals = [i for i in range(M+1) if a[i]]
b_vals = [i for i in range(M+1) if b[i]]

for i in a_vals:
    ai = a[i]
    for j in a_vals:
        a_lst[i+j] += ai * a[j]

for i in b_vals:
    bi = b[i]
    for j in b_vals:
        b_lst[i+j] += bi * b[j]

res = []
pre = 0
for k in range(2*M+1):
    pre += a_lst[k]
    res.append(pre)
    pre -= b_lst[k]

end = time.time()

#print(f'Before the output {end-start}')

print("\n".join(map(str, res)))


'''
# ALL tests pass within 600 MS

import sys
import math

input = sys.stdin.readline

# ---------------- FFT ---------------- #

def fft(a, invert):
    n = len(a)

    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    length = 2
    while length <= n:
        ang = 2 * math.pi / length * (-1 if invert else 1)
        wlen = complex(math.cos(ang), math.sin(ang))

        for i in range(0, n, length):
            w = 1 + 0j
            half = length // 2
            for j in range(half):
                u = a[i + j]
                v = a[i + j + half] * w
                a[i + j] = u + v
                a[i + j + half] = u - v
                w *= wlen

        length <<= 1

    if invert:
        for i in range(n):
            a[i] /= n


def convolution(a, b):
    n = 1
    while n < len(a) + len(b):
        n <<= 1

    fa = list(map(complex, a)) + [0] * (n - len(a))
    fb = list(map(complex, b)) + [0] * (n - len(b))

    fft(fa, False)
    fft(fb, False)

    for i in range(n):
        fa[i] *= fb[i]

    fft(fa, True)

    res = [0] * n
    for i in range(n):
        res[i] = int(round(fa[i].real))

    return res

# ---------------- Input ---------------- #

N, M = map(int, input().split())

a = [0] * (M + 1)
b = [0] * (M + 1)

for _ in range(N):
    x, y = map(int, input().split())
    a[x] += 1
    b[y] += 1

# ---------------- Convolution ---------------- #

A = convolution(a, a)
B = convolution(b, b)

# ---------------- Prefix sums ---------------- #

ansA = [0] * (2 * M + 1)
ansB = [0] * (2 * M + 1)

cur = 0
for i in range(2 * M + 1):
    cur += A[i]
    ansA[i] = cur

cur = 0
for i in range(2 * M + 1):
    cur += B[i]
    ansB[i] = cur

# ---------------- Output ---------------- #

out = []
for k in range(2 * M + 1):
    if k == 0:
        out.append(str(ansA[0]))
    else:
        out.append(str(ansA[k] - ansB[k - 1]))

print("\n".join(out))

'''
