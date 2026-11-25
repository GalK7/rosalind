seqs = {}

with open("samples/lcsm.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            current = line[1:]
            seqs[current] = ""
        else:
            seqs[current] += line


shortest_seq = list(seqs.values())[0]

for seq in seqs.values():
    if len(seq) < len(shortest_seq):
            shortest_seq = seq


for length in range(len(shortest_seq), 0, -1):
    for i in range(len(shortest_seq)):
        if i+length > len(shortest_seq):
            break
        motif = shortest_seq[i:i+length]
        if all(motif in seq for seq in seqs.values()):
            print(motif)
            exit()
        