import requests
import json
from pytube import YouTube
import ssl

# Desactiva la verificación del certificado SSL
ssl._create_default_https_context = ssl._create_unverified_context

# Obtiene la ID del video de YouTube
url = "https://www.youtube.com/watch?v=rnBmNgx-K9A"
video_id = url.split("=")[1]

# Descarga el video utilizando la biblioteca pytube
yt = YouTube(url)
stream = yt.streams.filter(only_audio=True).first()
stream.download()

# Obtiene la transcripción utilizando la API de YouTube Data
api_key = "AIzaSyAoUhgVQi7DHTWrxIy47du28-39FGBt1tQ"
transcription_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet%2C%20transcript&key={api_key}&id={video_id}"
response = requests.get(transcription_url)
data = json.loads(response.text)

# Guarda la transcripción en un archivo de texto
transcription = data["items"][0]["snippet"]["localized"]["title"] + "\n\n"
for part in data["items"][0]["transcript"]["parts"]:
    transcription += part["text"] + "\n"

with open("transcripcion.txt", "w") as f:
    f.write(transcription)


# from youtube_transcript_api import YouTubeTranscriptApi

# video_id = 'rnBmNgx-K9A'
# transcript = YouTubeTranscriptApi.get_transcript(video_id)

# with open('transcript.json', 'w') as f:
#     f.write(json.dumps(transcript))


# import json
# import srt

# with open('transcript.json', 'r') as f:
#     transcript = json.load(f)

# subtitles = []

# for i in range(len(transcript)):
#     start = transcript[i]['start']
#     end = transcript[i]['start'] + transcript[i]['duration']
#     text = transcript[i]['text']
#     subtitle = srt.Subtitle(i+1, start=start, end=end, content=text)
#     subtitles.append(subtitle)

# with open('subtitles.srt', 'w') as f:
#     f.write(srt.compose(subtitles))


