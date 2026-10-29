---
title: Panel Studio
description: Crie, edite, pré-visualize e publique aplicativos Panel sem sair do PlaidCloud — depois restaure uma versão anterior, veja o uso e a velocidade do aplicativo, configure alertas e resumos, liste-o na galeria e fixe-o no Início.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

O Panel Studio é o editor de aplicativos Panel dentro do PlaidCloud. Ele mostra os arquivos do aplicativo ao lado de um editor, cria uma pré-visualização privada que você pode abrir e publica o aplicativo quando você estiver pronto. Você não precisa de um repositório git para começar.

## Abrir o Panel Studio

- No quadro **Início** de um projeto, escolha **Open in Studio** em um aplicativo Panel.
- Em **Meus aplicativos Panel**, escolha **Open in Studio** na linha de um aplicativo.

Para começar um novo aplicativo, escolha **Create app** em qualquer um dos dois lugares.

## Criar um aplicativo

A caixa de diálogo **Create app** permite começar a partir de um de cinco pontos:

| Começar de | O que você recebe |
|---|---|
| **Em branco** | Um aplicativo mínimo com um `app.py` e um `requirements.txt`. |
| **Tabela** | Um aplicativo criado sobre a tabela que você escolher. |
| **Visão** | O mesmo, criado sobre uma visão do projeto. |
| **Modelo** | Um aplicativo pronto do [Panel App Kit](/pt-br/guides/panel-apps/app-kit/#comece-a-partir-de-um-modelo). |
| **Da galeria** | Uma cópia de um aplicativo que o seu espaço de trabalho listou na [galeria de aplicativos](/pt-br/guides/panel-apps/gallery/). |

Dê um nome ao aplicativo, escolha o **Projeto** dele e escolha **Criar**. O Studio abre o novo aplicativo com os arquivos listados à esquerda.

## Editar

Escolha um arquivo na lista para editá-lo no editor. Liste suas dependências Python em `requirements.txt`, um pacote por linha. Elas são instaladas quando o aplicativo é compilado.

Escolha **Ask Weave** para que o Weave escreva ou altere o aplicativo para você. Veja [Crie aplicativos Panel com o Weave](/pt-br/guides/panel-apps/build-with-weave/).

## Salvar, pré-visualizar e publicar

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Salvar mantém um rascunho que só você pode ver. Pré-visualizar cria uma cópia privada do rascunho para o editor. Publicar substitui o aplicativo ativo depois que você confirma." style="width:100%;max-width:660px;height:auto;">
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
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">o aplicativo ativo</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Suas edições só chegam aos visualizadores quando você publica.</figcaption>
</figure>

### Salvar

**Salvar** armazena suas alterações como rascunho. O aplicativo ativo não muda, e ninguém mais vê o rascunho.

### Pré-visualização

**Pré-visualização** cria o seu rascunho salvo como uma cópia privada e a abre. Somente os editores do aplicativo podem abrir uma pré-visualização.

- Uma pré-visualização é removida após 24 horas sem um salvamento.
- Um espaço de trabalho pode ter até 10 pré-visualizações ao mesmo tempo.
- Salve novamente e escolha **Pré-visualização** para ver suas edições mais recentes.

### Publicar

**Publicar** substitui o aplicativo ativo pelo seu rascunho salvo. Exige permissão de edição no projeto do aplicativo, e o Studio pede que você confirme antes.

Se outra pessoa publicou uma alteração depois que você abriu o aplicativo, o Studio informa um conflito em vez de sobrescrever o trabalho dela. Recarregue o aplicativo, traga suas edições e publique novamente.

## Status e erros de compilação

A guia **Build** mostra o status da compilação mais recente e é atualizada enquanto ela é executada. Quando uma compilação falha, a guia lista cada erro com seu arquivo e número de linha, para que você vá direto à linha. Problemas de dependência em `requirements.txt` vêm com uma dica sobre a correção.

Erros e avisos também são marcados nas respectivas linhas do editor, então você vê o problema onde ele está.

Para saber o que cada status significa depois que o aplicativo é publicado, veja [Usando um aplicativo Panel](/pt-br/guides/panel-apps/using/#status-de-compilação-aplicativos-de-servidor).

## Histórico e restauração

A guia **Histórico** lista todas as versões publicadas do aplicativo, da mais recente para a mais antiga, com o status de compilação de cada uma. Escolha **Carregar mais** para ver as mais antigas.

Para voltar a uma versão anterior, escolha **Restaurar** nela e confirme. A versão restaurada se torna o aplicativo ativo e é recompilada. Seu rascunho não salvo não se perde: ele permanece no rascunho e entra no ar sobre a versão restaurada na próxima vez que você publicar. Se o aplicativo já corresponde a essa versão, o Studio informa isso e não altera nada. Se alguém publicou enquanto você restaurava, o Studio não restaura nada e pede que você tente novamente.

## Insights

A guia **Insights** mostra como as pessoas usam o aplicativo e a rapidez com que ele responde. Escolha os últimos 7, 14 ou 30 dias.

| Seção | O que mostra |
|---|---|
| **Visualizações por dia** | Quantas vezes o aplicativo foi aberto em cada dia. |
| **Carregamento da página** | O tempo mediano de carregamento e o tempo que 95 por cento dos carregamentos superam, a partir dos carregamentos de página do período. |
| **Consultas mais lentas** | As consultas que levaram mais tempo, com a frequência com que foram executadas e seus tempos mediano, do extremo lento e mais lento. |
| **Erros** | O que deu errado no período, por tipo de erro e por onde no aplicativo aconteceu. |

Quando um período contém mais atividade do que o Insights consegue ler, ele informa que os valores são parciais. Quando os carregamentos de página ultrapassam o [orçamento de desempenho](/pt-br/guides/panel-apps/app-kit/#orçamentos-de-desempenho) do aplicativo, o Insights avisa quantos ultrapassaram e quais consultas foram lentas. O Insights nunca mostra os dados que uma consulta retornou nem os nomes das pessoas que abriram o aplicativo.

As duas guias exigem que o aplicativo esteja atribuído a um projeto; um aplicativo não atribuído mostra um aviso para atribuí-lo.

## Alertas e resumos

Escolha **Alerts & Digests** para configurar notificações que monitoram um número nos dados do aplicativo e avisam quando ele ultrapassa um limite, ou que enviam um resumo em um agendamento. Veja [Alertas e resumos](/pt-br/guides/panel-apps/alerts-and-digests/).

## Listar um aplicativo na galeria

Escolha **Gallery…** para listar o aplicativo como um modelo a partir do qual qualquer pessoa que possa visualizar o projeto dele pode criar o próprio aplicativo, ou para removê-lo da galeria. Veja [A galeria de aplicativos](/pt-br/guides/panel-apps/gallery/).

## Fixar no Início

Escolha **Pin to Home** para adicionar o aplicativo ao quadro **Início** do projeto e **Unpin from Home** para removê-lo.

## Excluir um aplicativo

Excluir um aplicativo Panel pede que você confirme antes. Em **Meus aplicativos Panel**, use o ícone de **menos** na linha do aplicativo. Cancelar a publicação também pede confirmação.

## Próximas etapas

- [Crie aplicativos Panel com o Weave](/pt-br/guides/panel-apps/build-with-weave/) — descreva o aplicativo e aprove a alteração exata.
- [O Panel App Kit](/pt-br/guides/panel-apps/app-kit/) — os componentes que os pontos de partida de tabela, visão e modelo do Studio usam.
- [Alertas e resumos](/pt-br/guides/panel-apps/alerts-and-digests/) — notifique as pessoas quando um número ultrapassar um limite ou em um agendamento.
- [A galeria de aplicativos](/pt-br/guides/panel-apps/gallery/) — compartilhe um aplicativo como ponto de partida para outras pessoas.
- [Usando um aplicativo Panel](/pt-br/guides/panel-apps/using/) — logs, uso e recompilações depois que você publica.
