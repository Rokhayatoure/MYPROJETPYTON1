# models/role.py

from enum import Enum

class Role(Enum):
    ETUDIANT = "Etudiant"
    ENSEIGNANT = "Enseignant"
    ADMIN = "Admin"
