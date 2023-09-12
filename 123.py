import PyPDF2

# Open the PDF file in read binary mode
with open('1.pdf', 'rb') as file:
    # Create a PDF reader object
    reader = PyPDF2.PdfReader(file)

    # Get the total number of pages in the PDF
    num_pages = len(reader.pages)

    # Extract text from each page and write to a text file
    with open('1.txt', 'w', encoding='utf-8') as output_file:
        for page_number in range(num_pages):
            # Get a specific page object
            page = reader.pages[page_number]

            # Extract text from the page
            text = page.extract_text()

            # Write the text to the output file
            output_file.write(text)
