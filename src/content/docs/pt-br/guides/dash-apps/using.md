---
title: Usar um aplicativo Dash
description: Acompanhe o status da compilação, abra, recompile, bloqueie, veja logs, edite e remova aplicativos Plotly Dash publicados na tela Meus aplicativos Panel do PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/using.md
---

Os aplicativos Dash aparecem na mesma tela **Meus aplicativos Panel** que seus aplicativos Panel WASM e de servidor, com **Dash** exibido na coluna **Tempo de execução** e um ícone próprio para que sejam fáceis de distinguir. Tudo nesta página espelha [Usar um aplicativo Panel](/pt-br/guides/panel-apps/using/) para um aplicativo de servidor, com uma exceção indicada abaixo: os aplicativos Dash ainda não têm **Métricas de uso**.

## Status da compilação

A coluna **Status** de um aplicativo Dash acompanha a compilação, e a lista é atualizada sozinha enquanto uma compilação está em andamento:

- **Compilando…** — o PlaidCloud está compilando seu repositório em um contêiner. O aplicativo ainda não tem URL.
- **Pronto** — a compilação foi bem-sucedida. A URL do aplicativo está ativa e o ícone **Abrir** aparece na linha dele.
- **Falhou** — a compilação não foi concluída. Verifique o ponto de entrada e o branch e depois edite o aplicativo para publicá-lo novamente.

## Recompilar um aplicativo Dash

Clique no ícone **Recompilar** na linha de um aplicativo Dash para recompilá-lo e reimplantá-lo sem alterar suas configurações. O status do aplicativo volta a **Compilando…** enquanto o PlaidCloud compila novamente o mesmo branch e o mesmo ponto de entrada e, em seguida, volta a **Pronto** quando a nova compilação está no ar.

Use **Recompilar** após alterações de dependências, atualizações da imagem base ou uma compilação que falhou de forma transitória. Editar e salvar um aplicativo Dash também o recompila, mas a recompilação não exige abrir o formulário de edição.

## Bloquear um aplicativo

Clique no ícone de **cadeado** na linha de um aplicativo para protegê-lo contra alterações acidentais. Enquanto um aplicativo Dash está bloqueado:

- **Editar**, **Remover** e **Recompilar** se recusam a ser executados e informam que o aplicativo está bloqueado.
- **Um push para o branch do aplicativo não o recompila** — a recompilação automática é ignorada até você desbloquear o aplicativo. Faça o push novamente (ou use **Recompilar**) depois de desbloquear para aplicar a alteração.
- Abrir o aplicativo e ver seus logs continuam funcionando — o bloqueio impede apenas alterações, nunca visualizadores.

Clique no ícone novamente para desbloquear. O ícone mostra o estado atual do aplicativo: fechado quando bloqueado, aberto quando não. O bloqueio é uma proteção contra acidentes, não um controle de segurança — qualquer pessoa que possa editar aplicativos Dash também pode desbloqueá-los.

## Abrir um aplicativo Dash

Clique no ícone **Abrir** no início da linha de um aplicativo pronto para iniciá-lo em uma nova guia, em `https://<your-tenant-host>/serve/<slug>/`. O ícone aparece somente quando o aplicativo está **Pronto**.

Um aplicativo Dash escala a zero quando fica inativo para economizar recursos, portanto a primeira abertura após um período de inatividade precisa reativá-lo. Enquanto isso acontece, você vê uma **tela de carregamento do PlaidCloud** em vez de uma guia em branco, e o aplicativo aparece sozinho quando fica pronto. Se um aplicativo não consegue iniciar, a tela de carregamento se transforma em uma mensagem **"This app didn't start"** com um botão **Tentar novamente**; se isso continuar acontecendo, edite o aplicativo para verificar o ponto de entrada e o branch e publique-o novamente.

> **Um `dcc.Interval` (ou qualquer outro polling sempre ativo) anula o escalonamento a zero enquanto a guia permanece aberta.** O escalonamento a zero depende de o aplicativo ficar silencioso — sem solicitações em andamento — quando ninguém o está usando ativamente. Um componente que continua fazendo solicitações em um temporizador, como o `dcc.Interval`, mantém o aplicativo ativo enquanto aquela guia estiver aberta, mesmo que a pessoa que o está olhando tenha se afastado. Se você quer que um aplicativo escale para baixo entre as visitas, evite o polling sempre ativo ou interrompa o intervalo depois que a página ficar inativa por um tempo.

## Ver logs

Clique no ícone **Ver logs** na linha de um aplicativo Dash para abrir o visualizador de logs, com as mesmas guias **Tempo de execução** e **Compilação**, filtros, intervalo de tempo e painel de detalhes de um aplicativo Panel de servidor — consulte [Ver logs](/pt-br/guides/panel-apps/using/#ver-logs-aplicativos-de-servidor) para a mecânica completa. Cada linha de log de execução é marcada com o **usuário** cuja sessão a produziu, da mesma forma que as de um aplicativo Panel de servidor.

**As Métricas de uso não estão disponíveis para aplicativos Dash nesta versão** — o ícone **Métricas de uso** que aparece na linha de um aplicativo Panel de servidor não aparece para aplicativos Dash, portanto ainda não há um detalhamento de usuários exclusivos/sessões para consultar.

## Editar um aplicativo

Clique no ícone de **lápis** na linha de um aplicativo Dash para editá-lo. Você pode alterar o nome, o slug, o branch, o ponto de entrada, a CPU, a memória, a janela de inatividade, o indicador público, os domínios de exibição incorporada e o memorando. A **Conexão Git** é fixa depois que o aplicativo é criado e é mostrada somente para leitura. Não há campo **Design** para editar — essa configuração é específica do Panel. Salvar recompila o aplicativo — o status volta a **Compilando…** até que a nova compilação esteja pronta.

## Remover um aplicativo

Clique no ícone de **menos** na linha de um aplicativo Dash e confirme. Removê-lo desfaz sua compilação e sua implantação, e a URL do aplicativo deixa de funcionar imediatamente.
