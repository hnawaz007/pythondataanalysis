from PIL import Image
import pytesseract

text = pytesseract.image_to_string("img.jpg")
print(text)
