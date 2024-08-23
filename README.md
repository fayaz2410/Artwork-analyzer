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
   
