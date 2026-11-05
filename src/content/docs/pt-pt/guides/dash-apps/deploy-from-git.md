---
title: Implementar uma aplicação Dash a partir do PlaidCloud Git
description: O percurso completo para disponibilizar uma aplicação Plotly Dash no PlaidCloud — colocar o código num repositório PlaidCloud Git, ligá-lo com uma ligação gerida sem credenciais e publicá-lo.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/deploy-from-git.md
---

Este é o percurso completo desde o código da aplicação Dash na sua máquina até um URL ativo, usando o **[PlaidCloud Git](/pt-pt/guides/git/)** — o serviço Git gerido, integrado na área de trabalho — como origem. Como o PlaidCloud Git é gerido, a ligação a partir da qual a aplicação é implementada **não precisa de URL do servidor, nome de utilizador nem token**: o PlaidCloud autentica em nome do utilizador.

Há cinco passos:

1. Escrever uma aplicação Dash mínima.
2. Colocá-la num repositório PlaidCloud Git.
3. Criar uma ligação PlaidCloud Git gerida.
4. Publicar uma aplicação Dash que aponte para o repositório.
5. Abrir a aplicação disponibilizada — e ler os registos de criação se não arrancar.

Este guia é quase idêntico a [Implementar uma aplicação Panel a partir do PlaidCloud Git](/pt-pt/guides/panel-apps/deploy-from-git/) — ambas são aplicações Python do lado do servidor, criadas a partir do Git e disponibilizadas da mesma forma. A diferença está no código da aplicação e num campo da caixa de diálogo de publicação.

## Antes de começar

- Abra **Git** na área de trabalho para confirmar que consegue aceder ao PlaidCloud Git. Por predefinição, a organização da área de trabalho inclui um repositório **`apps`** — a localização natural também para aplicações Dash.
- Tenha o `git` instalado localmente se pretender enviar código a partir da sua máquina (também pode adicionar ficheiros na interface web do Git).

## 1. Escrever uma aplicação Dash mínima

A aplicação precisa de um **ponto de entrada** — um ficheiro Python que cria uma aplicação Dash e expõe o respetivo servidor Flask — e, opcionalmente, de um **`requirements.txt`** para pacotes adicionais, na raiz do repositório ou junto ao ponto de entrada.

```
apps/
├── app.py            # entry point — exposes `server`
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Crie `app.py`:

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

Está completa. O `dash`, o `plotly`, o `dash-mantine-components`, o `dash-ag-grid` e as bibliotecas cliente do PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) já vêm pré-instalados, pelo que só tem de listar em `requirements.txt` os pacotes *adicionais*. Não passe `requests_pathname_prefix` nem `url_base_pathname` a `Dash(__name__)` — a plataforma define o prefixo do URL automaticamente através de `DASH_URL_BASE_PATHNAME`, e definir ambos provoca um erro de configuração no arranque. Para o contrato completo da aplicação e os auxiliares de acesso a dados, consulte [o contrato da aplicação](/pt-pt/guides/dash-apps/#contrato-da-aplicação) e [Ler dados e o utilizador com sessão iniciada numa aplicação Dash](/pt-pt/guides/dash-apps/accessing-data/).

## 2. Colocar a aplicação num repositório PlaidCloud Git

Use o repositório **`apps`** existente na área de trabalho ou [crie um novo](/pt-pt/guides/git/repositories/#criar-um-repositório). Depois, envie o código para lá.

Como a sessão é iniciada através do PlaidCloud, a conta Git não tem palavra-passe própria — [gere um token de acesso pessoal](/pt-pt/guides/git/repositories/#gerar-um-token-de-acesso-pessoal) (**o seu avatar → Definições → Aplicações**) com a permissão **write:repository** e use-o como palavra-passe quando o Git a pedir. Enviar para `apps` exige acesso de **Contributor**; peça a um administrador da área de trabalho que o adicione a **Git Contributors** se o separador **Git** indicar que tem acesso de Leitura. Selecione **Copy clone URL** no repositório, no separador **Git**, e depois execute:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello dash app"
git push
```

Tome nota do caminho do repositório — `<org>/apps` — em que `<org>` é o nome da organização da área de trabalho. Vai introduzi-lo no passo seguinte. Os detalhes completos de clonagem, commit e envio estão em [Repositórios](/pt-pt/guides/git/repositories/).

> **O token aqui serve apenas para *si* enviar código.** A ligação que vai criar a seguir é gerida e não precisa de token — não confunda os dois.

## 3. Criar uma ligação PlaidCloud Git gerida

