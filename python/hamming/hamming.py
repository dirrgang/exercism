def distance(strand_a: str, strand_b: str) -> int:

    if len(strand_a) != len(strand_b):
        # The Hamming distance is only defined for sequences of equal length,
        # so an attempt to calculate it between sequences of different 
        # lengths should not work. 
        raise ValueError("Strands must be of same length")

    elif strand_a.islower() != strand_b.islower():
        raise ValueError("Strands must be in same case")

    # If we compare two strands of DNA and count the differences between them
    # we can see how many mistakes occurred. This is known as the 
    # "Hamming Distance".
    return sum([a != b for (a, b) in zip(strand_a, strand_b)])
