---
title: Implementar uma aplicação Panel a partir do PlaidCloud Git
description: O percurso completo para disponibilizar uma aplicação HoloViz Panel no PlaidCloud — colocar o código num repositório PlaidCloud Git, ligá-lo com uma ligação gerida sem credenciais e publicá-lo em direto.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

Este é o percurso completo, desde o código da aplicação Panel no seu computador até um URL em direto, com o **[PlaidCloud Git](/pt-pt/guides/git/)** — o serviço Git gerido incorporado na sua área de trabalho — como origem. Como o PlaidCloud Git é gerido, a ligação a partir da qual a aplicação é implementada **não precisa de URL do servidor, nome de utilizador nem token**: o PlaidCloud autentica-se em seu nome.

Há cinco passos:

1. Escrever uma aplicação Panel mínima.
2. Colocá-la num repositório PlaidCloud Git.
3. Criar uma ligação PlaidCloud Git gerida.
4. Publicar uma aplicação de servidor que aponte para o repositório.
5. Abrir a aplicação disponibilizada — e ler os registos de compilação se esta não arrancar.

Cada passo remete para o guia mais detalhado dessa parte; esta página junta-os num único percurso.

## Antes de começar

- Abra **Git** a partir da sua área de trabalho para confirmar que consegue aceder ao PlaidCloud Git. Por predefinição, a organização da sua área de trabalho inclui um repositório **`apps`** (e um **`udfs`**) — o local natural para as aplicações Panel.
- Tenha o `git` instalado localmente se quiser enviar código a partir do seu computador (também pode adicionar ficheiros na interface web do Git).

## 1. Escrever uma aplicação Panel mínima

A aplicação precisa de um **ponto de entrada** — um ficheiro Python que cria uma aplicação Panel e a marca com `.servable()` — e, opcionalmente, de um ficheiro **`requirements.txt`** para pacotes adicionais, na raiz do repositório ou junto do ponto de entrada.

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

Esta é uma aplicação completa — a chamada a `.servable()` é o que o PlaidCloud disponibiliza. Os pacotes `panel`, `bokeh` e as bibliotecas cliente do PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) já vêm pré-instalados, pelo que deve listar em `requirements.txt` apenas os pacotes *adicionais*. Para exemplos mais completos, dependências e temas claro/escuro, consulte [Criar uma aplicação Panel](/pt-pt/guides/panel-apps/creating/).

## 2. Colocar a aplicação num repositório PlaidCloud Git

