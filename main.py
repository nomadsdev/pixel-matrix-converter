import os
from PIL import Image
import numpy as np

input_dir = 'bin/images'
output_dir = 'bin/output'
restored_dir = 'bin/restored'

os.makedirs(output_dir, exist_ok=True)

def is_image_file(filename):
    valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff']
    return any(filename.lower().endswith(ext) for ext in valid_extensions)

def convert_image_to_matrix():
    for filename in os.listdir(input_dir):
        if is_image_file(filename):
            file_path = os.path.join(input_dir, filename)

            image = Image.open(file_path)

            image_array = np.array(image)
            height, width, channels = image_array.shape

            output_file_path = os.path.join(output_dir, f'{os.path.splitext(filename)[0]}_Matrix.txt')
            with open(output_file_path, 'w') as f:
                f.write(f'{height},{width},{channels}\n')
                np.savetxt(f, image_array.reshape(-1, channels), fmt='%d')

            print(f"Processed {filename}: Shape = {image_array.shape}, Data saved to {output_file_path}")

def convert_matrix_to_image():
    txt_files = [f for f in os.listdir(output_dir) if f.endswith('_Matrix.txt')]

    if not txt_files:
        print("No matrix files found in output directory.")
        return

    print("Select a matrix file to convert back to image:")
    for idx, txt_file in enumerate(txt_files):
        print(f"{idx + 1}. {txt_file}")

    choice = int(input("Enter the number of the file: ")) - 1
    if choice < 0 or choice >= len(txt_files):
        print("Invalid choice.")
        return

    txt_file_path = os.path.join(output_dir, txt_files[choice])

    with open(txt_file_path, 'r') as f:
        height, width, channels = map(int, f.readline().strip().split(','))
        matrix = np.loadtxt(f, dtype=int)

    image_array = matrix.reshape((height, width, channels))

    image = Image.fromarray(np.uint8(image_array))

    output_image_path = os.path.join(restored_dir, f'{os.path.splitext(txt_files[choice])[0]}_restored.png')
    image.save(output_image_path)

    print(f"Image saved to {output_image_path}")

def main():
    print("Select an option:")
    print("1. Convert image to matrix")
    print("2. Convert matrix to image")

    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        convert_image_to_matrix()
    elif choice == '2':
        convert_matrix_to_image()
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()