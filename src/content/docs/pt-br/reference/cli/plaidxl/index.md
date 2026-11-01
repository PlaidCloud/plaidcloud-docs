---
title: PlaidXL
description: Use o suplemento PlaidXL para Excel para fazer login no seu espaço de trabalho do PlaidCloud, trazer tabelas de projeto e hierarquias de dimensão para as planilhas, atualizá-las sob demanda e criar relatórios ao vivo com as funções personalizadas do PlaidXL.
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

O PlaidXL é o suplemento do PlaidCloud para o Microsoft Excel. Ele conecta uma pasta de trabalho ao seu espaço de trabalho do PlaidCloud para que os seus modelos e relatórios leiam de tabelas de projeto e dimensões confiáveis, e não de uma cópia que fica desatualizada na próxima vez que um fluxo de trabalho for executado.

Você pode trabalhar com o PlaidXL de duas maneiras, e a maioria das pastas de trabalho usa as duas:

- **O painel de tarefas**: navegue pelos seus projetos, escolha uma tabela ou dimensão, selecione colunas e filtros e recupere os dados em uma planilha. **Refresh All Tables** traz os dados atuais de todas as tabelas que você recuperou, e **Save to PlaidCloud…** grava de volta uma tabela editada. A guia **Formulas** cria uma fórmula do PlaidXL para você.
- **Funções personalizadas**: fórmulas como `=PLAIDXL.TABLE.GET_TABLE("Sales")` e `=PLAIDXL.CELL(...)` que leem os dados do PlaidCloud diretamente para as células. Use-as para listar tabelas e dimensões, montar uma hierarquia e calcular valores consolidados para um relatório.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="O Excel contém o painel de tarefas do PlaidXL e as funções personalizadas do PlaidXL. Ambos enviam solicitações, com login feito como você, a um projeto no seu espaço de trabalho do PlaidCloud, que devolve linhas de tabela, hierarquias de dimensão e valores consolidados para as células da planilha." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="px-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="20" y="20" width="250" height="190" rx="10" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Pasta de trabalho do Excel</text>
  <rect x="40" y="62" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="84" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Painel de tarefas do PlaidXL</text>
  <text x="145" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">navegar, filtrar, recuperar, atualizar</text>
  <rect x="40" y="130" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="152" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Funções PLAIDXL.*</text>
  <text x="145" y="170" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">tabelas, hierarquias, valores nas células</text>
  <rect x="410" y="40" width="230" height="150" rx="10" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Espaço de trabalho do PlaidCloud</text>
  <rect x="430" y="80" width="190" height="94" rx="8" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="102" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Projeto</text>
  <text x="525" y="124" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">tabelas</text>
  <text x="525" y="142" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">dimensões e hierarquias</text>
  <path d="M252 98 L405 98" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">login como você</text>
  <path d="M405 150 L254 150" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="168" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">linhas, nós, valores</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">O painel de tarefas e as funções personalizadas leem do projeto que você seleciona, com as suas próprias permissões do PlaidCloud.</figcaption>
</figure>

O PlaidXL lê do PlaidCloud e só altera uma tabela de projeto quando você mesmo a salva de volta: edite uma planilha recuperada, clique em **Save to PlaidCloud…** e confirme. Nada é gravado até que você faça isso, e um ponto de restauração é mantido por 7 dias.

## Requisitos

- Excel para Microsoft 365, ou Excel 2021 ou posterior, no Windows ou no Mac. A guia PlaidCloud da faixa de opções e o painel de tarefas funcionam no Excel para desktop.
- Uma conta do PlaidCloud em pelo menos um espaço de trabalho e acesso aos projetos que você quer ler. O PlaidXL mostra apenas os projetos, as tabelas e as dimensões que a sua conta já pode ver no PlaidCloud.

## Tópicos

- [Instalar](/pt-br/reference/cli/plaidxl/install/): adicione o PlaidXL ao Excel e abra o painel de tarefas
- [Login](/pt-br/reference/cli/plaidxl/connect/): conecte-se ao seu espaço de trabalho, saia e troque de espaço de trabalho
- [Trabalhe com tabelas e dimensões](/pt-br/reference/cli/plaidxl/retrieve/): escolha um projeto, filtre uma tabela, recupere-a em uma planilha, atualize-a e salve-a de volta
- [Funções personalizadas](/pt-br/reference/cli/plaidxl/functions/): todas as funções `PLAIDXL`, seus argumentos e o que cada uma retorna
- [Crie um relatório com funções personalizadas](/pt-br/reference/cli/plaidxl/build-a-report/): monte uma hierarquia e preencha-a com valores consolidados
- [A faixa de opções do PlaidCloud](/pt-br/reference/cli/plaidxl/ribbon/): atualize, expanda uma hierarquia e converta em valores
- [Solução de problemas](/pt-br/reference/cli/plaidxl/troubleshooting/): correções para os problemas mais comuns

Novo no PlaidXL? O tutorial [Trabalhe no Excel com o PlaidXL](/pt-br/get-started/tutorials/excel-with-plaidxl/) leva você da instalação do suplemento até um primeiro relatório em cerca de 20 minutos.

## Relacionados

- [Projetos](/pt-br/guides/projects/): o que um projeto contém e como encontrar um
- [Tabelas e visões](/pt-br/guides/data/tables-views/): as tabelas que o PlaidXL recupera
- [Uso de dimensões](/pt-br/guides/dimensions/dimensions/): as hierarquias que o PlaidXL monta e consolida
