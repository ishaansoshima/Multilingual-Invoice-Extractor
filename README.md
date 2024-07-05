# Multilingual-Invoice-Extractor 

This Streamlit application uses the Google Generative AI model, Gemini Pro Vision, to extract information from invoice images and provide responses based on user prompts.

## Features

- Upload an invoice image (JPG, JPEG, PNG)
- Enter a prompt related to the invoice
- Get a response based on the uploaded invoice and the entered prompt

## How to Use

1. Clone the repository
2. Install the required packages using `pip install -r requirements.txt`
3. Set up your Google API key as an environment variable
4. Run the application using `streamlit run app.py`
5. Upload an invoice image using the file uploader
6. Enter a prompt related to the invoice in the text area
7. Click the "Tell me about the invoice" button to get a response

## Example Prompts

- What is the total amount of the invoice?
- Who is the invoice from?
- What is the due date of the invoice?

## Notes

- The application will display an error if no image is uploaded
- The response will be blocked if it is deemed unsafe
- The application uses the PIL library to display the uploaded image

## Dependencies

- streamlit
- google-generativeai
- PIL
- dotenv

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author

[Your Name](your-email@example.com)

## Acknowledgments

- Thanks to Google for providing the Gemini Pro Vision model
- Thanks to Streamlit for making it easy to create ML applications
