import os
import subprocess

def executar_scripts_em_pasta(raiz):
    aErrorList = []
    for dirpath, dirnames, filenames in os.walk(raiz):
        for filename in filenames:
            if (filename.endswith('SUITE.py') or filename.endswith('suite.py')) and filename != os.path.basename(__file__):
                caminho_completo = os.path.join(dirpath, filename)
                print(f'\n>>> Executando: {caminho_completo}')
                # Run a suite and capture the result
                result = subprocess.run(['python', caminho_completo])
                if ( result.returncode ) != 0:
                    aErrorList.append(caminho_completo)
    else:
        for erros in aErrorList:
            print(f'\n Falha na execução do teste: {erros}')

# Caminho da pasta onde os scripts estão
caminho_da_pasta = 'D:\\p2410\\tir\\tir-script-samples\\basic_template'  # <-- Altere aqui a pasta raiz contendo todos as nossas suites

executar_scripts_em_pasta(caminho_da_pasta)
