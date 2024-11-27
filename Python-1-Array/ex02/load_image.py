from PIL import Image
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    Charge une image depuis le chemin spécifié, affiche son format et retourne son contenu en RGB.

    Args:
        path (str): Chemin vers le fichier image.

    Returns:
        np.ndarray: Tableau NumPy représentant l'image en RGB.

    Raises:
        FileNotFoundError: Si le fichier n'est pas trouvé.
        ValueError: Si le format de l'image n'est pas supporté.
    """
    try:
        # Ouverture de l'image
        with Image.open(path) as img:
            # Vérification du format
            if img.format not in ['JPEG', 'JPG']:
                raise ValueError(f"Format d'image non supporté : {img.format}")

            # Conversion en RGB si nécessaire
            if img.mode != 'RGB':
                img = img.convert('RGB')

            # Conversion en tableau NumPy
            img_array = np.array(img)

            # Affichage des dimensions de l'image
            print(f"La forme de l'image est : {img_array.shape}")

            return img_array

    except FileNotFoundError:
        print(f"Erreur : Le fichier '{path}' est introuvable.")
    except ValueError as ve:
        print(f"Erreur : {ve}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")
