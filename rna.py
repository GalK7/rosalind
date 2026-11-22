with open("rosalind_rna.txt") as f:
    seq = f.read().strip()

print(seq.replace("T","U"))