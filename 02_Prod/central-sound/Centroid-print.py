import librosa
import numpy as np
import socket

# Charger le fichier audio
audio_path = 'Crystal_Sky_y1ETLWsngxw.mp3'
y, sr = librosa.load(audio_path)

# Calculer le spectre de puissance
D = np.abs(librosa.stft(y))**2

# Convertir en décibels
D_db = librosa.power_to_db(D, ref=np.max)

# Initialiser le centroid spectral
centroid = librosa.feature.spectral_centroid(S=D)[0]

# Créer un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Adresse IP et port pour l'envoi de données
UDP_IP = "127.0.0.1"
UDP_PORT = 8000

# Afficher le spectrogramme et le centroid spectral en direct dans la console
for i, value in enumerate(centroid):
    print(f"Frame {i + 1}, Spectral Centroid: {value}")
     
    # Convertir la valeur du centroid spectral en chaîne de caractères
    message = str(value).encode('utf-8')
    
    # Envoyer la valeur du centroid spectral via UDP
    sock.sendto(message, (UDP_IP, UDP_PORT))
