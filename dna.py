with open("rosalind_dna.txt") as f:
    seq = f.read().strip()

print(seq.count("A"), seq.count("C"), seq.count("G"), seq.count("T"))

