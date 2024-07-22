import pyautogui
import time

def jiggle(move_distance=10, move_interval=5, rest_interval=10):
    """
    Fonction pour déplacer la souris automatiquement à intervalles réguliers.
    
    Paramètres:
    - move_distance: Distance de déplacement en pixels.
    - move_interval: Temps (en secondes) entre les mouvements.
    - rest_interval: Temps (en secondes) entre les cycles de mouvement.
    """
    try:
        while True:
            # Déplacer la souris de move_distance pixels à droite
            pyautogui.moveRel(move_distance, 0)
            # Attendre move_interval secondes
            time.sleep(move_interval)
            # Remettre la souris à sa position initiale
            pyautogui.moveRel(-move_distance, 0)
            # Attendre rest_interval secondes
            time.sleep(rest_interval)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    # Appel de la fonction avec des valeurs par défaut
    jiggle()
