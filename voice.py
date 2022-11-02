import pyttsx3
from pathlib import Path


engine = pyttsx3.init()
# adjust type of voices from local machine
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_RU-RU_IRINA_11.0')


def text_to_voice(text: str):
    voice_data_name = text
    path_to_data = Path("voice_data")
    # check if folder with voices data exist and add new voice file to it
    if path_to_data.exists():
        engine.save_to_file(text, f'voice_data/{voice_data_name.replace(" ","_")}.mp3')
        engine.runAndWait()

    else:
        # create folder and add new voice file to it
        path_to_data.mkdir()
        engine.save_to_file(text, f'voice_data/{voice_data_name.replace(" ", "_")}.mp3')
        engine.runAndWait()
    return f'{voice_data_name.replace(" ", "_")}.mp3'

