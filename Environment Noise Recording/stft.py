import numpy as np
import matplotlib.pyplot as plt

# Load the .pcm audio file into an array (replace 'audio.pcm' with your file path)
audio_data = np.fromfile('Test/20230518_152109.pcm', dtype=np.int16)

# Define window size and overlap
window_size = 256
overlap = 128

# Apply Hann window to each frame of the audio data
window = np.hanning(window_size)
num_frames = len(audio_data) // overlap - 1
frames = np.lib.stride_tricks.sliding_window_view(audio_data, window_size, overlap)

windowed_frames = frames * window

# Compute STFT
frequencies, times, spectrogram = np.stft(windowed_frames, window='hann', nperseg=window_size, noverlap=overlap)

# Convert complex spectrogram to magnitude spectrogram
magnitude_spectrogram = np.abs(spectrogram)

# Visualize the spectrogram
plt.imshow(magnitude_spectrogram, aspect='auto', origin='lower')
plt.colorbar()
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Spectrogram')
plt.show()
