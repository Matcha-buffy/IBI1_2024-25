seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
maxlength = 0
for i in range(len(seq) - 1):
    if seq[i:i+2] == 'GT':
        for j in range(i + 2, len(seq) - 1):
            if seq[j:j+2] == 'AG':
                length = j - i - 1
                if length > maxlength:
                    maxlength = length
print("Length of the largest intron:", maxlength)