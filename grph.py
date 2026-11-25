seqs = {}

with open("samples/grph.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            current = line[1:]
            seqs[current] = ""
        else:
            seqs[current] += line

for name_s in seqs.keys():
    for name_t in seqs.keys():
        if name_s == name_t:
            continue
        if seqs[name_s][-3:] == seqs[name_t][:3]:
            print(name_s, name_t)