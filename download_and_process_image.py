import requests
from PIL import Image
from io import BytesIO


def download_and_process_image(url, output_path, size=(250, 122)):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # Resize the image
    img = img.resize(size)

    # Convert to black and white
    img = img.convert("L")

    # Save the processed image
    img.save(output_path)


# Example usage
if __name__ == "__main__":
    url = "https://alternative.me/crypto/fear-and-greed-index.png"
    output_path = "processed_fear_and_greed_index.png"
    print("HI!")
    download_and_process_image(url, output_path)
