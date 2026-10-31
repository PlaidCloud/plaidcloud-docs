---
title: A Galeria de aplicativos
description: Adicione um aplicativo Studio à galeria ou remova-o, e crie um novo aplicativo a partir de um já listado.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

A galeria de aplicativos é a prateleira em que seu espaço de trabalho guarda aplicativos Panel prontos. Qualquer pessoa que possa visualizar o projeto de um aplicativo listado pode criar sua própria cópia em um projeto que possa editar e alterá-la, de modo que um bom aplicativo se torna um ponto de partida em vez de algo que as pessoas refazem do zero.

## Criar um aplicativo a partir da galeria

1. Em **Meus aplicativos Panel**, escolha **Novo aplicativo Studio**.
2. Em **Começar de**, escolha **A partir da galeria**.
3. Selecione um aplicativo em **Aplicativo da galeria**. A descrição dele aparece abaixo do seletor.
4. Dê um nome ao seu aplicativo, selecione o **Projeto** dele e escolha **Criar**.

Você também pode escolher **Galeria** na barra de ferramentas de **Meus aplicativos Panel** para navegar pela galeria isoladamente. Ela lista cada aplicativo com seu nome, projeto e descrição, e **Criar aplicativo a partir disto…**. A galeria lista apenas aplicativos em projetos que você pode visualizar.

O novo aplicativo é uma cópia dos arquivos do aplicativo listado. Sua cópia e o original são independentes: alterar um nunca altera o outro.

## Listar seu aplicativo

Você precisa de acesso de edição ao projeto do aplicativo. Somente aplicativos criados no [Panel Studio](/pt-br/guides/panel-apps/studio/) que pertencem a um projeto podem ser listados; aplicativos de servidor, WASM e Dash não podem.

1. Abra o aplicativo no Studio e escolha **Galeria…**. O botão está disponível apenas para um aplicativo que pertence a um projeto.
2. Insira uma **Descrição** para exibir no cartão da galeria.
3. Escolha **Listar na galeria** e confirme.

Para alterar a descrição, escolha **Atualizar listagem**. Para remover o aplicativo da galeria, abra **Galeria…** e escolha **Remover da galeria**. Mover o aplicativo para outro projeto também o remove da galeria.

## Quem pode ver o quê

Todos que podem visualizar o projeto podem ler o código-fonte do aplicativo listado, incluindo as alterações que você publicar depois. Não coloque senhas nem anotações privadas nos arquivos de um aplicativo listado. Ao optar por listar um aplicativo, você precisa confirmar isso antes, e a listagem fica registrada no log de auditoria.

Quem cria a partir da galeria recebe uma cópia dos arquivos somente da pasta do próprio aplicativo. Essas pessoas nunca veem os detalhes do repositório, as conexões nem as configurações de webhook do aplicativo.

## Próximos passos

- [Panel Studio](/pt-br/guides/panel-apps/studio/) — edite e publique a cópia que você criar.
- [O Panel App Kit](/pt-br/guides/panel-apps/app-kit/) — os componentes dos quais a maioria dos aplicativos da galeria é feita.
