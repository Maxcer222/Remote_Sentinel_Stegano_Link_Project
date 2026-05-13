# Remote Sentinel Stegano Link Project
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-green)

## Overview

Remote Sentinel Stegano Link Project is a Python-based cybersecurity tool designed to securely hide encrypted remote links inside image files using steganography techniques.

The project combines encryption and image-based data hiding to create a secure communication method where sensitive information can be invisibly embedded into digital images.

## How It Works

1. The user enters a link or secret data.
2. The data is encrypted.
3. The encrypted data is hidden inside an image.
4. The hidden data can later be extracted and decrypted.
   
## Features

- Hide encrypted links inside image files
- Extract hidden data from encoded images
- Image steganography implementation
- Secure encryption techniques
- Simple command-line interface
- Lightweight and easy to use

## Technologies Used

- Python
- OpenCV
- NumPy
- Cryptography libraries
- Steganography algorithms

## Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the encoder:

```bash
python encode.py
```

Run the decoder:

```bash
python decode.py
```
## Author

Developed by Maxcer222
