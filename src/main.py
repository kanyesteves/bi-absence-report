import streamlit as st
import plotly.express as px
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

def calc_faltas(horas, faltas):
  quant_aula = (horas * 60) / 40
  quant_faltas = quant_aula * 0.25
  return quant_faltas

if len(pdf.dados_materias):
  ucs = list(pdf.dados_materias.keys())
  materia = st.selectbox("Materia", ucs)

  col1, col2, col3 = st.columns(3)
  for uc, dados in pdf.dados_materias.items():
    if uc == materia:
      result = calc_faltas(int(dados['Carga']), int(dados['Faltas']))
      col1.metric("Carga horaria da matéria", f"{dados['Carga']} horas", f"{(int(dados['Carga']) * 60) / 40:.0f} aulas")
      col2.metric("Quantidade de aulas que pode faltar", f"{result:.0f} aulas", "25%")
      col3.metric("Total de faltas", f"{dados['Faltas']} faltas", f"{result - int(dados['Faltas'])} aulas para faltar")
        
