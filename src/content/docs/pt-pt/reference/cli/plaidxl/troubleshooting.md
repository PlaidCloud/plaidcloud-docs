---
title: Resolução de problemas do PlaidXL
description: Soluções para problemas comuns do PlaidXL — o suplemento em falta no friso, uma janela de início de sessão que não abre, áreas de trabalho ou projetos em falta, tabelas apresentadas a vermelho, extrações lentas, erros em fórmulas e indicadores do PlaidXL, valores escritos que não são gravados e gravações que param.
sidebar:
  label: Resolução de problemas
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## O separador PlaidCloud não está no friso

- Feche todas as janelas do Excel e volte a abrir o Excel. Um suplemento recém-instalado aparece muitas vezes apenas depois de um reinício.
- Abra **Inserir → Os meus suplementos** e selecione **PlaidCloud**.
- Verifique se está a utilizar o Excel para computador do Microsoft 365, ou o Excel 2021 ou posterior. Consulte [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/).
- Se a sua organização gere os suplementos, pergunte ao administrador do Microsoft 365 se o suplemento **PlaidCloud** foi implementado para si.

## O pop-up de início de sessão não abre

Quando clica em **Sign In**, o Excel pergunta se deve mostrar uma janela. Permita-o. Se ignorou a pergunta, clique novamente em **Sign In**.

Se a janela abrir mas não conseguir concluir o início de sessão, tente iniciar sessão no PlaidCloud no navegador com o mesmo correio eletrónico. Um problema aí — uma palavra-passe expirada ou um dispositivo de autenticação de dois fatores que já não tem — tem de ser resolvido primeiro no PlaidCloud. Consulte [Autenticação de membros](/pt-pt/administration/access/member-authentication/).

## Uma área de trabalho não aparece na lista

**Select a workspace** lista as áreas de trabalho a que o seu endereço de correio eletrónico pertence. Se faltar uma, verifique se escreveu o mesmo correio eletrónico que utiliza nessa área de trabalho e, em seguida, peça a um administrador da área de trabalho que confirme que é membro. Consulte [Gerir os membros da área de trabalho](/pt-pt/administration/access/overview/managing-workspace-members/).

Para passar para outra área de trabalho a que pertença, abra o menu da conta e escolha **Switch workspace**.

## Falta um projeto, uma tabela ou uma dimensão

O PlaidXL mostra o que a sua conta consegue ver no PlaidCloud. Se faltar um projeto, peça ao respetivo proprietário que lhe dê acesso. Se faltar uma tabela, verifique se existe no projeto selecionado e se foi carregada com dados — uma tabela que nunca foi escrita mostra **Unable to get table metadata** quando a seleciona.

As pastas nas listas de projetos, tabelas e dimensões começam recolhidas. Escreva parte do nome na caixa de filtro, no topo da lista, para encontrar um item dentro de uma pasta.

## Uma tabela aparece a vermelho

