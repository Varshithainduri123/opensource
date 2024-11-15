p, q, r, m = map(int,input().split())
if p + q >= m or p + r >= m or q + r >= m:
    print("YES")
else:
    print("NO")
