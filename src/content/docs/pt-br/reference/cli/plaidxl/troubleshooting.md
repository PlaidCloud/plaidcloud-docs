---
title: Solução de problemas do PlaidXL
description: Correções para problemas comuns do PlaidXL — o suplemento ausente da faixa de opções, um pop-up de login que não abre, espaços de trabalho ou projetos ausentes, tabelas mostradas em vermelho, recuperações lentas, erros em fórmulas e métricas do PlaidXL, valores digitados que não são gravados e salvamentos que são interrompidos.
sidebar:
  label: Solução de problemas
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## A guia PlaidCloud não está na faixa de opções

- Feche todas as janelas do Excel e abra o Excel de novo. Um suplemento recém-instalado muitas vezes só aparece depois de uma reinicialização.
- Abra **Inserir → Meus Suplementos** e selecione **PlaidCloud**.
- Verifique se você está usando o Excel para desktop do Microsoft 365, ou o Excel 2021 ou posterior. Consulte [Instalar o PlaidXL](/pt-br/reference/cli/plaidxl/install/).
- Se a sua organização gerencia suplementos, pergunte ao administrador do Microsoft 365 se o suplemento **PlaidCloud** foi implantado para você.

## O pop-up de login não abre

Quando você clica em **Sign In**, o Excel pergunta se deve mostrar uma janela pop-up. Permita. Se você dispensou o aviso, clique em **Sign In** de novo.

Se o pop-up abre mas você não consegue concluir o login, tente entrar no PlaidCloud no navegador com o mesmo e-mail. Um problema ali — uma senha expirada ou um dispositivo de dois fatores que você não tem mais — precisa ser corrigido primeiro no PlaidCloud. Consulte [Autenticação de membros](/pt-br/administration/access/member-authentication/).

## Um espaço de trabalho não aparece na lista

**Select a workspace** lista os espaços de trabalho aos quais o seu endereço de e-mail pertence. Se algum estiver faltando, verifique se você digitou o mesmo e-mail que usa nesse espaço de trabalho e depois peça a um administrador do espaço de trabalho que confirme que você é membro. Consulte [Gerenciar membros do espaço de trabalho](/pt-br/administration/access/overview/managing-workspace-members/).

Para passar para outro espaço de trabalho ao qual você pertence, abra o menu da conta e escolha **Switch workspace**.

## Um projeto, tabela ou dimensão está faltando

O PlaidXL mostra o que a sua conta pode ver no PlaidCloud. Se um projeto estiver faltando, peça ao proprietário dele que lhe dê acesso. Se uma tabela estiver faltando, verifique se ela existe no projeto selecionado e se foi carregada com dados — uma tabela que nunca recebeu gravações mostra **Unable to get table metadata** quando você a seleciona.

As pastas nas listas de projetos, tabelas e dimensões começam recolhidas. Digite parte do nome na caixa de filtro no topo da lista para encontrar um item dentro de uma pasta.

## Uma tabela aparece em vermelho

