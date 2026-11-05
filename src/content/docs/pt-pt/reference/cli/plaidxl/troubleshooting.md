---
title: Resolução de problemas do PlaidXL
description: Soluções para problemas comuns do PlaidXL — o suplemento em falta na faixa de opções, uma janela de início de sessão que não abre, áreas de trabalho ou projetos em falta, tabelas apresentadas a vermelho, obtenções lentas, erros em fórmulas e indicadores do PlaidXL, valores escritos que não são gravados e gravações que são interrompidas.
sidebar:
  label: Resolução de problemas
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## O separador PlaidCloud não está na faixa de opções

- Feche todas as janelas do Excel e volte a abrir o Excel. Um suplemento acabado de instalar surge muitas vezes apenas depois de reiniciar.
- Abra **Inserir → Os meus suplementos** e selecione **PlaidCloud**.
- Verifique se está a utilizar o Excel de ambiente de trabalho para Microsoft 365, ou o Excel 2021 ou posterior. Consulte [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/).
- Se a sua organização gere os suplementos, pergunte ao administrador do Microsoft 365 se o suplemento **PlaidCloud** foi implementado para si.

## A janela de início de sessão não abre

Quando clica em **Iniciar sessão**, o Excel pergunta se deve mostrar uma janela de contexto. Permita-a. Se dispensou a pergunta, clique novamente em **Iniciar sessão**.

Se a janela de contexto abrir mas não conseguir concluir o início de sessão, tente iniciar sessão no PlaidCloud no seu navegador com o mesmo correio eletrónico. Um problema aí — uma palavra-passe expirada ou um dispositivo de dois fatores que já não tem — tem de ser resolvido primeiro no PlaidCloud. Consulte [Autenticação de membros](/pt-pt/administration/access/member-authentication/).

## Uma área de trabalho não está listada

**Select a workspace** lista as áreas de trabalho a que o seu endereço de correio eletrónico pertence. Se faltar uma, verifique se escreveu o mesmo correio eletrónico que utiliza nessa área de trabalho e peça depois a um administrador da área de trabalho que confirme que é membro. Consulte [Gerir os membros da área de trabalho](/pt-pt/administration/access/overview/managing-workspace-members/).

Para passar para outra área de trabalho a que pertence, abra o menu da conta e escolha **Switch workspace**.

## Falta um projeto, uma tabela ou uma dimensão

O PlaidXL mostra o que a sua conta consegue ver no PlaidCloud. Se faltar um projeto, peça ao respetivo proprietário que lhe dê acesso. Se faltar uma tabela, verifique se existe no projeto selecionado e se foi carregada com dados — uma tabela em que nunca foi escrito nada mostra **Unable to get table metadata** quando a seleciona.

As pastas nas listas de projetos, tabelas e dimensões começam reduzidas. Escreva parte do nome na caixa de filtro no topo da lista para encontrar um item dentro de uma pasta.

## Uma tabela aparece a vermelho

