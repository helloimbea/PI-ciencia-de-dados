# Projeto Integrador
Repositório para o segundo semestre da unidade curricular Projeto Integrador do curso de Análise e Desenvolvimento de Sistemas fornecido pelo SENAC.

## Tema do projeto

### *Explorando o Mercado de Dados no Brasil: Uma Análise com Base na Pesquisa State of Data Brazil 2024-2025*

Este projeto propõe a criação de um painel analítico a partir da base de dados da pesquisa *State of Data Brazil 2024-2025*, realizada pela Data Hackers em parceria com a Bain & Company. Por meio de um processo estruturado de ETL (Extract, Transform, Load) utilizando a biblioteca Pandas, os dados serão tratados e armazenados em uma base estruturada para posterior visualização com Streamlit.

A proposta é explorar múltiplas camadas do mercado de dados brasileiro, permitindo ao usuário final encontrar informações como:

 - Perfil demográfico dos profissionais (faixa etária, região, gênero, formação);
 - Distribuição por níveis de experiência (júnior, pleno, sênior);
 - Ferramentas e tecnologias mais utilizadas em diferentes áreas (engenharia, análise e ciência de dados);
 - Principais desafios enfrentados por times de dados;
 - Objetivos de carreira e tendências de especialização.

Espera-se não apenas aplicar os aprendizados técnicos das disciplinas do semestre, como também gerar um projeto funcional que possa servir como ferramenta de apoio para estudantes, profissionais e recrutadores interessados em compreender as tendências e oportunidades no setor de dados no Brasil.


## Integrantes
 - Beatriz Heimann Gesser. 
 - Davi Urbina Siqueira.
 - Emily Nascimento Klinke. 
 - Gabriel Hisatugu Alves De Oliveira.
 - Thalia Maria Machado.
 - Thalita Pastorini de Araujo.
 - Vitor Aluisio Souza Lopes.
 - Yago Henrique Zorzetto

### Planejamento das tarefas
**Primeira Etapa:**  
- Beatriz: Criação do repositório, README e adição dos membros. 
- Emily: Contexto do banco de dados  utilizado e transformações a serem realizadas. 
- Yago: Objetivo da análise do banco de dados e Justificativa. 
- Vitor: Ideia Inicial do Dashboard.
- Gabriel: Construção do Tema.
- Thalita: Cronograma.

**Segunda Etapa:**  
- Beatriz: Criação da base e estrutura do projeto. Visualização dos KPIs com Streamlit e Plotly
- Gabriel: Transformação dos dados usando Pandas e JupyterNotebook (pacote Anaconda)

### Cronograma
**Primeira Etapa:**  
🗓️ Semana 1 — Planejamento e Estruturação  
Beatriz: Criação do repositório no GitHub, elaboração do README.md e adição dos integrantes  
Gabriel: Construção do tema do projeto  
Emily: Elaboração do contexto da base de dados  
Yago: Definição do objetivo da análise e justificativa  
Vitor: Desenvolvimento da ideia inicial do dashboard  
Thalita: Elaboração do cronograma do projeto  
  
🗓️ Semana 2 — Consolidação da Documentação  
Beatriz: Organização e atualização do README.md  
Emily: Ajustes na descrição da base de dados e transformações  
Yago: Revisão do objetivo e justificativa  
Vitor: Refinamento da ideia do dashboard  
Gabriel: Revisão do tema do projeto  
Thalita: Ajustes no cronograma  
  
🗓️ Semana 3 — Definição das Transformações  
Emily: Detalhamento das transformações a serem realizadas nos dados (ETL). 
Thalita: Revisão e organização do planejamento no README. 
  
🗓️ Semana 4 — Estruturação da Proposta do Dashboard  
Vitor: Refinamento da estrutura do dashboard e definição dos indicadores (KPIs). 
Thalita: Atualização do cronograma conforme evolução do projeto. 
  
🗓️ Semana 5 — Revisão Geral da Etapa  
Todos os integrantes:  
Revisão das informações inseridas no README. 
Verificação de coerência entre tema, objetivo, justificativa e proposta. 
  
🗓️ Semana 6 — Finalização da Primeira Etapa  
Todos os integrantes:  
Ajustes finais na documentação. 
Organização do repositório. 
Preparação para entrega da primeira etapa. 

**Segunda Etapa:**  

