from tkinter import Tk, BOTH, Canvas, ttk, Label, StringVar, X
from PIL import ImageTk, Image
from ansii import Ansii  # Assuming 'Ansii' is a custom class for ASCII art conversion.

class Window:
    """
    A Tkinter-based GUI window for displaying an image and its ASCII art
    representations (grayscale and colored). It provides buttons to switch
    between these views.
    """
    def __init__(self, width: int, height: int, img: Image.Image):
        """
        Initializes the GUI window.

        Args:
            width (int): The desired width for the main image display area.
            height (int): The desired height for the main image display area.
            img (Image.Image): The PIL Image object to be displayed and converted.
        """
        self.image_display_width = width
        self.image_display_height = height
        
        # Calculate dimensions for the ASCII art display if it were to be directly rendered
        # This seems to be a placeholder or an old calculation, as the Ansii class handles its own resizing.
        # It's not directly used for the display area of the ASCII art, which reuses image_display_width/height.
        self.ansii_preview_width = int(width / 6.25)
        self.ansii_preview_height = 100 # This value seems arbitrary if not directly used.

        self.padding_margin = 5  # Margin/padding for UI elements.

        # Initialize the main Tkinter window.
        self.root = Tk()
        self.root.title("ASCII ART FROM IMAGE")
        # Set a protocol for closing the window, calling the 'close' method.
        self.root.protocol("WM_DELETE_WINDOW", self._on_window_close)
        
        # Create the main canvas for drawing and placing widgets.
        # The canvas size is slightly larger than the image display area to accommodate buttons.
        self._canvas = Canvas(self.root, bg="white", 
                              height=self.image_display_height + 100, 
                              width=self.image_display_width + 200)
        self._canvas.pack(fill=BOTH, expand=1)

        # Flag to control the main event loop.
        self._is_running = False
        
        # Store the original PIL Image object.
        self.original_image = img
        
        # Configure ttk (themed Tkinter) styles for buttons.
        self._configure_button_styles()

        # Flags to keep track of which view is currently displayed.
        self._is_picture_displayed = False
        self._is_grayscale_displayed = False
        self._is_color_displayed = False

        # Initialize and place the control buttons.
        self._create_picture_button()
        self._create_grayscale_button()
        self._create_color_button()
    
    def _configure_button_styles(self):
        """
        Configures the styles for Tkinter Themed Widgets (ttk.Button).
        Defines default, 'Red.TButton', and 'Blue.TButton' styles.
        """
        self.style = ttk.Style()
        self.style.configure(
            'TButton', 
            background='darkgray', 
            foreground='black', 
            font=('Arial', 12),
            padding=10, 
            width=13
        )
        self.style.configure(
            'Red.TButton', 
            background='red', 
            foreground='black', 
            font=('Helvetica', 12, 'bold'),
            padding=10, 
            width=13
        )
        self.style.configure(
            'Blue.TButton', 
            background='blue', 
            foreground='black', 
            font=('Helvetica', 12, 'bold'),
            padding=10, 
            width=13
        )

    def _redraw_window(self):
        """
        Updates the Tkinter window. This is necessary to refresh the display
        and process events within the main loop.
        """
        self.root.update()  

    def wait_for_close(self):
        """
        Starts the main event loop of the Tkinter window.
        The window will remain open and responsive until the user closes it
        or the `_is_running` flag is set to False.
        """
        self._is_running = True
        while self._is_running:
            self._redraw_window()
        print("Window closed....")

    def _on_window_close(self):
        """
        Callback function executed when the user attempts to close the window.
        It sets the internal running flag to False, which terminates the main loop.
        """
        self._is_running = False
    
    def _display_original_picture(self):
        """
        Displays the original image in the main display area of the window.
        """
        self._is_picture_displayed = True
        # Convert PIL Image to Tkinter PhotoImage.
        # Store a reference to prevent garbage collection issues with Tkinter.
        self._photo_image = ImageTk.PhotoImage(self.original_image)
        
        # Create and place a Label widget to display the image.
        self._image_display_label = Label(self.root, anchor='nw', padx=self.padding_margin, pady=self.padding_margin, 
                                          height=self.image_display_height, width=self.image_display_width, 
                                          image=self._photo_image)
        self._image_display_label.place(x=self.padding_margin, y=self.padding_margin)

    def _display_grayscale_ascii(self):
        """
        Converts the image to grayscale ASCII art using the Ansii class
        and displays it in the main display area.
        """
        self._is_grayscale_displayed = True
        # Create an Ansii object (without color) and convert the image to ASCII art.
        grayscale_ascii_image = Ansii(self.original_image).convert_image_to_ascii()
        
        # Convert the generated PIL Image (of ASCII art) to Tkinter PhotoImage.
        self._grayscale_ascii_photo_image = ImageTk.PhotoImage(grayscale_ascii_image)
        
        # Create and place a Label widget to display the grayscale ASCII art.
        self._grayscale_display_label = Label(self.root, anchor='nw', padx=self.padding_margin, pady=self.padding_margin, 
                                              height=self.image_display_height, width=self.image_display_width, 
                                              image=self._grayscale_ascii_photo_image)
        self._grayscale_display_label.place(x=self.padding_margin, y=self.padding_margin)        

    def _display_color_ascii(self):
        """
        Converts the image to colored ASCII art using the Ansii class
        and displays it in the main display area.
        """
        self._is_color_displayed = True
        # Create an Ansii object (with color enabled) and convert the image to ASCII art.
        color_ascii_image = Ansii(self.original_image, True).convert_image_to_ascii()
        
        # Convert the generated PIL Image (of colored ASCII art) to Tkinter PhotoImage.
        self._color_ascii_photo_image = ImageTk.PhotoImage(color_ascii_image)
        
        # Create and place a Label widget to display the colored ASCII art.
        self._color_display_label = Label(self.root, anchor='nw', padx=self.padding_margin, pady=self.padding_margin, 
                                          height=self.image_display_height, width=self.image_display_width, 
                                          image=self._color_ascii_photo_image)
        self._color_display_label.place(x=self.padding_margin, y=self.padding_margin) 
        
    def _create_picture_button(self):
        """
        Creates and places the "Actual Picture" button.
        """
        self._picture_button = ttk.Button(self.root, text="Actual Picture", 
                                          command=self._on_picture_button_click,
                                          style='Red.TButton')
        self._picture_button.place(x=(self.image_display_width + 10), y=100)

    def _create_grayscale_button(self):
        """
        Creates and places the "Grey Ansii text" button.
        """
        self._grayscale_button = ttk.Button(self.root, text="Grey Ansii text", 
                                            command=self._on_grayscale_button_click,
                                            style='TButton')
        self._grayscale_button.place(x=(self.image_display_width + 10), y=200)

    def _create_color_button(self):
        """
        Creates and places the "Color Ansii text" button.
        """
        self._color_button = ttk.Button(self.root, text="Color Ansii text", 
                                        command=self._on_color_button_click,
                                        style='Blue.TButton')
        self._color_button.place(x=(self.image_display_width + 10), y=300)

    def _on_picture_button_click(self):
        """
        Handles the click event for the "Actual Picture" button.
        Destroys other active views and displays the original picture.
        """
        self._destroy_grayscale_view()
        self._destroy_color_view()
        self._display_original_picture()
    
    def _on_grayscale_button_click(self):
        """
        Handles the click event for the "Grey Ansii text" button.
        Destroys other active views and displays the grayscale ASCII art.
        """
        self._destroy_picture_view()
        self._destroy_color_view()
        self._display_grayscale_ascii()

    def _on_color_button_click(self):
        """
        Handles the click event for the "Color Ansii text" button.
        Destroys other active views and displays the colored ASCII art.
        """
        self._destroy_picture_view()
        self._destroy_grayscale_view()
        self._display_color_ascii()
        
    def _destroy_picture_view(self):
        """
        Destroys the Label widget displaying the original picture, if it exists and is active.
        """
        if self._is_picture_displayed and hasattr(self, '_image_display_label'):
            self._image_display_label.destroy()
            self._is_picture_displayed = False
    
    def _destroy_grayscale_view(self):
        """
        Destroys the Label widget displaying the grayscale ASCII art, if it exists and is active.
        """
        if self._is_grayscale_displayed and hasattr(self, '_grayscale_display_label'):
            self._grayscale_display_label.destroy()
            self._is_grayscale_displayed = False

    def _destroy_color_view(self):
        """
        Destroys the Label widget displaying the colored ASCII art, if it exists and is active.
        """
        if self._is_color_displayed and hasattr(self, '_color_display_label'):
            self._color_display_label.destroy()
            self._is_color_displayed = False