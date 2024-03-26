import os
import shutil

def organize_downloads():
    # Define paths
    downloads_path = os.path.expanduser('~/Downloads')
    documents_path = os.path.join(downloads_path, 'Documents')
    images_path = os.path.join(downloads_path, 'Images')
    videos_path = os.path.join(downloads_path, 'Videos')
    executables_path = os.path.join(downloads_path, 'Executables')

    # Create directories if not exists
    for folder in [documents_path, images_path, videos_path, executables_path]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # List files in Downloads folder
    files = os.listdir(downloads_path)

    # Organize files
    for file in files:
        file_path = os.path.join(downloads_path, file)
        if os.path.isfile(file_path):
            # Check file type and move to corresponding folder
            if file.endswith(('.pdf', '.doc', '.docx', '.txt')):
                shutil.move(file_path, documents_path)
                print(f"Moved {file} to Documents folder.")
            elif file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                shutil.move(file_path, images_path)
                print(f"Moved {file} to Images folder.")
            elif file.endswith(('.mp4', '.mov', '.avi', '.mkv')):
                shutil.move(file_path, videos_path)
                print(f"Moved {file} to Videos folder.")
            elif file.endswith(('.exe', '.deb')):
                shutil.move(file_path, executables_path)
                print(f"Moved {file} to Executables folder.")

if __name__ == "__main__":
    organize_downloads()
