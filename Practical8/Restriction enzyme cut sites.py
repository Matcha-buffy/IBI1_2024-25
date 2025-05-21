DNA_sequence = input("DNA_sequence: ")
restriction_enzyme = input("restriction_enzyme: ")
def cut(DNA_sequence, restriction_enzyme):
    if not set(DNA_sequence).issubset("ACGT") or not set(restriction_enzyme).issubset("ACGT"):
        return "Only 'ACGT' are allowed."
    sites = []
    length = len(restriction_enzyme)
    for i in range(len(DNA_sequence) - len(restriction_enzyme) + 1):
        if DNA_sequence[i:i + length] == restriction_enzyme:
            sites.append(i) 
    
    return sites
print(cut(DNA_sequence,restriction_enzyme))
print("example:")
print(cut("ACGTACGTACGT", "ACGT"))