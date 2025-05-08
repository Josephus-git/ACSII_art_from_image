from PIL import Image, ImageDraw, ImageFont
class Ansii:
    def __init__(self, image, color=False):
        self.old_image = image
        self.image = self.logic_for_ansii_resize(self.old_image)
        self.color = color
        self.width, _ = self.image.size

    def logic_for_ansii_resize(self, image):
        width, height = image.size
        aspect_ratio = width/height
        r_width = 42
        r_height = int(r_width/aspect_ratio)
        new_size = image.resize((r_width, r_height))
        return new_size
    
    def to_png(self, ansii_char_list, ansii_color_list):
        width, height = len(ansii_char_list[0]), len(ansii_char_list)
        char_width, char_height = 12, 12
        img = Image.new("RGB", (width*char_width, height*char_height), color='white')
        canvas = ImageDraw.Draw(img)
        
        for h in range(height):
            for w in range(width):
                if self.color:
                    canvas.text((w*char_width, h*char_height),
                                 ansii_char_list[h][w],
                                 fill=ansii_color_list[h][w]
                                 )
                else:
                    canvas.text((w*char_width, h*char_height), ansii_char_list[h][w], fill="black")
        return img
    

    def _convert(self):
        img_grey = self.image.convert("I")
        img_color_data = self.image.convert("RGB")

        char_list = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
        """
        the data contained in the image is pixel values ranging from 0 to 255; representing
        darkest at 0 and light at 255.
        """
        pixels = img_grey.getdata()
        if self.color:
            color_pixels = img_color_data.getdata()
        new_pixels = [char_list[pixel//25] for pixel in pixels]
        """
        here we are addressing the 11 characters from the list arr[0] for the thickest characters
        and arr[10] for lightest characters.
        """
        new_pixels = ''.join(new_pixels)
        new_pixels_count = len(new_pixels)
        """
        split string of chars into multiple strings of length equal to width and create a list
        """

        ascii_char = []
        ascii_color_char = []
        ascii_to_png_data = []
        for i in range(0, new_pixels_count, self.width):
            if self.color:
                line_color = []
                line = ""
                for letter in range(i, i+self.width):
                    color_char = self._get_ansi_color(new_pixels[letter], color_pixels[letter])
                    line += color_char
                    line_color.append(color_pixels[letter])
                ascii_color_char.append(line)
                ascii_to_png_data.append(line_color)
            
            ascii_char.append(new_pixels[i:i+self.width])
        
        to_screen = self.to_png(ascii_char, ascii_to_png_data)

        if self.color:
            ascii_color_char_f = ("\n").join(ascii_color_char)
            print(ascii_color_char_f + "\n")
        else:
            ascii_char_f = ("\n").join(ascii_char)
            print(ascii_char_f + "\n")

        return to_screen
        

    def _get_ansi_color(self, char, rgb):
        """
        Return the ansii string to display colored characters in the terminal if true color is supported.
        """
        r, g, b = rgb
        return f"\x1b[38;2;{r};{g};{b}m{char}\x1b[0m"