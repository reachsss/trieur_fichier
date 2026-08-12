from trieur_fichier import trier_fichiers

def main():
    dossier = input(" Quel dossier voulez-vous ré-organiser ? ")

    trier_fichiers(dossier)

    print(f"Le dossier {dossier} a été ré-organisé avec succès !")


if __name__ == "__main__":
    main()
