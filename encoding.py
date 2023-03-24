# Documentation Pillow: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
from PIL import Image, ImageDraw

input_to_encode = "Hello World!"

if (len(input_to_encode) > 19 ): #19 char max dans une matrice 21x21
    print("Message trop long")
    exit()

input_bin = ''.join(format(ord(x), 'b') for x in input_to_encode)

#Test zone -----------------------------

print(input_bin)

#fin test zone -------------------------

# Définir la taille de l'image en pixels
width, height = 21, 21

# Créer une nouvelle image blanche avec les dimensions spécifiées
image = Image.new("RGB", (width, height), "white")

# Créer un objet ImageDraw pour dessiner sur l'image
draw = ImageDraw.Draw(image)

index_bin = 0
# Dessiner un motif en damier sur l'image
for x in range(0, width):
    for y in range(0, height):
        if input_bin[index_bin] == "1":
            draw.rectangle([x, y, x, y], fill="black")
        if index_bin < len(input_bin)-1:
            index_bin += 1
        else:
            break
    if not (index_bin < len(input_bin)-1):
        break

# Enregistrer l'image dans un fichier
image.save("test.png")