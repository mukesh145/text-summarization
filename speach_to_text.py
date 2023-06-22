import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import IPython.display as display

tokenizer = Wav2Vec2Tokenizer.from_pretrained("speech_modal")
model = Wav2Vec2ForCTC.from_pretrained("speech_modal")

def s_to_t():

    speech, rate = librosa.load("audio.mp3",sr=16000)

    display.Audio("audio.mp3", autoplay=True)

    input_values = tokenizer(speech, return_tensors = 'pt').input_values

    logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim =-1)

    transcriptions = tokenizer.decode(predicted_ids[0])

    return(transcriptions)


# text = s_to_t()