import openai
import PyPDF2

# Set up OpenAI API credentials
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to send a message to Chat GPT and receive a response
def chat_with_gpt(message):
    response = openai.Completion.create(
        engine='davinci-codex',
        prompt=message,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Main function
def main():
    # Prompt the user to enter the path to the PDF file
    pdf_file_path = input("Enter the path to the PDF file: ")

    # Extract text from the PDF file
    pdf_text = extract_text_from_pdf(pdf_file_path)

    # Send the extracted text to Chat GPT for a response
    gpt_response = chat_with_gpt(pdf_text)

    # Print the response from Chat GPT
    print("Chat GPT Response:")
    print(gpt_response)

# Run the program
if __name__ == '__main__':
    main()
