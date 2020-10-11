def e_complement(nucleotide_sequence, complimentary_base_pairs):
    complement_dna = ""
    try:
        for nucleotide in nucleotide_sequence:
            if nucleotide in complimentary_base_pairs.keys():
                complement_dna = complement_dna + complimentary_base_pairs[nucleotide]
        return(complement_dna)
    except:
        return("Error")

#print(d_dna_molecular_mass("ATAGCTATCGATCTAHAHAFSAGC"))