with open("samples/subs.txt") as f:
    seq = f.readline().strip()
    motif = f.readline().strip()


for i in range(0, len(seq)):
    if motif == seq[i:i+len(motif)]:
        print(i+1, end=" ")

