def find_anagrams(word, candidates):
    return [rec for rec in candidates if len(rec) == len(word) and word.upper(
    ) != rec.upper() and sorted(word.upper()) == sorted(rec.upper())]
