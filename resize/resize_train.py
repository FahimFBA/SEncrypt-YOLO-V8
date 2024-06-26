# Resize the train dataset's images

def resize_train(input, output, target_width, target_height):

    from PIL import Image
    import os

    input_folder_path = input
    output_folder_path = output
    target_size = (target_width, target_height) # Target resolution

    os.makedirs(output_folder_path, exist_ok=True)

    for filename in os.listdir(input_folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')): # files with .jpg, .jpeg, .png extensions
            input_image_path = os.path.join(input_folder_path, filename)
            output_image_path = os.path.join(output_folder_path, filename)

            # Open and resize the image using Lanczos resampling
            with Image.open(input_image_path) as img:
                resized_img = img.resize(target_size, Image.LANCZOS)

                resized_img.save(output_image_path)

    print("Train dataset resizing has been completed.")