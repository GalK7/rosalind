seqs={}

with open("samples/gc.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            current = line[1:]
            seqs[current] = ""
        else:
            seqs[current] += line

best_name = ""
best_gc = 0

for name, seq in seqs.items():
    seq_gc = round((seq.count("G") + seq.count("C")) * 100/ len(seq), 6)
    if seq_gc > best_gc:
        best_gc = seq_gc
        best_name = name

print(best_name)
print(best_gc)