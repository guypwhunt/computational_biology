def c_nucleotide_frequency(nucleotide_sequence, nucleotide_list):
    nucleotide_frequency = {}
    try:
        for nucleotide in nucleotide_list:
            nucleotide_frequency[nucleotide] = nucleotide_sequence.count(nucleotide)
        total = len(nucleotide_sequence)
        nucleotide_frequency["Total"] = total
        return(nucleotide_frequency)
    except:
        return({"Error":"Error"})

# This code is used to test the function
#from hivsequence import *
#nucleotide_sequence = hivSeq
#nucleotide_sequence = input()
#print(dna_nucleotide_frequency(nucleotide_sequence))
