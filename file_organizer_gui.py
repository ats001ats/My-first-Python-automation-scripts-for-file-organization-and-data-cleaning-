import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


# -----------------------------
# FILE CATEGORIES
# -----------------------------

categories = {
    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".webp",
        ".bmp", ".svg", ".ico", ".tiff"
    ],

    "Documents": [
        ".pdf", ".docx", ".doc", ".txt",
        ".xlsx", ".xls", ".pptx", ".ppt",
        ".csv", ".json", ".xml"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv", ".webm", ".m4v"
    ],

    "Audios": [
        ".mp3", ".wav", ".aac", ".flac",
        ".ogg", ".m4a", ".wma"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar",
        ".gz", ".bz2"
    ],

    "Programs": [
        ".exe", ".msi", ".apk", ".bat",
        ".cmd", ".py"
    ],

    "Web": [
        ".html", ".htm", ".css", ".js",
        ".php"
    ]
}


# -----------------------------
# BROWSE FOLDER
# -----------------------------

def browse_folder():
    selected_folder = filedialog.askdirectory()

    if selected_folder:
        folder_path.set(selected_folder)
        status_label.config(
            text="Folder selected. Ready to organize."
        )


# -----------------------------
# ORGANIZE FILES
# -----------------------------

def organize_files():

    target_dir = folder_path.get()

    if not target_dir:
        messagebox.showwarning(
            "Folder Missing",
            "Please select a folder first."
        )
        return

    if not os.path.isdir(target_dir):
        messagebox.showerror(
            "Invalid Folder",
            "Selected folder does not exist."
        )
        return

    # Get files only
    files = []

    for file in os.listdir(target_dir):

        file_path = os.path.join(target_dir, file)

        if os.path.isfile(file_path):
            files.append(file)

    total_files = len(files)

    if total_files == 0:
        messagebox.showinfo(
            "No Files",
            "There are no files to organize."
        )
        return

    # Counters
    counts = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Audios": 0,
        "Archives": 0,
        "Programs": 0,
        "Web": 0,
        "Others": 0
    }

    progress_bar["value"] = 0
    progress_bar["maximum"] = total_files

    status_label.config(
        text="Organizing files..."
    )

    window.update_idletasks()

    try:

        for index, file in enumerate(files, start=1):

            file_path = os.path.join(target_dir, file)

            extension = os.path.splitext(file)[1].lower()

            category = "Others"

            # Find category
            for category_name, extensions in categories.items():

                if extension in extensions:
                    category = category_name
                    break

            # Create category folder
            category_dir = os.path.join(
                target_dir,
                category
            )

            os.makedirs(
                category_dir,
                exist_ok=True
            )

            # Destination
            destination = os.path.join(
                category_dir,
                file
            )

            # Duplicate protection
            if os.path.exists(destination):

                name, extension = os.path.splitext(file)

                counter = 1

                while os.path.exists(destination):

                    new_name = (
                        f"{name}_{counter}{extension}"
                    )

                    destination = os.path.join(
                        category_dir,
                        new_name
                    )

                    counter += 1

            # Move file
            shutil.move(
                file_path,
                destination
            )

            counts[category] += 1

            # Update progress
            progress = (
                index / total_files
            ) * 100

            progress_bar["value"] = index

            progress_label.config(
                text=f"{int(progress)}%"
            )

            status_label.config(
                text=f"Organizing: {file}"
            )

            window.update_idletasks()

        # Result
        result_text = (
            f"Images:      {counts['Images']}\n"
            f"Documents:   {counts['Documents']}\n"
            f"Videos:      {counts['Videos']}\n"
            f"Audios:      {counts['Audios']}\n"
            f"Archives:    {counts['Archives']}\n"
            f"Programs:    {counts['Programs']}\n"
            f"Web:         {counts['Web']}\n"
            f"Others:      {counts['Others']}\n"
            f"\nTotal files: {total_files}"
        )

        result_label.config(
            text=result_text
        )

        status_label.config(
            text="✓ Organization completed successfully!"
        )

        progress_bar["value"] = total_files
        progress_label.config(text="100%")

        messagebox.showinfo(
            "Complete",
            f"{total_files} files organized successfully!"
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"Something went wrong:\n{error}"
        )

        status_label.config(
            text="Error occurred."
        )


# -----------------------------
# MAIN WINDOW
# -----------------------------

window = tk.Tk()

window.title(
    "Smart File Organizer"
)

window.geometry(
    "650x700"
)

window.resizable(
    False,
    False
)


# -----------------------------
# TITLE
# -----------------------------

title = tk.Label(
    window,
    text="SMART FILE ORGANIZER",
    font=("Arial", 24, "bold")
)

title.pack(pady=(25, 5))


subtitle = tk.Label(
    window,
    text="Organize your files automatically",
    font=("Arial", 11)
)

subtitle.pack(
    pady=(0, 25)
)


# -----------------------------
# FOLDER SECTION
# -----------------------------

folder_frame = tk.Frame(
    window
)

folder_frame.pack(
    padx=40,
    fill="x"
)


folder_label = tk.Label(
    folder_frame,
    text="Select Folder:",
    font=("Arial", 11, "bold")
)

folder_label.pack(
    anchor="w"
)


folder_path = tk.StringVar()


folder_entry = tk.Entry(
    folder_frame,
    textvariable=folder_path,
    font=("Arial", 10)
)

folder_entry.pack(
    side="left",
    fill="x",
    expand=True,
    pady=10
)


browse_button = tk.Button(
    folder_frame,
    text="Browse",
    command=browse_folder,
    width=12
)

browse_button.pack(
    side="right",
    padx=(10, 0),
    pady=10
)


# -----------------------------
# ORGANIZE BUTTON
# -----------------------------

organize_button = tk.Button(
    window,
    text="ORGANIZE FILES",
    command=organize_files,
    font=("Arial", 12, "bold"),
    width=25,
    height=2
)

organize_button.pack(
    pady=20
)


# -----------------------------
# PROGRESS
# -----------------------------

progress_title = tk.Label(
    window,
    text="PROGRESS",
    font=("Arial", 13, "bold")
)

progress_title.pack(
    pady=(5, 8)
)


progress_bar = ttk.Progressbar(
    window,
    orient="horizontal",
    length=500,
    mode="determinate"
)

progress_bar.pack()


progress_label = tk.Label(
    window,
    text="0%",
    font=("Arial", 11, "bold")
)

progress_label.pack(
    pady=5
)


status_label = tk.Label(
    window,
    text="Select a folder to get started.",
    font=("Arial", 10)
)

status_label.pack(
    pady=5
)


# -----------------------------
# RESULT
# -----------------------------

result_title = tk.Label(
    window,
    text="RESULT",
    font=("Arial", 14, "bold")
)

result_title.pack(
    pady=(20, 8)
)


result_label = tk.Label(
    window,
    text="No files organized yet.",
    font=("Arial", 11),
    justify="left"
)

result_label.pack()


# -----------------------------
# START APPLICATION
# -----------------------------

window.mainloop()