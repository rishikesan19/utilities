import os
from bs4 import BeautifulSoup

# Log file containing HTML code
log_file_path = 'E:\\python_test\\sample.txt'  # Replace 'your_log_file.log' with the actual log file path

# Directory to save individual HTML files
output_directory = 'E:\\python_test'  # Replace 'output_html_files' with your desired directory name

try:
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    with open(log_file_path, 'r') as log_file:
        log_content = log_file.read()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(log_content, 'html.parser')

        # Extract all HTML tags
        html_tags = soup.find_all(recursive=False)

        # Save each HTML tag into separate files
        for i, html_tag in enumerate(html_tags):
            output_file_path = os.path.join(output_directory, f'output_{i + 1}.html')
            with open(output_file_path, 'w') as output_file:
                output_file.write(str(html_tag))

            print(f"Tag {i + 1} saved to {output_file_path}")

except FileNotFoundError:
    print(f"File '{log_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")