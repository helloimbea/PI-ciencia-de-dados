# Projeto Integrador
Repositório para a unidade curricular Projeto Integrador do curso de Análise e Desenvolvimento de Sistemas fornecido pelo SENAC.

## Tema do projeto

### *Explorando o Mercado de Dados no Brasil: Uma Análise com Base na Pesquisa State of Data Brazil 2024-2025*

Este projeto propõe a criação de um painel analítico a partir da base de dados da pesquisa *State of Data Brazil 2024-2025*, realizada pela Data Hackers em parceria com a Bain & Company. Por meio de um processo estruturado de ETL (Extract, Transform, Load) utilizando a biblioteca Pandas, os dados serão tratados e armazenados em uma base estruturada para posterior visualização com Streamlit.

A proposta é explorar múltiplas camadas do mercado de dados brasileiro, permitindo ao usuário final encontrar informações como:

 - Perfil demográfico dos profissionais (faixa etária, região, gênero, formação);
 - Distribuição por níveis de experiência (júnior, pleno, sênior, gestão);
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
- Beatriz:
  Criação do repositório, README e adição dos membros. 
- Emily: Contexto do banco de dados  utilizado e transformações a serem realizadas. 
- Yago: Objetivo da análise do banco de dados e Justificativa
- Vitor: Ideia Inicial do Dashboard
- Gabriel: Construção do Tema

### Cronograma

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

Com isso, pretendemos gerar insights relevantes sobre o cenário atual da área.

### Transformações a serem realizadas
Para a realização da análise, serão aplicadas as seguintes transformações nos dados:

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