A tabela tem mais linhas ou colunas do que uma folha de cálculo do Excel comporta, ou o PlaidCloud não consegue comunicar a sua dimensão. Pode obtê-la, e as linhas que não cabem continuam em folhas adicionais, mas uma tabela repartida por várias folhas não pode ser guardada. Selecione **Avançado** para filtrar as linhas e desmarque as colunas de que não precisa, até caber. Consulte [Tabelas apresentadas a vermelho](/pt-pt/reference/cli/plaidxl/retrieve/#tabelas-apresentadas-a-vermelho).

## Uma obtenção é lenta

O Excel é mais lento com tabelas largas. Desmarque as caixas de verificação das colunas de que não precisa e filtre as linhas com **Avançado**. Obter apenas os dados com que trabalha é mais rápido e produz um livro mais pequeno.

## Uma fórmula mostra um erro

| O que vê | O que verificar |
|---|---|
| `#SPILL!` | Há algo nas células de que o resultado precisa. Limpe as células abaixo ou ao lado da fórmula. |
| `#NAME?` | O Excel não reconhece a função. Verifique se o PlaidXL está instalado — o separador **PlaidCloud** está na faixa de opções — e confirme a ortografia com [a lista de funções](/pt-pt/reference/cli/plaidxl/functions/). |
| Um erro de uma função `PLAIDXL` | Verifique se tem a sessão iniciada e se o projeto correto está selecionado e, depois, confirme todos os nomes de tabelas, colunas, dimensões e nós no PlaidCloud — os nomes têm de corresponder exatamente. |
| `CELL` comunica que não encontra uma coluna de filtro | O primeiro argumento de `DIMENSION_REPR` é uma coluna da tabela, não uma dimensão. Utilize exatamente o nome da coluna da tabela. Consulte [Valores](/pt-pt/reference/cli/plaidxl/functions/#valores). |
| `#VALUE!` de `METRIC` ou `METRIC_BREAKDOWN` | Passe o rato sobre a célula para ler o motivo. Consulte [Erros de indicadores](/pt-pt/reference/cli/plaidxl/functions/#erros-de-indicadores). |
| `#VALUE!` de `CELL` ou `CELLS` | Passe o rato sobre a célula para ler o motivo indicado pelo PlaidCloud, como uma coluna desconhecida, um nó que não existe ou não tem membros, ou um problema no cálculo do valor. Confirme os nomes no PlaidCloud. |
| `CELL` devolve um total inesperado | Um nó só é agregado numa coluna associada à respetiva dimensão; em qualquer outra coluna tem de corresponder exatamente a um valor. Verifique a coluna e o nó de cada filtro. |
| Os valores não mudam depois de os dados ou o projeto mudarem | Clique em **Recalculate PlaidXL formulas** no menu **Atualizar** da faixa de opções. |
| `MEASURE_TYPE` devolve um erro | Utilize um de `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, em minúsculas. |

## As fórmulas devolvem dados de outro projeto

As funções do PlaidXL leem do projeto associado ao livro. Abra o painel de tarefas nesse livro, escolha o projeto para o qual o relatório foi criado e clique depois em **Recalculate PlaidXL formulas** no menu **Atualizar** da faixa de opções. Cada livro tem o seu próprio projeto, pelo que escolher um noutro livro não altera este. Consulte [O projeto pertence ao livro](/pt-pt/reference/cli/plaidxl/retrieve/#o-projeto-pertence-ao-livro).

## As tabelas de outra área de trabalho são ignoradas

Depois de mudar de área de trabalho, **Refresh All Tables** indica que as tabelas ou dimensões de outra área de trabalho neste livro não foram atualizadas, e não estão listadas em **On this sheet**. Obtenha cada tabela novamente na área de trabalho atual para a associar.

## Um valor escrito não é gravado

Quando escreve por cima de um `CELL`, o painel de tarefas indica o que escreveu e lista tudo o que não escreveu, com o motivo. Consulte [Introduzir valores no PlaidCloud](/pt-pt/reference/cli/plaidxl/write-values/).

| O que vê | O que fazer |
|---|---|
| Apenas uma célula que contenha apenas um `PLAIDXL.CELL` aceita um valor escrito | Escreva por cima de uma célula cuja fórmula seja um único `CELL`, opcionalmente multiplicado, dividido ou negado. |
| Não é possível ler um argumento aqui | Os argumentos do `CELL` têm de ser células ou texto, não outros cálculos. |
| Um método de distribuição, forma ou retenção aplica-se apenas a somas | Códigos como `E1200`, `1200 like FY2025` e `H` só funcionam em células **soma**. Nas outras, escreva um número simples. |
| Todos os membros retidos | Liberte uma retenção com `H` e escreva o valor novamente. |
| A área de trabalho ainda não aceita valores escritos no Excel | Peça ao administrador que atualize a área de trabalho. |

## Uma gravação é recusada ou interrompida

Uma gravação escreve de imediato e raramente é interrompida. Isso acontece quando:

| O que vê | O que fazer |
|---|---|
| A linha de cabeçalho já não corresponde às colunas obtidas | Reponha o cabeçalho como estava quando foi obtido, ou obtenha a tabela novamente. |
| Não é possível converter um valor | Nada é escrito e as linhas são listadas. Corrija os valores para corresponderem ao tipo de dados da coluna. |
| A tabela continua noutras folhas | Uma tabela repartida por várias folhas não pode ser guardada. Obtenha-a com um filtro para que caiba numa só folha. |
| A tabela foi obtida com um filtro que a gravação não consegue respeitar | Obtenha-a novamente com um filtro de regras **igual a** e **in** unidas por **AND**, ou sem nenhum. |
| Há linhas fora do seu acesso a linhas | Nada é guardado. Remova essas linhas ou peça a um Arquiteto do projeto que as guarde. |
| A folha não está associada a uma tabela | Obtenha primeiro a tabela para a folha. Apenas as tabelas obtidas para a folha ativa são listadas em **On this sheet**. |

Para anular uma gravação, clique em **Anular** na mensagem ou em **Undo last write** na faixa de opções. O ponto de restauro é mantido durante 7 dias. Consulte [Guardar uma tabela no PlaidCloud](/pt-pt/reference/cli/plaidxl/retrieve/#guardar-uma-tabela-no-plaidcloud).

## Relacionado

- [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/)
- [Iniciar sessão no PlaidXL](/pt-pt/reference/cli/plaidxl/connect/)
- [Obter ajuda](/pt-pt/guides/support/getting-help/) — abra um pedido de suporte
