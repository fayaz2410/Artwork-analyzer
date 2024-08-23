# Image Captioning and Sentiment Analysis Web Application

This Flask web application generates captions for images and analyzes the sentiment of those captions using pre-trained models from Hugging Face. The application takes an image URL as input, generates a descriptive caption for the image, and then determines the emotional tone of the caption.

## Features

- **Image Captioning**: Generates descriptive captions for images using the BLIP model from Hugging Face.
- **Sentiment Analysis**: Analyzes the sentiment of the generated caption (Happy, Neutral, or Sad) using the CardiffNLP Twitter RoBERTa model.

## How It Works

1. **User Input**: The user provides a URL of an image.
2. **Caption Generation**: The application sends the image to the Hugging Face BLIP model API, which returns a descriptive caption.
3. **Sentiment Analysis**: The caption is analyzed using the Hugging Face sentiment analysis model, which returns the most likely emotion.

## Prerequisites

- Python 3.x
- A Hugging Face API key

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/fayaz2410/Artwork-analyzer.git
   cd Artwork-analyzer

2. **Download Pre-trained Models**

The application uses pre-trained models for image captioning and sentiment analysis, which are loaded locally. Download and save the models in the following directories:

Image Captioning Model: blip-image-captioning-large

Sentiment Analysis Model: twitter-roberta-base-sentiment

You can download these models from the Hugging Face Model Hub or another source and place them in the appropriate directories.

3. **Update Model Directories**

Modify the captioning_model_directory and sentiment_model_directory paths in app.py to point to the local directories where the models are saved.

4. **Run the Application**

Start the Flask server by running:

python app.py

The application will be accessible at http://localhost:5000 by default.

5. **Usage**
Open your web browser and go to http://localhost:5000.

Enter the URL of the image you want to analyze.

Submit the form to get a caption for the image and the sentiment of the caption.
7. **Files**
app.py: The main Flask application script.

templates/index.html: The HTML template for the web interface.

8. **Contributing**
Feel free to fork the repository, make changes, and submit pull requests. Contributions and suggestions are welcome!

**Acknowledgements**
The transformers library by Hugging Face for pre-trained models.
