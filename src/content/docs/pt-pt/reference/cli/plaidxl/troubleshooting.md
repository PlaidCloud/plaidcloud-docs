---
title: Resolução de problemas do PlaidXL
description: Soluções para problemas comuns do PlaidXL — o suplemento em falta no friso, um pop-up de início de sessão que não abre, áreas de trabalho ou projetos em falta, tabelas apresentadas a vermelho, obtenções lentas e erros em fórmulas PlaidXL.
sidebar:
  label: Resolução de problemas
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## O separador PlaidCloud não está no friso

- Feche todas as janelas do Excel e volte a abri-lo. Um suplemento recém-instalado aparece muitas vezes apenas após um reinício.
- Abra **Insert → My Add-ins** e selecione **PlaidCloud**.
- Verifique se está a utilizar o Excel para computador do Microsoft 365, ou o Excel 2021 ou posterior. Consulte [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/).
- Se a sua organização gere os suplementos, pergunte ao administrador do Microsoft 365 se o suplemento **PlaidCloud** foi implementado para si.

## O pop-up de início de sessão não abre

Quando clica em **Sign In**, o Excel pergunta se deve mostrar uma janela de pop-up. Permita-a. Se tiver ignorado a pergunta, clique novamente em **Sign In**.

Se o pop-up abrir mas não conseguir concluir o início de sessão, tente iniciar sessão no PlaidCloud no seu navegador com o mesmo e-mail. Um problema aí — uma palavra-passe expirada ou um dispositivo de dois fatores que já não tem — tem de ser resolvido primeiro no PlaidCloud. Consulte [Autenticação de membros](/pt-pt/administration/access/member-authentication/).

## Uma área de trabalho não aparece na lista

**Select a tenant** lista as áreas de trabalho a que o seu endereço de e-mail pertence. Se faltar alguma, verifique se escreveu o mesmo e-mail que usa nessa área de trabalho e peça a um administrador da área de trabalho que confirme que é membro. Consulte [Gerir membros da área de trabalho](/pt-pt/administration/access/overview/managing-workspace-members/).

Para passar para outra área de trabalho a que pertença, clique em **Logout** e inicie sessão novamente.

## Falta um projeto, uma tabela ou uma dimensão

O PlaidXL mostra o que a sua conta consegue ver no PlaidCloud. Se faltar um projeto, peça ao respetivo proprietário que lhe dê acesso. Se faltar uma tabela, verifique se existe no projeto selecionado e se foi carregada com dados — uma tabela em que nunca se escreveu mostra **Unable to get table metadata** quando a seleciona.

As pastas nas listas de projetos, tabelas e dimensões começam recolhidas. Escreva parte do nome na caixa de filtro no topo da lista para encontrar um item dentro de uma pasta.

## Uma tabela aparece a vermelho

A tabela tem mais linhas ou colunas do que uma folha de cálculo do Excel comporta. Selecione **Avançado** para filtrar as linhas e desmarque as colunas de que não precisa, até caber. Consulte [Tabelas apresentadas a vermelho](/pt-pt/reference/cli/plaidxl/retrieve/#tabelas-apresentadas-a-vermelho).

## Uma obtenção é lenta

O Excel é mais lento com tabelas largas. Desmarque as caixas das colunas de que não precisa e filtre as linhas com **Avançado**. Obter apenas os dados com que trabalha é mais rápido e produz um livro mais pequeno.

## Uma fórmula mostra um erro

| O que vê | O que verificar |
|---|---|
| `#SPILL!` | Há algo nas células de que o resultado precisa. Limpe as células abaixo ou ao lado da fórmula. |
| `#NAME?` | O Excel não reconhece a função. Verifique se o PlaidXL está instalado — o separador **PlaidCloud** está no friso — e confirme a grafia na [lista de funções](/pt-pt/reference/cli/plaidxl/functions/). |
| Um erro de uma função `PLAIDXL` | Verifique se tem sessão iniciada e se o projeto certo está selecionado e, em seguida, confirme no PlaidCloud todos os nomes de tabelas, colunas, dimensões e nós — os nomes têm de corresponder exatamente. |
| `CELL` indica que não encontra uma coluna de filtro | O primeiro argumento de `DIMENSION_REPR` é uma coluna da tabela, não uma dimensão. Utilize exatamente o nome da coluna da tabela. Consulte [Valores](/pt-pt/reference/cli/plaidxl/functions/#valores). |
| `CELL` devolve 0 ou um total inesperado | Confirme o nome do nó na dimensão — um nó que não existe não agrega nada e devolve 0. Um nó só é agregado numa coluna associada à respetiva dimensão; em qualquer outra coluna tem de corresponder exatamente a um valor. |
| Os valores não mudam depois de os dados ou o projeto mudarem | Force um novo cálculo completo — no Windows, **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` devolve um erro | Utilize um de `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, em minúsculas. |

## As fórmulas devolvem dados de outro projeto

As funções do PlaidXL leem do projeto selecionado no painel de tarefas, e essa seleção é partilhada por todos os livros que tenha abertos. Selecione o projeto para o qual o relatório foi criado e force um novo cálculo completo. **Definir como predefinição** guarda um projeto no livro, de modo que fica selecionado quando abre aí o painel de tarefas. Consulte [Definir um projeto predefinido](/pt-pt/reference/cli/plaidxl/retrieve/#definir-um-projeto-predefinido).

## Ver também

- [Instalar o PlaidXL](/pt-pt/reference/cli/plaidxl/install/)
- [Iniciar sessão no PlaidXL](/pt-pt/reference/cli/plaidxl/connect/)
- [Obter ajuda](/pt-pt/guides/support/getting-help/) — abra um pedido de suporte
