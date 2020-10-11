from dna_nucleotide_data import *
def d_dna_molecular_mass(nucleotide_sequence):
    molecular_mass = 0.0
    try:
        for nucleotide in nucleotide_sequence:
            if nucleotide in dna_nucleotide_data.molecular_mass:
                molecular_mass += dna_nucleotide_data.molecular_mass[nucleotide]
        return molecular_mass
    except:
        return 0

# This is to test the function
# print(d_dna_molecular_mass("AThkfdkhfgfkATATATATGC"))