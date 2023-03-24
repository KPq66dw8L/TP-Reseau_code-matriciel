from PIL import Image

try:
    # Open the image form working directory
    with Image.open('test.png') as im:
        print('test.png', im.format, f"{im.size}x{im.mode}")
        x = 0
        y = 0
        msg = ""
        # Loop over the image
        for x in range(0, im.width):
            for y in range(0, im.height):
                color = im.getpixel((x, y))
                if color == (0, 0, 0):
                    msg += "1"
                else:
                    msg += "0"
        # Print the message read in binary from the image
        print(msg) 

except OSError:
    pass