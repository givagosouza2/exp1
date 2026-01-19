import streamlit as st
import pandas as pd

st.title("Análise de Preferência de Saturação de Cor")

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
    df.columns = ['saturacao_1', 'saturacao_2', 'preferida']

    # Converte a coluna 'preferida' em valores reais de saturação
    df['saturacao_preferida'] = df.apply(
        lambda row: row['saturacao_1'] if row['preferida'] == 1 else row['saturacao_2'], axis=1
    )

    # Conta o número de vezes que cada saturação foi preferida
    contagem_preferencia = df['saturacao_preferida'].value_counts(
    ).sort_index()

    # Calcula a porcentagem
    porcentagem_preferencia = (
        contagem_preferencia / contagem_preferencia.sum()) * 100
    porcentagem_preferencia_df = porcentagem_preferencia.reset_index()
    porcentagem_preferencia_df.columns = [
        'saturacao', 'porcentagem_preferencia']

    # Exibe os resultados
    st.subheader("📊 Dados Carregados")
    st.dataframe(df)

    st.subheader("📈 Porcentagem de Preferência por Saturação")
    st.dataframe(porcentagem_preferencia_df)

    # Botão para exportar o resultado como CSV
    csv = porcentagem_preferencia_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="💾 Baixar resultado em CSV",
        data=csv,
        file_name='porcentagem_preferencia.csv',
        mime='text/csv',
    )
else:
    st.info("Por favor, carregue um arquivo .txt ou .csv para iniciar a análise.")
