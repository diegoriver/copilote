from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd

# Read the list of video IDs from a .csv file
df = pd.read_csv('texts/lista_completa_sr_biter.csv', sep=';')
video_ids = df['video_id'].tolist()

# Especifica el idioma que deseas descargar (en este caso, español)
language = 'es'

transcripts = []

for video_id in video_ids:
    try:
        # Obtener los subtítulos del video en el idioma especificado
        transcript = YouTubeTranscriptApi.get_transcript(
            video_id, languages=[language])

        # Concatenate the transcript text into a single string
        transcript_text = ' '.join(
            [line['text'].replace('\n', ' ') for line in transcript])

        # Add the transcript text to the list of transcripts
        transcripts.append(transcript_text)
    except (TranscriptsDisabled, NoTranscriptFound):
        print(f"No Spanish transcript found for video ID {video_id}")
        transcripts.append("No Spanish transcript found for video")

# Add the transcripts as a new column in the DataFrame
df['transcripcion'] = transcripts

# Save the updated DataFrame as a .csv file
df.to_csv('texts/lista_completa_sr_biter.csv', index=False)

print(df)



######################################################

# from youtube_transcript_api import YouTubeTranscriptApi
# from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


# import pandas as pd


# # Read the list of video IDs from a .csv file
# video_ids = pd.read_csv('texts/lista_conductores_nuevos_app.csv')['video_id'].tolist()

# # Especifica el idioma que deseas descargar (en este caso, español)
# language = 'es'

# transcripts = []

# for video_id in video_ids:
#     # # Obtener los subtítulos del video en el idioma especificado
#     # transcript = YouTubeTranscriptApi.get_transcript(
#     #     video_id, languages=[language])

#     # # Concatenate the transcript text into a single string
#     # transcript_text = ' '.join(
#     #     [line['text'].replace('\n', ' ') for line in transcript])

#     # # Add the transcript text to the list of transcripts
#     # transcripts.append(transcript_text)

#     try:
#         # Obtener los subtítulos del video en el idioma especificado
#         transcript = YouTubeTranscriptApi.get_transcript(
#             video_id, languages=[language])

#         # Concatenate the transcript text into a single string
#         transcript_text = ' '.join(
#             [line['text'].replace('\n', ' ') for line in transcript])

#         # Add the transcript text to the list of transcripts
#         transcripts.append(transcript_text)
#     except (TranscriptsDisabled, NoTranscriptFound):
#         print(f"No Spanish transcript found for video ID {video_id}")

# # Convert the list of transcripts to a pandas DataFrame
# df = pd.DataFrame({'conductores_nuevos_app': transcripts})

# # Save the DataFrame as a .csv file
# df.to_csv('texts/conductores_nuevos_app.csv', index=False)

# # Save the DataFrame as a .txt file
# with open('texts/conductores_nuevos_app.txt', 'w') as f:
#     for transcript_text in transcripts:
#         f.write(transcript_text + '\n')


# print(df)

#######################################################
# import pandas as pd
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context

# from youtube_transcript_api import YouTubeTranscriptApi

# video_id = "rnBmNgx-K9A"

# # Especifica el idioma que deseas descargar (en este caso, español)
# language = 'es'

# # Obtener los subtítulos del video en el idioma especificado
# transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])

# # Concatenate the transcript text into a single string
# transcript_text = ' '.join([line['text'].replace('\n', ' ') for line in transcript])

# # Convert the transcript text to a pandas DataFrame
# df = pd.DataFrame({'transcript': [transcript_text]})

# # Save the DataFrame as a .csv file
# df.to_csv('transcript.csv', index=False)

# # Save the DataFrame as a .txt file
# with open('transcript.txt', 'w') as f:
#     f.write(transcript_text)


# print(df)