Utilize o repositório **`apps`** existente da sua área de trabalho ou [crie um novo](/pt-pt/guides/git/repositories/#criar-um-repositório). Depois, coloque lá o seu código.

Como inicia sessão através do PlaidCloud, a sua conta Git não tem uma palavra-passe própria — [gere um token de acesso pessoal](/pt-pt/guides/git/repositories/#gerar-um-token-de-acesso-pessoal) (**o seu avatar → Definições → Aplicações**) com a permissão **write:repository** e utilize-o como palavra-passe quando o Git a pedir. Para enviar para `apps` é necessário acesso de **Contributor**; peça a um administrador da área de trabalho que o adicione a **Git Contributors** se o separador **Git** o apresentar como **Leitor**. Utilize o botão de cópia junto do endereço de clonagem do repositório no separador **Git** e, em seguida:

```bash
git clone <clone URL>
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Anote o caminho do repositório — `<org>/apps` — em que `<org>` é o nome da organização da sua área de trabalho. Vai introduzir esse caminho no passo seguinte. Os detalhes completos de clonagem, commit e envio encontram-se em [Repositórios](/pt-pt/guides/git/repositories/).

> **O token aqui serve apenas para *si* enviar código.** A ligação que vai criar a seguir é gerida e não precisa de token — não confunda os dois.

## 3. Criar uma ligação PlaidCloud Git gerida

Uma **ligação** indica a uma implementação Panel onde está o seu código. No caso do PlaidCloud Git, a ligação é *gerida* — o PlaidCloud fornece o anfitrião e as credenciais, pelo que só indica o destino do repositório.

1. Abra **Tools > Connections**, clique em **Nova ligação** e escolha **PlaidCloud Git**.
2. Dê à ligação um **Nome da conta** (por exemplo, `Apps Repo`).
3. Defina **Repository Path** como `<org>/apps` — o caminho que anotou no passo 2 — e **Ramo predefinido** como `main`. Deixe **Caminho inicial** em branco, a menos que as suas aplicações estejam num subdiretório.
4. Clique em **Criar**.

Não existe nenhum campo de URL do servidor, utilizador, palavra-passe nem SSL/SSH — o PlaidCloud Git é gerido, pelo que a plataforma trata do anfitrião e da autenticação. Para o formulário completo, incluindo a **Utilização** e o **Modelo de segurança** da ligação (quem na área de trabalho a pode utilizar), consulte [Ligação PlaidCloud Git](/pt-pt/guides/connections/plaidcloud-git/).

> **Está numa versão mais antiga da área de trabalho?** Se o formulário ainda apresentar um URL do servidor ou campos de credenciais, deixe-os em branco — a plataforma autentica-se em seu nome em qualquer dos casos.

## 4. Publicar a aplicação de servidor

Agora, faça uma implementação de servidor apontar para essa ligação.

1. Abra **As minhas aplicações Panel** e clique em **Nova aplicação de servidor**.
2. Em **Definições do diretório**, defina um **Nome da aplicação** e um **Slug de URL** — o slug é o URL e o nome interno da aplicação, pelo que deve utilizar letras minúsculas, algarismos e hífenes, começar por uma letra e ter 40 carateres ou menos (por exemplo, `hello-panel`).
3. Em **Ligação Git e monitor de publicação**:
   - **Ligação Git** — a ligação PlaidCloud Git que criou no passo 3.
   - **Ramo** — `main`. Os envios para este ramo recompilam e voltam a implementar a aplicação automaticamente.
   - **Ponto de entrada** — `app.py`.
4. Em **Tempo de execução**, escolha a **CPU**, a **Memória**, o **Design** (**FAST** para o aspeto moderno do PlaidCloud) e a janela de **Inatividade**. Assinale **Permitir acesso público** apenas se a aplicação deva estar acessível sem iniciar sessão.
5. Clique em **Publicar**.

Todos os campos desta caixa de diálogo estão descritos em [Criar uma aplicação Panel](/pt-pt/guides/panel-apps/creating/#publicar-a-aplicação).

## 5. Abrir a aplicação — e ler os registos se não arrancar

Depois de publicar, a aplicação é **compilada**: o PlaidCloud clona o ramo, instala o seu `requirements.txt` (o da raiz do repositório e o da pasta da aplicação, se existirem) e cria uma imagem de contentor. O respetivo **Estado** é apresentado na lista **As minhas aplicações Panel** e é atualizado automaticamente.

- Quando o Estado for **Pronta**, abra a aplicação em `https://<your-tenant-host>/serve/<slug>/`. O primeiro pedido depois de um período de inatividade põe-na a funcionar (cerca de 15 segundos).
- Se a compilação falhar, abra a aplicação e consulte os registos de **Compilação** — uma dependência em falta ou um erro de importação aparecem aí. Consulte [Utilizar uma aplicação Panel](/pt-pt/guides/panel-apps/using/) para saber o que significa cada estado, como ler os registos e como desencadear uma nova compilação.

A partir daí, **cada envio para o ramo da ligação recompila e volta a implementar a aplicação automaticamente** — edite `app.py`, execute `git push` e a alteração entra em direto. (A menos que a aplicação esteja **bloqueada** — consulte [Bloquear uma aplicação](/pt-pt/guides/panel-apps/using/#bloquear-uma-aplicação) — caso em que os envios são ignorados até a desbloquear.)

## Passos seguintes

- [Criar uma aplicação Panel](/pt-pt/guides/panel-apps/creating/) — exemplos mais completos, dependências e temas claro/escuro
- [Ligação PlaidCloud Git](/pt-pt/guides/connections/plaidcloud-git/) — o formulário completo da ligação, a utilização e o modelo de segurança
- [Ler dados e o utilizador com sessão iniciada](/pt-pt/guides/panel-apps/accessing-data/) — consultar dados do PlaidCloud como a pessoa que está a ver a aplicação
- [Repositórios](/pt-pt/guides/git/repositories/) — ramos, tokens e colaboração no PlaidCloud Git
