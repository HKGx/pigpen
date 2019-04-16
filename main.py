from os import getcwd
from string import ascii_lowercase
from PIL import Image

PATH_TO_CHARACTERS = '\\characters\\'
PATH_TO_FILE = "to_convert.txt"

all_chars = dict()

cwd = getcwd()
for char in ascii_lowercase:
    all_chars[char] = Image.open(f"{cwd}{PATH_TO_CHARACTERS}{char}.png")

with open(PATH_TO_FILE) as file:
    file_content = file.read()


def clean_line(line): return "".join(char.lower() for char in line if char.lower() in ascii_lowercase)


clean_file_content = "\n".join(clean_line(line) for line in file_content.splitlines() if len(clean_line(line)) != 0)

max_chars_count = max(len(line) for line in clean_file_content.splitlines())


STEP_WIDTH = 164
STEP_HEIGHT = 164

width = max_chars_count * STEP_HEIGHT
height = len(clean_file_content.splitlines()) * STEP_HEIGHT

image = Image.new("RGBA", (width, height))

current_char_index = 0


for y in range(0, height, STEP_HEIGHT):
    for x in range(0, width, STEP_WIDTH):
        current_char = clean_file_content[current_char_index]
        image.paste(all_chars[current_char], (x, y))
        current_char_index += 1

image.save("converted.png")
