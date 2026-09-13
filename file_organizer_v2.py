import os
import shutil

print("================================")
print("     SMART FILE ORGANIZER")
print("================================")

target_dir = input("Folder ka path likho: ").strip()

if not os.path.exists(target_dir):
    print("Error: Folder nahi mila!")
else:
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Audios": [".mp3", ".wav", ".aac"]
    }

    moved_count = 0

    for file in os.listdir(target_dir):

        file_path = os.path.join(target_dir, file)

        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(file)[1].lower()

        category = "Others"

        for category_name, extensions in categories.items():
            if file_ext in extensions:
                category = category_name
                break

        category_dir = os.path.join(target_dir, category)

        if not os.path.exists(category_dir):
            os.makedirs(category_dir)

        destination = os.path.join(category_dir, file)

        shutil.move(file_path, destination)

        print(f"Moved: {file} -> {category}")

        moved_count += 1

    print()
    print("================================")
    print("Task Complete!")
    print(f"Total files moved: {moved_count}")
    print("================================")