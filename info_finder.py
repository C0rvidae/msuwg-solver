import pytesseract


def amount_characters(image):
    data = image.load()
    five_colors = data[321, 5]
    seven_colors = data[44, 5]
    # 40 <= five_colors[0] <= 55 | 25 <= five_colors[1] <= 40 | 15 <= five_colors[2] <= 25
    if 55 >= five_colors[0] >= 40 >= five_colors[1] >= 25 >= five_colors[2] >= 15:
        return 6
    elif 230 <= seven_colors[0] <= 250 and 230 <= seven_colors[1] <= 250 and 220 <= seven_colors[2] <= 240:
        return 7
    else:
        return 5


def cut_characters(image, amount):
    characters = []
    x1 = 50 if amount == 6 else 5 if amount == 7 else 97
    x2 = x1 + 83
    for i in range(amount):
        box = (x1, 0, x2, 89)
        characters.append(image.crop(box))
        x1 = x2 + 8
        x2 = x1 + 83
    return characters


def isolate_characters(characters):
    box = (8, 8, 72, 80)
    for idx, c in enumerate(characters):
        img = c.convert('LA')
        data = img.load()
        w, h = img.size
        for y in range(h):
            for x in range(w):
                if data[x, y][0] > 150:
                    data[x, y] = (255, 0)
        characters[idx] = img
    for idx, c in enumerate(characters):
        characters[idx] = c.crop(box)
    return characters


def find_letters(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    amount = amount_characters(image)
    characters = cut_characters(image, amount)
    characters = isolate_characters(characters)
    for idx, c in enumerate(characters):
        print(f"{idx} | ", end='')
        print(pytesseract.image_to_string(c, lang='eng', config='--psm 10'), end='')
    print("--- DONE ---")

# To find how many possible words:
# 1. cut our word boxes image in columns
# 2. Isolate columns with the word box colors
# 3. Cut into lines
# 4. Count lines with colors
# 5. Now, two ideas
# 5.1 Again, cut into columns and count the colors
# 5.2 Find a way to obtain "sum" of color presence and make a simple ratio (e.g 3/8 of line is blue? -> 3 letters)
# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