🗓️ Semana 1 — Base do projeto  
Foi criada a base do projeto, como pastas e estrutura do programa.
  
🗓️ Semana 2 — Tratamento dos dados  
Os dados da database foram tratados e organizados em novas tabelas usando Pandas e JupyterNotebook, seguindo as ideias de transformação da primeira etapa.
  
🗓️ Semana 3 — Visualização 
Transformamos os dados em visualização com gráficos e métricas usando Plotly e Streamlit.  
O Streamlit foi utilizado como framework principal do dashboard, sendo responsável pela construção da interface visual e pela integração entre os dados e os indicadores apresentados.  
Com ele, foi possível desenvolver uma aplicação web interativa em Python de forma rápida e organizada, permitindo:  
exibição dos KPIs em tempo real;  
criação do layout do dashboard;  
organização dos gráficos na tela;  
renderização dinâmica dos dados carregados dos arquivos CSV;  
construção de uma aplicação acessível via navegador sem necessidade de desenvolvimento front-end tradicional.  
  
O Plotly foi utilizado para a criação das visualizações gráficas interativas do dashboard.  
A biblioteca permitiu transformar os dados processados em gráficos modernos e dinâmicos, melhorando a análise visual das informações relacionadas ao mercado de tecnologia e salários.  
Com o Plotly, foram desenvolvidos:  
gráficos de barras para distribuição de cargos e faixas salariais;  
gráfico de pizza para tecnologias mais utilizadas;  
gráficos comparativos relacionados ao uso de IA e salários;  
mapa de calor relacionando nível profissional e faixa salarial.  
  
🗓️ Semana 4 — Publicação 
Upload no Streamlit Cloud

## Base de dados utilizada
https://www.kaggle.com/datasets/datahackers/state-of-data-brazil-20242025


### Contexto
A base de dados utilizada faz parte do State of Data Brazil 2024-2025, o maior levantamento sobre o mercado de dados e inteligência artificial no Brasil, com mais de 5.200 profissionais participantes.

O dataset reúne informações sobre carreira, salários, tecnologias utilizadas, formação e tendências da área de dados, permitindo uma análise abrangente do cenário atual no país.

### Justificativa
O mercado de dados tem crescido rapidamente no Brasil, aumentando a demanda por profissionais como analistas, cientistas e engenheiros de dados. No entanto, muitas pessoas ainda possuem dúvidas sobre salários, tecnologias exigidas e caminhos de carreira na área.

Então este projeto se justifica pela necessidade de transformar dados reais do mercado em informações claras e acessíveis, auxiliando estudantes e profissionais na tomada de decisão sobre carreira.

### Objetivo da análise
O objetivo deste projeto é analisar os dados da pesquisa State of Data Brazil 2024-2025 para identificar padrões e tendências no mercado de dados no Brasil.

A análise busca responder questões como:
- Qual a faixa salarial dos profissionais da área?
- Quais tecnologias são mais utilizadas?
- Como o nível de experiência impacta o salário?
- Quais são os cargos mais comuns na área de dados?
- Os profissionais de dados que usam IA generativa ganham mais?

Com isso, pretendemos gerar insights relevantes sobre o cenário atual da área.

### Transformações a serem realizadas
Para a realização da análise, serão aplicadas as seguintes transformações nos dados:

- Remoção de espaços duplos e espaços vazios antes e depois dos valores nas células
- Remoção ou tratamento de valores nulos
- Padronização de nomes de cargos e tecnologias
- Seleção das colunas relevantes para a análise
- Agrupamento de dados por categorias (cargo, experiência, etc.)
- Cálculo de métricas como média salarial
- Filtragem de dados inconsistentes ou irrelevantes

## Ideia inicial do dashboard

O dashboard será desenvolvido em **Streamlit**, priorizando a entrega rápida e eficiente de indicadores reais:

### Indicadores de Mercado (KPIs)
O topo da aplicação apresentará cards interativos com cálculos em tempo real:
* **Média Salarial:** Valor médio baseado no cargo e nível selecionados.
* **Tecnologia Principal:** A ferramenta mais utilizada pelo perfil filtrado.
* **Amostra:** Quantidade de profissionais que compõem os dados visualizados.

# DASHBOARD PUBLICADO NO STREAMLIT CLOUD  
https://pi-ciencia-de-dados.streamlit.app  
![Print tela](/dashboard-kpis/assets/print-dashboard.png)
