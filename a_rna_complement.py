from rna_nucleotide_data import *
def a_rna_complement(nucleotide_sequence):
    complement_rna = ""
    try:
        for nucleotide in nucleotide_sequence:
            if nucleotide in rna_nucleotide_data.nucleotide_compliments.keys():
                complement_rna = complement_rna + rna_nucleotide_data.nucleotide_compliments[nucleotide]
        return(complement_rna)
    except:
        return("Error")

#print(d_dna_molecular_mass("ATAGCTATCGATCTAHAHAFSAGC"))