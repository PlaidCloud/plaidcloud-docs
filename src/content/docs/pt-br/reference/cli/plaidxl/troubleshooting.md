---
title: Solução de problemas do PlaidXL
description: Soluções para problemas comuns do PlaidXL — suplemento ausente da faixa de opções, pop-up de login que não abre, espaços de trabalho ou projetos ausentes, tabelas exibidas em vermelho, recuperações lentas e erros em fórmulas do PlaidXL.
sidebar:
  label: Solução de problemas
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/troubleshooting.md
---

## A guia PlaidCloud não está na faixa de opções

- Feche todas as janelas do Excel e abra o Excel novamente. Um suplemento recém-instalado muitas vezes só aparece após a reinicialização.
- Abra **Insert → My Add-ins** e selecione **PlaidCloud**.
- Verifique se você está usando o Excel para desktop do Microsoft 365, ou o Excel 2021 ou posterior. Consulte [Instalar o PlaidXL](/pt-br/reference/cli/plaidxl/install/).
- Se a sua organização gerencia os suplementos, pergunte ao administrador do Microsoft 365 se o suplemento **PlaidCloud** foi implantado para você.

## O pop-up de login não abre

Quando você clica em **Sign In**, o Excel pergunta se deve exibir uma janela pop-up. Permita. Se você dispensou o aviso, clique em **Sign In** novamente.

Se o pop-up abrir, mas você não conseguir concluir o login, tente fazer login no PlaidCloud no seu navegador com o mesmo e-mail. Um problema ali — uma senha expirada ou um dispositivo de dois fatores que você não tem mais — precisa ser corrigido primeiro no PlaidCloud. Consulte [Autenticação de membros](/pt-br/administration/access/member-authentication/).

## Um espaço de trabalho não está listado

**Select a tenant** lista os espaços de trabalho aos quais o seu endereço de e-mail pertence. Se um estiver faltando, verifique se você digitou o mesmo e-mail que usa nesse espaço de trabalho e peça a um administrador do espaço de trabalho que confirme que você é membro. Consulte [Gerenciamento de membros do espaço de trabalho](/pt-br/administration/access/overview/managing-workspace-members/).

Para passar para outro espaço de trabalho ao qual você pertence, clique em **Logout** e faça login novamente.

## Um projeto, uma tabela ou uma dimensão está ausente

O PlaidXL mostra o que a sua conta pode ver no PlaidCloud. Se um projeto estiver faltando, peça ao proprietário que conceda acesso a você. Se uma tabela estiver faltando, verifique se ela existe no projeto selecionado e se foi carregada com dados — uma tabela que nunca foi gravada mostra **Unable to get table metadata** quando você a seleciona.

As pastas nas listas de projetos, tabelas e dimensões começam recolhidas. Digite parte do nome na caixa de filtro no topo da lista para encontrar um item dentro de uma pasta.

## Uma tabela aparece em vermelho

A tabela tem mais linhas ou colunas do que uma planilha do Excel comporta. Selecione **Avançado** para filtrar as linhas e desmarque as colunas de que você não precisa até que ela caiba. Consulte [Tabelas exibidas em vermelho](/pt-br/reference/cli/plaidxl/retrieve/#tabelas-exibidas-em-vermelho).

## Uma recuperação está lenta

O Excel é mais lento com tabelas largas. Desmarque as caixas de seleção das colunas de que você não precisa e filtre as linhas com **Avançado**. Recuperar apenas os dados com os quais você trabalha é mais rápido e gera uma pasta de trabalho menor.

## Uma fórmula mostra um erro

| O que você vê | O que verificar |
|---|---|
| `#SPILL!` | Há algo nas células de que o resultado precisa. Limpe as células abaixo ou ao lado da fórmula. |
| `#NAME?` | O Excel não reconhece a função. Verifique se o PlaidXL está instalado — a guia **PlaidCloud** está na faixa de opções — e confira a grafia na [lista de funções](/pt-br/reference/cli/plaidxl/functions/). |
| Um erro de uma função `PLAIDXL` | Verifique se você fez login e se o projeto correto está selecionado; depois, confira no PlaidCloud o nome de cada tabela, coluna, dimensão e nó — os nomes devem corresponder exatamente. |
| `CELL` informa que uma coluna de filtro não foi encontrada | O primeiro argumento de `DIMENSION_REPR` é uma coluna da tabela, não uma dimensão. Use exatamente o nome da coluna da tabela. Consulte [Valores](/pt-br/reference/cli/plaidxl/functions/#valores). |
| `CELL` retorna 0 ou um total inesperado | Confira o nome do nó na dimensão — um nó que não existe não consolida nada e retorna 0. Um nó só é consolidado em uma coluna vinculada à sua dimensão; em qualquer outra coluna, ele deve corresponder exatamente a um valor. |
| Os valores não mudam depois que os dados ou o projeto mudam | Force um recálculo completo — no Windows, **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` retorna um erro | Use um destes: `sum`, `mean`, `median`, `min`, `max`, `std` ou `var`, em minúsculas. |

## As fórmulas retornam dados de outro projeto

As funções do PlaidXL leem do projeto selecionado no painel de tarefas, e essa seleção é compartilhada por todas as pastas de trabalho que você tiver abertas. Selecione o projeto para o qual o relatório foi criado e force um recálculo completo. **Definir como padrão** salva um projeto na pasta de trabalho, de modo que ele seja selecionado quando você abrir o painel de tarefas ali. Consulte [Definir um projeto padrão](/pt-br/reference/cli/plaidxl/retrieve/#definir-um-projeto-padrão).

## Relacionados

- [Instalar o PlaidXL](/pt-br/reference/cli/plaidxl/install/)
- [Fazer login no PlaidXL](/pt-br/reference/cli/plaidxl/connect/)
- [Obter ajuda](/pt-br/guides/support/getting-help/) — abra um chamado de suporte
