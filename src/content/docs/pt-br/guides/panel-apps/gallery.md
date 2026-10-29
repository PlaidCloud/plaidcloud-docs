---
title: A galeria de aplicativos
description: Liste um aplicativo Panel como um modelo a partir do qual o seu espaço de trabalho pode começar e crie um novo aplicativo a partir de um aplicativo listado.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

A galeria de aplicativos é a prateleira de aplicativos Panel prontos que o seu espaço de trabalho mantém. Quem pode visualizar o projeto de um aplicativo listado pode criar a própria cópia e alterá-la, então um bom aplicativo se torna um ponto de partida em vez de algo que as pessoas refazem.

## Criar um aplicativo a partir da galeria

1. Em **Meus aplicativos Panel**, escolha **Create app**.
2. Em **Começar de**, escolha **Da galeria**.
3. Escolha um aplicativo. A descrição dele aparece abaixo do seletor.
4. Dê um nome ao seu aplicativo, escolha o **Projeto** dele e escolha **Criar**.

Você também pode abrir a galeria separadamente, em que cada cartão mostra o nome, a descrição e o projeto do aplicativo, com **Create app from this…**. A galeria lista apenas aplicativos em projetos que você pode visualizar.

O novo aplicativo é uma cópia dos arquivos do aplicativo listado. Sua cópia e o original são separados: alterar um nunca altera o outro.

## Listar seu aplicativo

Você precisa de permissão de edição no projeto do aplicativo, e o aplicativo deve ter sido criado no [Panel Studio](/pt-br/guides/panel-apps/studio/) e atribuído a um projeto.

1. Abra o aplicativo no Studio e escolha **Gallery…**.
2. Informe uma **Descrição** para exibir no cartão da galeria.
3. Escolha **List in gallery** e confirme.

Para alterar a descrição, escolha **Update listing**. Para remover o aplicativo, escolha **Take out of gallery**. Mover o aplicativo para outro projeto também o remove da galeria.

## Quem pode ver o quê

Todos que podem visualizar o projeto podem ler o código-fonte do aplicativo listado, incluindo as alterações que você publicar depois. Não coloque senhas nem anotações privadas nos arquivos de um aplicativo listado. Ao escolher listar um aplicativo, você precisa confirmar isso antes, e a listagem é registrada no log de auditoria.

Quem cria a partir da galeria recebe uma cópia dos arquivos somente na pasta do próprio aplicativo. Essas pessoas nunca veem os detalhes do repositório, as conexões nem as configurações de webhook do aplicativo.

## Próximas etapas

- [Panel Studio](/pt-br/guides/panel-apps/studio/) — edite e publique a cópia que você criar.
- [O Panel App Kit](/pt-br/guides/panel-apps/app-kit/) — os componentes com que a maioria dos aplicativos da galeria é feita.
