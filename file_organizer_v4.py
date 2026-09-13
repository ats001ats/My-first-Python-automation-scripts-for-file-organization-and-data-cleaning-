import os
import shutil

print("================================")
print("     SMART FILE ORGANIZER V4")
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

    counts = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Audios": 0,
        "Others": 0
    }

    total = 0

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

        if os.path.exists(destination):

            name, extension = os.path.splitext(file)

            counter = 1

            while os.path.exists(destination):

                new_name = f"{name}_{counter}{extension}"

                destination = os.path.join(
                    category_dir,
                    new_name
                )

                counter += 1

        shutil.move(file_path, destination)

        print(f"Moved: {file} -> {category}")

        counts[category] += 1
        total += 1

    print()
    print("================================")
    print("          SUMMARY")
    print("================================")

    print(f"Images:      {counts['Images']}")
    print(f"Documents:   {counts['Documents']}")
    print(f"Videos:      {counts['Videos']}")
    print(f"Audios:      {counts['Audios']}")
    print(f"Others:      {counts['Others']}")

    print("--------------------------------")
    print(f"Total files: {total}")
    print("================================")
    print("Task Complete!")