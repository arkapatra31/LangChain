import os

# Export the text of summary.txt file
def export_transcript_text(file_path: str):
    transcript = ""

    # Check if the file exists
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as file:
                transcript = file.read()
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
    else:
        print(f"File not found: {file_path}")

    return transcript

__all__ = [export_transcript_text]