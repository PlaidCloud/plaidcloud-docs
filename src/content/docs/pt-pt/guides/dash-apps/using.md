---
title: Utilizar uma aplicação Dash
description: Acompanhe o estado da compilação, abra, recompile, bloqueie, consulte os registos, edite e remova aplicações Plotly Dash publicadas a partir do ecrã As minhas aplicações Panel do PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/using.md
---

As aplicações Dash aparecem no mesmo ecrã **As minhas aplicações Panel** que as aplicações Panel WASM e de servidor, com **Dash** indicado na coluna **Tempo de execução** e um ícone próprio para que sejam fáceis de distinguir. Tudo o que esta página descreve corresponde ao que está em [Utilizar uma aplicação Panel](/pt-pt/guides/panel-apps/using/) para uma aplicação de servidor, com uma exceção assinalada abaixo: as aplicações Dash ainda não dispõem de **Usage Metrics**.

## Estado da compilação

A coluna **Estado** de uma aplicação Dash acompanha a respetiva compilação, e a lista atualiza-se automaticamente enquanto uma compilação está em curso:

- **A compilar…** — o PlaidCloud está a compilar o repositório num contentor. A aplicação ainda não tem URL.
- **Pronta** — a compilação foi bem-sucedida. O URL da aplicação está ativo e o ícone **Abrir** aparece na respetiva linha.
- **Falhou** — a compilação não foi concluída. Verifique o ponto de entrada e o ramo e, em seguida, edite a aplicação para a voltar a publicar.

## Recompilar uma aplicação Dash

Clique no ícone **Recompilar** na linha de uma aplicação Dash para a recompilar e voltar a implementar sem alterar as respetivas definições. O estado da aplicação volta a **A compilar…** enquanto o PlaidCloud compila novamente o mesmo ramo e ponto de entrada, e passa de novo a **Pronta** quando a nova compilação estiver ativa.

Utilize **Recompilar** após alterações de dependências, atualizações da imagem base ou uma falha de compilação transitória. Editar e guardar uma aplicação Dash também a recompila, mas uma recompilação não exige abrir o formulário de edição.

## Bloquear uma aplicação

Clique no ícone de **cadeado** na linha de uma aplicação para a proteger contra alterações acidentais. Enquanto uma aplicação Dash estiver bloqueada:

- **Editar**, **Remover** e **Recompilar** recusam-se a ser executados e indicam que a aplicação está bloqueada.
- **Um push para o ramo da aplicação não a recompila** — a recompilação automática é ignorada até desbloquear a aplicação. Faça push novamente (ou utilize **Recompilar**) depois de desbloquear para incorporar a alteração.
- Abrir a aplicação e consultar os respetivos registos continuam a funcionar — o bloqueio impede apenas alterações, nunca o acesso de quem a visualiza.

Clique novamente no ícone para desbloquear. O ícone mostra o estado atual da aplicação: fechado quando está bloqueada, aberto quando não está. O bloqueio é uma proteção contra acidentes, não um controlo de segurança — qualquer pessoa que possa editar aplicações Dash também as pode desbloquear.

## Abrir uma aplicação Dash

Clique no ícone **Abrir** no início da linha de uma aplicação pronta para a iniciar num novo separador, em `https://<your-tenant-host>/serve/<slug>/`. O ícone só aparece quando a aplicação está **Pronta**.

Uma aplicação Dash é reduzida a zero quando está inativa para poupar recursos, pelo que a primeira abertura após um período de inatividade tem de a iniciar. Enquanto isso acontece, é apresentado um **ecrã de carregamento do PlaidCloud** em vez de um separador em branco, que mostra o progresso da aplicação pelas fases **A iniciar**, **A preparar** e **A carregar a aplicação**, e a aplicação aparece automaticamente quando estiver pronta. Se uma aplicação não conseguir iniciar, o ecrã de carregamento passa a apresentar uma mensagem a indicar que a aplicação não iniciou e em que passo parou, com um botão **Tentar novamente**; se isso continuar a acontecer, edite a aplicação para verificar o ponto de entrada e o ramo e volte a publicá-la.

> **Um `dcc.Interval` (ou qualquer outra consulta periódica permanente) anula a redução a zero enquanto o respetivo separador estiver aberto.** A redução a zero depende de a aplicação ficar em silêncio — sem pedidos em curso — quando ninguém a está a utilizar ativamente. Um componente que continua a fazer pedidos com base num temporizador, como `dcc.Interval`, mantém a aplicação ativa enquanto esse separador estiver aberto, mesmo que a pessoa que a está a ver se tenha ausentado. Se pretender que uma aplicação seja reduzida entre visitas, evite consultas periódicas permanentes ou pare o intervalo quando a página estiver inativa durante algum tempo.

## Consultar registos

Clique no ícone **Ver registos** na linha de uma aplicação Dash para abrir o respetivo visualizador de registos, com os mesmos separadores **Tempo de execução** e **Compilação**, filtros, intervalo de tempo e painel de detalhes que uma aplicação Panel de servidor tem — consulte [Consultar registos](/pt-pt/guides/panel-apps/using/#consultar-registos-aplicações-de-servidor) para conhecer o funcionamento completo. Cada linha do registo de tempo de execução é etiquetada com o **utilizador** cuja sessão a produziu, tal como acontece numa aplicação Panel de servidor.

**As Usage Metrics não estão disponíveis para aplicações Dash nesta versão** — o ícone **Usage Metrics** que aparece na linha de uma aplicação Panel de servidor não aparece nas aplicações Dash, pelo que ainda não existe uma discriminação de utilizadores únicos/sessões para consultar.

## Editar uma aplicação

Clique no ícone de **lápis** na linha de uma aplicação Dash para a editar. Pode alterar o nome, o slug, o ramo, o ponto de entrada, a CPU, a memória, o período de inatividade, a opção pública, os domínios de publicação incorporada e o memorando. A **Ligação Git** fica fixa depois de a aplicação ser criada e é apresentada apenas para leitura. Não existe um campo **Design** para editar — essa definição é específica do Panel. Guardar recompila a aplicação — o respetivo estado volta a **A compilar…** até a nova compilação estar pronta.

## Remover uma aplicação

Clique no ícone de **menos** na linha de uma aplicação Dash e confirme. A remoção desmantela a respetiva compilação e implementação, e o URL da aplicação deixa de funcionar imediatamente.
