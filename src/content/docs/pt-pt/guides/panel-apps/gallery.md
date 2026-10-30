---
title: A galeria de aplicações
description: Adicione uma aplicação Studio à galeria ou retire-a, e crie uma nova aplicação a partir de uma aplicação listada.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

A galeria de aplicações é a prateleira que a sua área de trabalho mantém com aplicações Panel prontas a usar. Qualquer pessoa que possa ver o projeto de uma aplicação listada pode criar a sua própria cópia num projeto que possa editar e alterá-la, para que uma boa aplicação se torne um ponto de partida em vez de algo que as pessoas voltam a construir.

## Criar uma aplicação a partir da galeria

1. Em **As minhas aplicações Panel**, escolha **Nova aplicação Studio**.
2. Em **Começar a partir de**, escolha **A partir da galeria**.
3. Selecione uma aplicação em **Aplicação da galeria**. A respetiva descrição aparece por baixo do seletor.
4. Dê um nome à aplicação, selecione o respetivo **Projeto** e escolha **Criar**.

Também pode escolher **Galeria** na barra de ferramentas de **As minhas aplicações Panel** para navegar pela galeria isoladamente. Esta lista cada aplicação com o respetivo nome, projeto e descrição, e **Criar aplicação a partir disto…**. A galeria lista apenas as aplicações em projetos que pode ver.

A nova aplicação é uma cópia dos ficheiros da aplicação listada. A sua cópia e o original são independentes: alterar um nunca altera o outro.

## Listar a sua aplicação

É necessário ter acesso de edição ao projeto da aplicação. Só as aplicações criadas no [Panel Studio](/pt-pt/guides/panel-apps/studio/) que pertencem a um projeto podem ser listadas; as aplicações de servidor, WASM e Dash não podem.

1. Abra a aplicação no Studio e escolha **Galeria…**. O botão só está disponível para uma aplicação que pertença a um projeto.
2. Introduza uma **Descrição** para mostrar no cartão da galeria.
3. Escolha **Listar na galeria** e confirme.

Para alterar a descrição, escolha **Atualizar listagem**. Para remover a aplicação da galeria, abra **Galeria…** e escolha **Retirar da galeria**. Mover a aplicação para outro projeto também a retira da galeria.

## Quem pode ver o quê

Todas as pessoas que podem ver o projeto podem ler o código-fonte da aplicação listada, incluindo as alterações que publicar mais tarde. Não coloque palavras-passe nem notas privadas nos ficheiros de uma aplicação listada. Ao escolher listar uma aplicação, é-lhe pedido que confirme isto primeiro, e a listagem fica registada no registo de auditoria.

As pessoas que criam a partir da galeria recebem apenas uma cópia dos ficheiros na pasta da própria aplicação. Nunca veem os detalhes do repositório da aplicação, as ligações nem as definições de webhook.

## Passos seguintes

- [Panel Studio](/pt-pt/guides/panel-apps/studio/) — edite e publique a cópia que criar.
- [O kit de aplicações Panel](/pt-pt/guides/panel-apps/app-kit/) — os componentes com que a maioria das aplicações da galeria é construída.
