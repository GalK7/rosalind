with open("samples/hamm.txt") as f:
    s = f.readline().strip()
    t = f.readline().strip()

mismatch_count = 0

for i in range(len(s)):
    if s[i] != t[i]:
        mismatch_count += 1

print(mismatch_count)