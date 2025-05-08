from PIL import Image
from window import Window
import sys


def main():
    try:
        _, image = sys.argv
        img = Image.open(image)
        resized_image = logic_for_resize(img)
        width, height = resized_image.size
        win = Window(width, height, resized_image)  
        win.draw_picture()
        win.wait_for_close()
    except Exception:
        print("Usage: python3 main.py path/to/image")

def logic_for_resize(image):
    width, height = image.size
    aspect_ratio = width/height
    r_width = 500
    r_height = int(r_width/aspect_ratio)
    new_size = image.resize((r_width, r_height))

    return new_size

if __name__ == "__main__":
    main()