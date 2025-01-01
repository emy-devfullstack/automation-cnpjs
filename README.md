[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/emy-devfullstack/automation-cnpjs/blob/main/README.md) [![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/emy-devfullstack/automation-cnpjs/blob/main/README.pt-br.md)  

# 📊 CNPJ Activity Status Retrieval

This Python script queries the public API of the Brazilian Federal Revenue to retrieve information about the activity status of corporate registrations (CNPJs).

## 🚀 Features:
- Queries information about the activity status of provided CNPJs.
- Performs asynchronous calls to optimize execution time.
- Handles connection errors or invalid CNPJs.
- Exports the results to an Excel file in the Downloads folder.

---

## 📦 Requirements:
Make sure you have the necessary libraries installed:
```bash
pip install aiohttp pandas
```

---

## 🛠️ How to use:
1. Copy the source code into a Python file (`consult_cnpjs.py`).
2. Configure the CNPJs in the correct format within the `cnpjs_blocos` block inside the code.
3. Run the script:
```bash
python consult_cnpjs.py
```

## 📄 Output:
An Excel file will be automatically generated in the user's Downloads folder with the following fields:

- CNPJ: Queried CNPJ number.
- Status: CNPJ status as returned by the Federal Revenue API.

Example output in Excel:
| **CNPJ**           | **Status**         |
|---------------------|--------------------|
| 33.000.167/0001-01 | Ativo              |
| 00.000.000/0001-91 | Suspenso           |
| 60.701.190/0001-04 | Erro: Não encontrado |

---

## 🌐 Notes:
- The script pauses between request blocks to avoid exceeding API request limits.
- The API used is public and may have usage limitations.
