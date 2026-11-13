---
title: Implantar um aplicativo Panel a partir do PlaidCloud Git
description: "O caminho completo para servir um aplicativo HoloViz Panel no PlaidCloud: coloque seu código em um repositório do PlaidCloud Git, conecte-o com uma conexão gerenciada sem credenciais e publique-o ao vivo."
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

Este é o caminho completo do código do aplicativo Panel na sua máquina até uma URL ao vivo, usando o **[PlaidCloud Git](/pt-br/guides/git/)**, o serviço Git gerenciado integrado ao seu espaço de trabalho, como origem. Como o PlaidCloud Git é gerenciado, a conexão a partir da qual seu aplicativo é implantado **não precisa de URL de servidor, nome de usuário nem token**: o PlaidCloud faz a autenticação em seu nome.

São cinco etapas:

1. Escreva um aplicativo Panel mínimo.
2. Coloque-o em um repositório do PlaidCloud Git.
3. Crie uma conexão gerenciada do PlaidCloud Git.
4. Publique um aplicativo de servidor que aponte para o repositório.
5. Abra o aplicativo servido e leia os logs de compilação se ele não iniciar.

Cada etapa tem um link para o guia mais detalhado sobre aquela parte; esta página reúne todas elas em um único caminho.

## Antes de Começar

- Abra o **Git** no seu espaço de trabalho para confirmar que você consegue acessar o PlaidCloud Git. Por padrão, a organização do seu espaço de trabalho inclui um repositório **`apps`** (e um **`udfs`**), o lugar natural para aplicativos Panel.
- Tenha o `git` instalado localmente se quiser fazer push do código a partir da sua máquina (você também pode adicionar arquivos na interface web do Git).

## 1. Escrever um Aplicativo Panel Mínimo

Seu aplicativo precisa de um **ponto de entrada**, um arquivo Python que cria um aplicativo Panel e o marca como `.servable()`, e, opcionalmente, de um **`requirements.txt`** para pacotes adicionais, na raiz do repositório ou ao lado do ponto de entrada.

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

Esse é um aplicativo completo: a chamada `.servable()` é o que o PlaidCloud serve. `panel`, `bokeh` e as bibliotecas cliente do PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) já vêm pré-instalados, então liste no `requirements.txt` apenas os pacotes *adicionais*. Para exemplos mais completos, dependências e temas claro/escuro, consulte [Criar um aplicativo Panel](/pt-br/guides/panel-apps/creating/).

## 2. Colocar Seu Aplicativo em um Repositório do PlaidCloud Git

