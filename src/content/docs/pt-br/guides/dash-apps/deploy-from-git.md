---
title: Implantar um aplicativo Dash a partir do PlaidCloud Git
description: O caminho completo para servir um aplicativo Plotly Dash no PlaidCloud — coloque seu código em um repositório do PlaidCloud Git, conecte-o com uma conexão gerenciada sem credenciais e publique-o.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

Este é o caminho completo, do código do aplicativo Dash na sua máquina até uma URL ativa, usando o **[PlaidCloud Git](/pt-br/guides/git/)** — o serviço Git gerenciado incorporado ao seu espaço de trabalho — como origem. Como o PlaidCloud Git é gerenciado, a conexão a partir da qual seu aplicativo é implantado **não precisa de URL do servidor, nome de usuário nem token**: o PlaidCloud se autentica em seu nome.

São cinco etapas:

1. Escreva um aplicativo Dash mínimo.
2. Coloque-o em um repositório do PlaidCloud Git.
3. Crie uma conexão gerenciada do PlaidCloud Git.
4. Publique um aplicativo Dash que aponte para o repositório.
5. Abra o aplicativo em execução — e leia os logs de build se ele não iniciar.

Este passo a passo é quase idêntico a [Implantar um aplicativo Panel a partir do PlaidCloud Git](/pt-br/guides/panel-apps/deploy-from-git/) — ambos são aplicativos Python do lado do servidor criados a partir do Git e servidos da mesma forma. A diferença está no código do aplicativo e em um campo da caixa de diálogo de publicação.

## Antes de começar

- Abra **Git** no seu espaço de trabalho para confirmar que você consegue acessar o PlaidCloud Git. Por padrão, a organização do seu espaço de trabalho inclui um repositório **`apps`** — o lugar natural para aplicativos Dash também.
- Instale o `git` localmente se quiser enviar código a partir da sua máquina (você também pode adicionar arquivos na interface web do Git).

## 1. Escreva um aplicativo Dash mínimo

Seu aplicativo precisa de um **ponto de entrada** — um arquivo Python que cria um aplicativo Dash e expõe o servidor Flask dele — e, opcionalmente, de um **`requirements.txt`** para pacotes extras, na raiz do repositório ou ao lado do ponto de entrada.

```
apps/
├── app.py            # entry point — exposes `server`
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Crie o `app.py`:

```python
import plaidcloud_dash as pcd
from dash import Dash, Input, Output, html

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you

app.layout = html.Div(
    [
        html.H1("Hello from PlaidCloud Git"),
        html.P(id="whoami"),
        html.Button("Who am I?", id="whoami-btn", n_clicks=0),
    ]
)


@app.callback(Output("whoami", "children"), Input("whoami-btn", "n_clicks"))
def _whoami(n_clicks):
    if not n_clicks:
        return ""
    return f"Signed in as {pcd.current_user()!r}"


if __name__ == "__main__":
    app.run(debug=True)
