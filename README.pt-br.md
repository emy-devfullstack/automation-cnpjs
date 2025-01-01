[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/emy-devfullstack/automation-cnpjs/blob/main/README.md) [![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/emy-devfullstack/automation-cnpjs/blob/main/README.pt-br.md)  

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
```

---

## 🛠️ Como usar:
1. Copie o código-fonte para um arquivo Python (consultar_cnpjs.py).
2. Configure os CNPJs no formato correto no bloco cnpjs_blocos dentro do código.
3. Execute o script:
```bash
python consultar_cnpjs.py
```

## 📄 Saída:
Um arquivo Excel será gerado automaticamente na pasta Downloads do usuário com os seguintes campos:

- CNPJ: Número do CNPJ consultado.
- Status: Situação do CNPJ conforme retornado pela Receita Federal.

Exemplo de saída no Excel:
| **CNPJ**           | **Status**         |
|---------------------|--------------------|
| 33.000.167/0001-01 | Ativo              |
| 00.000.000/0001-91 | Suspenso           |
| 60.701.190/0001-04 | Erro: Não encontrado |

---

## 🌐 Observações:
- O script realiza pausas entre blocos de consultas para evitar exceder limites de requisição da API.
- A API utilizada é pública e pode ter limitações de uso.
