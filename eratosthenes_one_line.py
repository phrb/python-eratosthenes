n = 50
print(sorted(set(range(2,n+1)).difference(set((p * f) for p in range(2,int(n**0.5) + 2) for f in range(2,int(n/p)+1)))))
