import pyautogui
import time
import threading

def ask_to_stop(stop_event):
    """Demande à l'utilisateur s'il souhaite arrêter le script."""
    while not stop_event.is_set():
        response = input("Voulez-vous arrêter l'application ? (y/n) : ").strip().upper()
        if response == 'y':
            stop_event.set()

def jiggle(move_distance=10, move_interval=5, rest_interval=10, stop_event=None):
    """
    Fonction pour déplacer la souris automatiquement à intervalles réguliers.
    
    Paramètres:
    - move_distance: Distance de déplacement en pixels.
    - move_interval: Temps (en secondes) entre les mouvements.
    - rest_interval: Temps (en secondes) entre les cycles de mouvement.
    - stop_event: Un threading.Event pour arrêter le jiggle
    """
    try:
        while not stop_event.is_set():
            # Déplacer la souris de move_distance pixels à droite
            x, y = pyautogui.position()
            pyautogui.moveRel(move_distance, 0)
            time.sleep(move_interval)
            # Remettre la souris à sa position initiale
            pyautogui.moveRel(-move_distance, 0)
            time.sleep(rest_interval)
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
    finally:
        print("Jiggler arrêté.")


if __name__ == "__main__":
    stop_event = threading.Event()

    # Lancement du thread pour le jiggle
    jiggle_thread = threading.Thread(target=jiggle, args=(10, 2, 5, stop_event))
    jiggle_thread.start()

    try:
        # Saisie dans le thread principal
        while not stop_event.is_set():
            response = input("Voulez-vous arrêter l'application ? (y/n) : ").strip().lower()
            if response == 'y':
                stop_event.set()
    except KeyboardInterrupt:
        stop_event.set()
        print("\nInterruption par l'utilisateur détectée.")
    
    # Attendre que le thread jiggle termine
    jiggle_thread.join()
    print("Fin du programme.")
    
