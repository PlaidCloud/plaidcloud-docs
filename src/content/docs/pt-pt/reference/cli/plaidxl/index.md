---
title: PlaidXL
description: Utilize o suplemento PlaidXL para Excel para iniciar sessão na sua área de trabalho PlaidCloud, trazer tabelas de projeto e hierarquias de dimensões para folhas de cálculo, criar relatórios em direto, detalhar e explicar números, ler indicadores governados, planear escrevendo valores de volta no PlaidCloud e perguntar ao Weave.
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

O PlaidXL é o suplemento do PlaidCloud para o Microsoft Excel. Liga um livro à sua área de trabalho PlaidCloud, para que os seus modelos e relatórios leiam de tabelas de projeto e dimensões de referência, e não de uma cópia que fica desatualizada na próxima vez que um fluxo de trabalho for executado.

Pode trabalhar com o PlaidXL de três formas, e a maioria dos livros utiliza todas:

- **O painel de tarefas** — navegue pelos seus projetos, escolha uma tabela ou dimensão, escolha colunas e filtros e obtenha os dados para uma folha de cálculo. Atualizar mantém-nos atuais, e **Save to PlaidCloud** escreve de volta uma tabela editada. Outros separadores criam uma fórmula ou um relatório completo por si, explicam de onde vem um número e permitem perguntar ao Weave por palavras suas.
- **Funções personalizadas** — fórmulas como `=PLAIDXL.TABLE.GET_TABLE("Sales")`, `=PLAIDXL.CELL(...)` e `=PLAIDXL.METRIC("Net Revenue")` que leem dados do PlaidCloud diretamente para as células. Utilize-as para listar tabelas e dimensões, dispor uma hierarquia, calcular valores agregados para um relatório e ler indicadores governados.
- **A faixa de opções e o menu de contexto** — detalhe uma dimensão a partir de qualquer célula, escolha membros, atualize, explique um número ou mostre as linhas por trás dele, com um atalho de teclado para cada um.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="O Excel contém o painel de tarefas do PlaidXL e as funções personalizadas do PlaidXL. Ambos enviam pedidos, com a sessão iniciada em seu nome, a um projeto da sua área de trabalho PlaidCloud, que devolve linhas de tabelas, hierarquias de dimensões e valores agregados para as células da folha de cálculo." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="px-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="20" y="20" width="250" height="190" rx="10" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Livro do Excel</text>
  <rect x="40" y="62" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="84" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Painel de tarefas do PlaidXL</text>
  <text x="145" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">navegar, filtrar, obter, atualizar</text>
  <rect x="40" y="130" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="152" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Funções PLAIDXL.*</text>
  <text x="145" y="170" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">tabelas, hierarquias, valores em células</text>
  <rect x="410" y="40" width="230" height="150" rx="10" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Área de trabalho PlaidCloud</text>
  <rect x="430" y="80" width="190" height="94" rx="8" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="102" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Projeto</text>
  <text x="525" y="124" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">tabelas</text>
  <text x="525" y="142" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">dimensões e hierarquias</text>
  <path d="M252 98 L405 98" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">sessão iniciada como si</text>
  <path d="M405 150 L254 150" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="168" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">linhas, nós, valores</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">O painel de tarefas e as funções personalizadas leem ambos do projeto que seleciona, com as suas próprias permissões no PlaidCloud.</figcaption>
</figure>

O PlaidXL lê do PlaidCloud e só altera uma tabela de projeto quando for o próprio a escrever nela: escreva um número por cima de um valor `CELL` ou guarde uma folha obtida com **Save to PlaidCloud**. Ambas as ações são escritas de imediato, e **Undo last write** reverte-as. Consulte [Introduzir valores no PlaidCloud](/pt-pt/reference/cli/plaidxl/write-values/).

## Requisitos

- Excel para Microsoft 365, ou Excel 2021 ou posterior, no Windows ou no Mac. O separador PlaidCloud da faixa de opções, o menu de contexto e o painel de tarefas funcionam no Excel de ambiente de trabalho.
- Uma conta PlaidCloud em pelo menos uma área de trabalho e acesso aos projetos que pretende ler. O PlaidXL mostra apenas os projetos, as tabelas e as dimensões que a sua conta já consegue ver no PlaidCloud.

## Tópicos

- [Instalar](/pt-pt/reference/cli/plaidxl/install/) — adicione o PlaidXL ao Excel e abra o painel de tarefas
- [Iniciar sessão](/pt-pt/reference/cli/plaidxl/connect/) — ligue-se à sua área de trabalho, termine a sessão e mude de área de trabalho
- [Trabalhar com tabelas e dimensões](/pt-pt/reference/cli/plaidxl/retrieve/) — escolha um projeto, filtre uma tabela, obtenha-a para uma folha, atualize-a e guarde-a de volta
- [Funções personalizadas](/pt-pt/reference/cli/plaidxl/functions/) — todas as funções `PLAIDXL`, os seus argumentos e o que devolvem
- [Criar um relatório](/pt-pt/reference/cli/plaidxl/build-a-report/) — estruture um relatório em direto a partir do painel de tarefas ou com fórmulas
- [Detalhar, escolher membros e explicar números](/pt-pt/reference/cli/plaidxl/drill/) — detalhe a partir de uma célula, escolha membros, explique um número e mostre as respetivas linhas de detalhe
- [Introduzir valores no PlaidCloud](/pt-pt/reference/cli/plaidxl/write-values/) — planeie escrevendo por cima dos valores do relatório e anule qualquer escrita
- [Perguntar ao Weave no Excel](/pt-pt/reference/cli/plaidxl/weave/) — crie, detalhe e corrija a partir de pedidos em linguagem corrente
- [A faixa de opções do PlaidCloud](/pt-pt/reference/cli/plaidxl/ribbon/) — todos os comandos, o menu de contexto e os atalhos de teclado
- [Resolução de problemas](/pt-pt/reference/cli/plaidxl/troubleshooting/) — soluções para os problemas mais comuns

É novo no PlaidXL? O tutorial [Trabalhar no Excel com o PlaidXL](/pt-pt/get-started/tutorials/excel-with-plaidxl/) leva-o da instalação do suplemento a um primeiro relatório em cerca de 20 minutos.

## Relacionado

- [Projetos](/pt-pt/guides/projects/) — o que um projeto contém e como encontrar um
- [Tabelas e vistas](/pt-pt/guides/data/tables-views/) — as tabelas que o PlaidXL obtém
- [Utilizar dimensões](/pt-pt/guides/dimensions/dimensions/) — as hierarquias que o PlaidXL dispõe e agrega
