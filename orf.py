codon_table = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
    "UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

seq = ""

with open("samples/orf.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            continue
        seq += line

rna = seq.replace("T", "U")
proteins = set()
rev_seq = ""
complement = {"A":"T", "C":"G", "G":"C", "T":"A"}

for nuc in seq:
    rev_seq += complement[nuc]
rev_seq = rev_seq[::-1]
rev_rna = rev_seq.replace("T","U")

for strand in [rna, rev_rna]:
    for i in range(len(strand)):
        if strand[i:i+3] == "AUG":
            prot =""
            for j in range(i, len(strand)-2, 3):
                codon = strand[j:j+3]
                aa = codon_table[codon]
                if aa == "Stop":
                    proteins.add(prot)
                    break
                prot += aa


for p in proteins:
    print(p)

