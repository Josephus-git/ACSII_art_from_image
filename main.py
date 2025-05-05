from PIL import Image

def main():
    print("snow")
    img = Image.open(r"test.png")
    img_grey = img.convert("I")
    resized_image = logic_for_resize(img_grey)
    ans = convert(resized_image)
    print(ans)
    


    #resized_image.show()

def convert(image):
    width, _ = image.size
    char_list = ["@", "J", "D", "%", "*", "P", "+", "Y", "$", ",", "."]
    pixels = image.getdata()
   
#the data contained in the image contains pixel values ranging from 0 to 255; representing
#darkest at 0 and light at 255.

    new_pixels = [char_list[pixel//25] for pixel in pixels]
#here we are addressing the 11 characters from the list arr[0] for the thickest characters
#and arr[10] for lightest characters.

    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)

# split string of chars into multiple strings of length equal to width and create a list
    ascii_image = []
    for i in range(0, new_pixels_count, width):
        ascii_image.append(new_pixels[i:i+width])
    ascii_image_f = ("\n").join(ascii_image)

# write to a text file.
    f = open("sample_ascii_image.txt", "w")
    f.write(ascii_image_f)

    return ascii_image_f






"""ascii_image = "\n".join(ascii_image)
print(ascii_image)
 

with open("sample_ascii_image.txt", "w") as f:
 f.write(ascii_image)
"""

def logic_for_resize(image):
    width, height = image.size
    aspect_ratio = width/height
    r_width = 50
    r_height = int(r_width/aspect_ratio)
    new_size = image.resize((r_width, r_height))

    return new_size

if __name__ == "__main__":
    main()