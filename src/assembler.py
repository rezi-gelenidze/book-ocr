import os
import config


def assemble(pages: [str]) -> None:
    for file_name, page_text in pages:
        # Save each page as a separate text file
        output_path = os.path.join(
            config.OUTPUT_DIR, f"{file_name.split('.')[0]}.txt"
        )

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(page_text)

    print("Extracted text saved to:", config.OUTPUT_DIR)
