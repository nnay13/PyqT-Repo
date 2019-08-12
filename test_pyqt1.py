import sys
import requests

# Commentaire
print(sys.version_info)
r = requests.get("https://www.google.fr")
print(r.status_code)