Use o repositório **`apps`** já existente no seu espaço de trabalho ou [crie um novo](/pt-br/guides/git/repositories/#criar-um-repositório). Depois, coloque seu código nele. Os aplicativos que você cria no [Panel Studio](/pt-br/guides/panel-apps/studio/#onde-seu-aplicativo-fica) já são pastas em `apps`, então você os encontrará lá, ao lado do seu.

Como você entra por meio do PlaidCloud, sua conta do Git não tem uma senha separada: [gere um token de acesso pessoal](/pt-br/guides/git/repositories/#gerar-um-token-de-acesso-pessoal) (**seu avatar → Settings → Applications**) com a permissão **write:repository** e use-o como senha quando o Git pedir. Fazer push em `apps` exige acesso de **Colaborador**; peça a um administrador do espaço de trabalho que adicione você a **Git Contributors** se a guia **Git** mostrar você como **Visualizador**. Use o botão de copiar ao lado do endereço de clone do repositório na guia **Git** e depois execute:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Anote o caminho do repositório, `<org>/apps`, em que `<org>` é o nome da organização do seu espaço de trabalho. Você vai informar esse caminho na próxima etapa. Os detalhes completos de clone, commit e push estão em [Repositories](/pt-br/guides/git/repositories/).

> **O token aqui serve apenas para *você* fazer push do código.** A conexão que você criará a seguir é gerenciada e não precisa de token; não confunda os dois.

## 3. Criar uma Conexão Gerenciada do PlaidCloud Git

Uma **conexão** informa a uma implantação do Panel onde está o código dela. No PlaidCloud Git, a conexão é *gerenciada*: o PlaidCloud fornece o host e as credenciais, então você informa apenas o destino do repositório.

1. Abra **Tools > Connections**, clique em **Nova conexão** e escolha **PlaidCloud Git**.
2. Dê à conexão um **Nome da conta** (por exemplo, `Apps Repo`).
3. Defina **Repository Path** como `<org>/apps`, o caminho que você anotou na etapa 2, e **Branch padrão** como `main`. Deixe **Caminho inicial** em branco, a menos que seus aplicativos fiquem em um subdiretório.
4. Clique em **Criar**.

Não há campo de URL do servidor, usuário, senha nem SSL/SSH: o PlaidCloud Git é gerenciado, então a plataforma cuida do host e da autenticação. Para ver o formulário completo, incluindo o **Uso** e o **Modelo de segurança** da conexão (quem no espaço de trabalho pode usá-la), consulte [Conexão do PlaidCloud Git](/pt-br/guides/connections/plaidcloud-git/).

> **Está em uma versão mais antiga do espaço de trabalho?** Se o formulário ainda mostrar uma URL do servidor ou campos de credenciais, basta deixá-los em branco: a plataforma faz a autenticação em seu nome de qualquer forma.

## 4. Publicar o Aplicativo de Servidor

Agora aponte uma implantação de servidor para essa conexão.

1. Abra **Meus aplicativos Panel** e clique em **Novo aplicativo de servidor**.
2. Em **Configurações do diretório**, defina um **Nome do aplicativo** e um **Slug de URL**; o slug é a URL e o nome interno do aplicativo, então use letras minúsculas, dígitos e hifens, começando com uma letra, com no máximo 40 caracteres (por exemplo, `hello-panel`).
3. Em **Conexão Git e monitor de publicação**:
   - **Conexão Git**: a conexão do PlaidCloud Git que você criou na etapa 3.
   - **Branch**: `main`. Os pushes para esse branch recompilam e reimplantam o aplicativo automaticamente.
   - **Ponto de entrada**: `app.py`.
4. Em **Tempo de execução**, escolha a **CPU**, a **Memória**, o **Design** (**FAST** para o visual moderno do PlaidCloud) e a janela de **Idle**. Marque **Permitir acesso público** somente se o aplicativo deve ser acessível sem fazer login.
5. Clique em **Publicar**.

Todos os campos desta caixa de diálogo são descritos em [Criar um aplicativo Panel](/pt-br/guides/panel-apps/creating/#publicar-o-aplicativo).

## 5. Abrir o Aplicativo e Ler os Logs se Ele Não Iniciar

Depois que você publica, o aplicativo é **compilado**: o PlaidCloud clona o branch, instala seu `requirements.txt` (o da raiz do repositório e o da pasta do seu aplicativo, se houver) e cria uma imagem de contêiner. O **Status** dele aparece na lista **Meus aplicativos Panel** e é atualizado automaticamente.

- Quando o Status for **Pronto**, abra o aplicativo em `https://<your-tenant-host>/serve/<slug>/`. A primeira solicitação depois de um período ocioso o reativa (cerca de 15 segundos).
- Se a compilação falhar, abra o aplicativo e confira os logs de **Compilação**: uma dependência ausente ou um erro de importação aparece ali. Consulte [Usar um aplicativo Panel](/pt-br/guides/panel-apps/using/) para saber o que significa cada status, como ler os logs e como acionar uma recompilação.

A partir daí, **cada push para o branch da conexão recompila e reimplanta o aplicativo automaticamente**: edite `app.py`, faça `git push` e sua alteração entra no ar. (A menos que o aplicativo esteja **bloqueado**, consulte [Bloquear um aplicativo](/pt-br/guides/panel-apps/using/#como-bloquear-um-aplicativo), caso em que os pushes são ignorados até você desbloqueá-lo.)

## Próximas Etapas

- [Criar um aplicativo Panel](/pt-br/guides/panel-apps/creating/): exemplos mais completos, dependências e temas claro/escuro
- [Conexão do PlaidCloud Git](/pt-br/guides/connections/plaidcloud-git/): o formulário completo da conexão, o uso e o modelo de segurança
- [Ler dados e o usuário conectado](/pt-br/guides/panel-apps/accessing-data/): consulte dados do PlaidCloud como a pessoa que está vendo o aplicativo
- [Repositories](/pt-br/guides/git/repositories/): branches, tokens e colaboração no PlaidCloud Git
