import os
import wave
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from scipy.io import wavfile

def process_wav_files(audio_folder='audio_data', output_folder='image_spectrograms', segment_length=15):
    """Processes all .wav files, splits them into segments, and saves spectrograms."""
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(audio_folder):
        if filename.endswith('.wav'):
            filepath = os.path.join(audio_folder, filename)
            save_spectrograms(filepath, output_folder, segment_length)

def save_spectrograms(filepath, output_folder, segment_length):
    """Splits a .wav file into segments and saves spectrogram images."""
    samplerate, data = wavfile.read(filepath)
    duration = len(data) / samplerate
    segment_samples = samplerate * segment_length
    num_segments = int(np.ceil(len(data) / segment_samples))
    
    for i in range(num_segments):
        start = i * segment_samples
        end = min((i + 1) * segment_samples, len(data))
        segment = data[start:end]
        
        if len(segment) < segment_samples:
            padding = np.zeros(segment_samples - len(segment))
            segment = np.concatenate((segment, padding))
        
        save_spectrogram(segment, samplerate, output_folder, os.path.basename(filepath), i)

def save_spectrogram(segment, samplerate, output_folder, filename, index):
    """Generates and saves a spectrogram image from an audio segment."""
    f, t, Sxx = scipy.signal.spectrogram(segment, samplerate)
    
    plt.figure(figsize=(10, 4))
    plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='gouraud', cmap='viridis')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [s]')
    plt.colorbar(label='Intensity [dB]')
    plt.title(f'Spectrogram {filename} - Segment {index}')
    
    output_path = os.path.join(output_folder, f'{filename}_segment{index}.png')
    plt.savefig(output_path)
    plt.close()
    
if __name__ == "__main__":
    process_wav_files()
