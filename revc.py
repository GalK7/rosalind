with open("rosalind_revc.txt") as f:
    seq = f.read().strip()

rev_seq = ""
complement = {"A":"T", "C":"G", "G":"C", "T":"A"}

for nuc in seq:
    rev_seq += complement[nuc]

print(rev_seq[::-1])