from PIL import Image 
from window import Window  
import sys  


def main():
    """
    The main function of the script. It processes a command-line argument
    (expected to be an image file path), opens and resizes the image,
    and then uses the 'Window' class to display it.
    """
    try:
        # sys.argv is a list of command-line arguments.
        # sys.argv[0] is the script name itself (e.g., 'main.py').
        # sys.argv[1] is the first argument provided by the user (expected to be the image path).
        image_path = sys.argv[1]

        # Open the image file using Pillow's Image.open() function.
        original_image = Image.open(image_path)
        
        # Resize the image to a predefined display size.
        display_image = _resize_image_for_display(original_image)
        
        # Get the dimensions of the resized image.
        image_width, image_height = display_image.size
        
        # Initialize the custom Window object with the image dimensions and the image itself.
        # The 'Window' class is expected to handle the graphical display of the image.
        display_window = Window(image_width, image_height, display_image)
        
        # Call a method on the Window object to draw/display the picture.
        display_window._display_original_picture()
        
        # Call a method on the Window object to keep the window open until the user closes it.
        display_window.wait_for_close()
        
    except ValueError:
        # This exception typically occurs if an incorrect number of arguments is provided.
        print("Usage: python3 src/main.py images/<target_image>")
    except FileNotFoundError:
        # This exception occurs if the specified image file does not exist.
        print(f"Error: Image file not found at '{image_path}'. Please check the path.")
    except Exception as e:
        # Catch any other unexpected exceptions and print a generic error message.
        print(f"An unexpected error occurred: {e}")
        print("Usage: python3 main.py <path/to/image>")

def _resize_image_for_display(image: Image.Image) -> Image.Image:
    """
    Resizes the input PIL Image to a fixed width of 500 pixels while maintaining
    its aspect ratio. This is a common practice for displaying images
    consistently, especially in a custom window environment.

    Args:
        image (Image.Image): The input PIL Image object to be resized.

    Returns:
        Image.Image: The resized PIL Image object.
    """
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height
    
    # Define a target width for display purposes.
    target_width = 500
    # Calculate the corresponding height to maintain the aspect ratio.
    target_height = int(target_width / aspect_ratio)
    
    resized_image = image.resize((target_width, target_height))

    return resized_image


if __name__ == "__main__":
    main()