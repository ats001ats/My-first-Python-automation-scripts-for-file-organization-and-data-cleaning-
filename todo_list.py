import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\n--- Aapki list khali hai! ---")
    else:
        print("\n--- Aapke Tasks ---")
        for index, task in enumerate(tasks, start=1):
            status = "✓ [Completed]" if task["done"] else "⏳ [Pending]"
            priority = f"[{task['priority']}]"
            print(f"{index}. {task['title']} {priority} - {status}")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- ADVANCED TO-DO LIST MENU ---")
        print("1. Task Add karein")
        print("2. Tasks Dekhein")
        print("3. Task ko Done (Mukammal) mark karein")
        print("4. Task Delete karein")
        print("5. Saare Tasks Clear karein")
        print("6. Exit (Band karein)")
        
        choice = input("Koi option chuniye (1-6): ")
        
        if choice == '1':
            title = input("Naya task likhein: ")
            print("Priority chuniye: 1. High  2. Medium  3. Low")
            p_choice = input("Option (1-3, default Medium): ")
            
            if p_choice == '1':
                priority = "High"
            elif p_choice == '3':
                priority = "Low"
            else:
                priority = "Medium"
                
            tasks.append({"title": title, "done": False, "priority": priority})
            save_tasks(tasks)
            print(f"'{title}' kamyabi se add ho gaya hai!")
            
        elif choice == '2':
            show_tasks(tasks)
            
        elif choice == '3':
            show_tasks(tasks)
            if tasks:
                try:
                    t_num = int(input("Jis task ko done karna hai uska number likhein: "))
                    if 1 <= t_num <= len(tasks):
                        tasks[t_num - 1]["done"] = True
                        save_tasks(tasks)
                        print("Task mukammal (done) ho gaya hai! 🎉")
                    else:
                        print("Ghalat number enter kiya hai!")
                except ValueError:
                    print("Barah-e-karam sirf valid number likhein!")
                    
        elif choice == '4':
            show_tasks(tasks)
            if tasks:
                try:
                    t_num = int(input("Delete karne ke liye task ka number likhein: "))
                    if 1 <= t_num <= len(tasks):
                        removed = tasks.pop(t_num - 1)
                        save_tasks(tasks)
                        print(f"'{removed['title']}' delete ho gaya hai.")
                    else:
                        print("Ghalat number enter kiya hai!")
                except ValueError:
                    print("Barah-e-karam sirf valid number likhein!")
                    
        elif choice == '5':
            confirm = input("Kya aap waqai saare tasks delete karna chahte hain? (y/n): ")
            if confirm.lower() == 'y':
                tasks.clear()
                save_tasks(tasks)
                print("Saari list clear kar di gayi hai!")
                
        elif choice == '6':
            print("Program band ho raha hai. Aapke tasks save ho chuke hain. Allah Hafiz!")
            break
        else:
            print("Ghalat option! 1 se 6 ke darmiyan koi number chuniye.")

if __name__ == "__main__":
    main()