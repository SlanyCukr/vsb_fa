from struct import unpack
from typing import Tuple

from PIL import Image

from encoder import Encoder


# detekce steganografie pomocí 2x2 matice, kde se dívám

# bonus = spočítat, jestli lze vůbec uložit tolik informací do obrázku

# další bonus = pokud nelze tolik informací uložit, navrhnout hodit ty informace do .PNG


if __name__ == "__main__":
    #filename = input("Provide path to file:")
    #text = input("Provide text to hide:")
    filename = "./image.jpeg"
    text = "i am hiding this text"

    encoder = Encoder()
    encoder.load_image(filename)

    encoder.save_message(text)
