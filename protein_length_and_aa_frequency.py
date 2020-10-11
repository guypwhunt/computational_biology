class file_details:
    file_name = "CHICK"
    file_extension = ".fasta"
    operation = "r"

class amino_acids:
    list_of_amino_acids = {"Alanine":"A","Arginine":"R","Asparagine":"N","Aspartic Acid":"D","Cysteine":"C","Glutamic Acid":"E","Glutamine":"Q","Glycine":"G","Histidine":"H","Isoleucine":"I","Leucine":"L","Lysine":"K","Methionine":"M","Phenylalanine":"F","Proline":"P","Serine":"S","Threonine":"T","Tryptophan":"W","Tyrosine":"Y","Valine":"V"}

def open_fasta(file_name, file_extension, operation):
    if file_name.find(file_extension) == -1:
        file_name = file_name + file_extension
    fasta = open(file_name, operation)
    results = {}
    results_final = {}
    protein = ""
    code = ""
    name = ""
    header_sequence = ">tr"
    count = 0
    while True:
        oneLine = fasta.readline()
        if oneLine == "": 
            break
        elif (header_sequence in oneLine) > 0:
            count += 1
            results["protein"] = protein
            results["code"] = code
            results["name"] = name
            results_final[count] = results
            (x, code, name) = oneLine.split('|')
            protein = ""
        else:
            protein += oneLine.rstrip()
    fasta.close()
    return(results_final)

results_final = open_fasta(file_details.file_name, file_details.file_extension, file_details.operation)

def calculate_length_of_protein(results_final):
    import statistics
    count = 1
    results = {}
    while count in results_final.keys():
        length = len(results_final[count]["protein"])
        results[count] = length
        count += 1
    average_length = statistics.mean(results.values())
    return(average_length)

average_length = calculate_length_of_protein(results_final)

def frequency_of_amino_acids(results_final, list_of_amino_acids):
    dict_of_frequency = {}
    for protein in results_final.values():
        for letter in protein["protein"]:
            if letter in dict_of_frequency:
                dict_of_frequency[letter] +=1
            else:
                dict_of_frequency[letter] = 1
    total = sum(dict_of_frequency.values())
    for aa in dict_of_frequency:
        dict_of_frequency[aa] = round(dict_of_frequency[aa]/total,2)
    return(dict_of_frequency)

frequency_of_amino_acids = frequency_of_amino_acids(results_final, amino_acids.list_of_amino_acids)

print(f'The average length of a chicken protein is {average_length}')
for aa in frequency_of_amino_acids:
    print(f'The frequency of {aa} in the chicken proteome is {frequency_of_amino_acids[aa]}')