import os

def bulk_rename(folder_path, new_name):
    try:
        files = os.listdir(folder_path)
        count = 1
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                extension = os.path.splitext(file)[1]
                new_file_name = f"{new_name}_{count}{extension}"
                new_file_path = os.path.join(folder_path, new_file_name)
                os.rename(file_path, new_file_path)
                count += 1
        print("All files renamed successfully.")
    except Exception as e:
        print("Error:", e)

# 🧪 Example Usage
folder = input("Enter folder path: ")
new_name = input("Enter new base file name: ")
bulk_rename(folder, new_name)
