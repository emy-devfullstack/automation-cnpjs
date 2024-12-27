import asyncio
import aiohttp
import pandas as pd
import os
from pathlib import Path
import time

cnpjs_blocos = [
    ["33.000.167/0001-01", "00.000.000/0001-91", "60.701.190/0001-04"],
    ["07.526.557/0001-00", "33.592.510/0001-54", "47.960.950/0001-21"]
]

async def consultar_cnpj(session, cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj.replace('.', '').replace('/', '').replace('-', '')}"
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()
            if "status" in data and data["status"] == "ERROR":
                return {"CNPJ": cnpj, "Status": f"Erro: {data.get('message', 'Erro desconhecido')}"}
            return {"CNPJ": cnpj, "Status": data.get("situacao", "Status desconhecido")}
    except Exception as e:
        return {"CNPJ": cnpj, "Status": f"Erro: {str(e)}"}

async def processar_blocos(cnpjs_blocos):
    resultados = []
    async with aiohttp.ClientSession() as session:
        for bloco in cnpjs_blocos:
            tarefas = [consultar_cnpj(session, cnpj) for cnpj in bloco]
            bloc_resultados = await asyncio.gather(*tarefas)
            resultados.extend(bloc_resultados)
            await asyncio.sleep(60)
            await asyncio.sleep(3)

    return resultados

resultados = asyncio.run(processar_blocos(cnpjs_blocos))

df = pd.DataFrame(resultados)

downloads_path = Path(os.path.expanduser("~")) / "Downloads"
arquivo_excel = downloads_path / "CNPJs_Status.xlsx"

df.to_excel(arquivo_excel, index=False)

print(f"Arquivo gerado com sucesso: {arquivo_excel}")
