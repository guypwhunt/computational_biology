# The standard genetic code
class genetic_code:
    gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
    
def translate(gencode):
    while True:
        try:
            user_input = input("Please input a DNA sequence to be converted into an amino acid sequence: ")
            n = 3
            protein = []
            protein_string = ""
            errors = []
            user_input = user_input.upper()
            user_input = user_input.replace(" ","")
            user_input = user_input.replace("_","")
            user_input_len = len(user_input)
            triplets = [user_input[i:i+n] for i in range(0, user_input_len, n)]
            for tip in triplets:
                if (tip in gencode) == True:
                    protein.append(gencode[tip])
                else:
                    errors.append(tip)
            protein_string = protein_string.join(protein)
            return(protein_string, errors)
        except:
            print("Appologies there was an error, please re-enter you sequence.")

results = translate(genetic_code.gencode)
protein = results[0]
errors = results[1]

print("\nThe amino acid sequence sequence is:\n" + protein)
print(f'\nThe following sequences caused an error and were ignored {errors}')