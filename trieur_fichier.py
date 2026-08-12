import os
import shutil


def trier_fichiers(dossier):

    if not os.path.isdir(dossier):
        print("Ce dossier n'existe pas.")
        return

    for fichier in os.listdir(dossier):

        chemin_fichier = os.path.join(dossier, fichier)

        if os.path.isfile(chemin_fichier):

            extension = os.path.splitext(fichier)[1].lower()

            if extension == "":
                nom_dossier = "Sans_extension"
            else:
                nom_dossier = extension[1:]

            dossier_destination = os.path.join(dossier, nom_dossier)

            os.makedirs(dossier_destination, exist_ok=True)

            shutil.move(
                chemin_fichier,
                os.path.join(dossier_destination, fichier)
            )

    print("Tri terminé !")


# Lancez la fonction trier_fichiers avec le dossier à trier ! 