```

Esse é um aplicativo completo. `dash`, `plotly`, `dash-mantine-components`, `dash-ag-grid` e as bibliotecas cliente do PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) já vêm instalados, então liste no `requirements.txt` apenas os pacotes *extras*. Não passe `requests_pathname_prefix` nem `url_base_pathname` para `Dash(__name__)` — a plataforma define o prefixo da URL por meio de `DASH_URL_BASE_PATHNAME` automaticamente, e definir os dois causa um erro de configuração na inicialização. Para o contrato completo do aplicativo e os auxiliares de acesso a dados, consulte [O contrato do aplicativo](/pt-br/guides/dash-apps/#contrato-do-aplicativo) e [Leitura de dados e do usuário conectado em um aplicativo Dash](/pt-br/guides/dash-apps/accessing-data/).

## 2. Coloque seu aplicativo em um repositório do PlaidCloud Git

Use o repositório **`apps`** existente do seu espaço de trabalho ou [crie um novo](/pt-br/guides/git/repositories/#criar-um-repositório). Depois, envie seu código para ele.

Como você entra pelo PlaidCloud, sua conta Git não tem uma senha separada — [gere um token de acesso pessoal](/pt-br/guides/git/repositories/#gerar-um-token-de-acesso-pessoal) (**seu avatar → Configurações → Applications**) com a permissão **write:repository** e use-o como senha quando o Git solicitar. Enviar para `apps` exige acesso de **Contributor**; peça a um administrador do espaço de trabalho que adicione você a **Git Contributors** se a guia **Git** mostrar você como **Visualizador**. Use o botão de cópia ao lado do endereço de clonagem do repositório na guia **Git** e, em seguida:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

Anote o caminho do repositório — `<org>/apps` — em que `<org>` é o nome da organização do seu espaço de trabalho. Você vai informar esse caminho na próxima etapa. Os detalhes completos de clonagem, commit e envio estão em [Repositórios](/pt-br/guides/git/repositories/).

> **O token aqui serve apenas para *você* enviar código.** A conexão que você vai criar a seguir é gerenciada e não precisa de token — não confunda os dois.

## 3. Crie uma conexão gerenciada do PlaidCloud Git

Uma **conexão** informa a uma implantação do Dash onde está o código dela. No PlaidCloud Git, a conexão é *gerenciada* — o PlaidCloud fornece o host e as credenciais, então você informa apenas o destino do repositório. É o mesmo tipo de conexão usado por um aplicativo Panel de servidor.

1. Abra **Tools > Connections**, clique em **Nova conexão** e escolha **PlaidCloud Git**.
2. Dê à conexão um **Nome da conta** (por exemplo, `Apps Repo`).
3. Defina **Repository Path** como `<org>/apps` — o caminho que você anotou na etapa 2 — e **Branch padrão** como `main`. Deixe **Caminho inicial** em branco, a menos que seus aplicativos estejam em um subdiretório.
4. Clique em **Criar**.

Não há campo de URL do servidor, usuário, senha nem SSL/SSH — o PlaidCloud Git é gerenciado, então a plataforma cuida do host e da autenticação. Para o formulário completo, incluindo o **Uso** e o **Modelo de segurança** da conexão (quem no espaço de trabalho pode usá-la), consulte [Conexão do PlaidCloud Git](/pt-br/guides/connections/plaidcloud-git/).

## 4. Publique o aplicativo Dash

Agora aponte uma implantação do Dash para essa conexão.

1. Abra **Aplicativos** e escolha **Novo app** > **App Dash**.
2. Em **Configurações do diretório**, defina um **Nome do aplicativo** e um **Slug de URL** — o slug é a URL e o nome interno do aplicativo, então use letras minúsculas, dígitos e hifens, começando com uma letra, com no máximo 40 caracteres (por exemplo, `hello-dash`). Um **Memorando** opcional descreve o aplicativo.
3. Em **Conexão Git e monitor de publicação**:
   - **Conexão Git** — a conexão do PlaidCloud Git que você criou na etapa 3.
   - **Branch** — `main`. Os envios para essa branch recriam e reimplantam o aplicativo automaticamente.
   - **Ponto de entrada** — `app.py`.
4. Em **Tempo de execução**, escolha **CPU**, **Memória** e a janela de **Inatividade (minutos)**. Marque **Permitir acesso público** somente se o aplicativo deve ficar acessível sem login. Não há configuração de **Design** — essa é uma opção específica do Panel.
5. Em **Avançado (exibição incorporada)** — opcional. Deixe vazio, a menos que você esteja incorporando o aplicativo em outro site.
6. Clique em **Publicar**.

## 5. Abra o aplicativo — e leia os logs se ele não iniciar

Depois de publicar, o aplicativo é **criado**: o PlaidCloud clona a branch, instala o seu `requirements.txt` e cria uma imagem de contêiner a partir da imagem `platform-dash-base`. O **Status** dele aparece na lista **Aplicativos** e é atualizado automaticamente.

- Quando o Status for **Pronto**, abra o aplicativo em `https://<your-tenant-host>/serve/<slug>/`. A primeira solicitação depois de um período de inatividade inicia o aplicativo, exibindo brevemente uma tela de carregamento do PlaidCloud.
- Se a criação falhar, abra o aplicativo e confira os logs de build — uma dependência ausente ou um erro de importação aparece ali. Consulte [Usar um aplicativo Dash](/pt-br/guides/dash-apps/using/) para saber o que cada status significa, como ler os logs e como iniciar uma nova criação.

A partir daí, **cada envio para a branch da conexão recria e reimplanta o aplicativo automaticamente** — edite o `app.py`, execute `git push` e sua alteração entra em operação. (A menos que o aplicativo esteja **bloqueado**; nesse caso, os envios são ignorados até você desbloqueá-lo — consulte [Usar um aplicativo Dash](/pt-br/guides/dash-apps/using/#como-bloquear-um-aplicativo).)

## Próximas etapas

- [Leitura de dados e do usuário conectado em um aplicativo Dash](/pt-br/guides/dash-apps/accessing-data/) — consulte dados do PlaidCloud como a pessoa que está vendo o aplicativo.
- [Usar um aplicativo Dash](/pt-br/guides/dash-apps/using/) — status da criação, logs, bloqueio e remoção do aplicativo.
- [Conexão do PlaidCloud Git](/pt-br/guides/connections/plaidcloud-git/) — o formulário completo da conexão, uso e modelo de segurança.
- [Repositórios](/pt-br/guides/git/repositories/) — branches, tokens e colaboração no PlaidCloud Git.
