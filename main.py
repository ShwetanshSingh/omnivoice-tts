from omnivoice import OmniVoice
import soundfile as sf
import torch


def main():
    print("Hello from omnivoice-tts!")
    # Load the model
    model = OmniVoice.from_pretrained(
        "k2-fsa/OmniVoice", device_map="cuda:0", dtype=torch.float16
    )

    # Generate audio
    audio = model.generate(
        text="Hello, this is a test of zero-shot voice cloning.",
        ref_text="Transcription of the reference audio.",
    )  # audio is a list of `np.ndarray` with shape (T,) at 24 kHz.

    sf.write("out.wav", audio[0], 24000)


if __name__ == "__main__":
    main()
