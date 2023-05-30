# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import signal

# # Load the audio data from the .pcm file
# data = np.fromfile('On-site Test 1/C1/20230511_172509_testing.pcm', dtype=np.int16)

# # Define the sampling rate (in Hz)
# fs = 44100

# # Use the signal module from scipy to compute the spectrogram
# frequencies, times, spectrogram = signal.spectrogram(data, fs)

# # Cap the frequency at 10 kHz
# # frequencies = frequencies[frequencies <= 11000]
# # spectrogram = spectrogram[:len(frequencies), :]

# # Plot the spectrogram
# # plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram), cmap='plasma')
# plt.pcolormesh(times, frequencies, 10 * np.log10(spectrogram), cmap='jet')
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
import matplotlib.pyplot as plt

# Read the .pcm file
with open('20230530_233611.pcm', 'rb') as f:
    pcm_data = f.read()

# Convert the raw PCM data to a NumPy array
data = np.frombuffer(pcm_data, dtype='int16')
for element in data:
        print(element)

# Set up audio recording parameters
sample_rate = 44100

# Plot the spectrogram
plt.specgram(data, Fs=sample_rate, cmap='jet',  vmin=-60, vmax=60)
plt.xlabel('Time [sec]')
# plt.ylim([12000, 12500])
plt.ylabel('Frequency [Hz]')
plt.title('Spectrogram of PCM file')
plt.colorbar()
plt.show()





# Read the .pcm file
with open('20230530_233611_processed.pcm', 'rb') as f:
    pcm_data = f.read()

# Convert the raw PCM data to a NumPy array
data = np.frombuffer(pcm_data, dtype='int16')
for element in data:
        print(element)

# Set up audio recording parameters
sample_rate = 44100

# Plot the spectrogram
plt.specgram(data, Fs=sample_rate, cmap='jet',  vmin=-60, vmax=60)
plt.xlabel('Time [sec]')
plt.ylim([12000, 13000])
plt.ylabel('Frequency [Hz]')
plt.title('Spectrogram of PCM file')
plt.colorbar()
plt.show()



# import numpy as np
# import matplotlib.pyplot as plt

# # Read the .pcm file
# with open('On-site Test 1/C1/20230511_172509_testing.pcm', 'rb') as f:
#     pcm_data = f.read()

# # Convert the raw PCM data to a NumPy array
# data = np.frombuffer(pcm_data, dtype='int16')

# # Set up audio recording parameters
# sample_rate = 44100

# # Plot the spectrogram
# plt.specgram(data, Fs=sample_rate, cmap='jet', vmin=-60, vmax=20)
# plt.xlabel('Time [sec]')
# plt.ylabel('Frequency [Hz]')
# plt.ylim([15000, 20000])
# plt.title('Spectrogram of PCM file')
# plt.colorbar()
# plt.show()