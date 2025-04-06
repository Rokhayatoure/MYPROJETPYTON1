from models.utilisateur import User
from models.role import Role
from models.etudiant import Etudiant
from services.auth_service import login
from services.mongo_service import ajouter_etudiant, collection
from services.redis_service import cache_etudiant, get_cached_etudiant, r
from tabulate import tabulate

# ---------- MENU PRINCIPAL ----------

def afficher_menu():
    print("=== Connexion ===")
    telephone = input("Téléphone: ")
    mot_de_passe = input("Mot de passe: ")
    utilisateur = login(telephone, mot_de_passe)

    if not utilisateur:
        return

    role = utilisateur["role"]

    while True:
        print("\n--- Menu ---")
        # if role == Role.ADMIN.value:
            print("1. Ajouter un étudiant")
            print("2. Afficher tous les étudiants")
            print("3. Rechercher un étudiant")
            print("4. Modifier les notes d’un étudiant")
            print("5. Supprimer un étudiant")
            print("6. Trier les étudiants par moyenne")
            print("0. Quitter")

            choix = input("Choix : ")

            if choix == "1":
                ajouter_etudiant_menu()
            elif choix == "2":
                afficher_etudiants()
            elif choix == "3":
                rechercher_etudiant()
            elif choix == "4":
                modifier_notes()
            elif choix == "5":
                supprimer_etudiant()
            elif choix == "6":
                trier_par_moyenne()
            elif choix == "0":
                print("👋 Déconnexion.")
                break
            else:
                print("Choix invalide.")

        elif role == Role.ENSEIGNANT.value:
            print("1. Modifier les notes d’un étudiant")
            print("0. Quitter")

            choix = input("Choix : ")
            if choix == "1":
                modifier_notes()
            elif choix == "0":
                break

        elif role == Role.ETUDIANT.value:
            print("1. Voir mes notes")
            print("0. Quitter")

            choix = input("Choix : ")
            if choix == "1":
                consulter_mes_notes(utilisateur)
            elif choix == "0":
                break
        else:
            print("❌ Rôle inconnu.")
            break
