
import openai
from openai.embeddings_utils import get_embedding
from openai.embeddings_utils import cosine_similarity

import streamlit as st
import pandas as pd
import ast

# openai.api_key = "sk-"
openai.api_key = "sk-"



def consultar (pregunta, df_embedding, Num_respuesta):
    # ## embeding de mi pregunta
    mi_prompt = get_embedding(pregunta, engine='text-embedding-ada-002')

    ## hace la comparación de similitud
    df_embedding["Similitud"] = df_embedding['Embedding'].apply(lambda x: cosine_similarity(x, mi_prompt))
    df_embedding = df_embedding.sort_values("Similitud", ascending=False)

    # Num_respuesta = 3

    # ordena los datos por la columna  en orden descendente, selecciona las primeras Num_respuesta filas y la columna
    respuestas = df_embedding.sort_values('Similitud', ascending=False).head(Num_respuesta)['Parrafo']
    respuestas = respuestas.drop(respuestas.index[Num_respuesta:])

    filas_concatenadas = respuestas.apply(lambda x: ''.join(map(str, x)))

    # ###Unir las filas en una sola cadena de texto
    texto_concatenado = '\n'.join(filas_concatenadas)

    # print(texto_concatenado)
    st.success(texto_concatenado)



 # ###Título
html_temp = """
<h1 style="color:#181082;text-align:center;">SISTEMA DE RESPUESTA AUTOMÁTICA ACERCA DEL CÓDIGO NACIONAL DE TRANSITO Y Sr. BITER</h1>
</div>
"""
st.markdown(html_temp, unsafe_allow_html=True)

if __name__ == '__main__':
        ## ## carga el archivo con los embeddings ya creados
    df_embedding = pd.read_csv('texts/df_embeddings_codigo_nacional.txt')

    ### convierte el archivo leido como string en List float
    df_embedding['Embedding'] = df_embedding['Embedding'].apply(ast.literal_eval)

    while True:
        # pregunta = input("realiza una consulta: ")
        pregunta = st.text_input("realiza una consulta:  ")
        Num_respuesta = st.number_input('ingrese el numero de respuestas',min_value=1, max_value=10, value= 1, step=1)


        if st.button("realizar la consulta"):
            
            if pregunta == "exit":
                st.success("Adios, gracias por consultar nuestros servicios" )
                break
            else:
                # Num_respuesta = int(input("ingrese el numero de respuestas "))
                consultar (pregunta, df_embedding, Num_respuesta)
