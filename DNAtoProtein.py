'''This program takes a DNA sequence
will return: RNA Sequence & Protein Tanslation along with original DNA Sequence adn its length

Author: Aryan Sharma'''


from Bio.Seq import Seq

from Bio.Seq import Seq
from collections import Counter

def read_fasta(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return "".join(line.strip() for line in lines if not line.startswith(">"))

sequence = read_fasta(r"") # Enter file name / path
print(f"\n{len(sequence)}\n")

print(f"Original Sequence: {sequence}\n")


def translation(tSeq):
    DNASeq = Seq(tSeq)
    RNAseq = DNASeq.transcribe()
    protseq = RNAseq.translate()
    return RNAseq, protseq

rna, protein = translation(sequence)

print(f"RNA Sequence: {rna}")
print(f"Protein Sequence: {protein}")