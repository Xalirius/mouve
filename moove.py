import pyautogui
import time
import threading
import tkinter as tk
from tkinter import messagebox

def ask_to_do(stop_event):
    # Demande à l'utilisateur ce qu'il veut faire 
    root = tk.Tk()
    root.title("MooveApp")
    root.geometry("300x200")
    root.resizable(False, False)
    
    label = tk.Label(root, text="L'application est en cours d'exécution.\nVoulez-vous l'arrêter ?", font=("Arial", 12))
    label.pack(pady=10)

    # Fonction pour arrêter le programme en activant l'événement de stop
    def on_stop_click():
        stop_event.set()  # Déclenche l'arrêt du mouvement
        root.destroy()  # Ferme la fenêtre principale
        # Affiche un message de confirmation

    # Bouton pour arrêter l'application
    stop_button = tk.Button(root, text="Fermer l'application", command=on_stop_click)
    stop_button.pack(pady=10)

    

    # Démarre la boucle Tkinter dans le thread principal
    root.mainloop()

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
        while not stop_event.is_set():  # Tant que l'événement n'est pas déclenché (n'est pas "True")
            # Déplacer la souris de move_distance pixels à droite
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
    stop_event = threading.Event()  # Contrôler l'arrêt du mouvement
    
    # Démarrage du thread de déplacement de la souris
    jiggle_thread = threading.Thread(target=jiggle, args=(10, 2, 5, stop_event))
    jiggle_thread.daemon = True  # Permet de fermer le programme sans attendre la fin du thread
    jiggle_thread.start()  # Lance immédiatement le thread

    # Affiche la fenêtre Tkinter pour interagir avec l'utilisateur
    ask_to_do(stop_event)

    # Attendre que le thread jiggle termine
    jiggle_thread.join()  # Ce point ne sera pas atteint tant que la fenêtre principale n'est pas fermée
    print("Fin du programme.")