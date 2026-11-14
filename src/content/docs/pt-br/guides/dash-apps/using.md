---
title: Como usar um aplicativo Dash
description: Acompanhe o status da compilação, abra, recompile, bloqueie, veja os logs, edite e remova aplicativos Plotly Dash publicados na tela Aplicativos do PlaidCloud.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/using.md
---

Os aplicativos Dash aparecem na mesma tela **Aplicativos** que seus aplicativos Panel WASM e de servidor, com **Dash** exibido na coluna **Tempo de execução** e um ícone próprio, para que seja fácil distingui-los. Tudo nesta página espelha [Como usar um aplicativo Panel](/pt-br/guides/panel-apps/using/) para um aplicativo de servidor, com uma exceção destacada abaixo: os aplicativos Dash ainda não têm **Usage Metrics**.

## Status da compilação

A coluna **Status** de um aplicativo Dash acompanha sua compilação, e a lista é atualizada sozinha enquanto uma compilação está em andamento:

- **Compilando…** — o PlaidCloud está compilando seu repositório em um contêiner. O aplicativo ainda não tem URL.
- **Pronto** — a compilação foi concluída com sucesso. A URL do aplicativo está ativa e o ícone **Abrir** aparece na linha dele.
- **Falhou** — a compilação não foi concluída. Verifique o ponto de entrada e o branch e, em seguida, edite o aplicativo para publicá-lo novamente.

## Como recompilar um aplicativo Dash

Clique no ícone **Recompilar** na linha de um aplicativo Dash para recompilá-lo e reimplantá-lo sem alterar suas configurações. O status do aplicativo volta para **Compilando…** enquanto o PlaidCloud compila novamente o mesmo branch e ponto de entrada e, depois, muda de volta para **Pronto** quando a nova compilação estiver ativa.

Use **Recompilar** após alterações de dependências, atualizações da imagem base ou uma falha transitória de compilação. Editar e salvar um aplicativo Dash também o recompila, mas a recompilação não exige abrir o formulário de edição.

## Como bloquear um aplicativo

Clique no ícone de **cadeado** na linha de um aplicativo para protegê-lo contra alterações acidentais. Enquanto um aplicativo Dash está bloqueado:

- **Editar**, **Remover** e **Recompilar** não são executados e informam que o aplicativo está bloqueado.
- **Um push no branch do aplicativo não o recompila** — a recompilação automática é ignorada até você desbloquear o aplicativo. Faça um novo push (ou use **Recompilar**) após o desbloqueio para incorporar a alteração.
- Abrir o aplicativo e ver seus logs continuam funcionando — o bloqueio impede apenas alterações, nunca quem o visualiza.

Clique no ícone novamente para desbloquear. O ícone mostra o estado atual do aplicativo: fechado quando bloqueado, aberto quando não. O bloqueio é uma proteção contra acidentes, não um controle de segurança — qualquer pessoa que pode editar aplicativos Dash também pode desbloqueá-los.

## Como abrir um aplicativo Dash

Clique no ícone **Abrir** no início da linha de um aplicativo pronto para iniciá-lo em uma nova guia, em `https://<your-tenant-host>/serve/<slug>/`. O ícone só aparece quando o aplicativo está **Pronto**.

Um aplicativo Dash é reduzido a zero quando ocioso para economizar recursos, então a primeira abertura após um período de inatividade precisa iniciá-lo. Enquanto isso acontece, você vê uma **tela de carregamento do PlaidCloud** em vez de uma guia em branco, mostrando o progresso do aplicativo pelas etapas **Iniciando**, **Preparando** e **Carregando aplicativo**, e o aplicativo aparece sozinho assim que estiver pronto. Se um aplicativo não conseguir iniciar, a tela de carregamento passa a exibir uma mensagem informando que o aplicativo não foi iniciado e em qual etapa ele parou, com um botão **Tentar novamente**; se isso continuar acontecendo, edite o aplicativo para verificar o ponto de entrada e o branch e publique-o novamente.

> **Um `dcc.Interval` (ou qualquer outra consulta periódica sempre ativa) impede a redução a zero enquanto a guia dele permanece aberta.** A redução a zero depende de o aplicativo ficar inativo — sem solicitações em andamento — quando ninguém o está usando ativamente. Um componente que continua fazendo solicitações em intervalos regulares, como `dcc.Interval`, mantém o aplicativo ativo enquanto essa guia estiver aberta, mesmo que a pessoa que o está vendo tenha se afastado. Se você quiser que um aplicativo seja reduzido entre as visitas, evite consultas periódicas sempre ativas ou interrompa o intervalo quando a página estiver ociosa por algum tempo.

## Como ver os logs

Clique no ícone **Ver logs** na linha de um aplicativo Dash para abrir o visualizador de logs dele, com as mesmas guias **Tempo de execução** e **Compilação**, filtros, intervalo de tempo e painel de detalhes de um aplicativo Panel de servidor — consulte [Como ver os logs](/pt-br/guides/panel-apps/using/#como-ver-os-logs-aplicativos-de-servidor) para conhecer o funcionamento completo. Cada linha de log de tempo de execução é marcada com o **usuário** cuja sessão a gerou, da mesma forma que as de um aplicativo Panel de servidor.

**Usage Metrics não está disponível para aplicativos Dash nesta versão** — o ícone **Usage Metrics** que aparece na linha de um aplicativo Panel de servidor não aparece para aplicativos Dash, portanto ainda não há um detalhamento de usuários exclusivos e sessões para consultar.

## Como editar um aplicativo

Clique no ícone de **lápis** na linha de um aplicativo Dash para editá-lo. Você pode alterar o nome, o slug, o branch, o ponto de entrada, a CPU, a memória, o período de inatividade, a opção pública, os domínios de exibição incorporada e o memorando. A **Conexão Git** é fixada quando o aplicativo é criado e é exibida como somente leitura. Não há um campo **Design** para editar — essa configuração é específica do Panel. Salvar recompila o aplicativo — o status dele volta para **Compilando…** até que a nova compilação esteja pronta.

## Como remover um aplicativo

Clique no ícone de **menos** na linha de um aplicativo Dash e confirme. A remoção desfaz a compilação e a implantação dele, e a URL do aplicativo para de funcionar imediatamente.
