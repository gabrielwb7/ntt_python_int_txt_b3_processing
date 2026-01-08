# Desafio: Manipulação, Análise Estatística e Visualização de Dados Históricos da B3 (Formato Posicional)

## Objetivo
Demonstrar habilidades em **manipulação de dados**, **análise estatística**, **visualização gráfica** e **persistência de informações** em um banco de dados SQL.

A tarefa envolve trabalhar com arquivos de séries históricas da **B3** em formato posicional, utilizando:

- **Pandas** para leitura e manipulação dos dados  
- **NumPy** para cálculos estatísticos  
- Geração de **gráficos**  
- Armazenamento das informações em um banco de dados **SQLite**  

Além disso, os dados formatados devem ser externalizados por meio de uma **API RESTful** desenvolvida com **Flask** ou **FastAPI**.

---

## Etapas do Desafio

### Etapa 1: Leitura e Extração dos Dados Posicionais com Pandas
- Utilizar a biblioteca **pandas** para carregar o arquivo posicional da B3.
- Definir o layout do arquivo (colunas e suas respectivas larguras).
- Garantir que os dados sejam carregados corretamente em um **DataFrame**.

---

### Etapa 2: Formatação dos Dados
- Converter os tipos de dados para formatos apropriados (ex.: datas, números decimais).
- Tratar valores ausentes (*missing values*) ou inconsistências.
- Garantir que os dados estejam limpos e prontos para análise.

---

### Etapa 3: Análise Estatística com NumPy
- Utilizar **NumPy** para calcular métricas estatísticas dos dados, como:
  - Média, mediana e desvio padrão dos preços (abertura, fechamento, máxima e mínima).
  - Correlação entre os preços de abertura e fechamento.
  - Identificar o ativo com maior volume médio negociado.
- Gerar tabelas ou gráficos que representem essas análises.

---

### Etapa 4: Geração de Gráficos
- Com base nos dados formatados e nas análises estatísticas, gerar gráficos que representem:
  - Evolução dos preços de abertura, fechamento, máxima e mínima ao longo do tempo.
  - Volume negociado por dia.
  - Distribuição dos preços (histograma).
  - Comparação entre diferentes ativos (se houver mais de um ativo no arquivo).
  - Gráficos baseados nas métricas estatísticas calculadas com NumPy.
- Utilizar bibliotecas como **Matplotlib**, **Seaborn**, **Plotly** ou outras ferramentas de visualização.

---

### Etapa 5: Persistência dos Dados
- Criar um banco de dados **SQLite** para armazenar as informações formatadas.
- Definir uma estrutura de tabelas adequada para os dados históricos.
- Inserir os dados formatados no banco de dados.

---

### Etapa 6: Documentação e Entrega
- Documentar todo o processo, explicando:
  - Como os dados foram extraídos do arquivo posicional.
  - Quais gráficos foram gerados e o que eles representam.
  - Como o banco de dados foi estruturado e populado.
  - Como as análises estatísticas foram realizadas e interpretadas.
- Entregar o código-fonte em **Python** com comentários explicativos.

---

### Etapa 7: Externalização dos Dados via API

#### Objetivo
Permitir que os dados formatados e armazenados no banco de dados SQLite sejam acessados por meio de uma **API RESTful**, desenvolvida com **Flask** ou **FastAPI**.

#### Subetapas

##### 1. Configuração da API
- Escolher entre **Flask** ou **FastAPI** para criar a API.
- Configurar o ambiente de desenvolvimento (instalação das dependências necessárias).

##### 2. Definição das Rotas
Criar rotas para acessar os dados armazenados no banco SQLite:

- `/ativos`  
  Retorna a lista de ativos disponíveis no banco.

- `/ativos/{ativo}`  
  Retorna os dados históricos de um ativo específico.

- `/ativos/{ativo}/estatisticas`  
  Retorna as métricas estatísticas calculadas para o ativo (média, mediana, desvio padrão, correlação, etc.).

- `/ativos/{ativo}/graficos`  
  Retorna links ou imagens dos gráficos gerados para o ativo.

- `/ativos/{ativo}/volume`  
  Retorna o volume negociado por dia para o ativo.

##### 3. Conexão com o Banco SQLite
- Utilizar bibliotecas como **sqlite3** ou **SQLAlchemy** para conectar a API ao banco de dados SQLite.
- Garantir que as consultas ao banco sejam otimizadas e seguras.

##### 4. Serialização dos Dados
- Converter os dados obtidos do banco para o formato **JSON**.
- Garantir que os dados estejam bem estruturados e documentados.

##### 5. Documentação da API
- **Flask**:
  - Criar documentação básica utilizando ferramentas como **Swagger** ou **Flask-RESTPlus**.
- **FastAPI**:
  - Utilizar a documentação automática gerada pelo framework (**Swagger UI** e **Redoc**).

##### 6. Testes da API
- Testar as rotas criadas para garantir que os dados sejam retornados corretamente.
- Validar o desempenho e a segurança da API.
