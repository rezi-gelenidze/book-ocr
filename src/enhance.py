import os
from openai import OpenAI
from src import config

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are a language model specialized in enhancing text extracted from OCR scans.\n"
        "The input is an OCR scan of a page from a book in the Georgian language. Your task is to:\n"
        "1. Remove noise: Eliminate any noise characters, unnecessary symbols, or incorrect artifacts introduced during OCR scanning.\n"
        "2. Fix errors: Correct grammatical, syntactical, or OCR-induced mistakes while preserving the original sentence structure. Do not restructure sentences unless necessary to fix OCR errors.\n"
        "3. Address ideological mess: Identify and correct any distortions or misinterpretations caused by OCR errors, ensuring the original meaning and intent of the text are preserved.\n"
        "4. Preserve structure: Retain the original formatting, including paragraphs, headings, lists, and other structural elements.\n"
        "5. Enhance readability: Ensure the text is clear and maintains the tone and context of the original, without altering the flow or style of the writing.\n"
        "6. Handle punctuation:\n"
        " - Replace sequences like ',.,' or similar with appropriate punctuation (e.g., '...').\n"
        "7. Handle disconnected sentences: Pay close attention to the start and end of pages. If a sentence is disconnected (e.g., ends with unexpectedly or starts mid-sentence), assume it continues from the previous page or onto the next page. Do not treat it as a complete sentence unless confirmed by context and not write '...' instead in the end, leave as is.\n"
        "8. As a response, write only the corrected text result, nothing else."
    ),
}


def enhance():
    """
    Enhances OCR text page by page and saves the results separately.
    """
    target_files = os.listdir(config.OUTPUT_DIR)

    # Sort and verify the files
    target_files = sorted(target_files, key=lambda x: int(x.split('.')[0]))
    print(f"Enhancing {len(target_files)} pages...")
    print(f"Pages range from {target_files[0].split('.')[0]} to {target_files[-1].split('.')[0]}")

    client = OpenAI(api_key=config.LLM_API_KEY)

    for file in target_files[6:]:
        file_path = os.path.join(config.OUTPUT_DIR, file)
        with open(file_path, 'r', encoding='utf-8') as f:
            file_content = f.read()

        page_number = int(file.split('.')[0])

        print(f"Sending request to OpenAI for page {page_number}...")

        try:
            # Process one page at a time
            response = client.chat.completions.create(
                model="gpt-4o",
                stream=False,
                messages=[
                    SYSTEM_PROMPT,
                    {
                        "role": "user",
                        "content": f"Here is an OCR-scanned page from a book in Georgian. Please enhance it:\n{file_content}"
                    }
                ]
            )

            print(f"Received response for page {page_number}")

            # Extract enhanced content
            enhanced_content = response.choices[0].message.content

            # Save enhanced page text
            revised_file_path = os.path.join(config.REVISED_SOURCE_DIR, f"{page_number}.txt")
            with open(revised_file_path, 'w', encoding='utf-8') as f:
                f.write(enhanced_content.strip())

        except Exception as e:
            print(f"Error enhancing page {page_number}: {e}")
            continue


if __name__ == "__main__":
    enhance()