A tabela tem mais linhas ou colunas do que uma planilha do Excel comporta, ou o PlaidCloud não consegue informar o tamanho dela. Você pode recuperá-la, e as linhas que não cabem continuam em outras planilhas, mas uma tabela dividida em várias planilhas não pode ser salva. Selecione **Avançado** para filtrar as linhas e desmarque as colunas de que você não precisa até que ela caiba. Consulte [Tabelas mostradas em vermelho](/pt-br/reference/cli/plaidxl/retrieve/#tabelas-mostradas-em-vermelho).

## Uma recuperação está lenta

O Excel é mais lento com tabelas largas. Desmarque as caixas de seleção das colunas de que você não precisa e filtre as linhas com **Avançado**. Recuperar apenas os dados com que você trabalha é mais rápido e gera uma pasta de trabalho menor.

## Uma fórmula mostra um erro

| O que você vê | O que verificar |
|---|---|
| `#SPILL!` | Há algo nas células de que o resultado precisa. Limpe as células abaixo ou ao lado da fórmula. |
| `#NAME?` | O Excel não reconhece a função. Verifique se o PlaidXL está instalado — a guia **PlaidCloud** está na faixa de opções — e confira a grafia na [lista de funções](/pt-br/reference/cli/plaidxl/functions/). |
| Um erro de uma função `PLAIDXL` | Verifique se você está conectado e se o projeto certo está selecionado e depois confira no PlaidCloud todos os nomes de tabelas, colunas, dimensões e nós — os nomes devem corresponder exatamente. |
| `CELL` informa que uma coluna de filtro não foi encontrada | O primeiro argumento de `DIMENSION_REPR` é uma coluna da tabela, não uma dimensão. Use exatamente o nome da coluna da tabela. Consulte [Valores](/pt-br/reference/cli/plaidxl/functions/#valores). |
| `#VALUE!` de `METRIC` ou `METRIC_BREAKDOWN` | Passe o ponteiro sobre a célula para ler o motivo. Consulte [Erros de métrica](/pt-br/reference/cli/plaidxl/functions/#erros-de-métrica). |
| `#VALUE!` de `CELL` ou `CELLS` | Passe o ponteiro sobre a célula para ler o motivo informado pelo PlaidCloud, como uma coluna desconhecida, um nó que não existe ou não tem membros, ou um problema ao calcular o valor. Confira os nomes no PlaidCloud. |
| `CELL` retorna um total inesperado | Um nó só é consolidado em uma coluna vinculada à sua dimensão; em qualquer outra coluna ele deve corresponder exatamente a um valor. Verifique a coluna e o nó de cada filtro. |
| Os valores não mudam depois que os dados ou o projeto mudam | Clique em **Recalculate PlaidXL formulas** no menu **Atualizar** da faixa de opções. |
| `MEASURE_TYPE` retorna um erro | Use um destes: `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, em minúsculas. |

## As fórmulas retornam dados de outro projeto

As funções do PlaidXL leem do projeto vinculado à pasta de trabalho. Abra o painel de tarefas nessa pasta de trabalho, escolha o projeto para o qual o relatório foi criado e depois clique em **Recalculate PlaidXL formulas** no menu **Atualizar** da faixa de opções. Cada pasta de trabalho tem o seu próprio projeto; portanto, escolher um em outra pasta de trabalho não altera este. Consulte [O projeto pertence à pasta de trabalho](/pt-br/reference/cli/plaidxl/retrieve/#o-projeto-pertence-à-pasta-de-trabalho).

## Tabelas de outro espaço de trabalho são ignoradas

Depois que você troca de espaço de trabalho, **Refresh All Tables** informa que tabelas ou dimensões de outro espaço de trabalho nesta pasta de trabalho não foram atualizadas, e elas não aparecem em **On this sheet**. Recupere cada tabela de novo no espaço de trabalho atual para vinculá-la.

## Um valor digitado não é gravado

Quando você digita sobre um `CELL`, o painel de tarefas diz o que gravou e lista o que não gravou, com o motivo. Consulte [Digitar valores no PlaidCloud](/pt-br/reference/cli/plaidxl/write-values/).

| O que você vê | O que fazer |
|---|---|
| Apenas uma célula que contém um único `PLAIDXL.CELL` aceita um valor digitado | Digite sobre uma célula cuja fórmula seja um único `CELL`, opcionalmente multiplicado, dividido ou negado. |
| Um argumento não pode ser lido aqui | Os argumentos do `CELL` devem ser células ou texto, não outros cálculos. |
| Um método de distribuição, formato ou retenção se aplica apenas a somas | Códigos como `E1200`, `1200 like FY2025` e `H` funcionam apenas em células **sum**. Digite um número simples nas demais. |
| Todos os membros retidos | Libere a retenção com `H` e digite o valor de novo. |
| O espaço de trabalho ainda não aceita valores digitados no Excel | Peça ao administrador que atualize o espaço de trabalho. |

## Um salvamento é recusado ou interrompido

Um salvamento grava imediatamente e raramente é interrompido. Ele é interrompido quando:

| O que você vê | O que fazer |
|---|---|
| A linha de cabeçalho não corresponde mais às colunas recuperadas | Coloque o cabeçalho de volta como foi recuperado ou recupere a tabela de novo. |
| Um valor não pode ser convertido | Nada é gravado e as linhas são listadas. Corrija os valores para corresponder ao tipo de dados da coluna. |
| A tabela continua em outras planilhas | Uma tabela dividida em várias planilhas não pode ser salva. Recupere-a com um filtro para que caiba em uma planilha. |
| A tabela foi recuperada com um filtro que o salvamento não consegue respeitar | Recupere-a de novo com um filtro de regras **igual a** e **em** unidas por **AND**, ou sem filtro. |
| Há linhas fora do seu acesso a linhas | Nada é salvo. Remova essas linhas ou peça a um Arquiteto do projeto que as salve. |
| A planilha não está vinculada a uma tabela | Recupere primeiro a tabela para a planilha. Apenas as tabelas recuperadas para a planilha ativa são listadas em **On this sheet**. |

Para desfazer um salvamento, clique em **Desfazer** na mensagem ou em **Undo last write** na faixa de opções. O ponto de restauração é mantido por 7 dias. Consulte [Salvar uma tabela no PlaidCloud](/pt-br/reference/cli/plaidxl/retrieve/#salvar-uma-tabela-no-plaidcloud).

## Relacionado

- [Instalar o PlaidXL](/pt-br/reference/cli/plaidxl/install/)
- [Entrar no PlaidXL](/pt-br/reference/cli/plaidxl/connect/)
- [Obter ajuda](/pt-br/guides/support/getting-help/) — abra um tíquete de suporte
