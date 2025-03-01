import os
from spectrograms import process_all_audio

AUDIO_FOLDER = "audio_data"
OUTPUT_FOLDER = "image_spectrograms"

def main():
    print("\n===== Starting Spectrogram Generation =====\n")
    
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    process_all_audio(AUDIO_FOLDER, OUTPUT_FOLDER)

    print("\n===== Spectrogram Generation Complete! =====\n")

if __name__ == "__main__":
    main()
