combination = input().strip()
output_file = f"{combination}_spliced_genes.fa"
tata = "TATATAT"
tata1 = "TATAAAA"
tata2 = "TATAAAT"
tata3 = "TATATAA"
import re
with open(r"C:\Users\ASUS\Desktop\ZJE\IBI1\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", 'r') as infile, open(output_file, 'w') as outfile:
    name = ""  
    sequence = ""  

    for line in infile:
        line = line.strip()
        if line.startswith('>'): 
            if (tata in sequence) or (tata1 in sequence) or (tata2 in sequence) or (tata3 in sequence):
                if (combination in sequence):
                    outfile.write(f">{name}\n{sequence}\n")
                name = line.split()[0][1:]
                sequence = "" 
        else:
            sequence += line 
    if (tata in sequence) or (tata1 in sequence) or (tata2 in sequence) or (tata3 in sequence):
        outfile.write(f">{name}\n{sequence}\n")