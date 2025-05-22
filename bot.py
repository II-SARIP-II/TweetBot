import tweepy
import csv
import random
import os

api_key = os.getenv("NfRvEqpn6nB7BbAVawZ7r7eBa")
api_secret = os.getenv("ol0gueUCp5F4FvOI2IuQQQQZufQCyxBHKjI9yaJ1HzPEd2sZxI")
access_token = os.getenv("1925570142198452224-I6Px9mavIco11kB9XMeeafzEglgdJh")
access_token_secret = os.getenv("Y8dYl6HZ6RTntMjcrs40AoLhvKU8Ey8cDaafMalPO4coh")

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Chargement des tweets depuis le CSV
def get_next_tweet_from_csv(filename="tweets.csv", index_file="index.txt"):
    # Lecture de l'index courant
    if os.path.exists(index_file):
        with open(index_file, "r") as f:
            try:
                index = int(f.read().strip())
            except ValueError:
                index = 0
    else:
        index = 0

    # Lecture des tweets dans le CSV
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        tweets = [row[0] for row in reader if row]

    if not tweets:
        raise ValueError("Le fichier CSV est vide ou mal formaté.")

    # Récupérer le tweet à l'index courant (modulo pour boucle)
    tweet = tweets[index % len(tweets)]

    # Mettre à jour l'index pour la prochaine exécution
    with open(index_file, "w") as f:
        f.write(str((index + 1) % len(tweets)))

    return tweet

# Poster le tweet
tweet = get_next_tweet_from_csv()
api.update_status(tweet)
print("Tweet envoyé :", tweet)