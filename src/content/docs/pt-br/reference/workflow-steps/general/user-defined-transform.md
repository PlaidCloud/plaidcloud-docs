---
title: User Defined Transform (etapa)
description: Crie transformações de dados personalizadas com código Python em uma etapa de fluxo de trabalho do PlaidCloud, para uma lógica de processamento de dados flexível e poderosa.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/user-defined-transform.md
---

## Descrição

As **Transformações padrão de fluxo de trabalho** que acompanham o PlaidCloud normalmente conseguem realizar quase todas as operações de que você precisa. Além disso, essas transformações padrão são continuamente otimizadas para desempenho e oferecem os dados mais robustos. No entanto, quando as opções padrão, usadas isoladamente ou em grupo, não atingem seus objetivos, você pode criar **User Defined Transforms** para atender às suas necessidades. O PlaidCloud permite usar código Python padrão, incluindo muitos pacotes avançados.

É necessário programar em Python para criar uma User Defined Transform, que é executada no Python 3.14. Para mais informações, visite o [site do Python.](https://www.python.org/)



## User Defined Transforms

Há duas maneiras de criar funções definidas pelo usuário (UDF):
 - Escrever e manter a lógica diretamente no PlaidCloud
 - Conectar-se a um repositório Git e apontar para um arquivo

Além do Python padrão, todas as funções da API do PlaidCloud estão prontamente disponíveis para interagir nativamente com o PlaidCloud.  Pacotes de análise avançada como SciPy, PySpark, Pandas e muitos outros estão prontos para importação.

### Escrever e manter uma UDF armazenada no PlaidCloud
Para criar uma nova função definida pelo usuário (UDF), abra o fluxo de trabalho que precisa da transformação personalizada, selecione a guia **Definido pelo usuário** e clique no botão **Add User Defined Function**. Especifique um ID para a UDF. Depois de criada, selecione o ícone Editar lógica da função (o mais à esquerda) para abrir a janela “Editar função definida pelo usuário”.

Como alternativa, uma função definida pelo usuário criada anteriormente pode ser importada com o botão **Importar** dentro da guia **Definido pelo usuário**. Basta pressionar esse botão e selecionar o fluxo de trabalho apropriado no menu suspenso (esse menu contém todos os fluxos de trabalho do espaço de trabalho atual). Em seguida, selecione a(s) função(ões) a importar e pressione o botão **Import Selected Functions**.

Depois que a função for criada/importada, vá para a guia **Analyze Steps** do fluxo de trabalho e adicione uma etapa **User Defined Transform** na posição apropriada, exatamente como você adicionaria uma **Transformação padrão**. Na janela de configuração, selecione UDF do Analyze como o tipo e, em seguida, selecione a **Função definida pelo usuário** apropriada no menu suspenso.

### Referenciar uma UDF em um repositório Git

Primeiro, você precisará criar uma conexão com o repositório Git (por exemplo, Github, Gitlab etc.) na área **Conexões de dados externas**.

Quando a conexão com o repositório Git estiver disponível, vá para a guia **Analyze Steps** do fluxo de trabalho e adicione uma etapa **User Defined Transform** na posição apropriada, exatamente como você adicionaria uma **Transformação padrão**. Na janela de configuração, selecione Repositório externo de código-fonte como o tipo e, em seguida, selecione a Conexão, o Branch e o Caminho do arquivo da UDF.  A seleção de Branch também permite selecionar tags, para viabilizar processos de release padrão.

As alterações nos arquivos no Git serão refletidas automaticamente na próxima vez que a UDF for executada.

## Configuração das tabelas de origem e de destino
Embora seja possível acessar tabelas diretamente em uma UDF sem defini-las na configuração da User Defined Transform, as dependências das tabelas não estarão disponíveis.  Por isso, recomenda-se definir na configuração todas as origens e destinos de tabelas usados na UDF.  Definir as tabelas na configuração também as torna prontamente disponíveis para uso dentro da UDF de forma mais simples (veja abaixo).

## Especificação de variáveis adicionais
As variáveis de nível de projeto e de fluxo de trabalho estão disponíveis dentro da UDF por meio dos métodos padrão da API; no entanto, muitas vezes há variáveis adicionais, específicas da etapa, que são úteis.  Elas podem ser definidas na seção **Outras variáveis** da configuração.

Os valores das variáveis podem ser definidos manualmente ou de forma dinâmica, usando combinações de variáveis de projeto e de fluxo de trabalho.

## Exemplos de UDF em Python

### Importações comuns com configuração da conexão com a API do PlaidCloud

```python
### COMMON PYTHON IMPORTS
# import os
# import pandas as pd
# import numpy as np

### COMMON PLAIDCLOUD IMPORTS
from plaidcloud.utilities.connect import PlaidConnection
from plaidcloud.utilities import frame_manager as fm
# from plaidcloud.utilities import data_helpers as dh

conn = PlaidConnection()
```

### Definir mensagens de log no log do aplicativo
```python
conn.logger.info('Sample Info Log Message')
conn.logger.warn('Sample Warning Log Message')
conn.logger.error('Sample Error Log Message')
```

### Acessar variáveis de projeto e de fluxo de trabalho
```python
workflow_vars = conn.analyze.workflow.variable_values(project_id=conn.project_id, workflow_id=conn.workflow_id)
variable_1 = workflow_vars.get('my_wf_var_1')

project_vars = conn.analyze.project.variable_values(project_id=conn.project_id)
variable_2 = project_vars.get('my_prj_var_2')
```

### Salvar dados em uma tabela
Este exemplo pressupõe que os dados existem em um dataframe do Pandas.

```python
fm.save(dfImport, name='/path_to_table/OUTBOUND_TABLE_NAME', append=False)
```

### Ler dados de uma tabela

Para usar uma tabela, primeiro você precisa obter o objeto da tabela.  Com o objeto em mãos, você pode consultá-lo usando o método `get_data()`.  O método `get_data()` também aceita a sintaxe do SQLAlchemy, para viabilizar a criação de consultas avançadas.  O resultado da consulta é um objeto dataframe do Pandas.

```python
tbl_object = conn.get_table('INBOUND_TABLE_NAME')
dfImport = conn.get_data(tbl_object)
dfImportQuery = conn.get_data(
    tblImport.select().with_only_columns(
        [tblImport.c.Col1, tblImport.c.Col2]
    ).where(
        tblImport.c.Col1 == 'FilterValue'
    )
)
```

### Acessar dados das tabelas de origem e de destino definidas
Ao usar tabelas de origem e de destino definidas que foram configuradas na configuração da etapa, a busca inicial do objeto (isto é, `get_table()`) é realizada automaticamente.  Usar as tabelas pré-configuradas segue este processo:

```python
# Source Tables as a dict
my_source = conn.udf.source_by_name('my_table')

# All sources as a list
my_sources = conn.udf.sources()

# Target Tables as a dict
my_target = conn.udf.target_by_name('my_table')

# All targets as a list
my_targets = conn.udf.targets()
```

### Acessar variáveis da etapa
Acessar as variáveis definidas na configuração da etapa é feito pelo seguinte processo:

```python
# Access variables by name
my_var = conn.udf.variable_by_name('my_var')

# All variables as a list
my_vars = conn.udf.variables()
```

### Ler arquivos do Document
Acessar arquivos no Document também é simples usando a conexão do PlaidCloud.  Este é um exemplo de função que obtém o conteúdo do arquivo e o salva em um caminho local no contêiner de execução.

```python
def get_from_document(conn, document_account, remote_path, local_file_path):
    # accounts = conn.document.view.shared_accounts()
    remote_file = base64.b64decode(
        conn.document.view.download(
            account_id=document_account,
            path=remote_path,
        )
    )
    with open(local_file_path, 'wb') as output_file:
        output_file.write(remote_file)

    return local_file_path
```
