text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
    " Integer urna nisl, facilicis vitae semper at, dignissim vitae libero"
)

ing_text = []
new_text = text.split()

for word in new_text:
    if word.isalpha() is False:
        p = word[-1]
        ing_text.append(word[:-1] + "ing" + p)
    else:
        ing_text.append(word + "ing")

print(" ".join(ing_text))
