import nucleotide_analysis
from dna_nucleotide_data import *
from rna_nucleotide_data import *

def master_process():
    # DNA Analysis
    while True:
        nucleotide_sequence = input("Please input a DNA sequence: ")
        try:
            nucleotide_list = dna_nucleotide_data.nucleotide_list
            molecular_mass_dict = dna_nucleotide_data.molecular_mass
            dna_complimentary_base_pairs = dna_nucleotide_data.nucleotide_compliments
            dna = nucleotide_analysis.nucleotide_analysis(nucleotide_sequence=nucleotide_sequence, nucleotide_list=nucleotide_list, molecular_mass_dict=molecular_mass_dict, complimentary_base_pairs=dna_complimentary_base_pairs)
            break
        except:
            print("There was an error entering your nucleotide sequence please try again.")
            break
    print("DNA Information")
    print(f'Cleansed Nucleotide Sequence: {dna.sequence_cleanser()}')
    print(f'Nucleotide Frequency: {dna.nucleotide_frequency()}')
    print(f'Nucleotide Sequence Molecular Mass: {dna.molecular_mass()}')
    print(f'Complementary Nucleotide Sequence: {dna.complement()}')

    # Complementary DNA Analysis
    while True:
        try:
            nucleotide_list = dna_nucleotide_data.nucleotide_list
            molecular_mass_dict = dna_nucleotide_data.molecular_mass
            dna_complimentary_base_pairs = dna_nucleotide_data.nucleotide_compliments
            complimentary_dna = nucleotide_analysis.nucleotide_analysis(nucleotide_sequence=dna.complement(), nucleotide_list=nucleotide_list, molecular_mass_dict=molecular_mass_dict, complimentary_base_pairs=dna_complimentary_base_pairs)
            break
        except:
            print("There was an error entering your nucleotide sequence please try again.")
            break
    print("\n Complementary DNA Information")
    print(f'Cleansed Nucleotide Sequence: {complimentary_dna.sequence_cleanser()}')
    print(f'Nucleotide Frequency: {complimentary_dna.nucleotide_frequency()}')
    print(f'Nucleotide Sequence Molecular Mass: {complimentary_dna.molecular_mass()}')
    print(f'Complementary Nucleotide Sequence: {complimentary_dna.complement()}')

    # DNA to RNA Conversion
    while True:
        try:
            nucleotide_list = dna_nucleotide_data.nucleotide_list
            molecular_mass_dict = dna_nucleotide_data.molecular_mass
            dna_to_rna_base_pairs = dna_nucleotide_data.nucleotide_rna_compliments
            rna_conversion = nucleotide_analysis.nucleotide_analysis(nucleotide_sequence=nucleotide_sequence, nucleotide_list=nucleotide_list, molecular_mass_dict=molecular_mass_dict, complimentary_base_pairs=dna_to_rna_base_pairs)
            break
        except:
            print("There was an error entering your nucleotide sequence please try again.")
            break
    print("\nRNA Information")
    print(f'Cleansed DNA Nucleotide Sequence: {rna_conversion.sequence_cleanser()}')
    print(f'Complementary RNA Nucleotide Sequence: {rna_conversion.complement()}')

    

    # RNA Analysis
    while True:
        try:
            nucleotide_list = rna_nucleotide_data.nucleotide_list
            molecular_mass_dict = rna_nucleotide_data.molecular_mass
            rna_complimentary_base_pairs = rna_nucleotide_data.nucleotide_compliments
            rna = nucleotide_analysis.nucleotide_analysis(nucleotide_sequence=rna_conversion.complement(), nucleotide_list=nucleotide_list, molecular_mass_dict=molecular_mass_dict, complimentary_base_pairs=rna_complimentary_base_pairs)
            break
        except:
            print("There was an error entering your nucleotide sequence please try again.")
            break
    print("\n RNA Analysis")
    print(f'Cleansed Nucleotide Sequence: {rna.sequence_cleanser()}')
    print(f'Nucleotide Frequency: {rna.nucleotide_frequency()}')
    print(f'Nucleotide Sequence Molecular Mass: {rna.molecular_mass()}')
    print(f'Complementary Nucleotide Sequence: {rna.complement()}')

    # Complementary RNA Analysis
    while True:
        try:
            nucleotide_list = rna_nucleotide_data.nucleotide_list
            molecular_mass_dict = rna_nucleotide_data.molecular_mass
            rna_complimentary_base_pairs = rna_nucleotide_data.nucleotide_compliments
            rna = nucleotide_analysis.nucleotide_analysis(nucleotide_sequence=rna.complement(), nucleotide_list=nucleotide_list, molecular_mass_dict=molecular_mass_dict, complimentary_base_pairs=rna_complimentary_base_pairs)
            break
        except:
            print("There was an error entering your nucleotide sequence please try again.")
            break
    print("\n Complementary RNA Analysis")
    print(f'Cleansed Nucleotide Sequence: {rna.sequence_cleanser()}')
    print(f'Nucleotide Frequency: {rna.nucleotide_frequency()}')
    print(f'Nucleotide Sequence Molecular Mass: {rna.molecular_mass()}')
    print(f'Complementary Nucleotide Sequence: {rna.complement()}')

x = master_process()

