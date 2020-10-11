import dna_nucleotide_data 

def dna_nucleotide_frequency(nucleotide_sequence):
    nuleotide_list = dna_nucleotide_data.nucleotide_list
    nucleotide_frequency = {}
    try:
        nucleotide_sequence = nucleotide_sequence.upper()
        for nucleotide in nuleotide_list:
            nucleotide_frequency[nucleotide] = nucleotide_sequence.count(nucleotide)
        total = len(nucleotide_sequence)
        total_nucleotides = sum(nucleotide_frequency.values())
        nucleotide_frequency["non-nucleotide"] = total - total_nucleotides
        return(nucleotide_frequency)
    except:
        return("Error")

from hivsequence import *

nucleotide_sequence = hivesequence.hivSeq

print(dna_nucleotide_frequency(nucleotide_sequence))
