from dna_nucleotide_data import *
def e_dna_complement(nucleotide_sequence):
    complement_dna = ""
    try:
        for nucleotide in nucleotide_sequence:
            if nucleotide in dna_nucleotide_data.nucleotide_compliments.keys():
                complement_dna = complement_dna + dna_nucleotide_data.nucleotide_compliments[nucleotide]
        return(complement_dna)
    except:
        return("Error")

#print(d_dna_molecular_mass("ATAGCTATCGATCTAHAHAFSAGC"))