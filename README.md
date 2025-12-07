# QR Code Generator

A simple and efficient web application built with Python and Streamlit that allows users to generate QR codes for any text or URL.

## Features

- **Instant Generation**: Generates QR codes instantly upon entering text or a URL.
- **Preview**: Displays the generated QR code directly in the web interface.
- **Download**: Allows users to download the generated QR code as a PNG image.
- **User-Friendly Interface**: Clean and simple UI with instructions.

## Prerequisites

Before running this project, ensure you have Python installed on your system.

## Installation

1.  **Clone the repository** (if applicable) or navigate to the project directory.

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment**:
    - On Windows:
      ```powershell
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4.  **Install the required dependencies**:
    ```bash
    pip install streamlit qrcode[pil]
    ```

## Usage

1.  **Run the Streamlit app**:
    ```bash
    streamlit run qr_generate.py
    ```

2.  **Open your browser**:
    The app will automatically open in your default web browser. If not, navigate to the URL shown in the terminal (usually `http://localhost:8501`).

3.  **Generate a QR Code**:
    - Enter a URL or text in the input field.
    - The QR code will appear on the screen.
    - Click the "Download QR Code" button to save it.

## Project Structure

- `qr_generate.py`: The main Python script containing the Streamlit application logic.
- `generated_qr.png`: Temporary file created during generation (overwritten each time).
- `venv/`: Virtual environment directory (created after setup).

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Framework for creating the web application.
- **qrcode**: Library for generating QR code images.

## License

MIT License

Copyright (c) 2025 harshit0017pro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
