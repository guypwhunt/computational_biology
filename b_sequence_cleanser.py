def b_sequence_cleanser(nucleotide_sequence, nucleotide_list):
    none_nucleotide_characters_removed = []
    try:
        nucleotide_sequence = nucleotide_sequence.upper()
        for character in nucleotide_sequence:
            if character not in nucleotide_list:
                nucleotide_sequence = nucleotide_sequence.replace(character,"")
                none_nucleotide_characters_removed.append(character)
        return(nucleotide_sequence, none_nucleotide_characters_removed)
    except:
        return("There was an error clensing the sequence, please retry.")

# This code is used to test the function
#from hivsequence import *
#nucleotide_sequence = hivSeq
#nucleotide_sequence = input()
#print(dna_sequence_clensor(nucleotide_sequence))
