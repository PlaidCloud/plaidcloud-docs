---
title: Conector PlaidCloud Git
description: Ligue uma aplicação Panel, uma aplicação Dash ou um fluxo de trabalho a um repositório no PlaidCloud Git — o serviço Git gerido e integrado — sem URL de servidor nem credenciais para configurar.
sidebar:
  order: 0
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/git/plaidcloud-git.md
---

O **PlaidCloud Git** é o serviço Git gerido integrado na sua área de trabalho. Uma ligação PlaidCloud Git aponta uma implementação Panel ou Dash — ou um fluxo de trabalho — para um dos seus repositórios. Como o serviço é gerido, **não precisa de URL de servidor, nome de utilizador nem token**: o PlaidCloud fornece o anfitrião e autentica em seu nome.

Para o passo a passo completo de disponibilizar uma aplicação a partir de uma destas ligações, consulte [Implementar uma aplicação Panel a partir do PlaidCloud Git](/pt-pt/guides/panel-apps/deploy-from-git/) ou [Implementar uma aplicação Dash a partir do PlaidCloud Git](/pt-pt/guides/dash-apps/deploy-from-git/). Para criar repositórios e enviar código, consulte os [guias do PlaidCloud Git](/pt-pt/guides/git/).

## Configuração

Em **Tools > Connections**, clique em **Nova ligação** e escolha **PlaidCloud Git**. O formulário omite as secções de autenticação, SSL e SSH que os fornecedores Git externos apresentam — as credenciais são derivadas da plataforma — ficando apenas a identidade da ligação, a utilização e o repositório de destino.

### Identificação

| Campo | Tipo | Descrição |
|---|---|---|
| Nome da conta | Texto | Nome de apresentação desta ligação. |
| Memo | Texto | Nota opcional sobre a finalidade da ligação. |

### Repositório

| Campo | Tipo | Descrição |
|---|---|---|
| Repositório | Seletor | O repositório a utilizar. Clique em **Atualizar** para listar os repositórios da sua área de trabalho — por exemplo, `apps` ou `udfs` — e escolha um. |
| Ramo predefinido | Seletor | O ramo a partir do qual ler, escolhido entre os ramos do repositório selecionado. |
| Caminho inicial | Seletor | Opcional. Navegue pelo repositório selecionado e escolha uma pasta para limitar todas as pesquisas de ficheiros a um subdiretório. |

A **Utilização** (`Active` / `Read Only`) e o **Modelo de segurança** (quem na área de trabalho pode utilizar a ligação) são as definições de ligação padrão — consulte o [guia da ligação](/pt-pt/guides/connections/plaidcloud-git/) e [Criar e gerir uma ligação](/pt-pt/guides/connections/create-connection/).

## Utilizações comuns

- Disponibilizar uma [aplicação HoloViz Panel](/pt-pt/guides/panel-apps/deploy-from-git/) ou uma [aplicação Plotly Dash](/pt-pt/guides/dash-apps/deploy-from-git/) a partir do repositório `apps` da sua área de trabalho.
- Obter funções definidas pelo utilizador, configuração ou ficheiros baseados em modelos que residem no PlaidCloud Git.

## Relacionado

- [Ligação PlaidCloud Git](/pt-pt/guides/connections/plaidcloud-git/) — guia de tarefas para criar a ligação, com utilização e modelo de segurança
- [Implementar uma aplicação Panel a partir do PlaidCloud Git](/pt-pt/guides/panel-apps/deploy-from-git/) — o caminho completo do repositório à aplicação disponibilizada
- [Implementar uma aplicação Dash a partir do PlaidCloud Git](/pt-pt/guides/dash-apps/deploy-from-git/) — o mesmo caminho para uma aplicação Plotly Dash
- [Guias do PlaidCloud Git](/pt-pt/guides/git/) — repositórios, problemas, pedidos de integração e mais
- [Ligações a repositórios Git](/pt-pt/reference/connectors/git/) — fornecedores Git externos (GitHub, GitLab e outros)
