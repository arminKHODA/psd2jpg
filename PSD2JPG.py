import os
from psd_tools import PSDImage
from PIL import Image

def convert_psd_to_jpg(psd_path, jpg_path):
    # Open the PSD file
    psd = PSDImage.open(psd_path)
    
    # Convert to PIL image and save as JPG
    image = psd.compose()
    image.save(jpg_path, 'JPEG')

def main():
    folder_path = input("Enter the folder path: ")
    
    if not os.path.exists(folder_path):
        print("The provided folder path does not exist.")
        return
    
    # Create the new folder named "convertPSD"
    output_folder = os.path.join(folder_path, "convertPSD")
    os.makedirs(output_folder, exist_ok=True)
    
    # Search for PSD files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.psd'):
                psd_path = os.path.join(root, file)
                jpg_path = os.path.join(output_folder, os.path.splitext(file)[0] + '.jpg')
                
                # Convert PSD to JPG and save
                convert_psd_to_jpg(psd_path, jpg_path)
                print(f"Converted {psd_path} to {jpg_path}")

if __name__ == "__main__":
    main()
