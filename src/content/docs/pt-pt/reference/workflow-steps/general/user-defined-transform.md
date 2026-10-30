---
title: User Defined Transform
description: Crie transformações de dados personalizadas com código Python num passo de fluxo de trabalho do PlaidCloud, para uma lógica de processamento de dados flexível e poderosa.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/user-defined-transform.md
---

## Descrição

As **transformações padrão de fluxo de trabalho** incluídas no PlaidCloud conseguem, em regra, realizar praticamente todas as operações de que precisa. Além disso, estas transformações padrão são otimizadas continuamente quanto ao desempenho e fornecem os dados mais robustos. No entanto, quando as opções padrão, utilizadas isoladamente ou em conjunto, não permitem atingir os seus objetivos, pode criar **transformações definidas pelo utilizador** para satisfazer as suas necessidades. O PlaidCloud permite utilizar código Python padrão, incluindo muitos pacotes avançados.

É necessário programar em Python para criar uma User Defined Transform, que é executada em Python 3.14. Para mais informações, visite o [sítio Web do Python.](https://www.python.org/)



## Transformações definidas pelo utilizador

Existem duas formas de criar funções definidas pelo utilizador (UDF):
 - Escrever e manter a lógica diretamente no PlaidCloud
 - Ligar a um repositório Git e indicar um ficheiro

Além de Python padrão, todas as funções da API do PlaidCloud estão prontamente disponíveis para interagir nativamente com o PlaidCloud.  Pacotes de análise avançada como SciPy, PySpark, Pandas e muitos outros estão prontos a importar.

### Escrever e manter uma UDF armazenada no PlaidCloud
Para criar uma nova função definida pelo utilizador (UDF), abra o fluxo de trabalho que precisa da transformação personalizada, selecione o separador **Definido pelo utilizador** e clique no botão **Add User Defined Function**. Especifique um ID para a UDF. Depois de criada, selecione o ícone Edit function logic (o primeiro à esquerda) para abrir a janela “Edit User Defined Function”.

Em alternativa, uma função definida pelo utilizador criada anteriormente pode ser importada com o botão **Importar** a partir do separador **Definido pelo utilizador**. Basta premir esse botão e selecionar o fluxo de trabalho adequado no menu pendente (este menu contém todos os fluxos de trabalho da área de trabalho atual). Em seguida, selecione a(s) função(ões) a importar e prima o botão **Import Selected Functions**.

Depois de a função ter sido criada/importada, avance para o separador **Analyze Steps** do fluxo de trabalho e adicione um passo **User Defined Transform** na posição adequada, tal como adicionaria uma **transformação padrão**. Na janela de configuração, selecione a UDF do Analyze como tipo e, em seguida, selecione a **Função definida pelo utilizador** adequada no menu pendente.

### Referenciar uma UDF num repositório Git

Primeiro, tem de criar uma ligação ao repositório Git (por exemplo, Github, Gitlab, etc...) na área **Ligações de dados externas**.

Quando a ligação ao repositório Git estiver disponível, avance para o separador **Analyze Steps** do fluxo de trabalho e adicione um passo **User Defined Transform** na posição adequada, tal como adicionaria uma **transformação padrão**. Na janela de configuração, selecione Repositório externo de código-fonte como tipo e, em seguida, selecione a Ligação, o Ramo e o Caminho do ficheiro da UDF.  A seleção do ramo também permite selecionar etiquetas (tags), para suportar processos de lançamento padrão.

As alterações aos ficheiros no Git serão refletidas automaticamente da próxima vez que a UDF for executada.

## Configuração das tabelas de origem e de destino
Embora seja possível aceder diretamente a tabelas numa UDF sem as definir na configuração da transformação UDF, as dependências das tabelas não ficarão disponíveis.  Por isso, recomenda-se que todas as tabelas de origem e de destino utilizadas na UDF sejam definidas na configuração.  Definir as tabelas na configuração também as torna prontamente disponíveis para utilização na UDF de uma forma mais direta (ver abaixo).

## Especificação de variáveis adicionais
As variáveis ao nível do projeto e do fluxo de trabalho estão disponíveis na UDF através dos métodos padrão da API; no entanto, existem frequentemente variáveis adicionais, específicas do passo, que são úteis.  Estas podem ser definidas na secção **Outras variáveis** da configuração.

Os valores das variáveis podem ser definidos manualmente ou de forma dinâmica, através de combinações de variáveis do projeto e do fluxo de trabalho.

## Exemplos de UDF em Python

### Importações comuns com configuração da ligação à API do PlaidCloud

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

### Definir mensagens de registo no registo da aplicação
```python
conn.logger.info('Sample Info Log Message')
conn.logger.warn('Sample Warning Log Message')
conn.logger.error('Sample Error Log Message')
```

### Aceder às variáveis do projeto e do fluxo de trabalho
```python
workflow_vars = conn.analyze.workflow.variable_values(project_id=conn.project_id, workflow_id=conn.workflow_id)
variable_1 = workflow_vars.get('my_wf_var_1')

project_vars = conn.analyze.project.variable_values(project_id=conn.project_id)
variable_2 = project_vars.get('my_prj_var_2')
```

### Guardar dados numa tabela
Este exemplo pressupõe que os dados existem num dataframe do Pandas.

```python
fm.save(dfImport, name='/path_to_table/OUTBOUND_TABLE_NAME', append=False)
```

### Ler dados de uma tabela

Para utilizar uma tabela, primeiro é preciso obter o objeto da tabela.  Depois de ter o objeto, pode consultá-lo com o método `get_data()`.  O método `get_data()` também suporta a sintaxe SQLAlchemy, para permitir a construção de consultas avançadas.  O resultado da consulta é um objeto dataframe do Pandas.

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

### Aceder a dados das tabelas de origem e de destino definidas
Quando se utilizam tabelas de origem e de destino definidas que foram configuradas na configuração do passo, a obtenção inicial do objeto (isto é, `get_table()`) é efetuada automaticamente.  A utilização das tabelas pré-configuradas segue o seguinte processo:

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

### Aceder às variáveis do passo
O acesso às variáveis definidas na configuração do passo faz-se através do seguinte processo:

```python
# Access variables by name
my_var = conn.udf.variable_by_name('my_var')

# All variables as a list
my_vars = conn.udf.variables()
```

### Ler ficheiros do Document
O acesso a ficheiros no Document também é simples com a ligação do PlaidCloud.  Este é um exemplo de uma função que obtém o conteúdo do ficheiro e o guarda num caminho local no contentor de execução.

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
