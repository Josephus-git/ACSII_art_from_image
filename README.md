# 🖼️ Image to ASCII Art Converter (GUI)

## ✍️ Description
This project provides a graphical user interface (GUI) application built with Python's Tkinter and Pillow library that allows users to convert any image into ASCII art. It supports both grayscale and color ASCII art representations and displays them within the application window. Additionally, the ASCII art is printed to the console for quick viewing or copying.

## 🤔 Why? (Motivation/Goal/Problem to Solve)
The primary motivation behind this project was to explore image processing techniques, specifically the conversion of raster images into character-based art, and to gain hands-on experience with GUI development using Tkinter.

**🎯 Goals:**
* To create a user-friendly application for generating ASCII art from images.
* To implement both grayscale and full-color ASCII conversion algorithms.
* To provide a visual comparison between the original image and its ASCII art versions directly within a GUI.
* To learn and demonstrate proficiency in Python's Pillow library for image manipulation and Tkinter for desktop application development.

This tool solves the problem of needing complex command-line arguments or external services to convert images to ASCII art, offering a simple, self-contained desktop solution.

## 🚀 Quick Start
Follow these steps to get the project up and running on your local machine.

### ✨ Prerequisites
* Python 3.8+
* `pip` (Python package installer)

### ⬇️ Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Josephus-git/ACSII_art_from_image.git
    cd image_to_ASCII_art 
    ```

2.  **Create a virtual environment (recommended):** 🐍
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:** 📦
    ```bash
    pip install -r requirements.txt
    ```

    [![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://www.python.org/)

### ▶️ Running the Application
To run the application, you need to provide the path to an image file as a command-line argument:

```bash
python src/main.py images/sample_image.jpg
```

(Replace images/sample_image.jpg with the actual path to your desired image.)

## 💡 Usage
Upon running the application, a new window will appear displaying the original image.

You will see three buttons on the right side of the window:

🖼️ "**Actual Picture**": Displays the original image. This is the default view.

⚫ "**Grey Ansii text**": Converts the image to grayscale ASCII art and displays it.

🌈 "**Color Ansii text**": Converts the image to colored ASCII art and displays it.

Click on these buttons to switch between the different views. The ASCII art representations will also be printed directly to your console 🖥️ when their respective buttons are clicked, allowing you to copy the text if needed.

**Example**:
Try running it with the provided sample image:
```
python src/main.py images/sample_image.jpg
```

## 📸 Screeshot 
![Screenshot from 2025-05-08 16-51-01](https://github.com/user-attachments/assets/c66ba65a-2b7a-4798-a065-4c8d5a584a3c)

**Original photo**

![Screenshot from 2025-05-08 16-51-16](https://github.com/user-attachments/assets/77996b67-b738-4c61-9e0c-7308ed150d35)

**Black and white**

![Screenshot from 2025-05-08 16-51-40](https://github.com/user-attachments/assets/c72e1784-0c7b-4742-ac16-5ed124ea1c4d)

**Colored acsii**

<img width="729" height="932" alt="Screenshot from 2025-07-16 08-31-45" src="https://github.com/user-attachments/assets/26283f75-de35-48d2-a38f-6aff30b88729" />

**Colored acsii in terminal**


## 🤝 Contribution
Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, please follow these steps:

1. **Fork the repository**. 🔱

2. **Create a new branch** for your feature or bug fix: 🌿

```
git checkout -b feature/your-feature-name
```
or
```
git checkout -b bugfix/fix-description
```

3. **Make your changes** and ensure the code adheres to existing style.

4. **Test your changes** thoroughly. ✅

5. **Commit your changes** with clear and concise commit messages. 📝

6. **Push your branch** to your forked repository. ⬆️

7. **Open a Pull Request** to the `main` branch of the original repository, describing your changes in detail. 📥

---
Feel free to open an issue if you encounter any bugs or have feature requests. Thank you for considering contributing! 🙏





