---
title: Conector PlaidCloud Git
description: Conecte um aplicativo Panel, um aplicativo Dash ou um fluxo de trabalho a um repositório no PlaidCloud Git, o serviço Git gerenciado e integrado, sem URL de servidor nem credenciais para configurar.
sidebar:
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/plaidcloud-git.md
---

O **PlaidCloud Git** é o serviço Git gerenciado integrado ao seu espaço de trabalho. Uma conexão PlaidCloud Git aponta uma implantação Panel ou Dash, ou um fluxo de trabalho, para um dos seus repositórios. Como o serviço é gerenciado, ele **não exige URL de servidor, nome de usuário nem token**: o PlaidCloud fornece o host e autentica em seu nome.

Para o passo a passo completo de como servir um aplicativo a partir de uma dessas conexões, consulte [Implantar um aplicativo Panel a partir do PlaidCloud Git](/pt-br/guides/panel-apps/deploy-from-git/) ou [Implantar um aplicativo Dash a partir do PlaidCloud Git](/pt-br/guides/dash-apps/deploy-from-git/). Para criar repositórios e enviar código, consulte os [guias do PlaidCloud Git](/pt-br/guides/git/).

## Configuração

Em **Tools > Connections**, clique em **Nova conexão** e escolha **PlaidCloud Git**. O formulário omite as seções de autenticação, SSL e SSH que os provedores Git externos exibem, pois as credenciais são derivadas da plataforma, e mantém a identidade da conexão, o uso e o repositório de destino.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome da conta | Texto | Nome de exibição desta conexão. |
| Memo | Texto | Observação opcional sobre a finalidade da conexão. |

### Repositório

| Campo | Tipo | Descrição |
|---|---|---|
| Repositório | Seletor | O repositório a ser usado. Clique em **Atualizar** para listar os repositórios do seu espaço de trabalho, por exemplo `apps` ou `udfs`, e escolha um. |
| Branch padrão | Seletor | O branch de onde ler, escolhido entre os branches do repositório selecionado. |
| Caminho inicial | Seletor | Opcional. Navegue pelo repositório selecionado e escolha uma pasta para restringir toda busca de arquivos a um subdiretório. |

O **Uso** (`Active` / `Read Only`) e o **Modelo de segurança** (quem no espaço de trabalho pode usar a conexão) são as configurações padrão de conexão. Consulte o [guia da conexão](/pt-br/guides/connections/plaidcloud-git/) e [Criar e gerenciar uma conexão](/pt-br/guides/connections/create-connection/).

## Usos comuns

- Servir um [aplicativo HoloViz Panel](/pt-br/guides/panel-apps/deploy-from-git/) ou um [aplicativo Plotly Dash](/pt-br/guides/dash-apps/deploy-from-git/) a partir do repositório `apps` do seu espaço de trabalho.
- Obter funções definidas pelo usuário, configurações ou arquivos de modelo que ficam no PlaidCloud Git.

## Relacionados

- [Conexão PlaidCloud Git](/pt-br/guides/connections/plaidcloud-git/) — guia de tarefas para criar a conexão, com uso e modelo de segurança
- [Implantar um aplicativo Panel a partir do PlaidCloud Git](/pt-br/guides/panel-apps/deploy-from-git/) — o caminho completo, do repositório ao aplicativo servido
- [Implantar um aplicativo Dash a partir do PlaidCloud Git](/pt-br/guides/dash-apps/deploy-from-git/) — o mesmo caminho para um aplicativo Plotly Dash
- [Guias do PlaidCloud Git](/pt-br/guides/git/) — repositórios, issues, pull requests e mais
- [Conexões com repositórios Git](/pt-br/reference/connectors/git/) — provedores Git externos (GitHub, GitLab e outros)
