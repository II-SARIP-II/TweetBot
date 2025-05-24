import os
import csv
from atproto import Client

# Charger les identifiants depuis les variables d’environnement ou en dur ici
HANDLE = "united-europe.bsky.social"
APP_PASSWORD = "You-can't-find-it"

# Init client
client = Client()
client.login(HANDLE, APP_PASSWORD)

# Fonction pour lire le prochain tweet à partir d’un CSV
def get_next_post_from_csv(filename="posts.csv", index_file="index.txt"):
    if os.path.exists(index_file):
        with open(index_file, "r") as f:
            try:
                index = int(f.read().strip())
            except ValueError:
                index = 0
    else:
        index = 0

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        posts = [row[0] for row in reader if row]

    if not posts:
        raise ValueError("Le fichier CSV est vide ou mal formaté.")

    post = posts[index % len(posts)]

    with open(index_file, "w") as f:
        f.write(str((index + 1) % len(posts)))

    return post

# Poster sur Bluesky
post = get_next_post_from_csv()
client.send_post(text=post)
print("Post envoyé sur Bluesky :", post)
