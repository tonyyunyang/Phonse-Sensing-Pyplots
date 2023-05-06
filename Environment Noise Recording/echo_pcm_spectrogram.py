# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal

# # Load the audio data from the .pcm file
# data = np.fromfile('Echo_Testings/20230506_195818.pcm', dtype=np.int16)

# # Define the sampling rate (in Hz)
# fs = 44100

# # Use the signal module from scipy to compute the spectrogram
# frequencies, times, spectrogram = signal.spectrogram(data, fs)

# # Plot the spectrogram
# plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram), cmap='magma')
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Load the audio data from the .pcm file
data = np.fromfile('Echo_Testings/20230506_195818.pcm', dtype=np.int16)

# Define the sampling rate (in Hz)
fs = 44100

# Use the signal module from scipy to compute the spectrogram
frequencies, times, spectrogram = signal.spectrogram(data, fs)

# Plot the spectrogram
plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram), cmap='plasma')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')

# Customize the color bar
cb = plt.colorbar()
cb.ax.set_ylabel('Power Spectral Density [dB]')
cb.ax.set_ylim([-90, 45])

# Add a title
plt.title('Spectrogram of Audio Signal')

# Show the plot
plt.show()