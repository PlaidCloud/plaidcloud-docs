---
title: Panel Studio
description: Crie, edite, pré-visualize e publique aplicações Panel sem sair do PlaidCloud, restaure depois uma versão anterior, consulte a utilização e a velocidade da aplicação, configure alertas e resumos, liste-a na galeria e afixe-a no Início.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

O Panel Studio é o editor de aplicações Panel dentro do PlaidCloud. Mostra os ficheiros da aplicação ao lado de um editor, cria uma pré-visualização privada que pode abrir e publica a aplicação quando estiver pronta. Não precisa de um repositório Git para começar.

## Abrir o Panel Studio

- No painel **Início** de um projeto, escolha **Abrir no Studio** numa aplicação Panel.
- Em **Aplicações**, escolha **Studio** na linha de uma aplicação.

Para iniciar uma nova aplicação, escolha **Novo app** > **Studio**. Também se encontra na linha **Aplicações Studio** do cartão **Aplicações e identidade visual** do separador **Início** de um projeto. Para criar a partir de uma tabela, selecione-a no separador **Tabelas** do projeto e escolha **Criar aplicação Panel**.

## Criar uma aplicação

A caixa de diálogo **Nova aplicação Studio** permite começar a partir de uma de cinco origens:

| Começar a partir de | Resultado |
|---|---|
| **Aplicação em branco** | Uma aplicação mínima com um `app.py` e um `requirements.txt`. |
| **A partir de uma tabela** | Uma aplicação criada sobre a tabela escolhida. |
| **A partir de uma vista** | O mesmo, criado sobre uma vista do projeto. |
| **A partir de outra aplicação Studio** | Uma cópia de uma das suas aplicações Studio. |
| **A partir da galeria** | Uma cópia de uma aplicação que a sua área de trabalho listou na [galeria de aplicações](/pt-pt/guides/panel-apps/gallery/). |

Dê um nome à aplicação, escolha o respetivo **Projeto** e selecione **Criar**. O Studio abre a nova aplicação com os ficheiros listados à esquerda. No caso de uma tabela ou de uma vista, o pedido do Weave para criar a primeira página da aplicação fica pronto a enviar. Consulte [Criar uma aplicação Panel](/pt-pt/guides/panel-apps/creating/).

## Onde reside a aplicação

Uma aplicação Studio é uma pasta com o nome da aplicação (`<app-slug>/`) dentro do repositório `apps` da sua área de trabalho no [PlaidCloud Git](/pt-pt/guides/git/), o mesmo repositório onde residem as suas outras aplicações Panel. O Studio não cria um repositório próprio para a aplicação, pelo que pode encontrar e editar o respetivo código-fonte em `apps`, junto das outras aplicações.

- **Ramo de rascunho.** O trabalho que ainda não está em produção é mantido num ramo com o nome `studio-<app-slug>`. **Publicar** copia a pasta da aplicação desse ramo para o ramo principal.
- **Recompilações.** Um push para `apps` só recompila uma aplicação quando a pasta dessa aplicação ou o `requirements.txt` na raiz do repositório tiverem sido alterados.
- **Aplicações existentes.** Uma aplicação Studio que estava num repositório próprio é movida automaticamente para a sua pasta. O repositório antigo é arquivado: permanece, só de leitura, e nunca é eliminado.

## Editar

Escolha um ficheiro na lista para o editar no editor. Indique as dependências Python em `requirements.txt`, um pacote por linha. São instaladas quando a aplicação é compilada.

Escolha **Perguntar ao Weave** para que o Weave escreva ou altere a aplicação por si. Consulte [Criar aplicações Panel com o Weave](/pt-pt/guides/panel-apps/build-with-weave/).

## Guardar, pré-visualizar e publicar

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="Guardar mantém um rascunho que só o utilizador vê. A pré-visualização cria uma cópia privada do rascunho para o editor. Publicar substitui a aplicação em produção após a confirmação." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Guardar</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">só rascunho</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Pré-visualização</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">só editores</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Publicar</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">a aplicação em produção</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">As suas edições só chegam aos visualizadores quando publica.</figcaption>
</figure>

### Guardar

**Guardar** armazena as alterações como rascunho. A aplicação em produção não muda e mais ninguém vê o rascunho.

### Pré-visualização

**Pré-visualização** compila o rascunho guardado como uma cópia privada e abre-a. Só os editores da aplicação podem abrir uma pré-visualização.

- Uma pré-visualização é removida após 24 horas sem que seja guardada qualquer alteração.
- Uma área de trabalho pode ter até 10 pré-visualizações em simultâneo.
- Guarde novamente e escolha **Pré-visualização** para ver as edições mais recentes.

### Publicar

**Publicar** substitui a aplicação em produção pelo rascunho guardado. Exige permissão de edição no projeto da aplicação e o Studio pede primeiro confirmação.

