import timeit
import pandas as pd
vowel = ['a', 'ı', 'o', 'u', 'e', 'i', 'ö', 'ü']
consonant = ['b', 'c', 'ç', 'd', 'f', 'g', 'ğ', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z']
spells = []


def word_printer():
    for hece in spells:
        print(hece+" - ", end="")
    print()


def spell(binary_word, size):
    mid = int(size / 2)
    if size == 1 or size == 2:
        spells.append(binary_word)
    else:
        if binary_word[mid] in consonant:
            if binary_word[mid-1] in vowel and binary_word[mid+1] in vowel:
                left = binary_word[:mid]
                right = binary_word[mid:]
                spell(left, len(left))
                spell(right, len(right))
            elif binary_word[mid-1] in consonant and binary_word[mid+1] in vowel:
                if size <= 3:
                    spells.append(binary_word)
                else:
                    left = binary_word[:mid]
                    right = binary_word[mid:]
                    spell(left, len(left))
                    spell(right, len(right))
            elif binary_word[mid - 1] in vowel and binary_word[mid + 1] in consonant:
                if size <= 4:
                    spells.append(binary_word)
                else:
                    left = binary_word[:mid+1]
                    right = binary_word[mid+1:]
                    spell(left, len(left))
                    spell(right, len(right))
            elif binary_word[mid - 1] in consonant and binary_word[mid + 1] in consonant:
                left = binary_word[:mid+1]
                right = binary_word[mid+1:]
                spell(left, len(left))
                spell(right, len(right))
        elif binary_word[mid] in vowel:
            if binary_word[mid - 1] in consonant and binary_word[mid + 1] in consonant:
                if size <= 4:
                    spells.append(binary_word)
                else:
                    left = binary_word[:mid-1]
                    right = binary_word[mid-1:]
                    spell(left, len(left))
                    spell(right, len(right))
            elif binary_word[mid - 1] in vowel and binary_word[mid + 1] in consonant:
                left = binary_word[:mid]
                right = binary_word[mid:]
                spell(left, len(left))
                spell(right, len(right))


def list_flush():
    spells.clear()


def main():
    df = pd.read_csv("TDK_Words.csv", encoding="ISO-8859–9")
    liste = df["Kelimeler"].tolist()
    # print(liste)
    for kelime in liste:
        kelime = kelime.lower()
        spell(kelime, len(kelime))
        # word_printer()
        list_flush()


start = timeit.default_timer()
main()
stop = timeit.default_timer()
print((stop - start))
