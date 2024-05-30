# Projeto BI para Relatório de Faltas por Aluno

## Introdução
Eu vi esse projeto na semana acadêmica onde curso meu último semestre de Analise e Desenvolvimento de sistemas. Um grupo de outro curso apresentou a ideia de criar um BI para melhorar a visualização e as tomadas de decisões nas faltas das matérias dos alunos. Eu adorei a ideia e resolvi criar um protótipo, e nessa documentação vou apresentar os requisitos para construção do mesmo.

## Problemática
Atualmente na faculdade, além das notas, todos os alunos precisam ter 75% de presença para poder passar na matéria. Diante desse contexto, toda vez que um aluno falta na aula, os professores lançam essas notas no sistema e a cordenação constrói um pdf com um relatório do total de faltas desse aluno em cada matéria. Mas esse pdf só informa a carga horária e o total de faltas, dificultando para o aluno saber quantas aulas ele ainda pode faltar.

## Linguagem de programação

- Python 3: Escolhi usar python pela flexibilidade e agilidade na construção das minhas ideias/soluções.

#### Bibliotecas

- Pypdf: Essa biblioteca consegue ler, extrair, editar e criar arquivos no formato PDF.
- Streamlit: Essa biblioteca é muito comum para construir BI intuitivos e ótimo para construir programas, sites e sistemas simples.