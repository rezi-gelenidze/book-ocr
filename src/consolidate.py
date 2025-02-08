import os
from src import config


def merge_txt_files():
    """
    Merges all .txt files in the specified directory into a single text file.
    """
    source_dir = config.LLM_OUTPUT_DIR
    output_file = os.path.join(config.BASE_DIR, 'result.txt')

    try:
        # Get all .txt files in the source directory
        txt_files = [f for f in os.listdir(source_dir) if f.endswith('.txt')]

        # Sort files numerically based on their filenames
        txt_files = sorted(txt_files, key=lambda x: int(os.path.splitext(x)[0]))

        # Open the output file in write mode
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for txt_file in txt_files:
                file_path = os.path.join(source_dir, txt_file)
                print(f"Appending '{txt_file}' to '{output_file}'")

                # Read content of the current file and write it to the output file
                with open(file_path, 'r', encoding='utf-8') as infile:
                    outfile.write(f"\n\n[გვერდი {os.path.splitext(txt_file)[0]}]\n\n")
                    outfile.write(infile.read().strip())  # Strip any extra leading/trailing spaces

        print(f"All files merged successfully into '{output_file}'")

    except Exception as e:
        print(f"Error during merging: {e}")

# Run the function
merge_txt_files()