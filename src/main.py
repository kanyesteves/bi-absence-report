import streamlit as st
from extractPdf import ExtractPdf


st.set_page_config(
    layout="wide",
    page_title="Relatorio de faltas SENAC"
)

st.title("Relatório de faltas por aluno")
st.divider()

pdf_path = st.sidebar.file_uploader("Importe o relatório de faltas aqui!!")

pdf = ExtractPdf(pdf_path)
pdf.extract()

# 1 dia equivale a 4 aulas considerando 1 hora por aula.
def calc_faltas(horas, faltas):
  quant_aula = horas / 4
  quant_faltas = quant_aula * 0.25
  return quant_faltas

if len(pdf.dados_materias):
  ucs = list(pdf.dados_materias.keys())
  st.subheader(pdf.aluno)
  materia = st.selectbox("Materia", ucs)

  col1, col2, col3 = st.columns(3)
  for uc, dados in pdf.dados_materias.items():
    if uc == materia:
      result = calc_faltas(int(dados['Carga']), int(dados['Faltas']))
      col1.metric("Carga horaria da matéria", f"{dados['Carga']} horas", f"{int(dados['Carga']) / 4:.0f} dias de aula")
      col2.metric("Quantidade de dias que pode faltar na materia", f"{result:.0f} dias", "25%")
      col3.metric("Total de faltas", f"{dados['Faltas']} faltas", f"{int(dados['Faltas']) / 4:.0f} dias")
        
