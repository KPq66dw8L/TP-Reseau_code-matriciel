# Documentation Pillow: https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
from PIL import Image, ImageDraw

# Définir la taille de l'image en pixels
width, height = 21, 21

# Créer une nouvelle image blanche avec les dimensions spécifiées
image = Image.new("RGB", (width, height), "white")

# Créer un objet ImageDraw pour dessiner sur l'image
draw = ImageDraw.Draw(image)

# Dessiner un motif en damier sur l'image
for x in range(0, width):
    for y in range(0, height):
        if (x + y) % 2 == 0:
            draw.rectangle([x, y, x, y], fill="black")

# Enregistrer l'image dans un fichier
image.save("test.png")