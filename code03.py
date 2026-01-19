import streamlit as st
import pandas as pd

st.title("Média da Saturação Inferida por Diferença de Luminância")

# Botão para importar o arquivo
uploaded_file = st.file_uploader(
    "📄 Carregue seu arquivo de dados (sem cabeçalho)", type=["txt", "csv"])

if uploaded_file is not None:
    # Leitura do arquivo sem cabeçalho
    try:
        df = pd.read_csv(uploaded_file, header=None, delim_whitespace=True)
    except:
        df = pd.read_csv(uploaded_file, header=None, sep=",")

    # Renomeia as colunas
    df.columns = ['diferenca_luminancia', 'saturacao_inferida']

    # Calcula a média por diferença de luminância
    media_por_luminancia = df.groupby('diferenca_luminancia')[
        'saturacao_inferida'].mean().reset_index()

    # Exibe os dados e resultados
    st.subheader("📊 Dados Carregados")
    st.dataframe(df)

    st.subheader("📈 Média da Saturação Inferida por Diferença de Luminância")
    st.dataframe(media_por_luminancia)

    # Botão para exportar o resultado como CSV
    csv = media_por_luminancia.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="💾 Baixar resultado em CSV",
        data=csv,
        file_name='media_saturacao_por_luminancia.csv',
        mime='text/csv',
    )
else:
    st.info("Por favor, carregue um arquivo .txt ou .csv para iniciar a análise.")
