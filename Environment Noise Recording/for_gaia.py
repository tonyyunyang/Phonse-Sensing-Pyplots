import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# Load audio file
audio_file = "Outdoor(Gaia).m4a"
y, sr = librosa.load(audio_file)

# Compute Short-Time Fourier Transform (STFT)
stft = librosa.stft(y)

# Convert power spectrogram to dB
log_stft = librosa.amplitude_to_db(abs(stft))

# Get the frequency axis in Hz
freqs = librosa.fft_frequencies(sr=sr, n_fft=len(stft))

# Visualize spectrogram
librosa.display.specshow(log_stft, x_axis='time', y_axis='linear', sr=sr, cmap='magma')
plt.colorbar(format='%+2.0f dB')
plt.title('Indoor')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')


# # Plot the spectrograms
# plt.figure(figsize=(15, 10))

# # First row
# plt.subplot(321)
# librosa.display.specshow(log_stft, sr=sr, cmap='rainbow')

# plt.subplot(322)
# librosa.display.specshow(log_stft, sr=sr, cmap='viridis')

# # Second row
# plt.subplot(323)
# librosa.display.specshow(log_stft, sr=sr, cmap='plasma')

# plt.subplot(324)
# librosa.display.specshow(log_stft, sr=sr, cmap='magma')

# # Third row
# plt.subplot(325)
# librosa.display.specshow(log_stft, sr=sr, cmap='inferno')

# plt.subplot(326)
# librosa.display.specshow(log_stft, sr=sr, cmap='cividis')

# plt.tight_layout()



plt.show()
