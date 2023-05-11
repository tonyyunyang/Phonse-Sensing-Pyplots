# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal

# # Load the audio data from the .pcm file
# data = np.fromfile('Chirp_Echo_Testing/Final/20230510_172336.pcm', dtype=np.int16)

# # Define the sampling rate (in Hz)
# fs = 44100

# # Use the signal module from scipy to compute the spectrogram
# frequencies, times, spectrogram = signal.spectrogram(data, fs)

# # Cap the frequency at 10 kHz
# # frequencies = frequencies[frequencies <= 11000]
# # spectrogram = spectrogram[:len(frequencies), :]

# # Plot the spectrogram
# plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram), cmap='plasma')
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')

# # Customize the color bar
# cb = plt.colorbar()
# cb.ax.set_ylabel('Power Spectral Density [dB]')
# # cb.ax.set_ylim([-90, 45])

# # Add a title
# plt.title('Spectrogram of Audio Signal')

# # Show the plot
# plt.show()


import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# set the path to the recording file
filename = "On-site Test 1/20230511_182815_testing.pcm"

# define the sampling rate and window size for the spectrogram
sr = 44100
win_size = int(0.01 * sr)  # 10ms window

# read the binary data from the PCM file and convert to integer samples
with open(filename, 'rb') as f:
    pcm_data = np.frombuffer(f.read(), np.int16)

# compute the spectrogram using a Hanning window and 50% overlap
spectrum, freqs, t, im = plt.specgram(
    pcm_data, NFFT=win_size, Fs=sr, window=np.hanning(win_size),
    noverlap=win_size // 2, cmap=plt.cm.jet)

# set the labels for the plot
plt.colorbar()
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')

# display the spectrogram
plt.show()