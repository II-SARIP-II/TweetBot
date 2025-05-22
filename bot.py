import tweepy
import csv
import random
import os

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_SECRET")

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