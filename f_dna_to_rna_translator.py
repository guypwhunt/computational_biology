from dna_nucleotide_data import *
def f_dna_to_rna_translator(nucleotide_sequence):
    complement_rna = ""
    try:
        for nucleotide in nucleotide_sequence:
            if nucleotide in dna_nucleotide_data.nucleotide_rna_compliments.keys():
                complement_rna = complement_rna + dna_nucleotide_data.nucleotide_rna_compliments[nucleotide]
        return(complement_rna)
    except:
        return("Error")

print(f_dna_to_rna_translator("ATAGCTATCGATCTAHAHAFSAGC"))