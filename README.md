# **Georgian Book Digitizer**

A Python automation tool for digitizing scanned Georgian books by extracting text via **OCR (Optical Character
Recognition)**, enhancing it using **GPT-4o**, and consolidating the processed content into a structured **digital
format**.

---

## **Features**

✅ **Page-by-Page OCR Extraction**: Uses **Tesseract OCR** (`kat` for Georgian) to process scanned images into individual
text files.  
✅ **AI-Enhanced Text Processing**: Runs **GPT-4o** to improve OCR quality while preserving formatting.  
✅ **Final Consolidation**: Merges all **AI-enhanced** pages into a structured single output file.

---

## **Workflow Overview**

1️⃣ **OCR Processing** → Extract text from scanned images (**per page**).  
2️⃣ **AI Enhancement** → Use `enhance.py` to **refine** OCR text using **GPT-4o**.  
3️⃣ **Final Consolidation** → Merge enhanced text into a single `result.txt` using `consolidate.py`.

---

## **Requirements**

**Python**: `3.10` or higher  
**Dependencies**:

- see in `Pipfile`

## **Setup**

1️⃣ **Clone the repository**

   ```bash
   git clone https://github.com/rezi-gelenidze/book-ocr.git
   cd book-ocr
   ```

2️⃣ **Install dependencies**

   ```bash
   pipenv shell
   pipenv install
   ```

️3️⃣ **Install Tesseract OCR**:

- View docs on web

️4️⃣ **Acquire GPT-4o API Key from OpenAI platform**:

- View docs on web


️5️⃣ **Prepare Directories**

- **Place per-page scanned images** inside `raw/`.

---

## **Usage**

### 1️⃣ **Extract OCR Text from Images**

```bash
python main.py
```

- Processes **each scanned page** and saves **raw OCR output** in `output/` as **separate `.txt` files** (e.g.,
  `1.txt`, `2.txt`, etc.).

### 2️⃣ **Enhance Text Using GPT-4o**

```bash
python enhance.py
```

- Reads raw OCR text from `output/`.
- Uses **GPT-4o** to correct errors and improve readability.
- Saves **enhanced** text per page in `revised/`.

### 3️⃣ **Merge All AI-Enhanced Text into a Single File**

```bash
python consolidate.py
```

- Collects **all enhanced pages** from `revised/`.
- Combines them into a **structured final result** → `result.txt`.

---

## **Outputs**

📂 **Processed Text Files (Per Page)** → `output/revised/`  
📄 **Final Consolidated File** → `output/result.txt`  

---

## **Example Workflow**

**Step 1:** OCR extracts `1.txt`, `2.txt`, ...  
**Step 2:** AI enhances `1.txt → revised/1.txt`, `2.txt → revised/2.txt`  
**Step 3:** All enhanced pages merge into `result.txt`  
