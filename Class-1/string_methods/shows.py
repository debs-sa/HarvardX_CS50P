SHOWS = [
    "Breaking Bad",
    "Stranger Things",
    "Game of Thrones",
    "The Office",
    "Friends",
    "The Crown",
    "Black Mirror",
    "The Mandalorian",
    "Sherlock",
    "The Simpsons"
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())
        
        print(', '.join(cleaned_shows))

main()