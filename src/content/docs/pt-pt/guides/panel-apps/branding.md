---
title: Identidade visual do projeto e projetos das aplicações
description: Defina uma só vez as cores da marca e um logótipo para um projeto, para que todas as aplicações Panel nele fiquem coerentes, e atribua aplicações Panel a um projeto ao publicá-las ou depois.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/branding.md
---

Uma aplicação Panel pertence a um projeto. O projeto faz duas coisas pela aplicação: é onde a aplicação lê as suas tabelas por predefinição e contém as cores e o logótipo que a aplicação apresenta. Defina a identidade visual uma só vez e todas as aplicações do projeto a adotam.

## Definir a identidade visual de um projeto

1. Abra o projeto e vá ao respetivo separador **Início**.
2. No grupo **Panel App Branding**, clique em **Edit Branding**.
3. Defina qualquer uma das cores. Clique numa amostra para escolher uma cor, ou escreva um valor hexadecimal como `#0078d4`.
4. Opcionalmente, escolha um logótipo.
5. Verifique a **Pré-visualização** e clique em **Guardar**.

Só os Gestores e os Arquitetos podem guardar a identidade visual. Os outros membros do projeto veem o formulário só de leitura.

**Reset to default** limpa todas as cores e o logótipo. Guardar substitui toda a identidade visual, pelo que uma cor que deixe em branco volta à predefinição do PlaidCloud.

### Cores

| Definição | O que colore |
|---|---|
| **Brand** | Botões, o separador ativo, manípulos de controlos deslizantes e outros controlos principais. |
| **Brand accent** | Destaques secundários. |
| **Brand hover** | Um controlo principal enquanto o ponteiro está sobre ele. |
| **Brand pressed** | Um controlo principal enquanto está premido. |
| **Header background** | A barra de cabeçalho da aplicação. |
| **Header text** | O título e o nome do utilizador no cabeçalho. |
| **Ligação** | Ligações. |
| **Text on brand** | Texto que se encontra sobre um controlo com a cor da marca. |

Estas oito são as únicas definições. As cores têm de ser valores hexadecimais de 3 ou 6 dígitos. As superfícies, o texto do corpo e as margens mantêm o aspeto do PlaidCloud nos modos claro e escuro, pelo que uma marca não pode tornar uma aplicação ilegível.

### Logótipo

O logótipo é uma imagem de uma [conta de documentos](/pt-pt/guides/documents/) na área de trabalho do projeto.

1. Carregue a imagem para uma pasta com o nome `branding` no nível superior da conta de documentos.
2. Em **Edit Branding**, escolha a **Conta de documentos** e depois a imagem em **Image in the branding/ folder**.

O logótipo pode ser um ficheiro PNG, JPEG, GIF, WebP ou SVG até 512 KB. Aparece no lado direito do cabeçalho da aplicação. A imagem tem de estar diretamente em `branding/` ou numa pasta dentro dela, e quem guardar a identidade visual tem de poder ler a conta.

### Quando as alterações aparecem

Uma aplicação lê a sua identidade visual quando a sessão de um visualizador começa. As alterações guardadas aparecem na próxima vez que alguém abrir a aplicação ou a recarregar.

## Atribuir uma aplicação a um projeto

### Ao publicar

A caixa de diálogo **Publicar aplicação Panel de servidor** tem um seletor **Projeto** em **Definições do diretório**. Escolha o projeto que é proprietário da aplicação. Precisa de acesso ao projeto para publicar nele. O projeto fica fixo depois de a aplicação ser publicada; para mover uma aplicação, use **Atribuir** conforme descrito abaixo.

Uma aplicação publicada com um projeto lê por predefinição as tabelas desse projeto, pelo que `table("sales")` não precisa de argumento de projeto.

### Para aplicações existentes

1. Abra **As minhas aplicações Panel**.
2. Clique no ícone **Atribuir** na linha da aplicação que pretende mover.
3. Escolha o **Projeto** e clique em **Rever**.
4. Leia o resultado. Lista os membros da área de trabalho que podem abrir hoje a aplicação mas não são membros do projeto.
5. Clique em **Atribuir**.

Rever não altera nada. A coluna **Projeto** em **As minhas aplicações Panel** mostra o projeto de cada aplicação.

### Acesso

Quem pode abrir uma aplicação não é alterado hoje pelo seu projeto: os visualizadores que já podiam abrir a aplicação continuam a poder. Com o tempo, o acesso a uma aplicação passará a seguir a pertença ao respetivo projeto, razão pela qual **Rever** lista os membros que não estão no projeto, para que os possa adicionar primeiro.

## Passos seguintes

- [O Panel App Kit](/pt-pt/guides/panel-apps/app-kit/) — os componentes que usam a sua identidade visual.
- [Criar uma aplicação Panel](/pt-pt/guides/panel-apps/creating/) — publique uma aplicação num projeto.
