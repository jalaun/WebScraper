from bs4 import BeautifulSoup
import requests
import tkinter as tk

def scrape_quotes():
    #request target website
    page_to_scrape = requests.get("http://quotes.toscrape.com")
    #parse html and store it as a variable
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    #use inspect element to find the class and author
    quotes = soup.findAll("span", attrs={"class": "text"})
    authors = soup.findAll("small", attrs={"class": "author"})

    for quote, author in zip(quotes, authors):
        text_box.insert(tk.END, quote.text + "- " + author.text + "\n")
        print(quote.text + "- " + author.text)


root=tk.Tk()
root.title("quote scraper")

text_box = tk.Text(root,height=20,width=80)
text_box.pack()

scrape_quotes()

root.mainloop()