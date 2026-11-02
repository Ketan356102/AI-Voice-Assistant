
import os
import winsound
from dotenv import load_dotenv
from deepgram import DeepgramClient, SpeakOptions

load_dotenv()

class TTS:
    def __init__(self):
        self.filename = "output.wav"

    def speak(self, text):
        try:
            # Initialize Deepgram client
            deepgram = DeepgramClient(
                api_key=os.getenv("DEEPGRAM_API_KEY")
            )

            # Configure speech options
            options = SpeakOptions(
                model="aura-asteria-en",
                encoding="linear16",
                container="wav"
            )

            # Generate speech
            SPEAK_OPTIONS = {"text": text}

            deepgram.speak.v("1").save(
                self.filename,
                SPEAK_OPTIONS,
                options
            )

            # Play generated WAV audio
            winsound.PlaySound(
                self.filename,
                winsound.SND_FILENAME
            )

        except Exception as e:
            print(f"Exception: {e}")


if __name__ == "__main__":
    tts = TTS()
    tts.speak("Hello, how can I help you today?")
