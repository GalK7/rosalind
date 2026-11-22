with open("samples/rna.txt") as f:
    seq = f.read().strip()

print(seq.replace("T","U"))