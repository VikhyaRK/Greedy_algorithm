#!/usr/bin/env python
# coding: utf-8

# In[1]:


def merge_strings(dna_strings):
    while len(dna_strings) > 1:
        max_overlap = -1
        merge_idx1 = -1
        merge_idx2 = -1

        for i in range(len(dna_strings)):
            for j in range(len(dna_strings)):
                if i != j:
                    overlap = 0
                    len1 = len(dna_strings[i])
                    len2 = len(dna_strings[j])

                    for k in range(1, min(len1, len2) + 1):
                        if dna_strings[i][len1 - k:] == dna_strings[j][:k]:
                            overlap = k

                    if overlap > max_overlap:
                        max_overlap = overlap
                        merge_idx1 = i
                        merge_idx2 = j

        if merge_idx1 != -1 and merge_idx2 != -1:
            merged = dna_strings[merge_idx1] + dna_strings[merge_idx2][max_overlap:]
            dna_strings[merge_idx1] = merged
            dna_strings.pop(merge_idx2)

    return dna_strings[0]


def main():
    with open("sequences.txt", "r") as file:
        dna_strings = [line.strip() for line in file]

    result = merge_strings(dna_strings)
    print("DNA sequence:", result)

if __name__ == "__main__":
    main()


# In[ ]:




