
# ALPHABETS PATTERN
# A
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        if (i == 1 and 1<j<n) or (j == 1 and i != 1) or (j == n and i != 1) or i == n//2 + 1 :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# B
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        # if (i == 1 and 1<j<n) or (j == 1 and 1<=i<=n) or (j == n and 1<i<n ) or (i == n//2 + 1 and 1<j<n) or (i ==n and 1<=j<n) :
        if (i == 1 and 1<j<n) or (j == 1 and 1<=i<=n) or (j == n and ((1 <i < n//2 + 1) or (n>i > n//2 + 1) )) or (i == n//2 + 1 and 1<j<n) or (i ==n and 1<=j<n) :

            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# C
n = 6
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<i<n) or (i == 1 and 1<j<=n) or (i == n and 1<j<=n)  :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# D
n = 6
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<i<n) or (i == 1 and 1<=j<n) or (i == n and 1<=j<n) or (j == n and 1<i<n)  :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# E
n = 7
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<i<n) or (i == 1 and 1<=j<=n) or (i == n and 1<=j<=n) or i ==n//2 + 1 :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# F
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<i<=n) or (i == 1 and 1<=j<=n) or i ==n//2 + 1 :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# G
n = 7
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<i<n) or (i == 1 and 1<=j<=n) or (i == n and 1<=j<=n//2 +1) or (i ==n//2 + 1 and j > n//2) or (i > n//2 and j == n) or (i > n//2 and j ==n//2 + 1):
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# H
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<=i<=n ) or (j == n and i != 0) or i == n//2 + 1 :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# I
n = 7
for i in range(1,n+1):
    for j in range(1,n +1):
        if  (i == 1 and 1<=j<=n) or (i == n and 1<=j<=n) or j ==n//2 + 1 :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# J
n = 7
for i in range(1,n+1):
    for j in range(1,n +1):
        if  (i == 1 and 1<=j<=n) or (i == n and j <= n//2) or j ==n//2 + 1 :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# K
n = 9
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<=i<=n) or (i+j == n + 1 and i <n//2 + 1) or (i == n//2 + 1 and j < n//2 + 1) or (i == j and i > n// 2) :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# L
n = 7
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<=i<=n)  or (i == n and 1<=j<=n) :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# M
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<=i<=n ) or (j == n and i != 0) or (i == j and j < n//2+1) or (i <= n//2+1 and i+j == n + 1) :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# N
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<=i<=n ) or (j == n and i != 0) or (i == j and j <= n) :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# O
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<i<n ) or (j == n and 1<i<n) or (i == 1 and 1<j<n) or (i == 5 and 1<j<n) :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# P
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<i<=n) or (i == 1 and 1<=j<=n) or ( j == n and i < n//2+1) or i ==n//2 + 1 :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# Q
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<i<n ) or (j == n and 1<i<n) or (i == 1 and 1<j<n) or (i == 5 and 1<j<n) or(i == j and j >= n//2+1) :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# R
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<i<=n) or (i == 1 and 1<=j<=n) or ( j == n and i < n//2+1) or(i == j and j >= n//2+1) or i ==n//2 + 1 :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# S
n = 7
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and i <= n//2+1) or (i == 1 and 1<=j<=n) or (i == n and 1<=j<=n) or (j == n and i >= n//2+1) or i ==n//2 + 1 :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# T
n = 7
for i in range(1,n+1):
    for j in range(1,n +1):
        if  (i == 1 and 1<=j<=n)  or j ==n//2 + 1 :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# U
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<i<n ) or (j == n and 1<i<n) or (i == 5 and 1<j<n) :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# V
n = 9
for i in range(1,n+1):
    for j in range(1,n +1):
        if  (i == j and j <= n//2+1) or (i <= n//2+1 and i+j == n + 1) :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# W
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        if (j == 1 and 1<=i<=n ) or (j == n and i != 0) or (i == j and j > n//2+1) or (i >= n//2+1 and i+j == n + 1) :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# X
n = 5
for i in range(1,n+1):
    for j in range(1,n +1):
        if (i == j) or (i+j == n + 1) :
            print('*',end = ' ')

        else:
            print(' ',end = ' ')
    print()

# Y
n = 11
for i in range(1,n+1):
    for j in range(1,n +1):
        if (i == j and j <= n//2+1) or (i+j == n + 1) :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()

# Z
n = 7
for i in range(1,n+1):
    for j in range(1,n +1):
        if  (i == 1 and 1<=j<=n) or (i == n and 1<=j<=n) or i+j == n+1 :
            print('*',end = ' ')
        else:
            print(' ',end = ' ')
    print()