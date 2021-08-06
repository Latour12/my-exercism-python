def distance(strand_a, strand_b):
    distance = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands's lenth must be the same.")
    return sum(1 for char_a, char_b in zip(strand_a, strand_b) if char_a != char_b)