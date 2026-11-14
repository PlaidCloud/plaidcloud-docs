---
title: Panel Studio
description: Crie, edite, pré-visualize e publique aplicativos Panel sem sair do PlaidCloud — depois restaure uma versão anterior, consulte o uso e a velocidade do aplicativo, configure alertas e resumos, liste-o na galeria e fixe-o no Início.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

O Panel Studio é o editor de aplicativos Panel dentro do PlaidCloud. Ele mostra os arquivos do aplicativo ao lado de um editor, cria uma pré-visualização privada que você pode abrir e publica o aplicativo quando você estiver pronto. Você não precisa de um repositório git para começar.

## Abrir o Panel Studio

- No quadro **Início** de um projeto, escolha **Abrir no Studio** em um aplicativo Panel.
- Em **Aplicativos**, escolha **Studio** na linha de um aplicativo.

Para começar um novo aplicativo, escolha **Novo app** > **Studio**. Ele também fica na linha **Aplicativos Studio** do cartão **Aplicativos e identidade visual** na guia **Início** de um projeto. Para criar a partir de uma tabela, selecione-a na guia **Tabelas** do projeto e escolha **Criar aplicativo Panel**.

## Criar um aplicativo

A caixa de diálogo **Novo aplicativo Studio** permite começar de um destes cinco pontos:

| Começar de | O que você recebe |
|---|---|
| **Aplicativo em branco** | Um aplicativo mínimo com um `app.py` e um `requirements.txt`. |
| **A partir de uma tabela** | Um aplicativo criado a partir da tabela que você escolher. |
| **A partir de uma visualização** | O mesmo, criado a partir de uma visão do projeto. |
| **A partir de outro aplicativo Studio** | Uma cópia de um dos seus aplicativos Studio. |
| **A partir da galeria** | Uma cópia de um aplicativo que seu espaço de trabalho listou na [galeria de aplicativos](/pt-br/guides/panel-apps/gallery/). |

Dê um nome ao aplicativo, escolha o **Projeto** e selecione **Criar**. O Studio abre o novo aplicativo com os arquivos listados à esquerda. No caso de uma tabela ou de uma visão, o prompt do Weave para criar a primeira página do aplicativo já está pronto para envio. Consulte [Criar um aplicativo Panel](/pt-br/guides/panel-apps/creating/).

## Onde o aplicativo fica

Um aplicativo Studio é uma pasta com o nome do aplicativo (`<app-slug>/`) dentro do repositório `apps` do seu espaço de trabalho no [PlaidCloud Git](/pt-br/guides/git/), o mesmo repositório onde ficam seus outros aplicativos Panel. O Studio não cria um repositório próprio para o aplicativo, então você pode encontrar e editar o código-fonte em `apps`, junto com seus outros aplicativos.

- **Branch de rascunho.** O trabalho que ainda não está no ar fica em um branch chamado `studio-<app-slug>`. **Publicar** copia a pasta do aplicativo desse branch para o branch principal.
- **Recompilações.** Um push para `apps` recompila um aplicativo somente quando a pasta desse aplicativo ou o `requirements.txt` da raiz do repositório mudou.
- **Aplicativos existentes.** Um aplicativo Studio que estava em um repositório próprio é movido para a sua pasta automaticamente. O repositório antigo é arquivado: ele permanece, somente leitura, e nunca é excluído.

## Editar

Escolha um arquivo na lista para editá-lo no editor. Liste suas dependências Python em `requirements.txt`, um pacote por linha. Elas são instaladas quando o aplicativo é compilado.

Escolha **Perguntar ao Weave** para que o Weave escreva ou altere o aplicativo para você. Consulte [Criar aplicativos Panel com o Weave](/pt-br/guides/panel-apps/build-with-weave/).

## Salvar, pré-visualizar e publicar

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Salvar mantém um rascunho que só você vê. Pré-visualização cria uma cópia privada do rascunho para o editor. Publicar substitui o aplicativo no ar depois que você confirma." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Salvar</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">somente rascunho</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Pré-visualização</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">somente editor</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Publicar</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">o aplicativo no ar</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Suas edições só chegam aos visualizadores quando você publica.</figcaption>
</figure>

### Salvar

**Salvar** armazena suas alterações como rascunho. O aplicativo no ar não muda, e ninguém mais vê o rascunho.

### Pré-visualização

**Pré-visualização** cria seu rascunho salvo como uma cópia privada e a abre. Somente os editores do aplicativo podem abrir uma pré-visualização.

- Uma pré-visualização é removida após 24 horas sem um salvamento.
- Um espaço de trabalho pode ter até 10 pré-visualizações ao mesmo tempo.
- Salve novamente e escolha **Pré-visualização** para ver suas edições mais recentes.

### Publicar

**Publicar** substitui o aplicativo no ar pelo seu rascunho salvo. Isso exige permissão de edição no projeto do aplicativo, e o Studio pede que você confirme antes.

