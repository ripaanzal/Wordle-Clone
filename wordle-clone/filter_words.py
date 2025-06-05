# save this as filter_words.py
with open("words_alpha.txt") as infile:
    words = [word.strip() for word in infile if len(word.strip()) == 5 and word.strip().isalpha()]

with open("words.txt", "w") as outfile:
    outfile.write("\n".join(words))

print(f"Saved {len(words)} 5-letter words.")
