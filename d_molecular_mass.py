def d_molecular_mass(nucleotide_sequence, molecular_mass_dict):
    molecular_mass = 0.0
    try:
        for nucleotide in nucleotide_sequence:
            if nucleotide in molecular_mass_dict:
                molecular_mass += molecular_mass_dict[nucleotide]
        return molecular_mass
    except:
        return 0

# This is to test the function
# print(d_dna_molecular_mass("AThkfdkhfgfkATATATATGC"))