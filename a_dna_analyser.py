import b_sequence_cleanser
import c_nucleotide_frequency
import d_molecular_mass
import e_complement
from dna_nucleotide_data import *
from rna_nucleotide_data import *

def master_process():
    while True:
        nucleotide_sequence = input("Please input a DNA sequence: ")
        # cleanse user input
        try:
            nucleotide_list = dna_nucleotide_data.nucleotide_list
            cleansed_resuts = b_sequence_cleanser.b_sequence_cleanser(nucleotide_sequence=nucleotide_sequence, nucleotide_list=nucleotide_list)
            cleansed_nucleotide_sequence = cleansed_resuts[0]
            removed_characters_from_nucleotide_sequence = cleansed_resuts[1]
            # print the errors in the sequence
            if len(removed_characters_from_nucleotide_sequence) >= 1:
                print(f'The following characters were remove from your input sequence: {removed_characters_from_nucleotide_sequence}')
            break
        except:
            print("There was an error cleansing your nucleotide sequence please try again.")
        
    # analyse the frequency of DNA nucleotides
    try:
        nucleotide_list = dna_nucleotide_data.nucleotide_list
        nucleotide_frequency = c_nucleotide_frequency.c_nucleotide_frequency(nucleotide_sequence = cleansed_nucleotide_sequence, nucleotide_list=nucleotide_list)
        if "Error" in nucleotide_frequency:
            print("\nThere was an error calculating the DNA nucleotide frequencies")
        else:
            print(f'\nThe DNA nucleotide frequencies are: {nucleotide_frequency}')
    except:
        print("\nThere was an error calculating the nucleotide frequencies")
    
    # calculate the molecular weight of the DNA strand
    try:
        molecular_mass_dict = dna_nucleotide_data.molecular_mass
        dna_mass = d_molecular_mass.d_molecular_mass(nucleotide_sequence = cleansed_nucleotide_sequence, molecular_mass_dict = molecular_mass_dict)
        if dna_mass == 0:
            print("\nThere was an error calculating the molecular mass of the DNA sequence")
        else:
            print(f'\nThe molecular mass of the DNA strand is: {round(dna_mass,1)}')
    except:
        print("\nThere was an error calculating the molecular mass of the DNA sequence")

    # calculate the complimentary DNA strand
    try:
        dna_complimentary_base_pairs = dna_nucleotide_data.nucleotide_compliments
        dna_complement_strand = e_complement.e_complement(nucleotide_sequence = cleansed_nucleotide_sequence, complimentary_base_pairs = dna_complimentary_base_pairs)
        if dna_complement_strand == "Error":
            print("\nThere was an error creating the complimentary DNA sequence")
        else:
            print(f'\nThe complimentary DNA sequence is: {dna_complement_strand}')
    except:
        print("\nThere was an error creating the complimentary DNA sequence")

    # calculate the RNA strand
    try:
        dna_to_rna_base_pairs = dna_nucleotide_data.nucleotide_rna_compliments
        rna_strand = e_complement.e_complement(nucleotide_sequence = cleansed_nucleotide_sequence, complimentary_base_pairs = dna_to_rna_base_pairs)
        if rna_strand == "Error":
            print("\nThere was an error creating the RNA sequence")
        else:
            print(f'\nThe  RNA sequence is: {rna_strand}')
    except:
        print("\nThere was an error creating the RNA sequence")

    # calculate the complimentary RNA strand
    try:
        rna_base_pairs = rna_nucleotide_data.nucleotide_compliments
        complimentary_rna_strand = e_complement.e_complement(nucleotide_sequence = rna_strand, complimentary_base_pairs = rna_base_pairs)
        if rna_strand == "Error":
            print("\nThere was an error creating the complementary RNA sequence")
        else:
            print(f'\nThe complementary RNA sequence is: {complimentary_rna_strand}')
    except:
        print("\nThere was an error creating the complementary RNA sequence")

x = master_process()