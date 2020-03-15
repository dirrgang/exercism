def proteins(strand):
    codondict = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA":  "Leucine",
        "UUG":  "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
    }

    codonList = []
    codon = ""

    for i in range(0, len(strand)):
        codon += strand[i]

        if len(codon) % 3 == 0:
            codon = codondict.get(codon)
            if codon == "STOP":
                break
            elif codon != None:
                codonList.append(codon)
                codon = ""

    return codonList
