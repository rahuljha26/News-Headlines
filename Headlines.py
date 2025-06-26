from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

def scrape_headlines():
    try:
# 1. Fetch HTML using requests
        url = "https://www.bbc.com/news"
        response = requests.get(url)
        if response.status_code != 200:
            messagebox.showerror("Error", "Failed to fetch news.")
            return

# 2. Parse <h2> tags using BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.find_all('h2')
        titles = [tag.get_text(strip=True) for tag in headlines if tag.get_text(strip=True)]

        if not titles:
            messagebox.showinfo("Info", "No headlines found.")
            return

# 3. Save to (news_headlines.txt) file
        with open("news_headlines.txt", "w", encoding="utf-8") as file:
            for i, title in enumerate(titles, start=1):
                file.write(f"{i}. {title}\n")

        # 4. Showing in Tkinter Text box
        textbox.delete("1.0", tk.END)
        for i, title in enumerate(titles, start=1):
            textbox.insert(tk.END, f"{i}. {title}\n")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n")


win = tk.Tk()
win.title("News Headlines Scraper")
win.geometry("600x500")

titlelabel = tk.Label(win, text="Top News Headlines", font=("Arial", 16, "bold"))
titlelabel.pack(pady=10)

button = tk.Button(win, text="Scrape Headlines", command=scrape_headlines, bg="navy", fg="white", font=("Arial", 12))
button.pack(pady=5)

textbox = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=70, height=20, font=("Arial", 10))
textbox.pack(padx=10, pady=10)

win.mainloop()
