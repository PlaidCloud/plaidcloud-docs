---
title: Onde estão os fluxos de trabalho
description: Navegue até os fluxos de trabalho do PlaidCloud em seus projetos e gerencie-os usando a interface de fluxos de trabalho e as ferramentas de navegação do projeto.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/where-are-workflows.md
---

Os fluxos de trabalho ficam dentro de projetos. Para encontrá-los:

1. No menu superior, abra **Projetos**.
2. Clique no projeto que contém os fluxos de trabalho que você procura.
3. Vá para a guia **Fluxos de trabalho**.

Você verá todos os fluxos de trabalho do projeto, organizados em uma hierarquia no estilo de pastas.

## O que você verá em cada fluxo de trabalho

- **Status** — em execução, concluído normalmente ou finalizado com um aviso ou erro
- Carimbos de data e hora de **Criado** e **Última atualização**, além dos nomes das pessoas responsáveis
- **Organização em pastas** — os fluxos de trabalho podem ser agrupados em pastas aninhadas para facilitar o gerenciamento em projetos grandes

Clique duas vezes em um fluxo de trabalho para abrir o **Workflow Explorer**, onde você pode ver as etapas, executar o fluxo de trabalho inteiro, executar uma única etapa ou escolher um intervalo.

## Por que um fluxo de trabalho pode não estar visível

Os fluxos de trabalho que você pode ver dependem de duas coisas:

- **Acesso ao projeto** — o administrador do seu espaço de trabalho concede acesso a projetos específicos. Se você espera ver um projeto e não o vê, peça a um proprietário do projeto que adicione você.
- **Função de visualização** — dentro de um projeto, você recebe uma de três funções:
  - **Arquiteto** — pode ver e editar tudo
  - **Gerente** — pode ver e executar fluxos de trabalho, mas não modificá-los
  - **Explorador** — visibilidade limitada; alguns fluxos de trabalho podem estar ocultos

Se você espera ver fluxos de trabalho específicos e não os vê, sua função pode estar filtrando-os. Um Arquiteto do projeto pode confirmar o que você deveria ver.

Sua função também decide se você pode alterar uma etapa. Se você consegue abrir um fluxo de trabalho, mas não modificá-lo, o formulário da etapa abre somente para leitura — seus campos ficam desativados e o botão **Salvar** fica oculto — para que você possa ler a configuração de uma etapa sem poder alterá-la. Isso vale onde quer que o formulário abra: o ícone de engrenagem e o menu de clique com o botão direito da tabela do fluxo de trabalho, a tela visual, a grade de **Etapas** do projeto e o menu **Nova etapa**.

## Alterações não salvas em uma janela de etapa

Uma janela de etapa marca as alterações não salvas com um **•** no título. Fechar a janela com **Esc**, o **X**, **Cancelar** ou o botão da guia pergunta **Descartar alterações não salvas?** para que uma edição não seja perdida por acidente. Escolha **Descartar** para fechar sem salvar, ou volte para continuar editando.

## Próximos passos

- [Workflow Explorer](/pt-br/guides/workflows/workflow-explorer/) — o que fazer dentro de um fluxo de trabalho aberto
- [Criar um fluxo de trabalho](/pt-br/guides/workflows/create-workflow/) — comece um novo
- [Executar um fluxo de trabalho](/pt-br/guides/workflows/run-a-workflow/) — execute de ponta a ponta
