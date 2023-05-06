import openai
import pandas as pd
import re
import math

# Configura la clave de API de OpenAI
openai.api_key = "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"


# Read the list of texts from a .csv file
df = pd.read_csv('texts/lista_completa_sr_biter.csv')
texts = df['transcripcion'].tolist()

summaries = []

for text in texts:
    try:
        # Dividir el texto en partes si excede el límite permitido por la API de OpenAI
        if len(text) > 2048:
            n_parts = math.ceil(len(text) / 2048)
            parts = [text[i:i+n_parts] for i in range(0, len(text), n_parts)]
        else:
            parts = [text]

        summary_parts = []

        for part in parts:
            # Buscar la palabra "artículo" y el número relacionado con ella en el texto
            match = re.search(r'\bartículo\s+(\d+)', part)
            if match:
                article_number = match.group(1)
                prompt = f"Resuma el siguiente texto en menos de 150 palabras e incluya la frase 'artículo {article_number}': {part}"
            else:
                prompt = f"Resuma el siguiente texto en menos de 150 palabras: {part}"

            # Generar un resumen del texto utilizando la API de OpenAI
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.5,
            )

            summary_part = response['choices'][0]['text'].strip()
            summary_parts.append(summary_part)

        summary = ' '.join(summary_parts)
        summaries.append(summary)
    except Exception as e:
        print(f"An error occurred: {e}")
        summaries.append("NO resumen por error de ejecución")

# Add the summaries as a new column in the DataFrame
df['summary'] = summaries

# Save the updated DataFrame as a .csv file
df.to_csv('texts/lista_completa_sr_biter.csv', index=False)

print(df)