Uma **ligação** indica a uma implementação Dash onde está o respetivo código. No PlaidCloud Git, a ligação é *gerida* — o PlaidCloud fornece o anfitrião e as credenciais, pelo que só indica o destino do repositório. É o mesmo tipo de ligação que uma aplicação Panel de servidor usa.

1. Abra **Ferramentas > Ligações**, clique em **Nova ligação** e escolha **PlaidCloud Git**.
2. Atribua à ligação um **Nome da conta** (por exemplo, `Apps Repo`).
3. Defina **Repository Path** como `<org>/apps` — o caminho que anotou no passo 2 — e **Ramo predefinido** como `main`. Deixe **Caminho inicial** em branco, a menos que as aplicações estejam num subdiretório.
4. Clique em **Criar**.

Não existe nenhum campo de URL do servidor, utilizador, palavra-passe ou SSL/SSH — o PlaidCloud Git é gerido, pelo que a plataforma trata do anfitrião e da autenticação. Para o formulário completo, incluindo a **Utilização** e o **Modelo de segurança** da ligação (quem na área de trabalho a pode usar), consulte [Ligação PlaidCloud Git](/pt-pt/guides/connections/plaidcloud-git/).

## 4. Publicar a aplicação Dash

Agora, aponte uma implementação Dash para essa ligação.

1. Abra **As minhas aplicações Panel** e clique em **Nova aplicação Dash**.
2. Em **Definições do diretório**, defina um **Nome da aplicação** e um **Slug de URL** — o slug é o URL e o nome interno da aplicação, pelo que deve usar letras minúsculas, dígitos e hífenes, começar por uma letra e ter 40 carateres ou menos (por exemplo, `hello-dash`). Um **Memorando** opcional descreve a aplicação.
3. Em **Ligação Git e monitor de publicação**:
   - **Ligação Git** — a ligação PlaidCloud Git que criou no passo 3.
   - **Ramo** — `main`. Os envios para este ramo recriam e reimplementam a aplicação automaticamente.
   - **Ponto de entrada** — `app.py`.
4. Em **Tempo de execução**, escolha a janela de **CPU**, **Memória** e **Inatividade (minutos)**. Assinale **Permitir acesso público** apenas se a aplicação deve estar acessível sem iniciar sessão. Não existe a definição **Design** — é uma opção específica do Panel.
5. Em **Avançado (disponibilização incorporada)** — opcional. Deixe vazio, a menos que esteja a incorporar a aplicação noutro site.
6. Clique em **Publicar**.

## 5. Abrir a aplicação — e ler os registos se não arrancar

Depois de publicar, a aplicação é **criada**: o PlaidCloud clona o ramo, instala o `requirements.txt` e cria uma imagem de contentor a partir da imagem `platform-dash-base`. O respetivo **Estado** aparece na lista **As minhas aplicações Panel** e é atualizado automaticamente.

- Quando o Estado for **Pronta**, abra a aplicação em `https://<your-tenant-host>/serve/<slug>/`. O primeiro pedido depois de um período de inatividade volta a iniciá-la, apresentando um breve ecrã de carregamento do PlaidCloud enquanto isso acontece.
- Se a criação falhar, abra a aplicação e consulte os registos de **Criar** — uma dependência em falta ou um erro de importação aparece aí. Consulte [Usar uma aplicação Dash](/pt-pt/guides/dash-apps/using/) para saber o que significa cada estado, como ler os registos e como acionar uma nova criação.

A partir daí, **cada envio para o ramo da ligação recria e reimplementa a aplicação automaticamente** — edite `app.py`, execute `git push` e a alteração entra em produção. (A menos que a aplicação esteja **bloqueada**; nesse caso, os envios são ignorados até a desbloquear — consulte [Usar uma aplicação Dash](/pt-pt/guides/dash-apps/using/#bloquear-uma-aplicação).)

## Passos seguintes

- [Ler dados e o utilizador com sessão iniciada numa aplicação Dash](/pt-pt/guides/dash-apps/accessing-data/) — consultar dados do PlaidCloud como a pessoa que está a ver a aplicação.
- [Usar uma aplicação Dash](/pt-pt/guides/dash-apps/using/) — estado da criação, registos, bloqueio e remoção da aplicação.
- [Ligação PlaidCloud Git](/pt-pt/guides/connections/plaidcloud-git/) — o formulário completo da ligação, a utilização e o modelo de segurança.
- [Repositórios](/pt-pt/guides/git/repositories/) — ramos, tokens e colaboração no PlaidCloud Git.
