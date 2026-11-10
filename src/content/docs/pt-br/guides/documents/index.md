---
title: Gerenciamento de arquivos
description: Gerencie contas de armazenamento de arquivos no PlaidCloud para importar e exportar dados em CSV, Excel, Parquet e outros formatos de arquivo.
sidebar:
  label: Visão geral
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud Documents: armazene, organize, pesquise e compartilhe arquivos junto com seus dados e fluxos de trabalho. Os documentos podem vir de qualquer conta de armazenamento conectada e ser referenciados em fluxos de trabalho.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="Contas de armazenamento conectadas, como S3, Google Cloud Storage e OneDrive, alimentam o PlaidCloud Documents, onde os arquivos são armazenados, organizados, pesquisados e compartilhados. As etapas do fluxo de trabalho então referenciam esses arquivos para importar e exportar dados." style="width:100%;max-width:680px;height:auto;">
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
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">armazenar · organizar · pesquisar · compartilhar</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">etapas do fluxo de trabalho</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">importar · exportar arquivos</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Os arquivos chegam ao Documents a partir de qualquer conta de armazenamento conectada, onde você os armazena, organiza, pesquisa e compartilha, e depois os referencia em etapas de fluxo de trabalho para importar e exportar dados.</figcaption>
</figure>

## O espaço de trabalho do Documents

**Documento** abre com uma barra lateral à esquerda e, ao lado dela, a página que você escolher. Os membros que não podem abrir uma página não veem o item dela.

| Item da barra lateral | O que mostra |
|---|---|
| **Visão geral** | Blocos para as suas contas (**Contas**, **Compartilhadas**, **Privadas para você**, **Buckets gerenciados**, **Serviços externos** e **Desativado** quando uma conta precisa de atenção), arquivos **Fixados**, **Contas por serviço** e **Quem pode usá-las**. Selecione um arquivo fixado para abrir **Procurar** na pasta dele, com o arquivo selecionado. |
| **Procurar** | O explorador de arquivos. Escolha a conta na lista do cabeçalho da página. Consulte [Usar contas de documentos](/pt-br/guides/documents/using-document/). |
| **Compartilhadas** | As contas compartilhadas com você. Clique duas vezes em uma linha para navegar por ela. |
| **Minhas privadas** | As contas que somente você pode usar. Clique duas vezes em uma linha para navegar por ela. |
| **Gerenciar** | As contas das quais você é proprietário, com **Nome**, **Serviço**, **Tipo de segurança**, **Status** e **Descrição**. Um administrador do espaço de trabalho vê todas as contas de documentos aqui e pode gerenciar qualquer uma delas. |

A barra lateral mostra uma contagem ao lado de **Compartilhadas**, **Minhas privadas** e **Gerenciar**. A Visão geral tem os botões **Procurar arquivos** e **Nova conta** para começar rapidamente.

### Ações de linha em Gerenciar

Abra o menu **⋯** de uma linha, clique com o botão direito na linha ou use o menu **Ações** da barra de ferramentas para:

- **Abrir** e **Editar**, que abrem a página da conta.
- **Clonar…**, **Histórico de versões** e **Onde é usado…**. Consulte [Onde uma conta de documentos é usada e reapontamento](/pt-br/guides/documents/account-management/document-account-used-by/).
- **Quem pode usá-la**, com **Membros**, **Grupos**, **Agentes** e **Proprietários**. Consulte [Controlar o acesso às contas de documentos](/pt-br/guides/documents/account-management/control-document-account-access/).
- **Ativar** ou **Desativar**, e **Excluir**.

### A página da conta

**Nova conta**, **Abrir** e **Editar** mostram a conta como uma página, com **Gerenciar contas** no topo para voltar. Ela tem cartões para:

- **Geral**: o nome, o serviço, o bucket e o caminho inicial da conta.
- **Acesso**: o modelo de segurança e quem pode usar a conta. **Membros**, **Grupos**, **Agentes** e **Proprietários** têm, cada um, um link **Editar** que abre o mesmo seletor do menu da linha.
- **Credenciais**: campos somente de gravação para o serviço que você escolheu. Uma observação **Credenciais salvas** mostra que as credenciais estão definidas, e os valores salvos nunca são exibidos. Deixe um campo em branco para manter o que está salvo. As contas SFTP também têm **Testar conexão**.
- **SSH**: as configurações de chave, somente para contas SFTP.

O cabeçalho tem **Procurar**, **Onde é usado** e um menu **Ações** com **Clonar**, **Histórico de versões**, **Ativar** ou **Desativar** e **Excluir**. Se você sair de uma página com alterações não salvas, o PlaidCloud pergunta se deve descartá-las.

Links e favoritos antigos para as telas de documentos ainda abrem a página correspondente.
