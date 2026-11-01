---
title: PlaidXL
description: Utilize o suplemento PlaidXL do Excel para iniciar sessão na sua área de trabalho PlaidCloud, obter tabelas de projeto e hierarquias de dimensões para folhas de cálculo, atualizá-las a pedido e criar relatórios em direto com as funções personalizadas do PlaidXL.
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

O PlaidXL é o suplemento do PlaidCloud para o Microsoft Excel. Liga um livro à sua área de trabalho PlaidCloud, para que os seus modelos e relatórios leiam de tabelas de projeto e dimensões de referência, e não de uma cópia que fica desatualizada da próxima vez que um fluxo de trabalho for executado.

Pode trabalhar com o PlaidXL de duas formas, e a maioria dos livros utiliza ambas:

- **O painel de tarefas** — navegue pelos seus projetos, escolha uma tabela ou dimensão, selecione colunas e filtros e obtenha os dados para uma folha de cálculo. **Refresh All Tables** obtém os dados atuais de todas as tabelas que já obteve e **Save to PlaidCloud…** grava de volta uma tabela editada. O separador **Formulas** cria uma fórmula PlaidXL por si.
- **Funções personalizadas** — fórmulas como `=PLAIDXL.TABLE.GET_TABLE("Sales")` e `=PLAIDXL.CELL(...)` que leem os dados do PlaidCloud diretamente para células. Utilize-as para listar tabelas e dimensões, dispor uma hierarquia e calcular valores agregados para um relatório.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="O Excel contém o painel de tarefas do PlaidXL e as funções personalizadas do PlaidXL. Ambos enviam pedidos, com a sessão iniciada como o utilizador, a um projeto na sua área de trabalho PlaidCloud, que devolve linhas de tabelas, hierarquias de dimensões e valores agregados para as células da folha de cálculo." style="width:100%;max-width:660px;height:auto;">
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
  <text x="330" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">sessão iniciada como o utilizador</text>
  <path d="M405 150 L254 150" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="168" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">linhas, nós, valores</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">O painel de tarefas e as funções personalizadas leem ambos do projeto que seleciona, com as suas próprias permissões do PlaidCloud.</figcaption>
</figure>

O PlaidXL lê do PlaidCloud e só altera uma tabela de projeto quando a guarda de volta por si: edite uma folha obtida, clique em **Save to PlaidCloud…** e confirme. Nada é escrito até o fazer, e é mantido um ponto de restauro durante 7 dias.

## Requisitos

- Excel para Microsoft 365, ou Excel 2021 ou posterior, no Windows ou no Mac. O separador PlaidCloud do friso e o painel de tarefas funcionam no Excel para computador.
- Uma conta PlaidCloud em pelo menos uma área de trabalho e acesso aos projetos que pretende ler. O PlaidXL mostra apenas os projetos, as tabelas e as dimensões que a sua conta já consegue ver no PlaidCloud.

## Tópicos

- [Instalar](/pt-pt/reference/cli/plaidxl/install/) — adicione o PlaidXL ao Excel e abra o painel de tarefas
- [Iniciar sessão](/pt-pt/reference/cli/plaidxl/connect/) — ligue-se à sua área de trabalho, termine a sessão e mude de área de trabalho
- [Trabalhar com tabelas e dimensões](/pt-pt/reference/cli/plaidxl/retrieve/) — escolha um projeto, filtre uma tabela, obtenha-a para uma folha, atualize-a e guarde-a de volta
- [Funções personalizadas](/pt-pt/reference/cli/plaidxl/functions/) — todas as funções `PLAIDXL`, os respetivos argumentos e o que devolvem
- [Criar um relatório com funções personalizadas](/pt-pt/reference/cli/plaidxl/build-a-report/) — disponha uma hierarquia e preencha-a com valores agregados
- [O friso do PlaidCloud](/pt-pt/reference/cli/plaidxl/ribbon/) — atualizar, expandir uma hierarquia e converter em valores
- [Resolução de problemas](/pt-pt/reference/cli/plaidxl/troubleshooting/) — soluções para os problemas mais comuns

É a primeira vez que utiliza o PlaidXL? O tutorial [Trabalhar no Excel com o PlaidXL](/pt-pt/get-started/tutorials/excel-with-plaidxl/) leva-o da instalação do suplemento a um primeiro relatório em cerca de 20 minutos.

## Relacionado

- [Projetos](/pt-pt/guides/projects/) — o que um projeto contém e como encontrar um
- [Tabelas e vistas](/pt-pt/guides/data/tables-views/) — as tabelas que o PlaidXL obtém
- [Utilizar dimensões](/pt-pt/guides/dimensions/dimensions/) — as hierarquias que o PlaidXL dispõe e agrega
