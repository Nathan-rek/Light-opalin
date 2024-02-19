import numpy as np
import librosa
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Charger le fichier audio
audio_path = 'Crystal_Sky_y1ETLWsngxw.mp3'
y, sr = librosa.load(audio_path)

# Calculer le spectre de puissance
D = np.abs(librosa.stft(y))**2

# Convertir en décibels
D_db = librosa.power_to_db(D, ref=np.max)

# Créer un graphique
fig, ax = plt.subplots(figsize=(10, 4))

# Afficher le spectrogramme
img = librosa.display.specshow(D_db, y_axis='log', x_axis='time', sr=sr, ax=ax)
ax.set_title('Spectrogramme')

# Tracer le centroid spectral
line, = ax.plot([], [], label='Centroid Spectral')
ax.legend()

def update(frame):
    # Calculer le centroid spectral pour le prochain segment d'échantillons audio
    start = int(frame * sr / 10)
    end = int((frame + 1) * sr / 10)
    centroid = librosa.feature.spectral_centroid(y=y[start:end], sr=sr)[0]

    # Mettre à jour les données de la ligne
    line.set_ydata(centroid)
    line.set_xdata(range(len(centroid)))
    return line,


# Créer l'animation
ani = FuncAnimation(fig, update, frames=int(len(y) / (sr / 10)), interval=100)

# Afficher l'animation
plt.show()
