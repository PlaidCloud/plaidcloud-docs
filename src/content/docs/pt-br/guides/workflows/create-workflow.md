---
title: Criar fluxo de trabalho (guia)
description: Crie um fluxo de trabalho no PlaidCloud e escolha seu tipo — Serial padrão, Paralelo padrão ou Avançado (tela de DAG) — para carregar, transformar e exportar dados.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/create-workflow.md
---

Para criar um novo fluxo de trabalho, você precisa de um projeto existente. Se ainda não tiver um, consulte [Gerenciar projetos](/pt-br/guides/projects/managing-projects/).

## Etapas

1. Abra o projeto que deve conter o fluxo de trabalho.
2. Vá para a guia **Fluxos de trabalho**.
3. Clique em **Novo fluxo de trabalho** na barra de ferramentas.
4. Preencha o formulário:
   - **Nome** — curto e descritivo (por exemplo, "Fechamento mensal — carregar valores realizados")
   - **Memorando** — descrição mais longa opcional, para dar contexto
   - **Tipo de fluxo de trabalho** — Serial padrão (padrão), Paralelo padrão ou Avançado (tela de DAG). Consulte [Escolher um tipo de fluxo de trabalho](#escolher-um-tipo-de-fluxo-de-trabalho) abaixo.
   - **Acionar fluxo de trabalho de correção em caso de erro** — opcional; ative-o para escolher um fluxo de trabalho de correção (consulte [Sobre os fluxos de trabalho de correção](#sobre-os-fluxos-de-trabalho-de-correção) abaixo).
5. Clique em **Criar**.

O fluxo de trabalho aparece na guia Fluxos de trabalho e está pronto para receber etapas. Clique duas vezes nele para abrir o [Explorador de fluxo de trabalho](/pt-br/guides/workflows/workflow-explorer/) e começar a construir.

## Ver quando uma tabela de origem mudou pela última vez

No formulário de uma etapa, um seletor de tabela mostra uma linha discreta **Última atualização** com a data e a hora, no seu horário local, abaixo da tabela selecionada, para que você veja de relance se os dados estão atuais. Passe o mouse sobre a linha para ver o texto completo. A linha fica oculta quando a seleção é dinâmica ou quando a tabela nunca foi atualizada.

## Escolher um tipo de fluxo de trabalho

O **Tipo de fluxo de trabalho** que você escolhe ao criar um fluxo de trabalho determina como suas etapas são organizadas e executadas. O padrão é **Serial padrão**, e você o define no seletor de tipo do formulário Novo fluxo de trabalho.

| Tipo | Como as etapas são organizadas e executadas |
|------|--------------------------------|
| **Serial padrão** | As etapas são executadas a partir da **lista de etapas**, uma de cada vez, em ordem. |
| **Paralelo padrão** | As etapas são executadas a partir da **lista de etapas**, em paralelo quando suas dependências permitem. |
| **Avançado (tela de DAG)** | As etapas são dispostas em uma **tela visual** e executadas na ordem das dependências, com ramificações independentes executadas em paralelo. O tipo Avançado também libera pontos de interrupção, contêineres, executar a partir daqui, simulação e colaboração em tempo real. |

Um quarto tipo, **Macro** — um fluxo de trabalho reutilizável e chamável, com entradas e saídas declaradas — estará disponível em breve e aparece no seletor como desabilitado.

:::note
Uma etapa só pode aparecer uma vez em um fluxo de trabalho. Inserir, copiar, clonar ou importar uma etapa em uma posição que a colocaria em um fluxo de trabalho pela segunda vez é recusado, citando a etapa — portanto, daqui em diante você não consegue criar essa situação. Se um fluxo de trabalho anterior a essa correção ainda tiver uma etapa em dois lugares, ele falha imediatamente em uma execução **Serial padrão**, com um erro que cita a etapa duplicada — assim como em uma execução **Paralelo padrão** interrompida em uma etapa final escolhida (consulte [Executar um intervalo de etapas em um fluxo de trabalho](/pt-br/guides/workflows/running-a-range-of-steps-in-a-workflow/)), já que executar até um ponto final também é feito em sequência. Uma execução **Paralelo padrão** até a conclusão tolera a duplicata e a executa apenas uma vez. Em ambos os casos, exclua a etapa duplicada para reparar o fluxo de trabalho — remover etapas nunca é restringido.
:::

Escolha **Avançado (tela de DAG)** aqui se quiser usar o [Designer visual de fluxo de trabalho](/pt-br/guides/workflows/advanced-workflows/) desde o início. A escolha não é permanente: você pode promover um fluxo de trabalho padrão mais tarde com **Converter em avançado…** na lista de Fluxos de trabalho.

## Sobre os fluxos de trabalho de correção

Se o novo fluxo de trabalho terminar com erro, o PlaidCloud pode executar automaticamente um **fluxo de trabalho de correção** em resposta. Isso é útil para:

- Enviar uma notificação a um canal do Slack, uma lista de distribuição de e-mail ou um webhook para que alguém investigue
- Acionar um fluxo de trabalho de reversão ou limpeza que restaure um estado válido conhecido
- Registrar a falha em uma tabela de auditoria

Um fluxo de trabalho de correção é opcional. Você pode deixá-lo em branco agora e configurá-lo depois, se necessário. O fluxo de trabalho de correção só é disparado em falhas terminais, não em avisos por etapa.

## Próximas etapas

- [Explorador de fluxo de trabalho](/pt-br/guides/workflows/workflow-explorer/) — adicione etapas ao seu novo fluxo de trabalho
- [Fluxos de trabalho avançados](/pt-br/guides/workflows/advanced-workflows/) — escolha um tipo de fluxo de trabalho e construa na tela visual
- [Executar um fluxo de trabalho](/pt-br/guides/workflows/run-a-workflow/) — execute o fluxo de trabalho quando ele tiver etapas
- [Gerenciar erros de etapas](/pt-br/guides/workflows/managing-step-errors/) — depuração de falhas
