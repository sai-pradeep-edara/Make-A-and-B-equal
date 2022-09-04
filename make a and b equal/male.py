# cook your dish here
for _ in range(int(input())):
    n = int(input())
    k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    t = d = 0
    for i in range(n):
        d += k[i] - l[i]
        t += abs(k[i] - l[i])
    if d == 0:
        print(t//2)
    else: 
        print(-1)
