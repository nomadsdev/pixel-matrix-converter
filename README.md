# PixelMatrix Converter

PixelMatrix Converter is a Python project that allows you to convert images to matrix files and vice versa. This tool is useful for handling image data in a matrix format and converting it back to visual images.

## Features

- **Convert Images to Matrix**: Converts images from supported formats (PNG, JPG, JPEG, BMP, TIFF) into matrix files containing pixel values.
- **Convert Matrix to Images**: Converts matrix files back into images using the pixel data.

## Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/nomadsdev/pixel-matrix-converter.git
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Install the required Python libraries using pip:
   ```sh
   pip install pillow numpy
   ```

## Usage

1. **Convert Image to Matrix**:
   - Place the images you want to convert in the `bin/images` directory.
   - Run the script and choose option `1` to convert images to matrix format.

   ```sh
   python main.py
   ```

2. **Convert Matrix to Image**:
   - Ensure that the matrix files are in the `bin/output` directory.
   - Run the script and choose option `2` to convert matrix files back to images.

   ```sh
   python main.py
   ```

   The restored images will be saved in the `bin/restored` directory.

## File Structure

- `bin/images/` - Directory to place images for conversion.
- `bin/output/` - Directory where matrix files will be saved.
- `bin/restored/` - Directory where restored images will be saved.

## Example

To convert an image to matrix format:
```sh
python main.py
```
Choose `1` and follow the instructions.

To convert a matrix file back to an image:
```sh
python main.py
```
Choose `2`, select the matrix file, and the image will be saved in the `bin/restored` directory.

## Support

For support or inquiries, please contact: support@jmmentertainment.com

## License

This project is licensed under the MIT License.
