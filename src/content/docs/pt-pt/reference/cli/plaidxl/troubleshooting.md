---
title: Resolução de problemas do PlaidXL
description: Soluções para problemas comuns do PlaidXL — o suplemento em falta no friso, uma janela instantânea de início de sessão que não abre, áreas de trabalho ou projetos em falta, tabelas apresentadas a vermelho, obtenções lentas e erros em fórmulas PlaidXL.
sidebar:
  label: Resolução de problemas
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## O separador PlaidCloud não está no friso

- Feche todas as janelas do Excel e volte a abrir o Excel. Um suplemento acabado de instalar aparece muitas vezes apenas após um reinício.
- Abra **Inserir → Os meus suplementos** e selecione **PlaidCloud**.
- Verifique se está a utilizar o Excel para computador do Microsoft 365, ou o Excel 2021 ou posterior. Consulte [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/).
- Se a sua organização gere os suplementos, pergunte ao administrador do Microsoft 365 se o suplemento **PlaidCloud** está implementado para si.

## A janela instantânea de início de sessão não abre

Quando clica em **Iniciar sessão**, o Excel pergunta se deve mostrar uma janela instantânea. Permita-a. Se ignorou o pedido, clique novamente em **Iniciar sessão**.

Se a janela instantânea abrir mas não conseguir concluir o início de sessão, experimente iniciar sessão no PlaidCloud no navegador com o mesmo correio eletrónico. Um problema aí — uma palavra-passe expirada ou um dispositivo de dois fatores que já não tem — tem de ser corrigido primeiro no PlaidCloud. Consulte [Autenticação de membros](/pt-pt/administration/access/member-authentication/).

## Uma área de trabalho não está listada

**Select a workspace** lista as áreas de trabalho a que o seu endereço de correio eletrónico pertence. Se faltar uma, verifique se escreveu o mesmo correio eletrónico que utiliza nessa área de trabalho e, depois, peça a um administrador da área de trabalho que confirme que é membro. Consulte [Gerir membros da área de trabalho](/pt-pt/administration/access/overview/managing-workspace-members/).

Para passar para outra área de trabalho a que pertença, abra o menu da conta e escolha **Switch workspace**.

## Um projeto, uma tabela ou uma dimensão está em falta

O PlaidXL mostra o que a sua conta consegue ver no PlaidCloud. Se faltar um projeto, peça ao respetivo proprietário que lhe dê acesso. Se faltar uma tabela, verifique se existe no projeto selecionado e se foi carregada com dados — uma tabela que nunca foi escrita mostra **Unable to get table metadata** quando a seleciona.

As pastas nas listas de projetos, tabelas e dimensões começam recolhidas. Escreva parte do nome na caixa de filtro no topo da lista para encontrar um item dentro de uma pasta.

## Uma tabela é apresentada a vermelho

A tabela tem mais linhas ou colunas do que uma folha de cálculo do Excel suporta. Selecione **Avançado** para filtrar as linhas e desmarque as colunas de que não precisa, até caber. Consulte [Tabelas apresentadas a vermelho](/pt-pt/reference/cli/plaidxl/retrieve/#tabelas-apresentadas-a-vermelho).

## Uma obtenção é lenta

O Excel é mais lento com tabelas largas. Desmarque as caixas de verificação das colunas de que não precisa e filtre as linhas com **Avançado**. Obter apenas os dados com que trabalha é mais rápido e produz um livro mais pequeno.

## Uma fórmula mostra um erro

| O que vê | O que verificar |
|---|---|
| `#SPILL!` | Há algo nas células de que o resultado precisa. Limpe as células abaixo ou ao lado da fórmula. |
| `#NAME?` | O Excel não reconhece a função. Verifique se o PlaidXL está instalado — o separador **PlaidCloud** está no friso — e verifique a grafia na [lista de funções](/pt-pt/reference/cli/plaidxl/functions/). |
| Um erro de uma função `PLAIDXL` | Verifique se tem a sessão iniciada e se o projeto correto está selecionado e, depois, verifique cada nome de tabela, coluna, dimensão e nó no PlaidCloud — os nomes têm de corresponder exatamente. |
| `CELL` indica que não encontra uma coluna de filtro | O primeiro argumento de `DIMENSION_REPR` é uma coluna da tabela, não uma dimensão. Utilize exatamente o nome da coluna da tabela. Consulte [Valores](/pt-pt/reference/cli/plaidxl/functions/#valores). |
| `#VALUE!` de `CELL` ou `CELLS` | Passe o rato sobre a célula para ler o motivo indicado pelo PlaidCloud, como uma coluna desconhecida, um nó que não existe ou não tem membros, ou um problema no cálculo do valor. Verifique os nomes no PlaidCloud. |
| `CELL` devolve um total inesperado | Um nó só é agregado numa coluna associada à respetiva dimensão; em qualquer outra coluna tem de corresponder exatamente a um valor. Verifique a coluna e o nó de cada filtro. |
| Os valores não mudam após a alteração dos dados ou do projeto | Force um recálculo completo — no Windows, **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` devolve um erro | Utilize um de `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, em minúsculas. |

## As fórmulas devolvem dados de outro projeto

As funções do PlaidXL leem do projeto associado ao livro. Abra o painel de tarefas nesse livro, escolha o projeto para o qual o relatório foi criado e, depois, force um recálculo completo. Cada livro tem o seu próprio projeto, pelo que escolher um noutro livro não altera este. Consulte [O projeto pertence ao livro](/pt-pt/reference/cli/plaidxl/retrieve/#o-projeto-pertence-ao-livro).

## As tabelas de outra área de trabalho são ignoradas

Depois de mudar de área de trabalho, o painel de tarefas indica quantas tabelas controladas pertencem a outra área de trabalho e são ignoradas por **Refresh All Tables**. Volte a obter cada tabela na área de trabalho atual para a associar.

## Uma gravação é recusada ou interrompida

| O que vê | O que fazer |
|---|---|
| Há linhas vazias dentro da tabela | Duas ou mais linhas vazias seguidas, com dados abaixo, interrompem uma gravação. Elimine as linhas vazias ou preencha-as e, depois, guarde novamente. |
| A tabela mudou desde que a obteve | Outra pessoa guardou a tabela no PlaidCloud. Volte a obtê-la e reaplique as suas edições. |
| Não é possível converter um valor | Nada é escrito e as linhas são listadas. Corrija os valores para corresponderem ao tipo de dados da coluna. |
| A folha não está associada a uma tabela | Obtenha primeiro a tabela para a folha. **Save to PlaidCloud…** só aparece para tabelas obtidas para a folha ativa. |

Para anular uma gravação, clique em **Restore previous version** na mensagem de confirmação ou abra a tabela no PlaidCloud e escolha a versão anterior à gravação no menu **As of**. O ponto de restauro é mantido durante 7 dias. Consulte [Guardar uma tabela no PlaidCloud](/pt-pt/reference/cli/plaidxl/retrieve/#guardar-uma-tabela-no-plaidcloud).

## Relacionado

- [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/)
- [Iniciar sessão no PlaidXL](/pt-pt/reference/cli/plaidxl/connect/)
- [Obter ajuda](/pt-pt/guides/support/getting-help/) — abra um pedido de suporte
