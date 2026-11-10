---
title: Gestão de ficheiros
description: Gira contas de armazenamento de ficheiros no PlaidCloud para importar e exportar dados através de CSV, Excel, Parquet e outros formatos de ficheiro.
sidebar:
  label: Descrição geral
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud Documents — armazene, organize, pesquise e partilhe ficheiros junto dos seus dados e fluxos de trabalho. Os documentos podem provir de qualquer conta de armazenamento ligada e ser referenciados em fluxos de trabalho.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="As contas de armazenamento ligadas, como S3, Google Cloud Storage e OneDrive, alimentam o PlaidCloud Documents, onde os ficheiros são armazenados, organizados, pesquisados e partilhados. Os passos de fluxo de trabalho referenciam depois esses ficheiros para importar e exportar dados." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="dc-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">contas de armazenamento</text>
  <rect x="16" y="40" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="60" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">S3</text>
  <rect x="16" y="82" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Cloud Storage</text>
  <rect x="16" y="124" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">OneDrive</text>
  <path d="M136 55 C186 55 206 92 246 96" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 97 L246 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 139 C186 139 206 108 246 104" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="248" y="70" width="180" height="64" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="338" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Documents</text>
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">armazenar · organizar · pesquisar · partilhar</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">passos de fluxo de trabalho</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">importar · exportar ficheiros</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Os ficheiros chegam ao Documents a partir de qualquer conta de armazenamento ligada, onde os armazena, organiza, pesquisa e partilha — e depois referencia-os a partir de passos de fluxo de trabalho para importar e exportar dados.</figcaption>
</figure>

## A aplicação Document

**Document** abre com uma barra lateral à esquerda e, ao lado, a página que escolher. Os membros que não podem abrir uma página não veem o respetivo item.

| Item da barra lateral | O que mostra |
|---|---|
| **Visão geral** | Mosaicos para as suas contas (**Contas**, **Partilhadas**, **Privadas para si**, **Buckets geridos**, **Serviços externos** e **Desativado** quando uma conta requer atenção), ficheiros **Afixados**, **Contas por serviço** e **Quem as pode utilizar**. Selecione um ficheiro afixado para abrir **Procurar** na respetiva pasta com o ficheiro selecionado. |
| **Procurar** | O explorador de ficheiros. Escolha a conta na lista do cabeçalho da página. Consulte [Utilizar contas de documentos](/pt-pt/guides/documents/using-document/). |
| **Partilhadas** | Contas partilhadas consigo. Faça duplo clique numa linha para a explorar. |
| **As minhas privadas** | Contas que só podem ser utilizadas por si. Faça duplo clique numa linha para a explorar. |
| **Gerir** | Contas de que é proprietário, com **Nome**, **Serviço**, **Tipo de segurança**, **Estado** e **Descrição**. Um administrador da área de trabalho vê aqui todas as contas de documentos e pode gerir qualquer conta que, de outra forma, possa gerir; as contas geridas pelo sistema são recusadas e as contas de bucket gerido não podem ser clonadas. |

A barra lateral mostra uma contagem junto a **Partilhadas**, **As minhas privadas** e **Gerir**. Para um administrador da área de trabalho que tem contas que não são suas, **Gerir** mostra **admin** em vez de uma contagem. A Visão geral tem os botões **Procurar ficheiros** e **Nova conta** para um início rápido.

### Ações de linha em Gerir

Abra o menu **⋯** de uma linha, clique com o botão direito na linha ou utilize o menu **Ações** da barra de ferramentas para:

- **Abrir** e **Editar**, que abrem a página da conta.
- **Clonar…**, **Histórico de versões** e **Onde é utilizado…**. Consulte [Onde é utilizado e redirecionamento](/pt-pt/guides/documents/account-management/document-account-used-by/).
- **Quem a pode usar**, com **Membros**, **Grupos**, **Agentes** e **Proprietários**. Consulte [Controlar o acesso às contas de documentos](/pt-pt/guides/documents/account-management/control-document-account-access/).
- **Ativar** ou **Desativar**, e **Eliminar**.

### A página da conta

**Nova conta**, **Abrir** e **Editar** mostram a conta como uma página, com **Gerir contas** no topo para voltar. A página tem cartões para:

- **Geral**: o nome, o serviço, o bucket e o caminho inicial da conta.
- **Acesso**: o modelo de segurança e quem pode utilizar a conta. **Membros**, **Grupos**, **Agentes** e **Proprietários** têm cada um uma ligação **Editar** que abre o mesmo seletor do menu da linha.
- **Credenciais**: campos só de escrita para o serviço escolhido. Uma nota **Credenciais guardadas** indica que as credenciais estão definidas, e os valores guardados nunca são mostrados. Deixe um campo em branco para manter o que está guardado. As contas SFTP também têm **Testar ligação**.
- **SSH**: as definições da chave, apenas para contas SFTP.

O cabeçalho tem **Procurar**, **Onde é utilizado** e um menu **Ações** com **Clonar**, **Histórico de versões**, **Ativar** ou **Desativar** e **Eliminar**. Se sair de uma página com alterações não guardadas, o PlaidCloud pergunta se pretende descartá-las.

As ligações e os marcadores antigos para ecrãs de documentos continuam a abrir a página correspondente.
