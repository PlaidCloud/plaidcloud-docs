---
title: Panel Studio
description: Crie, edite, pré-visualize e publique aplicações Panel sem sair do PlaidCloud — depois restaure uma versão anterior, consulte a utilização e a velocidade da aplicação, configure alertas e resumos, liste-a na galeria e afixe-a no Início.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

O Panel Studio é o editor de aplicações Panel dentro do PlaidCloud. Mostra os ficheiros da aplicação junto a um editor, cria uma pré-visualização privada que pode abrir e publica a aplicação quando estiver pronto. Não precisa de um repositório git para começar.

## Abrir o Panel Studio

- No quadro **Início** de um projeto, escolha **Open in Studio** numa aplicação Panel.
- Em **As minhas aplicações Panel**, escolha **Open in Studio** na linha de uma aplicação.

Para iniciar uma nova aplicação, escolha **Create app** em qualquer um dos locais.

## Criar uma aplicação

A caixa de diálogo **Create app** permite-lhe começar a partir de um de cinco locais:

| Começar a partir de | O que obtém |
|---|---|
| **Blank** | Uma aplicação mínima com um `app.py` e um `requirements.txt`. |
| **Tabela** | Uma aplicação criada sobre a tabela que escolher. |
| **Vista** | O mesmo, criado sobre uma vista do projeto. |
| **Modelo** | Uma aplicação pronta a usar do [Panel App Kit](/pt-pt/guides/panel-apps/app-kit/#começar-a-partir-de-um-modelo). |
| **From the gallery** | Uma cópia de uma aplicação que a sua área de trabalho listou na [galeria de aplicações](/pt-pt/guides/panel-apps/gallery/). |

Dê um nome à aplicação, escolha o seu **Projeto** e escolha **Criar**. O Studio abre a nova aplicação com os respetivos ficheiros listados à esquerda.

## Editar

Escolha um ficheiro na lista para o editar no editor. Liste as suas dependências Python em `requirements.txt`, um pacote por linha. São instaladas quando a aplicação é compilada.

Escolha **Ask Weave** para que o Weave escreva ou altere a aplicação por si. Consulte [Criar aplicações Panel com o Weave](/pt-pt/guides/panel-apps/build-with-weave/).

## Guardar, pré-visualizar e publicar

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Guardar mantém um rascunho que só o próprio vê. Pré-visualizar cria uma cópia privada do rascunho para o editor. Publicar substitui a aplicação em direto depois de confirmar." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Guardar</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">apenas rascunho</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Pré-visualização</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">apenas editor</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Publicar</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">a aplicação em direto</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">As suas edições só chegam aos visualizadores quando publica.</figcaption>
</figure>

### Guardar

**Guardar** armazena as suas alterações como rascunho. A aplicação em direto não muda e mais ninguém vê o rascunho.

### Pré-visualização

**Pré-visualização** cria o seu rascunho guardado como cópia privada e abre-a. Só os editores da aplicação podem abrir uma pré-visualização.

- Uma pré-visualização é removida após 24 horas sem guardar.
- Uma área de trabalho pode ter até 10 pré-visualizações em simultâneo.
- Guarde novamente e escolha **Pré-visualização** para ver as suas edições mais recentes.

### Publicar

**Publicar** substitui a aplicação em direto pelo seu rascunho guardado. Requer permissão de edição no projeto da aplicação, e o Studio pede-lhe primeiro que confirme.

Se outra pessoa publicou uma alteração depois de ter aberto a aplicação, o Studio comunica um conflito em vez de substituir o trabalho dessa pessoa. Recarregue a aplicação, transfira as suas edições e publique novamente.

## Estado da compilação e erros

O separador **Criar** mostra o estado da compilação mais recente e atualiza-se à medida que esta decorre. Quando uma compilação falha, o separador lista cada erro com o respetivo ficheiro e número de linha, para que possa ir diretamente à linha. Os problemas de dependências em `requirements.txt` vêm com uma sugestão de correção.

Os erros e os avisos também são assinalados nas respetivas linhas no editor, para ver o problema onde ele está.

Para saber o que significa cada estado depois de a aplicação ser publicada, consulte [Utilizar uma aplicação Panel](/pt-pt/guides/panel-apps/using/#estado-de-compilação-aplicações-de-servidor).

## Histórico e restauro

O separador **Histórico** lista todas as versões publicadas da aplicação, da mais recente para a mais antiga, com o respetivo estado de compilação. Escolha **Carregar mais** para ver as mais antigas.

Para voltar a uma versão anterior, escolha **Restaurar** nela e confirme. A versão restaurada passa a ser a aplicação em direto e é recompilada. O seu rascunho por guardar não se perde: permanece no rascunho e entra em produção sobre a versão restaurada da próxima vez que publicar. Se a aplicação já corresponder a essa versão, o Studio di-lo e não altera nada. Se alguém publicou enquanto restaurava, o Studio não restaura nada e pede-lhe que tente novamente.

## Análise

O separador **Análise** mostra como as pessoas usam a aplicação e a rapidez com que esta responde. Escolha os últimos 7, 14 ou 30 dias.

| Secção | Mostra |
|---|---|
| **Views per day** | Quantas vezes a aplicação foi aberta em cada dia. |
| **Page load** | O tempo de carregamento mediano e o tempo que 95 por cento dos carregamentos superam, a partir dos carregamentos de página do período. |
| **Slowest queries** | As consultas que demoraram mais, com a frequência com que foram executadas e os respetivos tempos mediano, do extremo lento e mais lento. |
| **Erros** | O que correu mal no período, por tipo de erro e local da aplicação onde ocorreu. |

Quando um período contém mais atividade do que a Análise consegue ler, indica que os valores são parciais. Quando os carregamentos de página ultrapassam o [limite de desempenho](/pt-pt/guides/panel-apps/app-kit/#limites-de-desempenho) da aplicação, a Análise avisa-o de quantos foram e de que consultas foram lentas. A Análise nunca mostra os dados que uma consulta devolveu nem os nomes das pessoas que abriram a aplicação.

Ambos os separadores exigem que a aplicação esteja atribuída a um projeto; uma aplicação não atribuída mostra uma indicação para a atribuir.

## Alertas e resumos

Escolha **Alerts & Digests** para configurar notificações que vigiam um número nos dados da aplicação e avisam quando ultrapassa um limite, ou que enviam um resumo de acordo com um agendamento. Consulte [Alertas e resumos](/pt-pt/guides/panel-apps/alerts-and-digests/).

## Listar uma aplicação na galeria

Escolha **Gallery…** para listar a aplicação como um modelo a partir do qual qualquer pessoa que possa ver o seu projeto pode criar a sua própria aplicação, ou para a retirar da galeria. Consulte [A galeria de aplicações](/pt-pt/guides/panel-apps/gallery/).

## Afixar no Início

Escolha **Pin to Home** para adicionar a aplicação ao quadro **Início** do projeto, e **Unpin from Home** para a remover.

## Eliminar uma aplicação

Eliminar uma aplicação Panel pede-lhe primeiro que confirme. Em **As minhas aplicações Panel**, use o ícone de **menos** na linha da aplicação. Anular a publicação também pede confirmação.

## Passos seguintes

- [Criar aplicações Panel com o Weave](/pt-pt/guides/panel-apps/build-with-weave/) — descreva a aplicação e aprove a alteração exata.
- [O Panel App Kit](/pt-pt/guides/panel-apps/app-kit/) — os componentes que os pontos de partida de tabela, vista e modelo do Studio utilizam.
- [Alertas e resumos](/pt-pt/guides/panel-apps/alerts-and-digests/) — notifique as pessoas quando um número ultrapassa um limite, ou de acordo com um agendamento.
- [A galeria de aplicações](/pt-pt/guides/panel-apps/gallery/) — partilhe uma aplicação como ponto de partida para outras pessoas.
- [Utilizar uma aplicação Panel](/pt-pt/guides/panel-apps/using/) — registos, utilização e recompilações depois de publicar.
