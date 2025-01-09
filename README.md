# Steganography and Watermarking Project

This project demonstrates techniques for encoding and decoding steganographic messages, detecting steganography using machine learning, and applying watermarks to images. It includes four Python scripts, each serving a distinct purpose.

---

## Folder Structure
The project contains the following files and folders:
1. **DecodeSteganography**: Decodes hidden messages from images.
2. **DetectSteganography**: Detects steganographic content in images using a convolutional neural network (CNN).
3. **EncodeSteganography**: Encodes text messages into images using steganography techniques.
4. **Watermarking**: Adds watermark layers to images.

---

## Scripts Overview

### 1. **DecodeSteganography.py**
This script extracts hidden messages encoded in an image's pixel data.

- **Inputs**:
  - `Encode_Flower.png`: An image with a hidden message.
- **Key Functionality**:
  - Reads the image.
  - Extracts the hidden message from the least significant bits of the pixel data.
- **Output**:
  - Prints the decoded message to the console.

#### Example Usage:
    ```bash
    python DecodeSteganography.py
    ```

### 2. **DetectSteganography.py**
This script uses a CNN model to detect steganographic images.

- **Key Features**:
  - A CNN with convolutional, pooling, and dense layers to classify images as steganographic or not.
  - Data preprocessing and augmentation using `ImageDataGenerator`.
  - Training and validation datasets for supervised learning.
  - Outputs the number of detected steganographic images.

- **File Requirements**:
  - Training dataset: `./archive/train`
  - Test dataset: `./archive/test`

#### Example Usage:
  ```bash
  python DetectSteganography.py
  ```

## 3. **EncodeSteganography.py**
This script hides a text message within an image by modifying pixel data.

- **Inputs**:
  - `Flower.jpg`: Original image for encoding.
  - `plain_text`: The text to encode.
- **Key Functionality**:
  - Converts the text into binary format.
  - Modifies the least significant bits of the image pixels to embed the message.
- **Output**:
  - `Encode_Flower.png`: The image containing the hidden message.

#### Example Usage:
  ```bash
  python EncodeSteganography.py
  ```

## 4. **Watermarking.py**
This script applies multiple transparent watermark layers to an image.

- **Inputs**:
  - `image.jpg`: The image to watermark.
  - `./masters/`: Folder containing watermark images.
  - `list_position`: List of coordinates defining watermark positions.
- **Key Functionality**:
  - Combines the original image with multiple watermarks at specified positions.
- **Output**:
  - `output.png`: The watermarked image.

#### Example Usage:
  ```bash
  python Watermarking.py
  ```

---

## Dependencies
Ensure the following libraries are installed before running the scripts:
- OpenCV: `pip install opencv-python`
- NumPy: `pip install numpy`
- TensorFlow: `pip install tensorflow`
- PIL: `pip install pillow`

---

## Project Workflow
1. **Encoding**: Use `EncodeSteganography.py` to hide a message in an image.
2. **Decoding**: Retrieve the hidden message using `DecodeSteganography.py`.
3. **Detection**: Check if an image contains steganographic content with `DetectSteganography.py`.
4. **Watermarking**: Apply multiple watermarks to an image using `Watermarking.py`.

---

## Future Improvements
- Support for additional image formats.
- Enhanced machine learning model for steganography detection.
- Dynamic text and image watermark positioning.


