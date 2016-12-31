def char_count(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

def letter_density_check(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        perc = 100 * (float(char_count(text, char))/text_length)
        print "Letter: {0},  Count: {1},  Percentage: {2}%".format(char,
                                                                   char_count(text, char),
                                                                   round(perc, 1))

with open(raw_input("Enter a filename: ")) as txtdoc:
    text = txtdoc.read()

text_length = float(len(text))

letter_density_check(text)
