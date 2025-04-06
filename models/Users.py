# models/utilisateur.py

from models.role import Role
import bcrypt

class User:
    def __init__(self, id, nom, prenom, telephone, classe, notes, role: Role, mot_de_passe):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.classe = classe
        self.notes = notes or []
        self.role = role
        self.mot_de_passe = self.hash_password(mot_de_passe)

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def verifie_mot_de_passe(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.mot_de_passe.encode('utf-8'))

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "prenom": self.prenom,
            "telephone": self.telephone,
            "classe": self.classe,
            "notes": self.notes,
            "role": self.role.value,
            "mot_de_passe": self.mot_de_passe
        }



   def calculer_moyenne(self):
        if not self.notes:
            return 0
        return sum(self.notes) / len(self.notes)