---
title: Utilizar uma aplicação Dash
description: Acompanhe o estado da compilação, abra, recompile, bloqueie, consulte os registos, edite e remova aplicações Plotly Dash publicadas a partir do ecrã As minhas aplicações Panel no PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/using.md
---

As aplicações Dash aparecem no mesmo ecrã **As minhas aplicações Panel** que as suas aplicações Panel WASM e de servidor, com **Dash** apresentado na coluna **Tempo de execução** e com um ícone próprio, para serem fáceis de distinguir. Tudo nesta página espelha [Utilizar uma aplicação Panel](/pt-pt/guides/panel-apps/using/) para uma aplicação de servidor, com uma exceção indicada abaixo: as aplicações Dash ainda não dispõem de **Usage Metrics**.

## Estado da compilação

A coluna **Estado** de uma aplicação Dash acompanha a respetiva compilação, e a lista é atualizada por si enquanto uma compilação está em curso:

- **A compilar…** — o PlaidCloud está a compilar o seu repositório num contentor. A aplicação ainda não tem URL.
- **Pronta** — a compilação foi bem-sucedida. O URL da aplicação está ativo e o ícone **Abrir** aparece na respetiva linha.
- **Falhou** — a compilação não foi concluída. Verifique o ponto de entrada e o ramo e, em seguida, edite a aplicação para voltar a publicar.

## Recompilar uma aplicação Dash

Clique no ícone **Recompilar** na linha de uma aplicação Dash para a recompilar e voltar a implementar sem alterar as respetivas definições. O estado da aplicação regressa a **A compilar…** enquanto o PlaidCloud volta a compilar o mesmo ramo e ponto de entrada, e depois passa novamente a **Pronta** quando a nova compilação estiver ativa.

Use **Recompilar** após alterações de dependências, atualizações da imagem base ou uma compilação falhada transitória. Editar e guardar uma aplicação Dash também a recompila, mas uma recompilação não exige a abertura do formulário de edição.

## Bloquear uma aplicação

Clique no ícone de **cadeado** na linha de uma aplicação para a proteger de alterações acidentais. Enquanto uma aplicação Dash está bloqueada:

- **Editar**, **Remover** e **Recompilar** recusam-se a executar e informam que a aplicação está bloqueada.
- **Um envio para o ramo da aplicação não a recompila** — a recompilação automática é ignorada até desbloquear a aplicação. Envie novamente (ou use **Recompilar**) após o desbloqueio para que a alteração seja aplicada.
- Abrir a aplicação e consultar os respetivos registos continuam ambos a funcionar — o bloqueio só impede alterações, nunca os leitores.

Clique novamente no ícone para desbloquear. O ícone mostra o estado atual da aplicação: fechado quando está bloqueada, aberto quando não está. O bloqueio é uma proteção contra acidentes, não um controlo de segurança — qualquer pessoa que possa editar aplicações Dash também as pode desbloquear.

## Abrir uma aplicação Dash

Clique no ícone **Abrir** no início da linha de uma aplicação pronta para a iniciar num novo separador, em `https://<your-tenant-host>/serve/<slug>/`. O ícone só aparece quando a aplicação está **Pronta**.

Uma aplicação Dash escala até zero quando está inativa para poupar recursos, pelo que a primeira abertura após um período de inatividade tem de a iniciar de novo. Enquanto isso acontece, vê um **ecrã de carregamento do PlaidCloud** em vez de um separador em branco, e a aplicação aparece por si própria quando estiver pronta. Se uma aplicação não conseguir arrancar, o ecrã de carregamento transforma-se numa mensagem **"This app didn't start"** com um botão **Tentar novamente**; se isso continuar a acontecer, edite a aplicação para verificar o ponto de entrada e o ramo e volte a publicar.

> **Um `dcc.Interval` (ou qualquer outra sondagem sempre ativa) anula a escala até zero enquanto o respetivo separador se mantiver aberto.** A escala até zero depende de a aplicação ficar silenciosa — sem pedidos em curso — quando ninguém a está a utilizar ativamente. Um componente que continua a fazer pedidos num temporizador, como o `dcc.Interval`, mantém a aplicação acordada enquanto esse separador estiver aberto, mesmo que a pessoa que o está a ver se tenha ausentado. Se pretende que uma aplicação reduza a escala entre visitas, evite a sondagem sempre ativa ou pare o intervalo depois de a página estar inativa durante algum tempo.

## Consultar os registos

Clique no ícone **Ver registos** na linha de uma aplicação Dash para abrir o respetivo visualizador de registos, com os mesmos separadores **Tempo de execução** e **Compilação**, filtros, intervalo de tempo e painel de detalhe de uma aplicação Panel de servidor — consulte [Consultar os registos](/pt-pt/guides/panel-apps/using/#ver-registos-aplicações-de-servidor) para conhecer o funcionamento completo. Cada linha de registo de execução é identificada com o **utilizador** cuja sessão a produziu, tal como acontece nas de uma aplicação Panel de servidor.

**Usage Metrics não estão disponíveis para aplicações Dash nesta versão** — o ícone **Usage Metrics** que aparece na linha de uma aplicação Panel de servidor não aparece para as aplicações Dash, pelo que ainda não existe uma discriminação de utilizadores únicos/sessões para consultar.

## Editar uma aplicação

Clique no ícone de **lápis** na linha de uma aplicação Dash para a editar. Pode alterar o nome, o slug, o ramo, o ponto de entrada, o CPU, a memória, a janela de inatividade, a indicação de acesso público, os domínios de disponibilização incorporada e o memorando. A **Ligação Git** fica fixa depois de a aplicação ser criada e é apresentada só de leitura. Não existe nenhum campo **Design** para editar — essa definição é específica do Panel. Guardar recompila a aplicação — o respetivo estado regressa a **A compilar…** até a nova compilação estar pronta.

## Remover uma aplicação

Clique no ícone de **menos** na linha de uma aplicação Dash e confirme. Remover a aplicação elimina a respetiva compilação e implementação, e o URL da aplicação deixa de funcionar imediatamente.