"""         cleansed_nucleotide_sequence = cleansed_resuts[0]
            removed_characters_from_nucleotide_sequence = cleansed_resuts[1]
            if len(removed_characters_from_nucleotide_sequence) >= 1:
                print(f'The following characters were remove from your input sequence: {removed_characters_from_nucleotide_sequence}')
            break
        except:
            print("There was an error cleansing your nucleotide sequence please try again.")
        
    # analyse the frequency of DNA nucleotides
    try:
        nucleotide_list = dna_nucleotide_data.nucleotide_list
        nucleotide_frequency = nucleotide_analysis.c_nucleotide_frequency(nucleotide_sequence = cleansed_nucleotide_sequence, nucleotide_list=nucleotide_list)
        if "Error" in nucleotide_frequency:
            print("\nThere was an error calculating the DNA nucleotide frequencies")
        else:
            print(f'\nThe DNA nucleotide frequencies are: {nucleotide_frequency}')
    except:
        print("\nThere was an error calculating the nucleotide frequencies")
    
    # calculate the molecular weight of the DNA strand
    try:
        molecular_mass_dict = dna_nucleotide_data.molecular_mass
        dna_mass = nucleotide_analysis.d_molecular_mass(nucleotide_sequence = cleansed_nucleotide_sequence, molecular_mass_dict = molecular_mass_dict)
        if dna_mass == 0:
            print("\nThere was an error calculating the molecular mass of the DNA sequence")
        else:
            print(f'\nThe molecular mass of the DNA strand is: {round(dna_mass,1)}')
    except:
        print("\nThere was an error calculating the molecular mass of the DNA sequence")

    # calculate the complimentary DNA strand
    try:
        dna_complimentary_base_pairs = dna_nucleotide_data.nucleotide_compliments
        dna_complement_strand = nucleotide_analysis.e_complement(nucleotide_sequence = cleansed_nucleotide_sequence, complimentary_base_pairs = dna_complimentary_base_pairs)
        if dna_complement_strand == "Error":
            print("\nThere was an error creating the complimentary DNA sequence")
        else:
            print(f'\nThe complimentary DNA sequence is: {dna_complement_strand}')
    except:
        print("\nThere was an error creating the complimentary DNA sequence")

    # calculate the molecular weight of the complimentary DNA strand
    try:
        molecular_mass_dict = dna_nucleotide_data.molecular_mass
        complimentary_dna_mass = nucleotide_analysis.d_molecular_mass(nucleotide_sequence = cleansed_nucleotide_sequence, molecular_mass_dict = molecular_mass_dict)
        if dna_mass == 0:
            print("\nThere was an error calculating the molecular mass of the complimentary DNA sequence")
        else:
            print(f'\nThe molecular mass of the complimentary DNA strand is: {round(complimentary_dna_mass,1)}')
    except:
        print("\nThere was an error calculating the molecular mass of the complimentary DNA sequence")

    # calculate the RNA strand
    try:
        dna_to_rna_base_pairs = dna_nucleotide_data.nucleotide_rna_compliments
        rna_strand = nucleotide_analysis.e_complement(nucleotide_sequence = cleansed_nucleotide_sequence, complimentary_base_pairs = dna_to_rna_base_pairs)
        if rna_strand == "Error":
            print("\nThere was an error creating the RNA sequence")
        else:
            print(f'\nThe  RNA sequence is: {rna_strand}')
    except:
        print("\nThere was an error creating the RNA sequence")
    
    # calculate the molecular weight of the RNA strand
    try:
        molecular_mass_dict = rna_nucleotide_data.molecular_mass
        rna_mass = nucleotide_analysis.d_molecular_mass(nucleotide_sequence = rna_strand, molecular_mass_dict = molecular_mass_dict)
        if dna_mass == 0:
            print("\nThere was an error calculating the molecular mass of the RNA sequence")
        else:
            print(f'\nThe molecular mass of the RNA strand is: {round(rna_mass,1)}')
    except:
        print("\nThere was an error calculating the molecular mass of the RNA sequence")

    # calculate the complimentary RNA strand
    try:
        rna_base_pairs = rna_nucleotide_data.nucleotide_compliments
        complimentary_rna_strand = nucleotide_analysis.e_complement(nucleotide_sequence = rna_strand, complimentary_base_pairs = rna_base_pairs)
        if rna_strand == "Error":
            print("\nThere was an error creating the complementary RNA sequence")
        else:
            print(f'\nThe complementary RNA sequence is: {complimentary_rna_strand}')
    except:
        print("\nThere was an error creating the complementary RNA sequence")

    # calculate the molecular weight of the complimentary RNA strand
    try:
        molecular_mass_dict = rna_nucleotide_data.molecular_mass
        complimentary_rna_mass = nucleotide_analysis.d_molecular_mass(nucleotide_sequence = complimentary_rna_strand, molecular_mass_dict = molecular_mass_dict)
        if dna_mass == 0:
            print("\nThere was an error calculating the molecular mass of the complimentary RNA sequence")
        else:
            print(f'\nThe molecular mass of the RNA strand is: {round(complimentary_rna_mass,1)}')
    except:
        print("\nThere was an error calculating the molecular mass of the complimentary RNA sequence")

    # To add, RNA to amino acid converter, DNA transcription start stop identifier, RNA translation start stop identifier 

x = master_process()"""