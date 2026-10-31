---
title: Implante um aplicativo Panel a partir do PlaidCloud Git
description: O caminho completo para servir um aplicativo HoloViz Panel no PlaidCloud — coloque seu código em um repositório PlaidCloud Git, conecte-o com uma conexão gerenciada sem credenciais e publique-o ao vivo.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

Este é o caminho completo do código do aplicativo Panel na sua máquina até uma URL ativa, usando o **[PlaidCloud Git](/pt-br/guides/git/)** — o serviço Git gerenciado incorporado ao seu espaço de trabalho — como origem. Como o PlaidCloud Git é gerenciado, a conexão da qual seu aplicativo é implantado **não precisa de URL de servidor, nome de usuário nem token**: o PlaidCloud autentica em seu nome.

São cinco etapas:

1. Escrever um aplicativo Panel mínimo.
2. Colocá-lo em um repositório PlaidCloud Git.
3. Criar uma conexão gerenciada do PlaidCloud Git.
4. Publicar um aplicativo de servidor que aponte para o repositório.
5. Abrir o aplicativo servido — e ler os logs de compilação se ele não iniciar.

Cada etapa tem um link para o guia mais detalhado sobre aquele ponto; esta página as une em um único caminho.

## Antes de começar

- Abra **Git** no seu espaço de trabalho para confirmar que você consegue acessar o PlaidCloud Git. Por padrão, a organização do seu espaço de trabalho inclui um repositório **`apps`** (e um **`udfs`**) — o lugar natural para aplicativos Panel.
- Tenha o `git` instalado localmente se quiser enviar código da sua máquina (você também pode adicionar arquivos na interface web do Git).

## 1. Escreva um aplicativo Panel mínimo

Seu aplicativo precisa de um **ponto de entrada** — um arquivo Python que constrói um aplicativo Panel e o marca como `.servable()` — e, opcionalmente, um **`requirements.txt`** para pacotes extras, na raiz do repositório ou ao lado do ponto de entrada.

```
apps/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

Crie `app.py`:

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello from PlaidCloud Git 👋\n\nServed straight from your workspace repository.").servable()
```

Esse é um aplicativo completo — a chamada `.servable()` é o que o PlaidCloud serve. `panel`, `bokeh` e as bibliotecas cliente do PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) já vêm instalados, então liste no `requirements.txt` apenas pacotes *extras*. Para exemplos mais completos, dependências e temas claro/escuro, veja [Criando um aplicativo Panel](/pt-br/guides/panel-apps/creating/).

## 2. Coloque seu aplicativo em um repositório PlaidCloud Git

