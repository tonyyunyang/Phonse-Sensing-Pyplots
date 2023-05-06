import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load the audio files
west_audio, west_sr = librosa.load('West.m4a')
middle_audio, middle_sr = librosa.load('Middle.m4a')
east_audio, east_sr = librosa.load('East.m4a')

# Compute the spectrograms for each audio file
west_spec = librosa.stft(west_audio)
middle_spec = librosa.stft(middle_audio)
east_spec = librosa.stft(east_audio)

# Plot the spectrograms
plt.figure(figsize=(15, 5))
plt.subplot(131)
librosa.display.specshow(librosa.amplitude_to_db(west_spec, ref=np.max), sr=west_sr, y_axis='log', x_axis='time', fmax=20000, cmap='magma')
plt.title('West Area 2022/05/04 18:33')

plt.subplot(132)
librosa.display.specshow(librosa.amplitude_to_db(middle_spec, ref=np.max), sr=middle_sr, y_axis='log', x_axis='time', fmax=20000, cmap='magma')
plt.title('Middle Area 2022/05/04 18:32')

plt.subplot(133)
img = librosa.display.specshow(librosa.amplitude_to_db(east_spec, ref=np.max), sr=east_sr, y_axis='log', x_axis='time', fmax=20000, cmap='magma')
plt.title('East Area 2022/05/04 18:35')

# Add colorbar
plt.colorbar(img, format="%+2.0f dB")

plt.tight_layout()
plt.show()
