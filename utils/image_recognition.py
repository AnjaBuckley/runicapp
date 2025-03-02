import base64
import requests
import io
from PIL import Image


def analyze_drawing(image_data, expected_rune):
    """
    Analyze the user's drawing using an LLM with image recognition capabilities

    Args:
        image_data: The image data from the canvas
        expected_rune: The name of the expected rune

    Returns:
        tuple: (is_correct, feedback)
    """
    # In a real implementation, you would:
    # 1. Convert the canvas data to an image
    # 2. Send it to an API like OpenAI's GPT-4 Vision or Claude 3
    # 3. Process the response to determine if the drawing matches

    # This is a placeholder implementation
    # You would replace this with actual API calls to an LLM with vision capabilities

    try:
        # Convert image data to a format suitable for API submission
        # (This depends on the specific API you're using)

        # Example API call (pseudocode)
        """
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4-vision-preview",
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f"Does this drawing resemble the runic character '{expected_rune}'? Provide a yes/no answer and brief explanation."
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ]
            }
        )
        """

        # For this example, we'll just return a placeholder response
        # In a real implementation, you would parse the API response

        # Simulated response (replace with actual API integration)
        is_correct = False  # This would be determined by the API response
        feedback = "Your drawing doesn't quite match the expected rune. Try making the vertical lines straighter."

        return is_correct, feedback

    except Exception as e:
        return False, f"Error analyzing image: {str(e)}"
