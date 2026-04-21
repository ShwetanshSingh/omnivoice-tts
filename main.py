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
        text="Google इनपुट उपकरण आपके द्वारा चुनी गई भाषा में वेब पर कहीं भी लिखना आसान बनाता है. और जानें| इसे आज़माने के लिए, नीचे अपनी भाषा और इनपुट उपकरण चुनें और लिखना आरंभ करें.",
        ref_audio="ref.wav",
        ref_text="मुझे यह कहना है कि हमने जो अभी सारी जानकारी दी है इनको, क्या यह जानकारी सही है या गलत यह जानने के लिए हम क्या करें?",
    )  # audio is a list of `np.ndarray` with shape (T,) at 24 kHz.

    sf.write("out.wav", audio[0], 24000)


if __name__ == "__main__":
    main()
