class nucleotide_analysis():
    def __init__(self, nucleotide_sequence, nucleotide_list, molecular_mass_dict, complimentary_base_pairs):
        self.nucleotide_sequence = nucleotide_sequence
        self.nucleotide_list = nucleotide_list
        self.molecular_mass_dict = molecular_mass_dict
        self.complimentary_base_pairs = complimentary_base_pairs
    def sequence_cleanser(self):
        """This function cleanses 
        nucleotide sequences of 
        non-nucleotide characters
        """
        none_nucleotide_characters_removed = []
        dict_results = {}
        nucleotide_sequence = self.nucleotide_sequence
        nucleotide_list = self.nucleotide_list
        try:
            nucleotide_sequence = nucleotide_sequence.upper()
            for character in nucleotide_sequence:
                if character not in nucleotide_list:
                    nucleotide_sequence = nucleotide_sequence.replace(character,"")
                    none_nucleotide_characters_removed.append(character)
            dict_results["cleansed_nucleotide_sequence"] = nucleotide_sequence
            dict_results["none_nucleotide_characters_removed"] = none_nucleotide_characters_removed
            self.nucleotide_sequence = nucleotide_sequence
            return(dict_results)
        except:
            return("There was an error clensing the sequence, please retry.")
    def nucleotide_frequency(self):
        """This function calculates 
        the frequency of each 
        nucleotide within a sequence
        """
        nucleotide_frequency = {}
        nucleotide_sequence = self.nucleotide_sequence
        nucleotide_list = self.nucleotide_list
        try:
            for nucleotide in nucleotide_list:
                nucleotide_frequency[nucleotide] = nucleotide_sequence.count(nucleotide)
            total = len(nucleotide_sequence)
            nucleotide_frequency["Total"] = total
            return(nucleotide_frequency)
        except:
            return({"Error":"Error"})
    def molecular_mass(self):
        """This function calculates 
        the molecular mass of a  
        sequence of nucleotides
        """
        nucleotide_sequence = self.nucleotide_sequence
        molecular_mass_dict = self.molecular_mass_dict
        molecular_mass = 0.0
        try:
            for nucleotide in nucleotide_sequence:
                if nucleotide in molecular_mass_dict:
                    molecular_mass += molecular_mass_dict[nucleotide]
            return molecular_mass
        except:
            return 0
    def complement(self):
        """This function calculates 
        the complementary strand of a  
        sequence of nucleotides
        """
        nucleotide_sequence = self.nucleotide_sequence
        complimentary_base_pairs = self.complimentary_base_pairs
        complement_dna = ""
        try:
            for nucleotide in nucleotide_sequence:
                if nucleotide in complimentary_base_pairs.keys():
                    complement_dna = complement_dna + complimentary_base_pairs[nucleotide]
            return(complement_dna)
        except:
            return("Error")