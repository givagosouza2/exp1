import streamlit as st
import pandas as pd

st.title("Média da Saturação Inferida por Saturação Física")

# Botão para importar o arquivo
uploaded_file = st.file_uploader("📄 Carregue seu arquivo de dados (sem cabeçalho)", type=["txt", "csv"])

if uploaded_file is not None:
    # Leitura do arquivo sem cabeçalho
    try:
        # Tenta ler como espaço em branco
        df = pd.read_csv(uploaded_file, header=None, delim_whitespace=True)
    except:
        # Se não funcionar, tenta como CSV padrão
        df = pd.read_csv(uploaded_file, header=None, sep=",")

    # Renomeia as colunas
    df.columns = ['saturacao_fisica', 'saturacao_inferida']

    # Calcula a média por saturação física
    media_por_saturacao = df.groupby('saturacao_fisica')['saturacao_inferida'].mean().reset_index()

    # Exibe o DataFrame original e o resultado
    st.subheader("📊 Dados Carregados")
    st.dataframe(df)

    st.subheader("📈 Média por Saturação Física")
    st.dataframe(media_por_saturacao)

    # Botão para exportar o resultado como CSV
    csv = media_por_saturacao.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="💾 Baixar resultado em CSV",
        data=csv,
        file_name='media_saturacao.csv',
        mime='text/csv',
    )
else:
    st.info("Por favor, carregue um arquivo .txt ou .csv para iniciar a análise.")
