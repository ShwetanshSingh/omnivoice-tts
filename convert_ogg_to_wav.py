import torchaudio
import os

def convert_ogg_to_wav(ogg_path, wav_path):
    # Load the .ogg file
    waveform, sample_rate = torchaudio.load(ogg_path)
    
    # Save as .wav file
    torchaudio.save(wav_path, waveform, sample_rate)
    print(f"Successfully converted {ogg_path} to {wav_path}")

if __name__ == "__main__":
    source_file = "sample_for_clone.ogg"
    target_file = "sample_for_clone.wav"
    
    if os.path.exists(source_file):
        convert_ogg_to_wav(source_file, target_file)
    else:
        print(f"Error: {source_file} not found.")