Se outra pessoa publicou uma alteração depois que você abriu o aplicativo, o Studio informa um conflito em vez de sobrescrever o trabalho dela. Recarregue o aplicativo, traga suas edições e publique novamente.

## Status da compilação e erros

A guia **Criar** mostra o status da compilação mais recente e é atualizada enquanto ela é executada. Quando uma compilação falha, a guia lista cada erro com seu arquivo e número de linha, para que você vá direto à linha. Problemas de dependência em `requirements.txt` vêm com uma dica sobre a correção.

Erros e avisos também são marcados nas respectivas linhas no editor, então você vê o problema onde ele está.

Para saber o que cada status significa depois que o aplicativo é publicado, consulte [Usar um aplicativo Panel](/pt-br/guides/panel-apps/using/#status-da-compilação-aplicativos-de-servidor).

## Histórico e restauração

A guia **Histórico** lista todas as versões publicadas do aplicativo, da mais recente para a mais antiga, com o status de compilação de cada uma. Escolha **Carregar mais** para ver as mais antigas.

Para voltar a uma versão anterior, escolha **Restaurar** nela e confirme. A versão restaurada passa a ser o aplicativo no ar e é recompilada. Seu rascunho não salvo não se perde: ele continua no rascunho e entra no ar sobre a versão restaurada na próxima vez que você publicar. Se o aplicativo já corresponde a essa versão, o Studio avisa e não altera nada. Se alguém publicou enquanto você restaurava, o Studio não restaura nada e pede que você tente novamente.

## Insights

A guia **Insights** mostra como as pessoas usam o aplicativo e a rapidez com que ele responde. Escolha os últimos 7, 14 ou 30 dias.

| Seção | Mostra |
|---|---|
| **Visualizações por dia** | Quantas vezes o aplicativo foi aberto em cada dia. |
| **Carregamento de página** | O tempo mediano de carregamento e o tempo que 95 por cento dos carregamentos superam, com base nos carregamentos de página do período. |
| **Consultas mais lentas** | As consultas que levaram mais tempo, com a frequência com que foram executadas e seus tempos mediano, do extremo lento e mais lento. |
| **Erros** | O que deu errado no período, por tipo de erro e pelo local do aplicativo em que ocorreu. |

Quando um período contém mais atividade do que o Insights consegue ler, ele informa que os números são parciais. Quando os carregamentos de página ultrapassam o [orçamento de desempenho](/pt-br/guides/panel-apps/app-kit/#orçamentos-de-desempenho) do aplicativo, o Insights avisa quantos ultrapassaram e quais consultas estavam lentas. O Insights nunca mostra os dados que uma consulta retornou nem os nomes das pessoas que abriram o aplicativo.

As guias **Histórico** e **Insights** exigem que o aplicativo esteja atribuído a um projeto; um aplicativo não atribuído mostra uma solicitação para atribuí-lo.

## Alertas e resumos

Escolha **Alertas e resumos** para configurar notificações que acompanham um número nos dados do aplicativo e avisam você quando ele ultrapassa um limite, ou que enviam um resumo em um agendamento. Consulte [Alertas e resumos](/pt-br/guides/panel-apps/alerts-and-digests/).

## Listar um aplicativo na galeria

Escolha **Galeria…** no Studio. Escolha **Listar na galeria** para listar o aplicativo como um modelo a partir do qual qualquer pessoa que possa ver o projeto dele pode criar seu próprio aplicativo, ou **Remover da galeria** para removê-lo. O botão está disponível para aplicativos que pertencem a um projeto. Você precisa de acesso de edição ao projeto. Consulte [A galeria de aplicativos](/pt-br/guides/panel-apps/gallery/).

## Fixar no Início

Escolha **Fixar no Início** para adicionar o aplicativo ao quadro **Início** do projeto e **Desafixar do Início** para removê-lo.

## Excluir um aplicativo

Excluir um aplicativo Panel pede que você confirme antes. Em **Aplicativos**, use o ícone de **menos** na linha do aplicativo. Cancelar a publicação também pede confirmação.

## Próximas etapas

- [Criar aplicativos Panel com o Weave](/pt-br/guides/panel-apps/build-with-weave/) — descreva o aplicativo e aprove a alteração exata.
- [O Panel App Kit](/pt-br/guides/panel-apps/app-kit/) — os componentes que as opções de tabela e visão do Studio usam.
- [Alertas e resumos](/pt-br/guides/panel-apps/alerts-and-digests/) — avise as pessoas quando um número ultrapassa um limite ou em um agendamento.
- [A galeria de aplicativos](/pt-br/guides/panel-apps/gallery/) — compartilhe um aplicativo como ponto de partida para outras pessoas.
- [Usar um aplicativo Panel](/pt-br/guides/panel-apps/using/) — logs, uso e recompilações depois que você publica.
