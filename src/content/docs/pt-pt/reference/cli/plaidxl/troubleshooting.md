---
title: Resolução de problemas do PlaidXL
description: Soluções para problemas comuns do PlaidXL — o suplemento em falta no friso, um pop-up de início de sessão que não abre, áreas de trabalho ou projetos em falta, tabelas a vermelho, obtenções lentas, erros em fórmulas e indicadores do PlaidXL, valores escritos que não são gravados e gravações que param.
sidebar:
  label: Resolução de problemas
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## O separador PlaidCloud não está no friso

- Feche todas as janelas do Excel e volte a abrir o Excel. Um suplemento acabado de instalar aparece muitas vezes apenas depois de reiniciar.
- Abra **Insert → My Add-ins** e selecione **PlaidCloud**.
- Verifique se está a utilizar o Excel para computador do Microsoft 365, ou o Excel 2021 ou posterior. Consulte [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/).
- Se a sua organização gere os suplementos, pergunte ao administrador do Microsoft 365 se o suplemento **PlaidCloud** foi implementado para si.

## O pop-up de início de sessão não abre

Quando clica em **Sign In**, o Excel pergunta se deve mostrar uma janela de pop-up. Permita-a. Se recusou o pedido, clique novamente em **Sign In**.

Se o pop-up abrir mas não conseguir concluir o início de sessão, tente iniciar sessão no PlaidCloud no navegador com o mesmo e-mail. Um problema aí — uma palavra-passe expirada ou um dispositivo de dois fatores que já não tem — tem de ser resolvido primeiro no PlaidCloud. Consulte [Autenticação de membros](/pt-pt/administration/access/member-authentication/).

## Uma área de trabalho não aparece na lista

**Select a workspace** lista as áreas de trabalho a que o seu endereço de e-mail pertence. Se faltar uma, verifique se introduziu o mesmo e-mail que utiliza nessa área de trabalho e peça a um administrador da área de trabalho que confirme que é membro. Consulte [Gerir os membros da área de trabalho](/pt-pt/administration/access/overview/managing-workspace-members/).

Para passar para outra área de trabalho a que pertence, abra o menu da conta e escolha **Switch workspace**.

## Falta um projeto, uma tabela ou uma dimensão

O PlaidXL mostra o que a sua conta pode ver no PlaidCloud. Se faltar um projeto, peça ao respetivo proprietário que lhe dê acesso. Se faltar uma tabela, verifique se existe no projeto selecionado e se foi carregada com dados — uma tabela em que nunca foi escrito nada mostra **Unable to get table metadata** quando a seleciona.

As pastas nas listas de projetos, tabelas e dimensões começam fechadas. Escreva parte do nome na caixa de filtro no topo da lista para encontrar um item dentro de uma pasta.

## Uma tabela aparece a vermelho

