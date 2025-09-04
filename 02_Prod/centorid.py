import numpy as np
import sounddevice as sd
import time
import librosa

# Load the audio file
y, sr = librosa.load('Crystal_Sky_y1ETLWsngxw.mp3')

# Define the output buffer
buffer = np.zeros(int(sr * 0.1))

# Define the callback function
def callback(indata, frames, time, status):
    global buffer
    # Compute the spectral centroid
    D = np.abs(librosa.stft(indata)) ** 2
    freqs = librosa.core.fft_frequencies(sr=sr)
    centroid = np.dot(freqs, D) / (np.sum(D) + np.finfo(float).eps)
    # Print the centroid
    print("Centroid: ", centroid)
    # Append the new audio data to the output buffer
    buffer = np.append(buffer, indata)
    return buffer,

# Define the stream
stream = sd.InputStream(callback=callback)

# Define a function to play the audio
def play_audio():
    with stream:
        sd.sleep(len(y) // sr)

# Play the audio
play_audio()
