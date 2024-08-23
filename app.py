from flask import Flask, render_template, request  # Import necessary modules from Flask
import requests  # Import requests to handle HTTP requests
from PIL import Image  # Import PIL to handle image processing
import io  # Import io to handle in-memory byte streams
import json  # Import json to parse JSON responses

app = Flask(__name__)  # Initialize the Flask application

# Define the Hugging Face API keys and endpoints
captioning_api_url = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
sentiment_api_url = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
headers = {"Authorization": "Bearer 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"}  # Replace with your actual Hugging Face API key

def generate_caption(image_url):
    """
    Function to generate a caption for the provided image URL.
    It downloads the image, sends it to the Hugging Face API, and returns the generated caption.
    """
    # Download the image from the URL
    response = requests.get(image_url)
    image = Image.open(io.BytesIO(response.content))  # Open the image using PIL
    
    # Save the image to a temporary file
    image_filename = "temp_image.jpg"
    image.save(image_filename)
    
    # Send the image to the Hugging Face API for captioning
    with open(image_filename, "rb") as f:
        image_data = f.read()
    response = requests.post(captioning_api_url, headers=headers, data=image_data)
    
    # Parse the JSON response to get the caption
    caption_data = response.json()
    caption = caption_data[0]['generated_text']  # Extract the generated caption from the response
    return caption

def analyze_sentiment(caption):
    """
    Function to analyze the sentiment of the provided caption.
    It sends the caption to the Hugging Face API and returns the highest scoring sentiment label.
    """
    # Prepare the payload with the caption to be analyzed
    payload = {
        "inputs": caption
    }
    
    # Send the caption to the sentiment analysis API
    response = requests.post(sentiment_api_url, headers=headers, json=payload)
    
    # Parse the JSON response to get the sentiment data
    sentiment_data = response.json()
    
    # Extract the list of sentiment predictions (this should be a list of dictionaries)
    sentiment_list = sentiment_data[0]
    
    # Sort sentiment labels by their score in descending order
    sentiment_list = sorted(sentiment_list, key=lambda d: d['score'], reverse=True)
    
    # Get the highest scoring sentiment
    top_sentiment = sentiment_list[0]
    
    # Map the sentiment label to a human-readable format
    label_mapping = {
        'LABEL_0': 'Sad',
        'LABEL_1': 'Neutral',
        'LABEL_2': 'Happy'
    }
    
    # Return the corresponding sentiment label
    sentiment = label_mapping[top_sentiment['label']]
    return sentiment

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Main route to handle both GET and POST requests.
    Renders the form for input on GET and processes the image URL on POST.
    """
    description = None  # Initialize the description variable
    emotion = None  # Initialize the emotion variable
    image_url = None  # Initialize the image URL variable
    
    if request.method == "POST":  # Check if the request method is POST
        image_url = request.form["image_url"]  # Get the image URL from the form
        description = generate_caption(image_url)  # Generate a caption for the image
        emotion = analyze_sentiment(description)  # Analyze the sentiment of the generated caption
    
    # Render the index.html template with the generated description, emotion, and image URL
    return render_template("index.html", description=description, emotion=emotion, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask application in debug mode
