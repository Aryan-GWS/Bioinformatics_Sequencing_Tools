'''
"Sequence Analysis"
This code takes a FASTA file ans input
It extracts its DNA sequence polishes it ad this provides its sevral attributes

Author: Aryan Sharma

'''




from Bio.Seq import Seq
from collections import Counter

def read_fasta(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return "".join(line.strip() for line in lines if not line.startswith(">"))

sequence = read_fasta(r"C:\Users\ARYAN SHARMA\OneDrive\Documents\BIOINFORMATICS PYTHON\01_Lesson\fasta.txt")

print(f"Original Sequence: {sequence}\n")



def seqProcess(rawseq):
    Rseq = Seq(rawseq)
    print(f"Length of Sequence: {len(Rseq)}\n")
    print(f"Reverse Seq: {Rseq[::-1]}\n")
    print(f"Complimentary Sequence: {Rseq.complement()}\n")
    reverseRNA = Rseq.complement_rna()
    print(f"Complimentary RNA: {reverseRNA}\n")
    print(f"RNA Sequence: {reverseRNA[::-1]}\n")

seqProcess(sequence)

count = Counter(sequence)

for base, num in count.items():
    print("BASE:COUNT")
    print(f"{base} : {num}")