Use o repositório **`apps`** existente do seu espaço de trabalho ou [crie um novo](/pt-br/guides/git/repositories/#criar-um-repositório). Depois, coloque seu código nele.

Como você faz logon pelo PlaidCloud, sua conta Git não tem uma senha separada — [gere um token de acesso pessoal](/pt-br/guides/git/repositories/#gerar-um-token-de-acesso-pessoal) (**seu avatar → Settings → Applications**) com escopos de **leitura** e **gravação** do repositório e use-o como senha quando o Git pedir. Copie a URL de clonagem **HTTPS** do repositório no botão **Código** dele e depois:

```bash
git clone https://<your-git-host>/<org>/apps.git
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Anote o caminho do repositório — `<org>/apps` — em que `<org>` é o nome da organização do seu espaço de trabalho. Você vai informar esse caminho na próxima etapa. Os detalhes completos de clonar, fazer commit e enviar estão em [Repositórios](/pt-br/guides/git/repositories/).

> **O token aqui serve apenas para *você* enviar código.** A conexão que você cria a seguir é gerenciada e não precisa de token — não confunda os dois.

## 3. Crie uma conexão gerenciada do PlaidCloud Git

Uma **conexão** diz a uma implantação do Panel onde o código dela está. Para o PlaidCloud Git, a conexão é *gerenciada* — o PlaidCloud fornece o host e as credenciais, então você informa apenas o destino do repositório.

1. Abra **Tools > Connections**, clique em **Nova conexão** e escolha **PlaidCloud Git**.
2. Dê à conexão um **Nome da conta** (por exemplo, `Apps Repo`).
3. Defina **Repository Path** como `<org>/apps` — o caminho que você anotou na etapa 2 — e **Branch padrão** como `main`. Deixe **Caminho inicial** em branco, a menos que seus aplicativos fiquem em um subdiretório.
4. Clique em **Criar**.

Não há campo de URL do servidor, usuário, senha nem SSL/SSH — o PlaidCloud Git é gerenciado, então a plataforma cuida do host e da autenticação. Para o formulário completo, incluindo o **Uso** e o **Modelo de segurança** da conexão (quem no espaço de trabalho pode usá-la), veja [Conexão PlaidCloud Git](/pt-br/guides/connections/plaidcloud-git/).

> **Em uma compilação mais antiga do espaço de trabalho?** Se o formulário ainda mostrar uma URL de servidor ou campos de credencial, basta deixá-los em branco — a plataforma autentica em seu nome de qualquer forma.

## 4. Publique o aplicativo de servidor

Agora aponte uma implantação de servidor para essa conexão.

1. Abra **Meus aplicativos Panel** e clique em **Novo aplicativo de servidor**.
2. Em **Configurações do diretório**, defina um **Nome do aplicativo** e um **Slug de URL** — o slug é a URL e o nome interno do aplicativo, então use letras minúsculas, dígitos e hifens, começando com uma letra, com 40 caracteres ou menos (por exemplo, `hello-panel`).
3. Em **Conexão Git e monitor de publicação**:
   - **Conexão Git** — a conexão do PlaidCloud Git que você criou na etapa 3.
   - **Branch** — `main`. Envios para esse branch recompilam e reimplantam o aplicativo automaticamente.
   - **Ponto de entrada** — `app.py`.
4. Em **Tempo de execução**, escolha **CPU**, **Memória**, **Design** (**FAST** para o visual moderno do PlaidCloud) e a janela de **Idle**. Marque **Permitir acesso público** somente se o aplicativo deve ser acessível sem logon.
5. Clique em **Publicar**.

Cada campo desta caixa de diálogo é descrito em [Criando um aplicativo Panel](/pt-br/guides/panel-apps/creating/#publicar-o-aplicativo).

## 5. Abra o aplicativo — e leia os logs se ele não iniciar

Depois que você publica, o aplicativo é **compilado**: o PlaidCloud clona o branch, instala o seu `requirements.txt` (o da raiz do repositório e o da pasta do aplicativo, se existirem) e constrói uma imagem de contêiner. O **Status** dele aparece na lista **Meus aplicativos Panel** e é atualizado automaticamente.

- Quando o Status for **Pronto**, abra o aplicativo em `https://<your-tenant-host>/serve/<slug>/`. A primeira solicitação depois de um período ocioso o inicia (~15 segundos).
- Se a compilação falhar, abra o aplicativo e confira os logs de **Build** — uma dependência ausente ou um erro de importação aparece ali. Veja [Usando um aplicativo Panel](/pt-br/guides/panel-apps/using/) para saber o que cada status significa, como ler os logs e como disparar uma recompilação.

A partir daí, **cada envio para o branch da conexão recompila e reimplanta o aplicativo automaticamente** — edite `app.py`, execute `git push` e sua alteração entra no ar. (A menos que o aplicativo esteja **bloqueado** — veja [Bloqueando um aplicativo](/pt-br/guides/panel-apps/using/#bloquear-um-aplicativo) — caso em que os envios são ignorados até você desbloqueá-lo.)

## Próximas etapas

- [Criando um aplicativo Panel](/pt-br/guides/panel-apps/creating/) — exemplos mais completos, dependências e temas claro/escuro
- [Conexão PlaidCloud Git](/pt-br/guides/connections/plaidcloud-git/) — o formulário de conexão completo, o uso e o modelo de segurança
- [Lendo dados e o usuário conectado](/pt-br/guides/panel-apps/accessing-data/) — consulte dados do PlaidCloud como a pessoa que está visualizando o aplicativo
- [Repositórios](/pt-br/guides/git/repositories/) — branches, tokens e colaboração no PlaidCloud Git
