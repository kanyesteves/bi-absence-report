import pypdf
import streamlit as st

class ExtractPdf:
  def __init__(self, path):
    self.path = path
    self.materias = []
    self.carga_hrs = []
    self.total_faltas_materia = []
    self.dados_materias = {}
      

  def extract(self):
    try: 
      pdf = pypdf.PdfReader(self.path)
      page = pdf.pages[0]
      text_content = page.extract_text()
      lines = text_content.split('\n')

      for i, line in enumerate(lines):
        if "Unidade Curricular" in line:
          parts = line.split('- ch: ')
          unidade_curricular = parts[0].replace("Unidade Curricular: ", "").strip()
          ch = parts[1].strip()
          self.carga_hrs.append(ch)
          self.materias.append(unidade_curricular)

        if line.split()[-1] == "Final":
          next_line = lines[i + 1].strip()
          total_faltas = next_line.split()[-1]
          self.total_faltas_materia.append(total_faltas)

      for uc, ch, tfm in zip(self.materias, self.carga_hrs, self.total_faltas_materia): 
        self.dados_materias[uc] = {'Carga': ch, 'Faltas': tfm}

    except:
      st.warning("Sem dados")