from string import ascii_lowercase
from PIL import Image
from os import getcwd, path

CHARACTER_IMAGE_FORMAT = ".png"
PATH_TO_FILE = "to_convert.txt"
STEP_WIDTH = 164
STEP_HEIGHT = 164
SPACE_EXTRA_WIDTH = 32
ALPHABET = set(ascii_lowercase)
CHARACTERS_WITH_CUSTOM_BEHAVIOR = {" ", "\n"}


def get_path():
    """
    You can implement your own way to obtain path.
    """
    return path.join(getcwd(), "characters")


all_characters = dict()

for char in ALPHABET:
    all_characters[char] = Image.open(path.join(get_path(), f"{char}{CHARACTER_IMAGE_FORMAT}"))

with open(PATH_TO_FILE) as file:
    file_content = file.read()


def clean_line(line): return "".join(char.lower()
                                     for char
                                     in line
                                     if char.lower()
                                     in ALPHABET | CHARACTERS_WITH_CUSTOM_BEHAVIOR)


clean_file_content = "\n".join(clean_line(line) for line in file_content.splitlines() if len(clean_line(line)) != 0)

width = max(len(line) * STEP_WIDTH + line.count(' ') * SPACE_EXTRA_WIDTH for line in clean_file_content.splitlines())
height = len(clean_file_content.splitlines()) * STEP_HEIGHT

image = Image.new("RGBA", (width, height))

current_x = 0
current_y = 0


def custom_behavior(character: str):
    """
    Define your custom behaviour of characters.
    First value of tuple defines to what value will current_x change.
    Second value of tuple defines to what value will current_y change.
    """
    if character == "\n":
        return current_x, STEP_HEIGHT
    if character == " ":
        return current_x + STEP_WIDTH + SPACE_EXTRA_WIDTH, current_y
    return current_x, current_y


for current_character in clean_file_content:
    if current_character in CHARACTERS_WITH_CUSTOM_BEHAVIOR:
        custom_behavior_result = custom_behavior(current_character)
        current_x = custom_behavior_result[0]
        current_y = custom_behavior_result[1]
    else:
        image.paste(all_characters[current_character], (current_x, current_y))
        current_x += STEP_WIDTH

image.save("converted.png")
