import b_dna_clenser
import c_dna_nucleotide_frequency
import d_dna_molecular_mass
import e_dna_complement
import f_dna_to_rna_translator
import a_rna_complement

def master_process():
    while True:
        nucleotide_sequence = input("Please input a DNA sequence: ")
        # cleanse user input
        try:
            cleansed_resuts = b_dna_clenser.b_dna_sequence_clensor(nucleotide_sequence)
            cleansed_nucleotide_sequence = cleansed_resuts[0]
            removed_characters_from_nucleotide_sequence = cleansed_resuts[1]
            # print the errors in the sequence
            if len(removed_characters_from_nucleotide_sequence) >= 1:
                print(f'The following characters were remove from your input sequence: {removed_characters_from_nucleotide_sequence}')
            break
        except:
            print("There was an error cleansing your nucleotide sequence please try again.")
        
    # analyse the frequency of nucleotides
    try:
        nucleotide_frequency = c_dna_nucleotide_frequency.c_dna_nucleotide_frequency(cleansed_nucleotide_sequence)
        if "Error" in nucleotide_frequency:
            print("\nThere was an error calculating the nucleotide frequencies")
        else:
            print(f'\nThese are the nucleotide frequencies from your input: {nucleotide_frequency}')
    except:
        print("\nThere was an error calculating the nucleotide frequencies")
    
    # calculate the molecular weight of the DNA strand
    try:
        dna_mass = d_dna_molecular_mass.d_dna_molecular_mass(cleansed_nucleotide_sequence)
        if dna_mass == 0:
            print("\nThere was an error calculating the molecular mass of the DNA sequence")
        else:
            print(f'\nThe molecular mass of the DNA strand is: {round(dna_mass,1)}')
    except:
        print("\nThere was an error calculating the molecular mass of the DNA sequence")

    # calculate the complimentary DNA strand
    try:
        dna_complement_strand = e_dna_complement.e_dna_complement(cleansed_nucleotide_sequence)
        if dna_complement_strand == "Error":
            print("\nThere was an error creating the complimentary DNA sequence")
        else:
            print(f'\nThe complimentary DNA sequence is: {dna_complement_strand}')
    except:
        print("\nThere was an error creating the complimentary DNA sequence")

    # calculate the RNA strand
    try:
        rna_strand = f_dna_to_rna_translator.f_dna_to_rna_translator(cleansed_nucleotide_sequence)
        if rna_strand == "Error":
            print("\nThere was an error creating the RNA sequence")
        else:
            print(f'\nThe RNA sequence is: {rna_strand}')
    except:
        print("\nThere was an error creating the RNA sequence")

    # calculate the complimentary RNA strand
    try:
        rna_complement_strand = a_rna_complement.a_rna_complement(rna_strand)
        if rna_complement_strand == "Error":
            print("\nThere was an error creating the complementary RNA sequence")
        else:
            print(f'\nThe complementary RNA sequence is: {rna_complement_strand}')
    except:
        print("\nThere was an error creating the complementary RNA sequence")


x = master_process()