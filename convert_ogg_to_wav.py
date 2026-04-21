import torchaudio
import os
import argparse

def convert_ogg_to_wav(ogg_path, wav_path):
    # Load the .ogg file
    waveform, sample_rate = torchaudio.load(ogg_path)
 
    # Save as .wav file
    torchaudio.save(wav_path, waveform, sample_rate)
    print(f"Successfully converted {ogg_path} to {wav_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert OGG to WAV using torchaudio")
    parser.add_argument("input", help="Path to the input OGG file")
    parser.add_argument("output", help="Path to the output WAV file")
 
    args = parser.parse_args()
 
    if os.path.exists(args.input):
        convert_ogg_to_wav(args.input, args.output)
    else:
        print(f"Error: {args.input} not found.")
