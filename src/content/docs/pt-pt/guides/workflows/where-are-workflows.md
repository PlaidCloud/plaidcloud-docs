---
title: Onde estão os fluxos de trabalho
description: Navegue até aos fluxos de trabalho do PlaidCloud nos seus projetos e faça a sua gestão através da interface de fluxos de trabalho e das ferramentas de navegação de projetos.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/where-are-workflows.md
---

Os fluxos de trabalho existem dentro de projetos. Para os encontrar:

1. No menu superior, abra **Projetos**.
2. Clique no projeto que contém os fluxos de trabalho que procura.
3. Mude para o separador **Fluxos de trabalho**.

Verá todos os fluxos de trabalho do projeto, organizados numa hierarquia de estilo pastas.

## O que verá para cada fluxo de trabalho

- **Estado** — em execução, concluído normalmente ou terminado com um aviso ou erro
- Datas e horas de **Criado** e **Última atualização**, bem como os nomes das pessoas responsáveis
- **Organização em pastas** — os fluxos de trabalho podem ser agrupados em pastas aninhadas para facilitar a gestão em projetos grandes

Faça duplo clique num fluxo de trabalho para abrir o **Workflow Explorer**, onde pode ver os passos, executar o fluxo de trabalho completo, executar um único passo ou escolher um intervalo.

## Por que motivo um fluxo de trabalho pode não estar visível

Os fluxos de trabalho que pode ver dependem de duas coisas:

- **Acesso ao projeto** — o administrador da sua área de trabalho concede-lhe acesso a projetos específicos. Se espera ver um projeto e não o vê, peça a um proprietário do projeto que o adicione.
- **Perfil de visualização** — dentro de um projeto, é-lhe atribuído um de três perfis:
  - **Arquiteto** — pode ver e editar tudo
  - **Gestor** — pode ver e executar fluxos de trabalho, mas não os modificar
  - **Explorador** — visibilidade limitada; alguns fluxos de trabalho podem estar ocultos

Se espera ver fluxos de trabalho específicos e não os vê, o seu perfil pode estar a filtrá-los. Um Arquiteto do projeto pode confirmar o que deve ver.

O seu perfil também decide se pode alterar um passo. Se conseguir abrir um fluxo de trabalho mas não o modificar, o formulário do passo abre em modo só de leitura: os seus campos estão desativados e o botão **Guardar** está oculto, pelo que pode ler a configuração de um passo sem a poder alterar. Isto aplica-se onde quer que o formulário abra: o ícone de engrenagem e o menu de contexto da tabela do fluxo de trabalho, a área de desenho visual, a grelha de **Passos** do projeto e o menu **Novo passo**.

## Alterações não guardadas numa janela de passo

Uma janela de passo marca as alterações não guardadas com um **•** no seu título. Fechar a janela com **Esc**, o **X**, **Cancelar** ou o botão do seu separador pergunta **Descartar as alterações não guardadas?** para que uma edição não se perca por acidente. Escolha **Descartar** para fechar sem guardar, ou volte atrás para continuar a editar.

## Um passo foi alterado desde que o abriu

**Guardar** num formulário de passo nunca sobrescreve uma alteração guardada depois de abrir o formulário, quer tenha sido feita pelo Weave quer por outra pessoa. Nada é guardado: o formulário continua aberto com as suas alterações, e um aviso com o título **Falha ao atualizar** indica *Este passo foi alterado desde que o abriu. Recarregue para ver a versão mais recente; as suas alterações não guardadas serão perdidas.* Escolha **Recarregar** para mostrar o passo tal como está agora e volte a fazer as suas alterações. Adicionar ou remover uma das etiquetas do passo não conta como alteração. Se outros guardares continuarem a chegar ao passo enquanto o seu é escrito, uma mensagem **Falha ao atualizar** indica *Este passo continuou a mudar enquanto era guardado. Tente novamente.* e nada é guardado; guarde novamente quando pararem.

Através da REST API, `GET /rest/v1/analyze/projects/{project_id}/transform/{step_id}` devolve o passo com o respetivo `_etag`. Envie-o de volta como `if_match` num `PUT` para o mesmo caminho, e um guardar sobre uma alteração mais recente é recusado com `412` e nada é escrito. Sem ele, prevalece o último guardar. Um `PUT` que outros guardares continuem a ultrapassar é recusado com `503` e com o mesmo *Este passo continuou a mudar enquanto era guardado. Tente novamente.*, e nada é escrito. Quando um `PUT` inclui `labels` e só estas não puderam ser escritas, responde com `503` e *O passo foi guardado, mas as respetivas etiquetas não: continuaram a mudar enquanto eram gravadas. Defina as etiquetas novamente.* Os assistentes de IA ligados por MCP têm a mesma verificação ao passar o `_etag` de `step_describe` como `if_match` para `step_upsert`.

## Passos seguintes

- [Workflow Explorer](/pt-pt/guides/workflows/workflow-explorer/) — o que fazer dentro de um fluxo de trabalho aberto
- [Criar um fluxo de trabalho](/pt-pt/guides/workflows/create-workflow/) — iniciar um novo
- [Executar um fluxo de trabalho](/pt-pt/guides/workflows/run-a-workflow/) — executar de ponta a ponta
