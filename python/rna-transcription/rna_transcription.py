def to_rna(dna_strand):
    """ Given a DNA strand, return its RNA complement (per RNA transcription).
    Both DNA and RNA strands are a sequence of nucleotides.
    The four nucleotides found in DNA are adenine (A), cytosine (C), guanine (G) and thymine (T).
    The four nucleotides found in RNA are adenine (A), cytosine (C), guanine (G) and uracil (U).
    Given a DNA strand, its transcribed RNA strand is formed by replacing each nucleotide with its complement:
        G -> C
        C -> G
        T -> A
        A -> U
    """

    # The maketrans() method returns a translation table that maps each character in the intabstring 
    # into the character at the same position in the outtab string. Then this table is passed to the 
    # translate() function.
    transtab = str.maketrans("GCTA", "CGAU")

    return dna_strand.translate(transtab)
