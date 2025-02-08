# Separated responsibility modules
import splitter, recognition, llm, consolidation


def main():
    # Step 1: Load pairs/ and split each pair into separate pages
    splitter.split_pairs()

    # Step 2: Load pages/ and recognize text from each page and save as txt files
    recognition.recognize_pages()

    # Step 3: Enhance the recognized text using OpenAI's LLM
    llm.enhance_with_ai()

    # Step 4: Assemble the enhanced text into a single file
    consolidation.merge_txt_files()


if __name__ == "__main__":
    main()
