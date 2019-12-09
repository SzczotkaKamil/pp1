class book():
    def __init__(self,author,title,pages):
        self.author=author
        self.title=title
        self.pages=pages
        self.current_page=0
        self.is_open=False
    def show_status(self):
        print(f"Author:{self.author}")
        print(f"Title: {self.title}")
        print(f"Number of pages: {self.pages}")
        print(f"You're on the page number: {self.current_page}")
        print()
    def read(self):
        if self.is_open:
            if self.current_page<self.pages:
                self.current_page+=1
        else:
            print("The book is closed, open it to start reading.")
    def open_book(self):
        self.is_open=True
    def close_book(self):
        self.is_open=False          
            
x = book('Stephen King','It',352)
x.show_status()
x.read()
x.open_book()
x.read()
x.show_status()
x.close_book()
x.read()