import torchaudio
import os
import argparse


def convert_ogg_to_wav(ogg_path, wav_path):
    # Load the .ogg file
    waveform, sample_rate = torchaudio.load(ogg_path)

    # Save as .wav file
    torchaudio.save(wav_path, waveform, sample_rate)
    print(f"Successfully converted {ogg_path} to {wav_path}")


def convert_wav_to_ogg(wav_path, ogg_path):
    # Load the .wav file
    waveform, sample_rate = torchaudio.load(wav_path)

    # Save as .ogg file
    torchaudio.save(ogg_path, waveform, sample_rate)
    print(f"Successfully converted {wav_path} to {ogg_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert between OGG and WAV using torchaudio"
    )
    parser.add_argument("input", help="Path to the input file")
    parser.add_argument("output", help="Path to the output file")

    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"Error: {args.input} not found.")
    else:
        input_ext = os.path.splitext(args.input)[1].lower()
        output_ext = os.path.splitext(args.output)[1].lower()

        if input_ext == ".ogg" and output_ext == ".wav":
            convert_ogg_to_wav(args.input, args.output)
        elif input_ext == ".wav" and output_ext == ".ogg":
            convert_wav_to_ogg(args.input, args.output)
        else:
            print(f"Error: Unsupported conversion from {input_ext} to {output_ext}")
