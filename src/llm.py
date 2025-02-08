import os
from openai import OpenAI
from src import config


SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are a language model specialized in cleaning OCR-scanned text while preserving every single letter and sentence exactly as it is in the source.\n\n"
        "The input is an OCR-extracted text from a book in the Georgian language. Your task is to:\n\n"
        "1. Strictly remove noise: Delete unnecessary symbols, artifacts, or any OCR-induced errors without altering any letters or words.\n"
        "2. Protect punctuation: Ensure correct punctuation usage without adding or removing letters. Do not modify sentence structure—just clean up redundant, misplaced, or noisy punctuation.\n"
        "3. Do not modify the text: Every letter must remain exactly as it is in the input. You must not change, replace, or paraphrase words—only clean artifacts caused by OCR scanning.\n"
        "4. Retain formatting: Preserve the paragraph structure, spacing, and flow without introducing new elements or restructuring any part of the text.\n"
        "5. Handle broken punctuation:\n"
        "   - Fix redundant sequences like ',.' or '.,' into appropriate punctuation (e.g., '...').\n"
        "   - Ensure that dashes, commas, and colons appear correctly where intended, but never introduce new ones unless correcting obvious OCR noise.\n"
        "6. Preserve page breaks and fragmented sentences: If the text cuts off at the start or end of the page, do not assume the next word. Leave it as is, with no ellipsis.\n\n"

        "As a response, return only the cleaned text—without any explanations, summaries, or modifications."
    )
}


def enhance_with_ai():
    """
    Enhances OCR text page by page and saves the results separately.
    """
    target_files = os.listdir(config.OCR_OUTPUT_DIR)

    # Sort and verify the files
    target_files = sorted(target_files, key=lambda x: int(x.split('.')[0]))
    print(f"Enhancing {len(target_files)} pages...")
    print(f"Pages range from {target_files[0].split('.')[0]} to {target_files[-1].split('.')[0]}")

    client = OpenAI(api_key=config.LLM_API_KEY)

    for file in target_files:
        file_path = os.path.join(config.OCR_OUTPUT_DIR, file)
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
                        "content": f"Here is an OCR-scanned page from a book in Georgian. Please enhance it as I told you in system prompt:\n{file_content}"
                    }
                ]
            )

            print(f"Received response for page {page_number}")

            # Extract enhanced content
            enhanced_content = response.choices[0].message.content

            # Save enhanced page text
            revised_file_path = os.path.join(config.LLM_OUTPUT_DIR, f"{page_number}.txt")
            with open(revised_file_path, 'w', encoding='utf-8') as f:
                f.write(enhanced_content.strip())

        except Exception as e:
            print(f"Error enhancing page {page_number}: {e}")
            continue


if __name__ == "__main__":
    enhance_with_ai()
