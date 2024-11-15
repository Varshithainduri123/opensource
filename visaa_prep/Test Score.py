p, q, r = map(int, input().split())
if r % q == 0 and r <= p * q:
    print("YES")
else:
    print("NO")
