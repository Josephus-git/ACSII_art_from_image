from PIL import Image

def main():
    img = Image.open(r"sample/serpent.png")
    resized_image = logic_for_resize(img)
    ans = convert(resized_image, False)
    print(ans)
    


    #resized_image.show()

def _get_ansi_color(char, rgb):
        """
        Return the ansii string to display colored characters in the terminal if true color is supported.
        """
        if type(rgb) == int:
            r = g = b = rgb
        else:
            r, g, b = rgb
        return f"\x1b[38;2;{r};{g};{b}m{char}\x1b[0m"

def convert(image, color=False):
    width, _ = image.size
    img_grey = image.convert("I")
    img_color_data = image.convert("RGB")

    char_list = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
    """
    the data contained in the image contains pixel values ranging from 0 to 255; representing
    darkest at 0 and light at 255.
    """
    pixels = img_grey.getdata()
    if color:
        color_pixels = img_color_data.getdata()
        #new_color_pixels = [char_list[pixel//25] for pixel in color_pixels]
    """
    here we are addressing the 11 characters from the list arr[0] for the thickest characters
    and arr[10] for lightest characters.
    """
    new_pixels = [char_list[pixel//25] for pixel in pixels]

    
    
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    """
    split string of chars into multiple strings of length equal to width and create a list
    """

    ascii_image = []
    for i in range(0, new_pixels_count, width):
        if color:
            line = ""
            for letter in range(i, i+width):
                color_char = _get_ansi_color(new_pixels[letter], color_pixels[letter])
                line += color_char
            ascii_image.append(line)
        else:
            ascii_image.append(new_pixels[i:i+width])
    
    ascii_image_f = ("\n").join(ascii_image)


    return ascii_image_f






def logic_for_resize(image):
    width, height = image.size
    aspect_ratio = width/height
    r_width = 50
    r_height = int(r_width/aspect_ratio)
    new_size = image.resize((r_width, r_height))

    return new_size

if __name__ == "__main__":
    main()