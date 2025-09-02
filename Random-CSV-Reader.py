import csv
import random
import pyttsx3
import time  # Import the time module for delay


def read_random_row_from_csv(file_path):
    """
    Reads a CSV file, selects a random row, and speaks its content aloud.

    Args:
        file_path (str): The path to the CSV file.
    """
    try:
        # Open the CSV file and read all rows.
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Check if the file is empty.
        if not rows:
            print(f"The file '{file_path}' is empty. No content to read.")
            return

        # Initialize the text-to-speech engine.
        engine = pyttsx3.init()

        # Loop to keep reading random rows with a delay.
        while True:
            # Select a random row from the list of rows.
            random_row = random.choice(rows)

            # Join the elements of the row into a single string to be read.
            text_to_read = ", ".join(random_row)

            print(f"Randomly selected content: {text_to_read}")

            # Say the text and wait for the speech to finish.
            engine.say(text_to_read)
            engine.runAndWait()

            # Wait for 10 seconds before reading the next row.
            time.sleep(15)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found. Please check the file path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # --- Instructions for use ---
    # 1. Ensure you have a CSV file in the same directory as this script,
    #    or provide the full path to your file.
    # 2. Update the 'your_file.csv' below with the actual name of your file.
    # 3. Make sure the CSV file has at least one row of data.
    # 4. If you haven't already, install the necessary library: pip install pyttsx3
    # Example usage:
    csv_file_path = '/home/dskbee/Desktop/sambashare/CSVAsBB/BB-ALL-TECHS&KATAS.csv'
    read_random_row_from_csv(csv_file_path)