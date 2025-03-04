from PIL import Image
import argparse


def process_image(input_path, output_path):
    """
    Process an image by converting it to grayscale and resizing it.

    Args:
        input_path (str): The path to the input image file.
        output_path (str): The path to save the processed image file.

    Returns:
        str: The path to the saved processed image file.
    """
    # Open the image
    image = Image.open(input_path)

    # Convert to grayscale
    grayscale_image = image.convert("L")

    # Resize to 255x122
    resized_image = grayscale_image.resize((250, 122))

    # Save the processed image
    resized_image.save(output_path)
    return output_path


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process an image.")
    parser.add_argument("input_path", help="Path to the input image")
    parser.add_argument("output_path", help="Path to save the processed image")
    args = parser.parse_args()

    # Process the image with provided arguments
    process_image(args.input_path, args.output_path)
