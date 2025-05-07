from tkinter import Tk, BOTH, Canvas, ttk, Label, StringVar, X
from PIL import ImageTk
from ansii import Ansii

class Window:
    def __init__(self, width, height, img):
        self.width = width
        self.height = height
        self.ansii_width, self.ansii_height = int(width/6.25), int(100)
        self.margin = 5
        self.root = Tk()
        self.root.title("ASCII_ART_FROM_IMAGE")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.__C = Canvas(self.root, bg="white", height=self.height+100, width=self.width+200)
        self.__C.pack(fill=BOTH, expand=1)
        self.__running = False
        self.img = img
        self.style = ttk.Style()
        self.style.configure(
                'TButton', 
                background='darkgray', 
                foreground='black', 
                font=('Arial', 12),
                padding=10, 
                width = 13
        )
        self.style.configure(
                'Red.TButton', 
                background='red', 
                foreground='black', 
                font=('Helvetica', 12, 'bold'),
                padding=10,
                width = 13
        )
        self.style.configure(
                'Blue.TButton', 
                background='blue', 
                foreground='black', 
                font=('Helvetica', 12, 'bold'),
                padding=10, 
                width = 13
        )
        self.pic, self.grey, self.color = False, False, False
        self.draw_pic_button()
        self.draw_grey_button()
        self.draw_color_button()
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()  

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed....")

    def close(self):
        self.__running = False
    
    def draw_picture(self):
        self.pic = True
        self.photo = ImageTk.PhotoImage(self.img)
        self.image_label = Label(self.root, anchor='nw', padx=5, pady=5, height=self.height, 
                                 width=self.width, image=self.photo)
        self.image_label.place(x=self.margin, y=self.margin)

    def draw_grey(self):
        self.grey = True
        ansii_str = Ansii(self.img)._convert()
        text = StringVar()
        print(ansii_str)
        text.set(ansii_str)
        self.grey_label = Label(self.root, anchor='nw', padx=5, pady=5, background="white",
                                 width=self.ansii_width, textvariable=text,
                                 font=("Arial",8), justify='left')
        self.grey_label.place(x=self.margin, y=self.margin)

    def draw_color(self):
        self.color = True
        ansii_str_color = Ansii(self.img, True)._convert()
        print(ansii_str_color)
        text_color = StringVar()
        text_color.set(ansii_str_color)
        self.color_label = Label(self.root, anchor='nw', padx=5, pady=5, background="white",
                                 width=self.ansii_width, textvariable=text_color,
                                 font=("Arial",8))
        self.color_label.place(x=self.margin, y=self.margin)
        
    def draw_pic_button(self):
        button = ttk.Button(self.root, text="Actual Picture", 
                            command=self.draw_pic_button_click,
                            style='Red.TButton')
        button.place(x=(self.width+10), y=(100))

    def draw_grey_button(self):
        button1 = ttk.Button(self.root, text="Grey Ansii text", 
                            command=self.draw_grey_button_click,
                            style='TButton')
        button1.place(x=(self.width+10), y=(200))

    def draw_color_button(self):
        button2 = ttk.Button(self.root, text="Color Ansii text", 
                            command=self.draw_color_button_click,
                            style='Blue.TButton')
        button2.place(x=(self.width+10), y=(300))

    def draw_pic_button_click(self):
        self.pic_destroy()
        self.grey_destroy()
        self.draw_picture()
    
    def draw_grey_button_click(self):
        self.pic_destroy()
        self.color_destroy()
        self.draw_grey()

    def draw_color_button_click(self):
        self.pic_destroy()
        self.grey_destroy()
        self.draw_color()
        
        
    def pic_destroy(self):
        if self.pic and hasattr(self, 'image_label'):
            self.image_label.destroy()
            self.pic = False
    
    def grey_destroy(self):
        if self.grey and hasattr(self, 'grey_label'):
            self.grey_label.destroy()
            self.grey = False

    def color_destroy(self):
        if self.color and hasattr(self, 'color_label'):
            self.color_label.destroy()
            self.color = False
