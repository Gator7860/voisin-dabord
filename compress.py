from PIL import Image

img = Image.open("logo.png")
img.thumbnail((800, 800))
img.save("logo.png", "PNG", optimize=True)

print("Logo compressé")