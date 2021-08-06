def proteins(strand):
    base = {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine', 'UUA': 'Leucine',
            'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine', 'UCG': 'Serine',
            'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UGC': 'Cysteine', 'UGU': 'Cysteine',
            'UGG': 'Tryptophan', 'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'}
    strand = [strand[i:i+3] for i in range(0, len(strand), 3)]
    result = []
    print(strand)
    for drop in strand:
        for codon, protein in base.items():
            if protein == 'STOP':
                break
            if drop == codon and protein not in result:
                result.append(protein)
    return result