A tabela tem mais linhas ou colunas do que uma folha de cálculo do Excel suporta, ou o PlaidCloud não consegue indicar a sua dimensão. Pode extraí-la, e as linhas que não cabem continuam noutras folhas, mas uma tabela dividida por várias folhas não pode ser guardada. Selecione **Avançado** para filtrar as linhas e desmarque as colunas de que não necessita até que caiba. Consulte [Tabelas apresentadas a vermelho](/pt-pt/reference/cli/plaidxl/retrieve/#tabelas-apresentadas-a-vermelho).

## Uma obtenção é lenta

O Excel é mais lento com tabelas largas. Desmarque as caixas de verificação das colunas de que não necessita e filtre as linhas com **Avançado**. Extrair apenas os dados com que trabalha é mais rápido e produz um livro mais pequeno.

As tabelas grandes são extraídas e atualizadas muito mais depressa no Excel na Web e no Excel para computador atual. As versões mais antigas do Excel continuam a funcionar, mas sem esta aceleração.

Se o painel indicar **PlaidXL was updated — reload the pane**, feche o painel de tarefas, volte a abri-lo e extraia novamente. Depois de o PlaidXL ser atualizado, o painel adota a nova versão da próxima vez que é carregado.

Se uma extração indicar **This PlaidCloud workspace needs an update for PlaidXL**, peça ao administrador que atualize a área de trabalho para uma versão atual do PlaidCloud.

## Uma fórmula mostra um erro

| O que vê | O que verificar |
|---|---|
| `#SPILL!` | Existe algo nas células de que o resultado necessita. Limpe as células abaixo ou ao lado da fórmula. |
| `#NAME?` | O Excel não reconhece a função. Verifique se o PlaidXL está instalado — o separador **PlaidCloud** está no friso — e confirme a ortografia na [lista de funções](/pt-pt/reference/cli/plaidxl/functions/). |
| Um erro de uma função `PLAIDXL` | Verifique se iniciou sessão e se o projeto correto está selecionado e, em seguida, confirme no PlaidCloud todos os nomes de tabelas, colunas, dimensões e nós — os nomes têm de corresponder exatamente. |
| `CELL` indica que não encontra uma coluna de filtro | O primeiro argumento de `DIMENSION_REPR` é uma coluna da tabela, não uma dimensão. Utilize exatamente o nome da coluna da tabela. Consulte [Valores](/pt-pt/reference/cli/plaidxl/functions/#valores). |
| `#VALUE!` de `METRIC` ou `METRIC_BREAKDOWN` | Passe o rato sobre a célula para ler o motivo. Consulte [Erros de indicadores](/pt-pt/reference/cli/plaidxl/functions/#erros-de-indicadores). |
| `#VALUE!` de um indicador: **This PlaidCloud workspace can't combine an alternate hierarchy with other members yet. Ask your administrator to update the workspace.** | A área de trabalho tem de ser atualizada para que um indicador possa combinar um membro de uma hierarquia alternativa com outros membros. Pergunte ao administrador. As outras células no mesmo recálculo continuam a responder. |
| `#VALUE!` de `CELL` ou `CELLS` | Passe o rato sobre a célula para ler o motivo indicado pelo PlaidCloud, como uma coluna desconhecida, um nó que não existe ou que não tem membros, ou um problema no cálculo do valor. Confirme os nomes no PlaidCloud. |
| `CELL` devolve um total inesperado | Um nó só é agregado numa coluna associada à sua dimensão; em qualquer outra coluna tem de corresponder exatamente a um valor. Verifique a coluna e o nó de cada filtro. |
| Os valores não mudam depois de os dados ou o projeto mudarem | Clique em **Recalculate PlaidXL formulas** no menu **Atualizar** do friso. |
| `MEASURE_TYPE` devolve um erro | Utilize um de `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, em minúsculas. |

## As fórmulas devolvem dados de outro projeto

As funções do PlaidXL leem do projeto associado ao livro. Abra o painel de tarefas nesse livro, escolha o projeto para o qual o relatório foi criado e, em seguida, clique em **Recalculate PlaidXL formulas** no menu **Atualizar** do friso. Cada livro tem o seu próprio projeto, pelo que escolher um noutro livro não altera este. Consulte [O projeto pertence ao livro](/pt-pt/reference/cli/plaidxl/retrieve/#o-projeto-pertence-ao-livro).

## As tabelas de outra área de trabalho são ignoradas

Depois de mudar de área de trabalho, **Refresh All Tables** indica que as tabelas ou dimensões de outra área de trabalho neste livro não foram atualizadas, e não são listadas em **On this sheet**. Extraia cada tabela novamente na área de trabalho atual para a associar.

## Um valor escrito não é gravado

Quando escreve por cima de uma `CELL`, o painel de tarefas indica o que escreveu e lista tudo o que não escreveu, com o motivo. Consulte [Escrever valores no PlaidCloud](/pt-pt/reference/cli/plaidxl/write-values/).

| O que vê | O que fazer |
|---|---|
| Apenas uma célula que contenha uma única `PLAIDXL.CELL` aceita um valor escrito | Escreva por cima de uma célula cuja fórmula seja uma única `CELL`, opcionalmente multiplicada, dividida ou negada. |
| Não é possível ler um argumento aqui | Os argumentos da `CELL` têm de ser células ou texto, não outros cálculos. |
| Um método de distribuição, uma forma ou uma retenção aplica-se apenas a somas | Códigos como `E1200`, `1200 like FY2025` e `H` só funcionam em células de **soma**. Escreva um número simples nas restantes. |
| Todos os membros retidos | Liberte uma retenção com `H` e, em seguida, escreva novamente o valor. |
| A área de trabalho ainda não aceita valores escritos no Excel | Peça ao administrador que atualize a área de trabalho. |

## Uma gravação é recusada ou interrompida

Uma gravação é escrita de imediato e raramente é interrompida. Interrompe-se quando:

| O que vê | O que fazer |
|---|---|
| A linha de cabeçalho já não corresponde às colunas extraídas | Reponha o cabeçalho como foi extraído, ou extraia a tabela novamente. |
| Não é possível converter um valor | Nada é escrito e as linhas são listadas. Corrija os valores para corresponderem ao tipo de dados da coluna. |
| A tabela continua noutras folhas | Uma tabela dividida por várias folhas não pode ser guardada. Extraia-a com um filtro para que caiba numa única folha. |
| A tabela foi extraída com um filtro que a gravação não consegue respeitar | Extraia-a novamente com um filtro de regras **igual a** e **em** unidas por **AND**, ou sem filtro. |
| Existem linhas fora do seu acesso às linhas | Nada é guardado. Remova essas linhas e guarde novamente. |
| As colunas contêm texto mais longo do que os 32 767 carateres de uma célula do Excel | O Excel mostra o texto truncado, e guardar truncá-lo-ia também no PlaidCloud, pelo que a opção de guardar fica desativada para esta tabela. Extraia a tabela sem essas colunas para a guardar. |
| A tabela foi escrita apenas parcialmente | O Excel recusou parte da última atualização. Atualize a tabela e, em seguida, guarde-a. |
| A folha não está associada a uma tabela | Extraia primeiro a tabela para a folha. Apenas as tabelas extraídas para a folha ativa são listadas em **On this sheet**. |

Para anular uma gravação, clique em **Anular** na mensagem ou em **Undo last write** no friso. Cada gravação mantém o seu próprio ponto de restauro durante 7 dias, pelo que pode anular qualquer gravação até 7 dias depois de a fazer. Consulte [Guardar uma tabela no PlaidCloud](/pt-pt/reference/cli/plaidxl/retrieve/#guardar-uma-tabela-no-plaidcloud).

## Ver também

- [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/)
- [Iniciar sessão no PlaidXL](/pt-pt/reference/cli/plaidxl/connect/)
- [Obter ajuda](/pt-pt/guides/support/getting-help/) — abra um pedido de suporte
