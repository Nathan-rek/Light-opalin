import librosa
import numpy as np

# Charger le fichier audio
audio_path = 'Crystal_Sky_y1ETLWsngxw.mp3'
y, sr = librosa.load(audio_path)

# Calculer le spectre de puissance
D = np.abs(librosa.stft(y))**2

# Convertir en décibels
D_db = librosa.power_to_db(D, ref=np.max)

# Initialiser le centroid spectral
centroid = librosa.feature.spectral_centroid(S=D)[0]

# Afficher le spectrogramme et le centroid spectral en direct dans la console
for i, value in enumerate(centroid):
    print(f"Frame {i + 1}, Spectral Centroid: {value}")

# Vous pouvez également utiliser la bibliothèque matplotlib pour afficher le spectrogramme et le centroid spectral si nécessaire
