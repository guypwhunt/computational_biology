class file_class:
    file_name = input("Please provide FASTA file name: ")
    file_extension = ".fas"
    operation = "r"


def open_fasta(file_name, file_extension, operation):
    if file_name.find(file_extension) == -1:
        file_name = file_name + file_extension
    fasta = open(file_name, operation)
    header = fasta.readline()
    (code, name) = header.split('|') 
    protein = ""
    while True:
        oneLine = fasta.readline()
        if oneLine == "": 
            break
        protein += oneLine.rstrip()
    fasta.close()
    results = {}
    results["protein"] = protein
    results["code"] = code
    results["name"] = name
    return(results)

def calculate_charge(protein):
    charge = -0.002
    aacharge={"C":-0.045, "D": -0.999, "E": -0.998, "H": 0.091, "K": 1.0, "R": 1.0,"Y": -0.001}
    for amino_acid in protein:
        if (amino_acid in aacharge) == True:
            charge += aacharge[amino_acid]
    return(charge)

results = open_fasta(file_class.file_name, file_class.file_extension, file_class.operation)
charge = calculate_charge(results)
        
print(f'Code: {results["code"]}\n\nName: {results["name"]}\n\nProtein Charge: {charge}' )