import redis

# Remplace <WSL_IP> par l’IP trouvée (ex: 172.21.176.1)
r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

# Test de connexion
print(r.ping())  # Doit afficher True

# Ajouter une clé
r.set('nom', 'Rokhaya')
print(r.get('nom'))  # Doit afficher "Rokhaya"
