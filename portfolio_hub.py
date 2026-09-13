import os

def show_banner():
    print("=" * 45)
    print("    WELCOME TO MY PYTHON PORTFOLIO HUB    ")
    print("=" * 45)
    print(" Developer: Python Automation & Tools Expert")
    print("-" * 45)

def main():
    while True:
        show_banner()
        print("1. Secure Password Generator & Checker")
        print("2. Advanced To-Do List Manager")
        print("3. Pro Web Scraper (CSV Data Extractor)")
        print("4. Exit Hub")
        
        choice = input("\nKonsa project run karna chahte hain? (1-4): ")
        
        if choice == '1':
            print("\n--- Running Password Generator ---")
            os.system("python password_generator.py")
            input("\nWapis menu par jane ke liye Enter dabayein...")
            
        elif choice == '2':
            print("\n--- Running To-Do List ---")
            os.system("python todo_list.py")
            input("\nWapis menu par jane ke liye Enter dabayein...")
            
        elif choice == '3':
            print("\n--- Running Web Scraper ---")
            os.system("python web_scraper.py")
            input("\nWapis menu par jane ke liye Enter dabayein...")
            
        elif choice == '4':
            print("\nPortfolio Hub band ho raha hai. Allah Hafiz!")
            break
        else:
            print("\nGhalat option! Barah-e-karam 1 se 4 ke darmiyan number chuniye.\n")

if __name__ == "__main__":
    main()