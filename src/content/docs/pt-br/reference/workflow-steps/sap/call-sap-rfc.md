---
title: Etapa Call SAP RFC
description: Chame módulos de função RFC do SAP a partir de uma etapa de fluxo de trabalho do PlaidCloud para integração direta com os sistemas SAP ECC e S/4HANA.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-rfc.md
---

## Descrição


Chama uma Remote Function Call (RFC) do SAP ECC / S/4HANA e recupera os dados em formato tabular. Esses dados ficam disponíveis para os processos de transformação no PlaidCloud.


## Destino dos dados

Grave o resultado da RFC em um arquivo ou em uma tabela.

**Arquivo** grava o resultado como **JSON**, **Delimitado por vírgulas**, **Delimitado por tabulações**, **Delimitado por barras verticais** ou **Parquet**. Um arquivo Parquet mantém os mesmos tipos de coluna de uma tabela.

**Tabela** grava o resultado em uma **Tabela de destino**, com tipos definidos a partir das definições de campo da própria função RFC:

| Tipo de campo do SAP | Como é gravado |
|---|---|
| Data | Data. Uma data em branco ou inicial é gravada vazia. Uma data inválida é gravada vazia, e a etapa termina com um aviso que indica a coluna. |
| Decimal compactado | Decimal exato. Mais de 10 casas decimais ou 28 dígitos inteiros são gravados como texto, e a etapa termina com um aviso que indica a coluna. |
| Inteiro | Inteiro. |
| `FLOAT` | Double. |
| Float decimal | Texto exato. |
| `NUMC`, `CHAR` | Texto, com os zeros à esquerda mantidos. |
| Hora | Texto, no formato `HH:MM:SS`. |
| Bytes brutos | Texto hexadecimal. |
| `UTCLONG` | Texto. |

Se o SAP não conseguir descrever os campos da função, os decimais são gravados como texto exato.

Quando o SAP descreve a função, cada parâmetro é convertido para o tipo esperado: datas para `YYYYMMDD`, horas para `HHMMSS`, inteiros e decimais para números, campos de texto para texto e parâmetros de estrutura e de tabela campo a campo. Um valor que não pode ser convertido para um parâmetro inteiro ou decimal faz a etapa falhar.

## Exemplos


### Parâmetros RFC


Selecione o Agente a usar. Selecione Diretório de destino na lista suspensa e navegue abaixo até a pasta filha correta de destino do arquivo. Em seguida, dê um nome apropriado ao “Target File Name”. Em “Function Call Information”, informe a função (Function), o Parâmetro de valor de retorno e selecione os parâmetros.

Você pode optar por Inserir linha ou Anexar linha na seção de parâmetros, além de nomear os parâmetros e atribuir valores a eles. Escolha o número de Máx. de solicitações simultâneas e selecione Wait for RFC to Complete. Clique em Salvar e executar etapa.



### Iteração avançada de valores


Você pode selecionar “No Iterators” na parte superior desta guia e, em seguida, clicar em Salvar e executar etapa, se quiser, ou pode especificar iteradores.


Aqui, você pode selecionar “Specify Argument Values” em Iterar sobre e criar argumentos para depois ir ao Valor da iteração.


Ao lado de Selecione o argumento iterador para editar os valores, há as opções Inserir linha, Anexar linha, Excluir linha, Mover para baixo e Mover para o final. Abaixo, você pode escolher Iteradores de intervalo usando a mesma lista suspensa. A última seção se chama “Exclusions for Selected Range Iteration”, com as mesmas opções por linha para adicionar, excluir etc. Os valores excluídos podem ser informados abaixo. Clique em Salvar e executar etapa.
