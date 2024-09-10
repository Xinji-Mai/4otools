import base64
from open_chat.api.gpt4o import GPT4oClient

# Initialize GPT-4o client with your API key
api_key = "your_api_key_here"  # Replace with your actual API key
openai_client = GPT4oClient(api_key=api_key, qpm=60)

def encode_image(image_path):
    """Encode image from the given path to base64."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def generate_prompt(text_list, image_list):
    """Generate a prompt for GPT-4o using text and image inputs."""
    prompt = []

    # Add all text inputs to the prompt
    for text in text_list:
        prompt.append({"type": "text", "text": text})

    # Add all image inputs to the prompt (encoded as base64)
    for image_path in image_list:
        image_base64 = encode_image(image_path)
        prompt.append({"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}})

    return prompt

def send_to_gpt4o(text_list, image_list):
    """Send prompt to GPT-4o and get the response."""
    prompt = generate_prompt(text_list, image_list)
    response = openai_client.get_res([{"role": "user", "content": prompt}])

    return response if response else 'GPT-4o failed'

if __name__ == '__main__':
    # Example input: text and image paths
    texts = ["Describe this product", "What is the main feature?"]
    images = ["path/to/image1.jpg", "path/to/image2.jpg"]

    result = send_to_gpt4o(texts, images)
    print(result)
