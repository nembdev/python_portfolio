def hamming(dna_one, dna_two):
    """
    If we compare two strands of DNA and count the differences between them we can see how many mistakes occurred. This is known as the "Hamming Distance"
    """
    distance = 0
    for i in range(len(dna_one)):
        if dna_one[i] != dna_two[i]:
            distance += 1
    print(distance)


hamming("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
