---
title: Call SAP RFC
description: Chame módulos de função RFC do SAP a partir de um passo de fluxo de trabalho do PlaidCloud, para uma integração direta com sistemas SAP ECC e S/4HANA.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-rfc.md
---

## Descrição


Chama uma Remote Function Call (RFC) do SAP ECC / S/4HANA e obtém os dados em formato tabular. Estes dados ficam então disponíveis para processos de transformação na PlaidCloud.


## Destino dos dados

Coloque o resultado da RFC num ficheiro ou numa tabela.

**Ficheiro** escreve o resultado como **JSON**, **Delimitado por vírgulas**, **Delimitado por tabulações**, **Delimitado por barras verticais** ou **Parquet**. Um ficheiro Parquet mantém os mesmos tipos de coluna que uma tabela.

**Tabela** coloca o resultado numa **Tabela de destino**, com tipos obtidos das definições de campos da própria função RFC:

| Tipo de campo SAP | Fica como |
|---|---|
| Data | Data. Uma data em branco ou inicial fica vazia. Uma data inválida fica vazia e o passo termina com um aviso que indica a coluna. |
| Decimal compactado | Decimal exato. Mais de 10 casas decimais ou 28 dígitos inteiros ficam como texto e o passo termina com um aviso que indica a coluna. |
| Inteiro | Inteiro. |
| `FLOAT` | Double. |
| Vírgula flutuante decimal | Texto exato. |
| `NUMC`, `CHAR` | Texto, com os zeros à esquerda mantidos. |
| Hora | Texto, como `HH:MM:SS`. |
| Bytes em bruto | Texto hexadecimal. |
| `UTCLONG` | Texto. |

Se o SAP não conseguir descrever os campos da função, os decimais ficam como texto exato.

Quando o SAP descreve a função, cada parâmetro é convertido para o tipo esperado: datas para `YYYYMMDD`, horas para `HHMMSS`, inteiros e decimais para números, campos de texto para texto, e parâmetros de estrutura e de tabela campo a campo. Um valor que não possa ser convertido para um parâmetro inteiro ou decimal faz o passo falhar.

## Exemplos


### Parâmetros RFC


Selecione o **Agente a utilizar**. Selecione o **Diretório de destino** na lista pendente e navegue abaixo até à subpasta de destino correta para o ficheiro. Em seguida, atribua um nome adequado ao "Nome do ficheiro de destino". Em "Informações da chamada de função", introduza a função e o **Parâmetro do valor de retorno**, e selecione os parâmetros.

Pode optar por **Inserir linha** ou **Acrescentar linha** na secção de parâmetros, bem como dar nome aos parâmetros e atribuir-lhes valores. Escolha o número em **Máximo de pedidos simultâneos** e selecione "Aguardar a conclusão da RFC". **Guardar e executar passo**.



### Iteração de valores avançada


Pode selecionar "Sem iteradores" no topo deste separador e depois **Guardar e executar passo**, se pretender, ou pode especificar.


Aqui, pode selecionar "Especificar valores de argumentos" em **Iterar sobre** e criar argumentos para depois passar ao **Valor da iteração**.


Junto a **Selecione o argumento do iterador para editar os valores**, existe a opção de inserir linha, **Acrescentar linha**, **Eliminar linha**, **Mover para baixo** a linha ou **Mover para o fim** a linha.
Abaixo, pode escolher **Iteradores de intervalo** com o mesmo menu pendente. A última secção chama-se "Exclusões para a iteração de intervalo selecionada",
com as mesmas opções por linha para adicionar, eliminar, etc. Os valores excluídos podem ser introduzidos abaixo. **Guardar e executar passo**.
