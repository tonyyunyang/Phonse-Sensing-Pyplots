import numpy as np
import matplotlib.pyplot as plt

# Load .pcm audio file
filename = "On-site Test 1/C3/20230511_172825_testing.pcm"
sample_rate = 44100  # Replace with the actual sample rate of your audio file
with open(filename, 'rb') as file:
    data = np.frombuffer(file.read(), dtype=np.int16)

# Compute the one-sided PSD
psd = np.abs(np.fft.fft(data))**2 / len(data)
freq = np.fft.fftfreq(len(data), 1 / sample_rate)
freq = freq[:len(freq) // 2]  # Keep only positive frequencies
psd = psd[:len(psd) // 2]

# Plot the PSD
plt.figure(figsize=(10, 6))
plt.plot(freq, 10 * np.log10(psd))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (dB/Hz)')
plt.title('Power Spectral Density')
plt.grid(True)
plt.show()
