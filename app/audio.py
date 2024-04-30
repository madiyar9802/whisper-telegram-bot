import torch
import whisper
from os import remove


def speech_recognition(file, model='medium'):
    speech_model = whisper.load_model(model, device=torch.device('cuda'))
    if file == None:
        return 'Не удалось транскрибировать аудио'
    else:
        audio = whisper.load_audio(file)
    result = speech_model.transcribe(audio=audio)
    # Если нужно сохранить текст в .txt
    # with open(f'transcription_{model}.txt', 'w') as file:
    #     file.write(result['text'])
    remove(file)

    # Возвращаем результат
    return result['text']


if __name__ == '__main__':
    speech_recognition()
