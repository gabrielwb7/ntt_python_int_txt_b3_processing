
# 📊 Tratamento de Dados B3

## 📌 Visão Geral

Este projeto faz parte de um **desafio interno promovido pela NTT Data**, dentro da trilha **Python Intermediate**.
A descrição completa do desafio pode ser consultada no arquivo [desafio.md](./docs/desafio.md).

A solução foi dividida em **duas aplicações independentes**:

* **Processamento e tratamento de dados** (este repositório)
* **API de exposição dos dados tratados** (repositório separado)

Este repositório é responsável exclusivamente pela **leitura, tratamento, validação e persistência** dos dados históricos da B3.

---

## 🎯 Objetivo

O objetivo principal do projeto é automatizar o processamento dos arquivos de **cotações históricas da B3**, seguindo rigorosamente o layout oficial.

### Etapas do processamento

1. Ler o arquivo de cotação histórica em formato TXT
2. Estruturar os dados conforme o layout descrito no documento[SeriesHistoricas_Layout.pdf](./docs/SeriesHistoricas_Layout.pdf)
3. Persistir os dados tratados em um banco de dados **MySQL**

---

## ⚙️ Estratégia de Execução

A aplicação foi pensada para funcionar como um **script automatizado**, podendo ser executado por meio de um **scheduler** (ex.: cron, task scheduler).

Em uma evolução futura (**v2**), a solução poderá ser:

* Containerizada
* Executada em ambiente **AWS**

---

