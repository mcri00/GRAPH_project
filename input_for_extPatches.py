import cv2
import os

input_dir = "../BreaKHis_v1/BreaKHis_v1/histology_slides/breast"  # path to dataset (input directory)
output_dir = "./resized_images"  # path to output directory
target_size = (270, 270)  # Dimension required for patches extraction

# Creation of the output directory (no errors if it already exists)
os.makedirs(output_dir, exist_ok=True)

# Traverse the directory tree
for root, dirs, files in os.walk(input_dir):
    for file in files:
        # Filter only files with supported extensions
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            # Create the full path and add to the list
            img_path = os.path.join(root, file)
            img = cv2.imread(img_path)

            # Resize the image
            resized_img = cv2.resize(img, target_size)

            # Save the preprocessed image in the output directory
            output_path = os.path.join(output_dir, file)
            cv2.imwrite(output_path, resized_img)        



print("Preprocessing DONE")


# list all files in the directory and count them
images = [im for im in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, im))]

# print the number of files
print(f"The number of resized images is: {len(images)}")

