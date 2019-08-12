import requests

# Commentaire
r = requests.get("https://www.google.fr")
print(r.status_code)
print(r.ok)
