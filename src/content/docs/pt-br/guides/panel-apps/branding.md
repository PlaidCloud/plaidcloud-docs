---
title: Identidade visual do projeto e projetos de aplicativos
description: Defina cores da marca e um logotipo uma vez para um projeto, de modo que todos os aplicativos Panel dele sigam o mesmo visual, e atribua aplicativos Panel a um projeto ao publicá-los ou depois.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/branding.md
---

Um aplicativo Panel pertence a um projeto. O projeto faz duas coisas pelo aplicativo: é de onde o aplicativo lê suas tabelas por padrão e guarda as cores e o logotipo que o aplicativo exibe. Defina a identidade visual uma vez e todos os aplicativos do projeto a adotam.

## Aplicar a identidade visual a um projeto

1. Abra o projeto e vá para a guia **Início** dele.
2. No grupo **Panel App Branding**, clique em **Edit Branding**.
3. Defina qualquer uma das cores. Clique em uma amostra para escolher uma cor ou digite um valor hexadecimal, como `#0078d4`.
4. Opcionalmente, escolha um logotipo.
5. Confira a **Pré-visualização** e clique em **Salvar**.

Somente Gerentes e Arquitetos podem salvar a identidade visual. Os outros membros do projeto veem o formulário somente para leitura.

**Reset to default** limpa todas as cores e o logotipo. Salvar substitui a identidade visual inteira, então uma cor que você deixar em branco volta ao padrão do PlaidCloud.

### Cores

| Configuração | O que ela colore |
|---|---|
| **Brand** | Botões, a guia ativa, controles deslizantes e outros controles primários. |
| **Brand accent** | Destaques secundários. |
| **Brand hover** | Um controle primário enquanto o ponteiro está sobre ele. |
| **Brand pressed** | Um controle primário enquanto ele está pressionado. |
| **Header background** | A barra de cabeçalho do aplicativo. |
| **Header text** | O título e o nome do usuário no cabeçalho. |
| **Link** | Links. |
| **Text on brand** | Texto que fica sobre um controle na cor da marca. |

Essas oito são as únicas configurações. As cores devem ser valores hexadecimais de 3 ou 6 dígitos. Superfícies, texto do corpo e bordas mantêm o visual do PlaidCloud nos modos claro e escuro, então uma identidade visual não pode tornar um aplicativo ilegível.

### Logotipo

O logotipo é uma imagem de uma [conta de documentos](/pt-br/guides/documents/) no espaço de trabalho do projeto.

1. Envie a imagem para uma pasta chamada `branding` na raiz da conta de documentos.
2. Em **Edit Branding**, escolha a **Conta de documentos** e depois a imagem em **Image in the branding/ folder**.

O logotipo pode ser um arquivo PNG, JPEG, GIF, WebP ou SVG de até 512 KB. Ele aparece no lado direito do cabeçalho do aplicativo. A imagem deve estar diretamente em `branding/` ou em uma pasta dentro dela, e quem salvar a identidade visual precisa conseguir ler a conta.

### Quando as alterações aparecem

Um aplicativo lê sua identidade visual quando a sessão de um visualizador começa. As alterações salvas aparecem na próxima vez que alguém abrir o aplicativo ou recarregá-lo.

## Atribuir um aplicativo a um projeto

### Ao publicar

A caixa de diálogo **Publicar aplicativo Panel de servidor** tem um seletor **Projeto** em **Configurações do diretório**. Escolha o projeto proprietário do aplicativo. Você precisa ter acesso ao projeto para publicar nele. O projeto é fixo depois que o aplicativo é publicado; para mover um aplicativo, use **Atribuir** conforme descrito abaixo.

Um aplicativo publicado com um projeto lê as tabelas desse projeto por padrão, então `table("sales")` não precisa de argumento de projeto.

### Para aplicativos existentes

1. Abra **Meus aplicativos Panel**.
2. Clique no ícone **Atribuir** na linha do aplicativo que você quer mover.
3. Escolha o **Projeto** e clique em **Revisar**.
4. Leia o resultado. Ele lista os membros do espaço de trabalho que hoje conseguem abrir o aplicativo, mas não são membros do projeto.
5. Clique em **Atribuir**.

Revisar não altera nada. A coluna **Projeto** em **Meus aplicativos Panel** mostra o projeto de cada aplicativo.

### Acesso

Quem pode abrir um aplicativo não muda hoje por causa do projeto dele: os visualizadores que já podiam abrir o aplicativo continuam podendo. Com o tempo, o acesso a um aplicativo passará a seguir a participação no projeto dele, e é por isso que **Revisar** lista os membros que não estão no projeto, para que você possa adicioná-los antes.

## Próximas etapas

- [O Panel App Kit](/pt-br/guides/panel-apps/app-kit/) — os componentes que usam a sua identidade visual.
- [Criando um aplicativo Panel](/pt-br/guides/panel-apps/creating/) — publique um aplicativo em um projeto.
