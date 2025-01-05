# Georgian Book Digitizer

A Python automation tool for processing scanned Georgian books, extracting text using OCR (Optical Character Recognition), and exporting the content into digital formats such as TXT, PDF, or DOCX.

---

## Features

- **Image Optimization**: Prepares scanned images for accurate text recognition by enhancing quality and readability.
- **Georgian OCR Support**: Utilizes Tesseract OCR with Georgian language support (`kat`).
- **Multi-format Export**: Outputs extracted text as:
    - Plain text (`.txt`)
    - PDF file (`.pdf`)
    - Word document (`.docx`)

---

## Requirements

- **Python**: `3.10` or higher
- **Dependencies**:
    - `fpdf`
    - `python-docx`
    - `numpy`
    - `pillow`
    - `pytesseract`
    - `opencv-python-headless`

Install dependencies using the provided `Pipfile`:
```bash
pipenv install
```

- **Tesseract OCR**: Install Tesseract and Georgian language data:
    - On Linux:
      ```bash
      sudo apt update
      sudo apt install tesseract-ocr tesseract-ocr-kat
      ```
    - On macOS:
      ```bash
      brew install tesseract
      brew install tesseract-lang
      ```
    - On Windows: Download from the [official site](https://github.com/tesseract-ocr/tesseract).

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/rezi-gelenidze/book-ocr.git
   cd book-ocr
   ```

2. Install the dependencies:
   ```bash
   pipenv shell
   pipenv install
   ```

3. Prepare directories:
    - Place scanned images of the Georgian book in the `source/raw/` directory.

---

## Usage

Run the script:
```bash
python main.py
```

The script will:
1. Optimize scanned images in the `raw_images` folder.
2. Perform OCR to extract text from the optimized images.
3. Combine the extracted text into a single digital file (`.txt`, `.pdf`, or `.docx`) in the `output` folder.

---

## Outputs

- **Text File**: Plain text format (`output.txt`).
- **PDF**: Portable Document Format (`output.pdf`).
- **Word Document**: Editable Word file (`output.docx`).
