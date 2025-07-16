from PIL import Image, ImageDraw, ImageFont

class Ansii:
    """
    A class to convert images into ASCII art, with optional color support.
    It resizes the image, maps pixel intensity to ASCII characters,
    and can either print the ASCII art to the console or generate a PNG image.
    """
    def __init__(self, image: Image.Image, color: bool = False):
        """
        Initializes the Ansii object.

        Args:
            image (Image.Image): The input PIL Image object.
            color (bool): If True, the generated ASCII art will attempt to preserve original colors.
                          If False, it will be grayscale. Defaults to False.
        """
        self.original_image = image  # Stores the original image for reference.
        # Resize the image to a suitable dimension for ASCII conversion.
        self.processed_image = self._resize_for_ascii(self.original_image)
        self.enable_color = color  # Flag to determine if color ASCII art should be generated.
        self.width, _ = self.processed_image.size # Get the width of the processed image.

    def _resize_for_ascii(self, image: Image.Image) -> Image.Image:
        """
        Resizes the input image to a fixed width while maintaining its aspect ratio.
        This is crucial for consistent ASCII art generation, as terminal output has
        a different character aspect ratio than pixels.

        Args:
            image (Image.Image): The PIL Image object to be resized.

        Returns:
            Image.Image: The resized PIL Image object.
        """
        original_width, original_height = image.size
        aspect_ratio = original_width / original_height
        
        # Define a target width for the ASCII art output.
        # This can be adjusted to control the detail level and output size.
        target_width = 42 
        # Calculate the corresponding height to maintain the aspect ratio.
        target_height = int(target_width / aspect_ratio)
        
        resized_image = image.resize((target_width, target_height))
        return resized_image
    
    def _create_png_from_ascii(self, ascii_character_matrix: list[list[str]], ascii_color_matrix: list[list[tuple]] = None) -> Image.Image:
        """
        Generates a PNG image from the ASCII character matrix.
        Each character is drawn onto a new image, with optional color applied.

        Args:
            ascii_character_matrix (list[list[str]]): A 2D list where each inner list represents a row
                                                       of ASCII characters.
            ascii_color_matrix (list[list[tuple]]): An optional 2D list where each inner list contains
                                                     RGB tuples corresponding to the color of each character.
                                                     Only used if self.enable_color is True. Defaults to None.

        Returns:
            Image.Image: A PIL Image object representing the ASCII art as a PNG.
        """
        # Determine the dimensions of the ASCII art grid.
        grid_width = len(ascii_character_matrix[0])
        grid_height = len(ascii_character_matrix)
        
        # Define the size of each character in the output PNG.
        # These values can be adjusted based on desired font size and appearance.
        char_pixel_width, char_pixel_height = 12, 12
        
        # Create a new blank RGB image with a white background.
        png_image = Image.new("RGB", (grid_width * char_pixel_width, grid_height * char_pixel_height), color='white')
        canvas = ImageDraw.Draw(png_image)
        
        # Iterate through each character in the ASCII character matrix.
        for row_index in range(grid_height):
            for col_index in range(grid_width):
                # If color is enabled, use the color from the color matrix.
                if self.enable_color:
                    canvas.text(
                        (col_index * char_pixel_width, row_index * char_pixel_height),
                        ascii_character_matrix[row_index][col_index],
                        fill=ascii_color_matrix[row_index][col_index]  # Use the specific RGB color for the character
                    )
                # Otherwise, draw the character in black.
                else:
                    canvas.text(
                        (col_index * char_pixel_width, row_index * char_pixel_height),
                        ascii_character_matrix[row_index][col_index],
                        fill="black"
                    )
        return png_image
    
    def convert_image_to_ascii(self) -> Image.Image:
        """
        Converts the processed image into ASCII art, printing it to the console
        and returning a PIL Image object of the ASCII art.

        The process involves:
        1. Converting the image to grayscale to determine intensity.
        2. Mapping pixel intensities to a predefined set of ASCII characters.
        3. If color is enabled, extracting the original pixel colors.
        4. Arranging the characters into lines based on the image width.
        5. Printing the ASCII art to the console (with ANSI color codes if enabled).
        6. Generating a PNG image of the ASCII art.

        Returns:
            Image.Image: A PIL Image object representing the ASCII art.
        """
        # Convert the image to a single-channel 'I' mode (integer pixels) for grayscale intensity.
        grayscale_image = self.processed_image.convert("I")
        # Convert the image to 'RGB' mode to extract color information if needed.
        rgb_image_data = self.processed_image.convert("RGB")

        # Define the set of ASCII characters ordered from darkest to lightest.
        # The number of characters determines the granularity of the intensity mapping.
        ascii_character_set = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
        
        # Get pixel data from the grayscale image. Each pixel value ranges from 0 (darkest) to 255 (lightest).
        grayscale_pixels = grayscale_image.getdata()
        
        # If color is enabled, get pixel data from the RGB image.
        if self.enable_color:
            color_pixels = rgb_image_data.getdata()
        
        # Map each grayscale pixel intensity to an ASCII character.
        # Dividing by 25 (255 / 11 characters approx) distributes pixels across the character set.
        mapped_ascii_characters = [ascii_character_set[pixel_value // 25] for pixel_value in grayscale_pixels]
        
        # Join the list of characters into a single string.
        # This string now represents the entire image as a sequence of ASCII characters.
        ascii_string_representation = ''.join(mapped_ascii_characters)
        total_ascii_characters_count = len(ascii_string_representation)
        
        # Prepare lists to store the formatted ASCII art for console and PNG output.
        ascii_lines_for_display = []        # For printing to console (grayscale)
        ascii_color_lines_for_display = []  # For printing to console (colored)
        ascii_colors_for_png = []           # For generating PNG with colors

        # Split the single string of ASCII characters into lines, based on the processed image's width.
        for i in range(0, total_ascii_characters_count, self.width):
            if self.enable_color:
                current_line_colors = []
                current_line_colored_ascii = ""
                # Iterate through characters in the current line.
                for char_index in range(i, i + self.width):
                    # Get the ANSI color escape sequence for the character.
                    colored_char = self._get_ansi_color_code(
                        ascii_string_representation[char_index],
                        color_pixels[char_index]
                    )
                    current_line_colored_ascii += colored_char
                    current_line_colors.append(color_pixels[char_index])
                ascii_color_lines_for_display.append(current_line_colored_ascii)
                ascii_colors_for_png.append(current_line_colors)
            
            # For both color and grayscale modes, build the basic ASCII character lines.
            ascii_lines_for_display.append(ascii_string_representation[i : i + self.width])
        
        # Generate the PNG image from the ASCII character matrix and color matrix (if enabled).
        generated_png_image = self._create_png_from_ascii(
            ascii_character_matrix=ascii_lines_for_display,
            ascii_color_matrix=ascii_colors_for_png if self.enable_color else None
        )

        # Print the ASCII art to the console.
        if self.enable_color:
            # Join the colored ASCII lines with newlines for terminal display.
            formatted_color_output = ("\n").join(ascii_color_lines_for_display)
            print(formatted_color_output + "\n")
        else:
            # Join the grayscale ASCII lines with newlines for terminal display.
            formatted_grayscale_output = ("\n").join(ascii_lines_for_display)
            print(formatted_grayscale_output + "\n")

        return generated_png_image
        
    def _get_ansi_color_code(self, char: str, rgb: tuple) -> str:
        """
        Generates an ANSI escape sequence string to display a character with a specific RGB color
        in a terminal that supports true color (24-bit color).

        Args:
            char (str): The ASCII character to be colored.
            rgb (tuple): A tuple containing the (Red, Green, Blue) color values for the character.

        Returns:
            str: The ANSI escape sequence string for the colored character.
        """
        r, g, b = rgb
        # ANSI escape sequence for 24-bit true color: \x1b[38;2;R;G;Bm<character>\x1b[0m
        # 38;2 indicates true color foreground, R;G;B are the color components.
        # \x1b[0m resets the color to default.
        return f"\x1b[38;2;{r};{g};{b}m{char}\x1b[0m"