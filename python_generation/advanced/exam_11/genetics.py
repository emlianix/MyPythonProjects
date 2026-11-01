complement = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

dna = input()
rna = ''.join(complement[n] for n in dna)
print(rna)