Se outra pessoa tiver publicado uma alteração depois de ter aberto a aplicação, o Studio indica um conflito em vez de substituir o trabalho dessa pessoa. Volte a carregar a aplicação, transfira as suas edições e publique novamente.

## Estado da compilação e erros

O separador **Criar** mostra o estado da compilação mais recente e é atualizado à medida que esta decorre. Quando uma compilação falha, o separador lista cada erro com o respetivo ficheiro e número de linha, para que possa ir diretamente à linha. Os problemas de dependências em `requirements.txt` incluem uma sugestão para a correção.

Os erros e os avisos também são assinalados nas respetivas linhas no editor, pelo que vê o problema onde ele ocorre.

Para saber o que significa cada estado depois de a aplicação ser publicada, consulte [Utilizar uma aplicação Panel](/pt-pt/guides/panel-apps/using/#estado-da-compilação-aplicações-de-servidor).

## Histórico e restauro

O separador **Histórico** lista todas as versões publicadas da aplicação, da mais recente para a mais antiga, com o respetivo estado de compilação. Escolha **Carregar mais** para ver as mais antigas.

Para voltar a uma versão anterior, escolha **Restaurar** nessa versão e confirme. A versão restaurada passa a ser a aplicação em produção e é recompilada. O rascunho não guardado não se perde: permanece no rascunho e entra em produção por cima da versão restaurada na próxima vez que publicar. Se a aplicação já corresponder a essa versão, o Studio indica-o e não altera nada. Se alguém tiver publicado durante o restauro, o Studio não restaura nada e pede que tente novamente.

## Análises

O separador **Análises** mostra como as pessoas utilizam a aplicação e a rapidez com que esta responde. Escolha os últimos 7, 14 ou 30 dias.

| Secção | Mostra |
|---|---|
| **Visualizações por dia** | Quantas vezes a aplicação foi aberta em cada dia. |
| **Carregamento de página** | O tempo de carregamento mediano e o tempo que 95 por cento dos carregamentos não excedem, a partir dos carregamentos de página do período. |
| **Consultas mais lentas** | As consultas que demoraram mais tempo, com a frequência com que foram executadas e os respetivos tempos mediano, do extremo lento e mais lento. |
| **Erros** | O que correu mal no período, por tipo de erro e local da aplicação onde ocorreu. |

Quando um período contém mais atividade do que as Análises conseguem ler, é indicado que os valores são parciais. Quando os carregamentos de página ultrapassam o [orçamento de desempenho](/pt-pt/guides/panel-apps/app-kit/#orçamentos-de-desempenho) da aplicação, as Análises avisam quantos o fizeram e quais as consultas que foram lentas. As Análises nunca mostram os dados devolvidos por uma consulta nem os nomes das pessoas que abriram a aplicação.

Os separadores **Histórico** e **Análises** exigem que a aplicação esteja atribuída a um projeto; uma aplicação sem atribuição mostra um pedido para a atribuir.

## Alertas e resumos

Escolha **Alertas e resumos** para configurar notificações que vigiam um número nos dados da aplicação e avisam quando ultrapassa um limite, ou que enviam um resumo de acordo com um agendamento. Consulte [Alertas e resumos](/pt-pt/guides/panel-apps/alerts-and-digests/).

## Listar uma aplicação na galeria

Escolha **Galeria…** no Studio. Escolha **Listar na galeria** para listar a aplicação como um modelo a partir do qual qualquer pessoa que possa ver o respetivo projeto pode criar a sua própria aplicação, ou **Retirar da galeria** para a remover. O botão está disponível para aplicações que pertencem a um projeto. É necessário acesso de edição ao projeto. Consulte [A galeria de aplicações](/pt-pt/guides/panel-apps/gallery/).

## Afixar no Início

Escolha **Afixar no Início** para adicionar a aplicação ao painel **Início** do projeto e **Desafixar do Início** para a remover.

## Eliminar uma aplicação

Eliminar uma aplicação Panel pede primeiro confirmação. Em **Aplicações**, utilize o ícone **menos** na linha da aplicação. Anular a publicação também pede confirmação.

## Passos seguintes

- [Criar aplicações Panel com o Weave](/pt-pt/guides/panel-apps/build-with-weave/) — descreva a aplicação e aprove a alteração exata.
- [O kit de aplicações Panel](/pt-pt/guides/panel-apps/app-kit/) — os componentes que os pontos de partida do Studio para tabelas e vistas utilizam.
- [Alertas e resumos](/pt-pt/guides/panel-apps/alerts-and-digests/) — notifique as pessoas quando um número ultrapassa um limite ou de acordo com um agendamento.
- [A galeria de aplicações](/pt-pt/guides/panel-apps/gallery/) — partilhe uma aplicação como ponto de partida para outras pessoas.
- [Utilizar uma aplicação Panel](/pt-pt/guides/panel-apps/using/) — registos, utilização e recompilações depois de publicar.
