[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/emy-devfullstack/automation-cnpjs/blob/main/README.md)  
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/emy-devfullstack/automation-cnpjs/blob/main/README.pt-br.md)  

# 📊 Busca de Dados de Atividade a partir do CNPJ

Este script em Python consulta a API pública da Receita Federal para buscar informações sobre o status da atividade de registros de pessoas jurídicas (CNPJs).

## 🚀 Funcionalidades:
- Consulta informações sobre o status de atividade dos CNPJs fornecidos.
- Realiza chamadas assíncronas para otimizar o tempo de execução.
- Trata erros de conexão ou CNPJs inválidos.
- Exporta os resultados para um arquivo Excel na pasta de Downloads.

---

## 📦 Requisitos:
Certifique-se de que possui as bibliotecas necessárias instaladas:
```bash
pip install aiohttp pandas
