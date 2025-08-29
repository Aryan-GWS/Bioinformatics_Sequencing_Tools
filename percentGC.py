from Bio.Seq import Seq
from collections import Counter

sequence = Seq("ATGGCATCATGCCGTGGAGCAATagGGCA")

# sequence = Seq("gcgcgccgcggcgccggc")
nucleotides = ["A", "T", "C", "G"]

usequence = sequence.upper()
# set(usequence)
if set(usequence).issubset(nucleotides) is False:
    print("Your sequence is incorrect, contains other than A, G, T, C")
else:
    print(f"Original Sequence: {usequence}\n")
# print(set(sequence).issubset(nucleotides)) #True/False



ntdlen = len(usequence)
print(f"Length of Sequence: {ntdlen}\n")



ntdnum = Counter(usequence)

for base, count in ntdnum.items():
    print(f"Base:Count\n{base} : {count}") 


def percentGC(countsequence):
    i=0
    j=0
    for cbase in countsequence:
        if cbase == "G":
            i+=1
        if cbase == "C":
            j+=1
    return i, j

a, b = percentGC(usequence)

c = a+b
gc = c/ntdlen
pergc = gc*100

print(f"\n% GC content: {pergc}")
