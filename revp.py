seq = ""
with open("samples/revp.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            continue
        seq += line

complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

for i in range(len(seq)):
    for length in range(4,13):
        if i+length > len(seq):
            break
        sub = seq[i:i+length]
        revc = ""
        for nuc in sub:
            revc += complement[nuc]
        if revc == sub[::-1]:
            print(i+1, length)


