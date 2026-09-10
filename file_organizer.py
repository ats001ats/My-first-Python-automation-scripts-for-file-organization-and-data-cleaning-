import os
import shutil

# Yahan apne test folder ka path do (backslash ki jagah forward slash / use karna)
target_dir = "J:/Test_Downloads/"

# Agar folder nahi milta toh error se bachne ke liye check
if not os.path.exists(target_dir):
    print("Folder nahi mila! Path check karo.")
else:
    # Folder ke andar ki sari files ki list lo
    files = os.listdir(target_dir)
    
    for file in files:
        # File ka full path banate hain
        file_path = os.path.join(target_dir, file)
        
        # Agar yeh folder hai toh isko chhor do (sirf files par kaam karna hai)
        if os.path.isdir(file_path):
            continue
            
        # File ka extension (jaise .jpg, .pdf) alag karte hain aur chote letters mein convert karte hain
        file_ext = os.path.splitext(file)[1].lower()
        
        # Categories ke hisaab se folder ka naam decide karna
        if file_ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
            category = "Images"
        elif file_ext in ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx']:
            category = "Documents"
        elif file_ext in ['.mp4', '.mkv', '.avi', '.mov']:
            category = "Videos"
        elif file_ext in ['.mp3', '.wav', '.aac']:
            category = "Audios"
        else:
            category = "Others"
            
        # Category wala folder ka rasta
        category_dir = os.path.join(target_dir, category)
        
        # Agar category folder pehle se nahi hai toh usko bana do
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
            
        # File ko uske category folder mein move kar do
        shutil.move(file_path, os.path.join(category_dir, file))
        print(f"Moved: {file} ---> {category}")

    print("Task Complete! Sab files organize ho gayi hain.")