A tabela tem mais linhas ou colunas do que uma folha de cálculo do Excel suporta, ou o PlaidCloud não consegue indicar o seu tamanho. Pode obtê-la, e as linhas que não cabem continuam noutras folhas, mas uma tabela dividida por várias folhas não pode ser guardada. Selecione **Avançado** para filtrar as linhas e desmarque as colunas de que não precisa, até caber. Consulte [Tabelas a vermelho](/pt-pt/reference/cli/plaidxl/retrieve/#tabelas-apresentadas-a-vermelho).

## Uma obtenção é lenta

O Excel é mais lento com tabelas largas. Desmarque as caixas das colunas de que não precisa e filtre as linhas com **Avançado**. Obter apenas os dados com que trabalha é mais rápido e produz um livro mais pequeno.

## Uma fórmula mostra um erro

| O que vê | O que verificar |
|---|---|
| `#SPILL!` | Há algo nas células de que o resultado precisa. Limpe as células abaixo ou ao lado da fórmula. |
| `#NAME?` | O Excel não reconhece a função. Verifique se o PlaidXL está instalado — o separador **PlaidCloud** está no friso — e confirme a grafia na [lista de funções](/pt-pt/reference/cli/plaidxl/functions/). |
| Um erro de uma função `PLAIDXL` | Verifique se tem sessão iniciada e se o projeto certo está selecionado, e depois confirme no PlaidCloud o nome de cada tabela, coluna, dimensão e nó — os nomes têm de coincidir exatamente. |
| `CELL` indica que uma coluna de filtro não foi encontrada | O primeiro argumento de `DIMENSION_REPR` é uma coluna da tabela, não uma dimensão. Utilize exatamente o nome da coluna da tabela. Consulte [Valores](/pt-pt/reference/cli/plaidxl/functions/#valores). |
| `#VALUE!` de `METRIC` ou `METRIC_BREAKDOWN` | Passe o rato sobre a célula para ler o motivo. Consulte [Erros de indicadores](/pt-pt/reference/cli/plaidxl/functions/#erros-de-indicadores). |
| `#VALUE!` de um indicador: **This PlaidCloud workspace can't combine an alternate hierarchy with other members yet. Ask your administrator to update the workspace.** | É necessário atualizar a área de trabalho para que um indicador possa combinar um membro de uma hierarquia alternativa com outros membros. Contacte o administrador. As outras células do mesmo recálculo continuam a responder. |
| `#VALUE!` de `CELL` ou `CELLS` | Passe o rato sobre a célula para ler o motivo indicado pelo PlaidCloud, como uma coluna desconhecida, um nó que não existe ou não tem membros, ou um problema no cálculo do valor. Confirme os nomes no PlaidCloud. |
| `CELL` devolve um total inesperado | Um nó só é agregado numa coluna associada à sua dimensão; em qualquer outra coluna tem de coincidir exatamente com um valor. Verifique a coluna e o nó de cada filtro. |
| Os valores não mudam depois de os dados ou o projeto mudarem | Clique em **Recalculate PlaidXL formulas** no menu **Atualizar** do friso. |
| `MEASURE_TYPE` devolve um erro | Utilize um de `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, em minúsculas. |

## As fórmulas devolvem dados de outro projeto

As funções do PlaidXL leem do projeto associado ao livro. Abra o painel de tarefas nesse livro, escolha o projeto para o qual o relatório foi criado e depois clique em **Recalculate PlaidXL formulas** no menu **Atualizar** do friso. Cada livro tem o seu próprio projeto, pelo que escolher um noutro livro não altera este. Consulte [O projeto pertence ao livro](/pt-pt/reference/cli/plaidxl/retrieve/#o-projeto-pertence-ao-livro).

## As tabelas de outra área de trabalho são ignoradas

Depois de mudar de área de trabalho, **Refresh All Tables** indica que as tabelas ou dimensões de outra área de trabalho neste livro não foram atualizadas, e não aparecem em **On this sheet**. Obtenha cada tabela novamente na área de trabalho atual para a associar.

## Um valor escrito não é gravado

Quando escreve sobre uma `CELL`, o painel de tarefas indica o que gravou e lista tudo o que não gravou, com o motivo. Consulte [Escrever valores no PlaidCloud](/pt-pt/reference/cli/plaidxl/write-values/).

| O que vê | O que fazer |
|---|---|
| Só uma célula que contenha apenas uma `PLAIDXL.CELL` aceita um valor escrito | Escreva sobre uma célula cuja fórmula seja uma única `CELL`, opcionalmente multiplicada, dividida ou negada. |
| Um argumento não pode ser lido aqui | Os argumentos da `CELL` têm de ser células ou texto, não outros cálculos. |
| Um método de distribuição, uma forma ou uma retenção aplica-se apenas a somas | Códigos como `E1200`, `1200 like FY2025` e `H` só funcionam em células de **soma**. Escreva um número simples nas outras. |
| Todos os membros retidos | Liberte uma retenção com `H` e depois volte a escrever o valor. |
| A área de trabalho ainda não aceita valores escritos no Excel | Peça ao seu administrador que atualize a área de trabalho. |

## Uma gravação é recusada ou interrompida

Uma gravação escreve de imediato e raramente pára. Pára quando:

| O que vê | O que fazer |
|---|---|
| A linha de cabeçalho já não corresponde às colunas obtidas | Reponha o cabeçalho como foi obtido, ou obtenha a tabela novamente. |
| Um valor não pode ser convertido | Nada é escrito e as linhas são listadas. Corrija os valores para corresponderem ao tipo de dados da coluna. |
| A tabela continua noutras folhas | Uma tabela dividida por várias folhas não pode ser guardada. Obtenha-a com um filtro para que caiba numa só folha. |
| A tabela foi obtida com um filtro que o Save não consegue respeitar | Obtenha-a novamente com um filtro de regras **Igual a** e **in** unidas por **AND**, ou sem filtro. |
| Há linhas fora do seu acesso a linhas | Nada é guardado. Remova essas linhas e guarde novamente. |
| A folha não está associada a uma tabela | Obtenha primeiro a tabela para a folha. Só as tabelas obtidas para a folha ativa aparecem em **On this sheet**. |

Para anular uma gravação, clique em **Anular** na mensagem ou em **Undo last write** no friso. Cada gravação mantém o seu próprio ponto de restauro durante 7 dias, pelo que pode anular qualquer gravação até 7 dias depois de a ter feito. Consulte [Guardar uma tabela no PlaidCloud](/pt-pt/reference/cli/plaidxl/retrieve/#guardar-uma-tabela-no-plaidcloud).

## Ver também

- [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/)
- [Iniciar sessão no PlaidXL](/pt-pt/reference/cli/plaidxl/connect/)
- [Obter ajuda](/pt-pt/guides/support/getting-help/) — abrir um pedido de suporte
