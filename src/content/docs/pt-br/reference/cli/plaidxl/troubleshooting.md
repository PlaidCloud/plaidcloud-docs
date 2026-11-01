---
title: Solução de problemas do PlaidXL
description: "Correções para problemas comuns do PlaidXL: o suplemento ausente da faixa de opções, um pop-up de login que não abre, espaços de trabalho ou projetos ausentes, tabelas exibidas em vermelho, recuperações lentas e erros nas fórmulas do PlaidXL."
sidebar:
  label: Solução de problemas
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## A guia PlaidCloud não está na faixa de opções

- Feche todas as janelas do Excel e abra o Excel novamente. Um suplemento recém-instalado muitas vezes só aparece depois de uma reinicialização.
- Abra **Insert → My Add-ins** e selecione **PlaidCloud**.
- Verifique se você está usando o Excel para desktop do Microsoft 365, ou o Excel 2021 ou posterior. Consulte [Instalar o PlaidXL](/pt-br/reference/cli/plaidxl/install/).
- Se a sua organização gerencia os suplementos, pergunte ao administrador do Microsoft 365 se o suplemento **PlaidCloud** foi implantado para você.

## O pop-up de login não abre

Quando você clica em **Sign In**, o Excel pergunta se deve mostrar uma janela pop-up. Permita. Se você dispensou o aviso, clique em **Sign In** novamente.

Se o pop-up abrir, mas você não conseguir concluir o login, tente fazer login no PlaidCloud no navegador com o mesmo e-mail. Um problema ali, como uma senha expirada ou um dispositivo de dois fatores que você não tem mais, precisa ser corrigido primeiro no PlaidCloud. Consulte [Autenticação de membros](/pt-br/administration/access/member-authentication/).

## Um espaço de trabalho não aparece na lista

**Select a workspace** lista os espaços de trabalho aos quais o seu endereço de e-mail pertence. Se um estiver faltando, confira se você digitou o mesmo e-mail que usa nesse espaço de trabalho e depois peça a um administrador do espaço de trabalho que confirme que você é membro. Consulte [Gerenciamento de membros do espaço de trabalho](/pt-br/administration/access/overview/managing-workspace-members/).

Para mudar para outro espaço de trabalho ao qual você pertence, abra o menu da conta e escolha **Switch workspace**.

## Um projeto, uma tabela ou uma dimensão está faltando

O PlaidXL mostra o que a sua conta pode ver no PlaidCloud. Se um projeto estiver faltando, peça ao proprietário dele que conceda acesso a você. Se uma tabela estiver faltando, verifique se ela existe no projeto selecionado e se foi carregada com dados; uma tabela que nunca foi gravada mostra **Unable to get table metadata** quando você a seleciona.

As pastas nas listas de projetos, tabelas e dimensões começam recolhidas. Digite parte do nome na caixa de filtro no topo da lista para encontrar um item dentro de uma pasta.

## Uma tabela aparece em vermelho

A tabela tem mais linhas ou colunas do que uma planilha do Excel comporta. Selecione **Avançado** para filtrar as linhas e desmarque as colunas de que você não precisa, até que ela caiba. Consulte [Tabelas exibidas em vermelho](/pt-br/reference/cli/plaidxl/retrieve/#tabelas-exibidas-em-vermelho).

## Uma recuperação está lenta

O Excel fica mais lento com tabelas largas. Desmarque as caixas de seleção das colunas de que você não precisa e filtre as linhas com **Avançado**. Recuperar apenas os dados com os quais você trabalha é mais rápido e gera uma pasta de trabalho menor.

## Uma fórmula mostra um erro

| O que você vê | O que verificar |
|---|---|
| `#SPILL!` | Há algo nas células de que o resultado precisa. Limpe as células abaixo ou ao lado da fórmula. |
| `#NAME?` | O Excel não reconhece a função. Verifique se o PlaidXL está instalado (a guia **PlaidCloud** está na faixa de opções) e confira a grafia na [lista de funções](/pt-br/reference/cli/plaidxl/functions/). |
| Um erro de uma função `PLAIDXL` | Verifique se você fez login e se o projeto correto está selecionado e, em seguida, confira todos os nomes de tabela, coluna, dimensão e nó no PlaidCloud; os nomes devem corresponder exatamente. |
| `CELL` informa que uma coluna de filtro não foi encontrada | O primeiro argumento de `DIMENSION_REPR` é uma coluna da tabela, não uma dimensão. Use exatamente o nome da coluna da tabela. Consulte [Valores](/pt-br/reference/cli/plaidxl/functions/#valores). |
| `#VALUE!` de `CELL` ou `CELLS` | Passe o mouse sobre a célula para ler o motivo informado pelo PlaidCloud, como uma coluna desconhecida, um nó que não existe ou não tem membros, ou um problema ao calcular o valor. Confira os nomes no PlaidCloud. |
| `CELL` retorna um total inesperado | Um nó só é consolidado em uma coluna vinculada à sua dimensão; em qualquer outra coluna, ele deve corresponder exatamente a um valor. Confira a coluna e o nó de cada filtro. |
| Os valores não mudam depois que os dados ou o projeto mudam | Force um recálculo completo; no Windows, **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` retorna um erro | Use um destes valores: `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, em minúsculas. |

## As fórmulas retornam dados de outro projeto

As funções do PlaidXL leem do projeto vinculado à pasta de trabalho. Abra o painel de tarefas nessa pasta de trabalho, escolha o projeto para o qual o relatório foi criado e, em seguida, force um recálculo completo. Cada pasta de trabalho tem o seu próprio projeto; assim, escolher um em outra pasta de trabalho não altera este. Consulte [O projeto pertence à pasta de trabalho](/pt-br/reference/cli/plaidxl/retrieve/#o-projeto-pertence-à-pasta-de-trabalho).

## Tabelas de outro espaço de trabalho são ignoradas

Depois que você troca de espaço de trabalho, o painel de tarefas informa quantas tabelas monitoradas pertencem a outro espaço de trabalho e são ignoradas por **Refresh All Tables**. Recupere cada tabela novamente no espaço de trabalho atual para vinculá-la.

## Um salvamento é recusado ou interrompido

| O que você vê | O que fazer |
|---|---|
| Há linhas vazias dentro da tabela | Duas ou mais linhas vazias seguidas, com dados abaixo delas, interrompem um salvamento. Exclua as linhas vazias ou preencha-as e salve novamente. |
| A tabela mudou desde que você a recuperou | Outra pessoa salvou a tabela no PlaidCloud. Recupere-a novamente e reaplique as suas edições. |
| Um valor não pode ser convertido | Nada é gravado e as linhas são listadas. Corrija os valores para que correspondam ao tipo de dados da coluna. |
| A planilha não está vinculada a uma tabela | Recupere primeiro a tabela para a planilha. **Save to PlaidCloud…** aparece apenas para tabelas recuperadas na planilha ativa. |

Para desfazer um salvamento, clique em **Restore previous version** na mensagem de confirmação ou abra a tabela no PlaidCloud e escolha no menu **As of** a versão anterior ao salvamento. O ponto de restauração é mantido por 7 dias. Consulte [Salve uma tabela no PlaidCloud](/pt-br/reference/cli/plaidxl/retrieve/#salve-uma-tabela-no-plaidcloud).

## Relacionados

- [Instalar o PlaidXL](/pt-br/reference/cli/plaidxl/install/)
- [Faça login no PlaidXL](/pt-br/reference/cli/plaidxl/connect/)
- [Obtenção de ajuda](/pt-br/guides/support/getting-help/): abra um tíquete de suporte
