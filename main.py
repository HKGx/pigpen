from os import getcwd
from string import ascii_lowercase
from PIL import Image

PATH_TO_CHARACTERS = '\\characters\\'
PATH_TO_FILE = "to_convert.txt"
STEP_WIDTH = 164
STEP_HEIGHT = 164
SPACE_EXTRA_WIDTH = 32

cwd = getcwd()

all_chars = dict()

for char in ascii_lowercase:
    all_chars[char] = Image.open(f"{cwd}{PATH_TO_CHARACTERS}{char}.png")

with open(PATH_TO_FILE) as file:
    file_content = file.read()


def clean_line(line): return "".join(char.lower() for char in line if char.lower() in ascii_lowercase + " ")


clean_file_content = "\n".join(clean_line(line) for line in file_content.splitlines() if len(clean_line(line)) != 0)

max_chars_count = max(len(line)+(line.count(' ')) for line in clean_file_content.splitlines())


width = max_chars_count * STEP_HEIGHT
height = len(clean_file_content.splitlines()) * STEP_HEIGHT

image = Image.new("RGBA", (width, height))

# I guess that it's not the very pythonic way to do it, but I don't really want to mess up with it.

current_char_index = 0
current_x = 0
current_y = 0

while current_char_index < len(clean_file_content):
    current_char = clean_file_content[current_char_index]
    if current_char == "\n":
        current_y += STEP_HEIGHT
        current_x = 0
    elif current_char == " ":
        current_x += STEP_HEIGHT + SPACE_EXTRA_WIDTH
    else:
        image.paste(all_chars[current_char], (current_x, current_y))
        current_x += STEP_WIDTH
    current_char_index += 1

image.save("converted.png")
