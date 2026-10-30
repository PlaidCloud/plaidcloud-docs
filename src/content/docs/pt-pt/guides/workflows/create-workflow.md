---
title: Criar um fluxo de trabalho (guia)
description: Crie um fluxo de trabalho no PlaidCloud e escolha o respetivo tipo — Standard Serial, Standard Parallel ou Avançado (tela DAG) — para carregar, transformar e exportar dados.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/create-workflow.md
---

Para criar um novo fluxo de trabalho, é necessário um projeto existente. Se ainda não tem um, consulte [Gerir projetos](/pt-pt/guides/projects/managing-projects/).

## Passos

1. Abra o projeto que deve conter o fluxo de trabalho.
2. Mude para o separador **Fluxos de trabalho**.
3. Clique em **Novo fluxo de trabalho** na barra de ferramentas.
4. Preencha o formulário:
   - **Nome** — curto e descritivo (por exemplo, "Fecho mensal — carregar valores reais")
   - **Memorando** — descrição mais longa opcional, para contexto
   - **Tipo de fluxo de trabalho** — Standard Serial (predefinido), Standard Parallel ou Avançado (tela DAG). Consulte [Escolher um tipo de fluxo de trabalho](#escolher-um-tipo-de-fluxo-de-trabalho) abaixo.
   - **Acionar o fluxo de trabalho de correção em caso de erro** — opcional; ative-o para escolher um fluxo de trabalho de correção (consulte [Sobre os fluxos de trabalho de correção](#sobre-os-fluxos-de-trabalho-de-correção) abaixo).
5. Clique em **Criar**.

O fluxo de trabalho aparece no separador Fluxos de trabalho e está pronto para lhe serem adicionados passos. Faça duplo clique nele para abrir o [Explorador de fluxos de trabalho](/pt-pt/guides/workflows/workflow-explorer/) e começar a construir.

## Ver quando uma tabela de origem foi alterada pela última vez

No formulário de um passo, um seletor de tabela mostra uma linha discreta **Última atualização** com a data e a hora, na sua hora local, por baixo da tabela que selecionou, para que possa ver de relance se os dados estão atualizados. Passe o cursor sobre a linha para ver o texto completo. A linha fica oculta quando a seleção é dinâmica ou quando a tabela nunca foi atualizada.

## Escolher um tipo de fluxo de trabalho

O **Tipo de fluxo de trabalho** que escolhe ao criar um fluxo de trabalho determina como os respetivos passos são organizados e executados. Por predefinição é **Standard Serial**, e define-se no seletor de tipo do formulário Novo fluxo de trabalho.

| Tipo | Como os passos são organizados e executados |
|------|--------------------------------|
| **Standard Serial** | Os passos são executados a partir da **lista de passos**, um de cada vez, por ordem. |
| **Standard Parallel** | Os passos são executados a partir da **lista de passos**, em paralelo sempre que as suas dependências o permitam. |
| **Avançado (tela DAG)** | Os passos são dispostos numa **área de desenho visual** e executados por ordem de dependência, com os ramos independentes a serem executados em paralelo. O tipo Avançado também disponibiliza pontos de interrupção, contentores, execução a partir daqui, simulação e colaboração em tempo real. |

Um quarto tipo, **Macro** — um fluxo de trabalho reutilizável e invocável, com entradas e saídas declaradas — estará brevemente disponível e aparece no seletor como desativado.

:::note
Um passo só pode aparecer uma vez num fluxo de trabalho. Inserir, copiar, clonar ou importar um passo para uma posição que o colocaria num fluxo de trabalho uma segunda vez é recusado, com indicação do nome do passo — pelo que, de agora em diante, não é possível criar este estado. Se um fluxo de trabalho anterior a essa correção ainda tiver um passo em dois locais, falha de imediato numa execução **Standard Serial** com um erro que indica o passo duplicado — tal como numa execução **Standard Parallel** interrompida num passo final escolhido (consulte [Executar um intervalo de passos num fluxo de trabalho](/pt-pt/guides/workflows/running-a-range-of-steps-in-a-workflow/)), uma vez que executar até um ponto final também é feito sequencialmente. Uma execução **Standard Parallel** até à conclusão tolera o duplicado e executa-o apenas uma vez. Em qualquer dos casos, elimine o passo duplicado para reparar o fluxo de trabalho — a remoção de passos nunca é restringida.
:::

Escolha aqui **Avançado (tela DAG)** se pretender o [Estruturador visual de fluxos de trabalho](/pt-pt/guides/workflows/advanced-workflows/) desde o início. A escolha não é permanente: pode promover mais tarde um fluxo de trabalho Standard com **Converter para avançado…** na lista Fluxos de trabalho.

## Sobre os fluxos de trabalho de correção

Se o novo fluxo de trabalho terminar com um erro, o PlaidCloud pode executar automaticamente um **fluxo de trabalho de correção** como resposta. Isto é útil para:

- Enviar uma notificação para um canal do Slack, uma lista de distribuição de correio eletrónico ou um webhook, para que alguém investigue
- Acionar um fluxo de trabalho de reversão ou de limpeza que restaura um estado válido conhecido
- Registar a falha numa tabela de auditoria

Um fluxo de trabalho de correção é opcional. Pode deixá-lo em branco agora e configurá-lo mais tarde, se necessário. O fluxo de trabalho de correção só é acionado em falhas terminais, não em avisos por passo.

## Passos seguintes

- [Explorador de fluxos de trabalho](/pt-pt/guides/workflows/workflow-explorer/) — adicione passos ao novo fluxo de trabalho
- [Fluxos de trabalho avançados](/pt-pt/guides/workflows/advanced-workflows/) — escolha um tipo de fluxo de trabalho e construa na área de desenho visual
- [Executar um fluxo de trabalho](/pt-pt/guides/workflows/run-a-workflow/) — execute o fluxo de trabalho assim que tiver passos
- [Gerir erros de passos](/pt-pt/guides/workflows/managing-step-errors/) — depuração de falhas
