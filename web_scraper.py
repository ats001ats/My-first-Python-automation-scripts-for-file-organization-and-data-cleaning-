import requests
from bs4 import BeautifulSoup
import csv

def scrape_to_csv():
    print("--- Pro Web Scraper Started ---")
    
    # Hum multiple pages se data nikalne ke liye loop chalayenge (Misal ke tor par first 2 pages)
    all_quotes_data = []
    
    for page in range(1, 3):
        url = f"http://quotes.toscrape.com/page/{page}/"
        print(f"Scraping page {page}...")
        
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                quotes = soup.find_all('span', class_='text')
                authors = soup.find_all('small', class_='author')
                
                for quote, author in zip(quotes, authors):
                    all_quotes_data.append({
                        'Quote': quote.text,
                        'Author': author.text
                    })
            else:
                print(f"Page {page} load nahi ho saka!")
        except Exception as e:
            print(f"Error aaya hai: {e}")
            
    # Ab is saare data ko CSV file (Excel file) mein save karna
    filename = "quotes_pro_data.csv"
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['Quote', 'Author']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            for item in all_quotes_data:
                writer.writerow(item)
                
        print(f"\nKamyabi! {len(all_quotes_data)} quotes '{filename}' file mein save ho chuke hain.")
        print("Aap apne folder mein check kar sakte hain, wahan yeh file ban gayi hogi.")
        
    except Exception as e:
        print(f"File save karne mein error aaya: {e}")

if __name__ == "__main__":
    scrape_to_csv()