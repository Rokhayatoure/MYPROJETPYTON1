# services/etudiant_service.py

from services.mongo_service import db
from models.utilisateur import User
from models.role import Role

etudiant_collection = db['etudiants']

# ➕ Ajouter un étudiant
def ajouter_etudiant(user: User):
    # if user.role != Role.ETUDIANT:
    #     raise ValueError("Le rôle doit être Étudiant")
    
    if etudiant_collection.find_one({'telephone': user.telephone}):
        raise ValueError("Téléphone déjà utilisé")

    doc = user.__dict__.copy()
    doc["role"] = user.role.value
    etudiant_collection.insert_one(doc)
    print("✅ Étudiant ajouté avec succès.")

# 📖 Lister tous les étudiants
def lister_etudiants():
    return list(etudiant_collection.find({"role": Role.ETUDIANT.value}))

# 🔍 Rechercher un étudiant
def rechercher_etudiant(critere: str, valeur: str):
    return list(etudiant_collection.find({critere: valeur, "role": Role.ETUDIANT.value}))

# ✏️ Modifier les notes
def modifier_notes(telephone, nouvelles_notes):
    if any(note < 0 or note > 20 for note in nouvelles_notes):
        raise ValueError("Les notes doivent être entre 0 et 20")

    result = etudiant_collection.update_one(
        {"telephone": telephone, "role": Role.ETUDIANT.value},
        {"$set": {"notes": nouvelles_notes}}
    )

    if result.matched_count:
        print("✅ Notes modifiées.")
    else:
        print("❌ Étudiant non trouvé.")

# ❌ Supprimer un étudiant
def supprimer_etudiant(telephone):
    result = etudiant_collection.delete_one({"telephone": telephone, "role": Role.ETUDIANT.value})
    if result.deleted_count:
        print("🗑️ Étudiant supprimé.")
    else:
        print("❌ Aucun étudiant trouvé.")
