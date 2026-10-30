---
title: Implementar uma aplicação Panel a partir do PlaidCloud Git
description: O percurso completo para disponibilizar uma aplicação HoloViz Panel no PlaidCloud — coloque o seu código num repositório PlaidCloud Git, ligue-o com uma ligação gerida sem credenciais e publique-o em direto.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/deploy-from-git.md
---

Este é o percurso completo desde o código da aplicação Panel na sua máquina até um URL em direto, usando como origem o **[PlaidCloud Git](/pt-pt/guides/git/)** — o serviço Git gerido integrado na sua área de trabalho. Como o PlaidCloud Git é gerido, a ligação a partir da qual a aplicação é implementada **não precisa de URL de servidor, nome de utilizador nem token**: o PlaidCloud autentica-se por si.

Há cinco passos:

1. Escreva uma aplicação Panel mínima.
2. Coloque-a num repositório PlaidCloud Git.
3. Crie uma ligação PlaidCloud Git gerida.
4. Publique uma aplicação de servidor que aponte para o repositório.
5. Abra a aplicação disponibilizada — e leia os registos de compilação se não arrancar.

Cada passo liga ao guia mais detalhado sobre essa parte; esta página junta-os num único percurso.

## Antes de começar

- Abra **Git** a partir da sua área de trabalho para confirmar que consegue aceder ao PlaidCloud Git. Por predefinição, a organização da sua área de trabalho inclui um repositório **`apps`** (e um **`udfs`**) — o local natural para aplicações Panel.
- Tenha o `git` instalado localmente se quiser enviar código a partir da sua máquina (também pode adicionar ficheiros na interface Web do Git).

## 1. Escrever uma aplicação Panel mínima

A sua aplicação precisa de um **ponto de entrada** — um ficheiro Python que cria uma aplicação Panel e a marca com `.servable()` — e, opcionalmente, de um **`requirements.txt`** para pacotes adicionais, na raiz do repositório ou junto ao ponto de entrada.

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

Esta é uma aplicação completa — a chamada `.servable()` é o que o PlaidCloud disponibiliza. O `panel`, o `bokeh` e as bibliotecas cliente do PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) estão pré-instalados, pelo que deve listar em `requirements.txt` apenas pacotes *adicionais*. Para exemplos mais completos, dependências e temas claro/escuro, consulte [Criar uma aplicação Panel](/pt-pt/guides/panel-apps/creating/).

## 2. Colocar a aplicação num repositório PlaidCloud Git

Use o repositório **`apps`** existente da sua área de trabalho, ou [crie um novo](/pt-pt/guides/git/repositories/#criar-um-repositório). Depois, coloque lá o seu código.

Como inicia sessão através do PlaidCloud, a sua conta Git não tem palavra-passe separada — [gere um token de acesso pessoal](/pt-pt/guides/git/repositories/#gerar-um-token-de-acesso-pessoal) (**o seu avatar → Settings → Applications**) com âmbitos de **leitura** e **escrita** do repositório, e use-o como palavra-passe quando o Git a pedir. Copie o URL de clonagem **HTTPS** do repositório a partir do botão **Código**, e depois:

```bash
git clone https://<your-git-host>/<org>/apps.git
cd apps
# add app.py (and requirements.txt), then:
git add app.py requirements.txt
git commit -m "Add hello panel app"
git push
```

Tome nota do caminho do repositório — `<org>/apps` — em que `<org>` é o nome da organização da sua área de trabalho. Vai introduzi-lo no passo seguinte. Os detalhes completos de clonagem, submissão e envio estão em [Repositórios](/pt-pt/guides/git/repositories/).

> **O token aqui serve apenas para *si* enviar código.** A ligação que cria a seguir é gerida e não precisa de token — não confunda os dois.

## 3. Criar uma ligação PlaidCloud Git gerida

Uma **ligação** indica a uma implementação do Panel onde reside o seu código. No PlaidCloud Git, a ligação é *gerida* — o PlaidCloud fornece o anfitrião e as credenciais, pelo que só introduz o destino do repositório.

1. Abra **Tools > Connections**, clique em **Nova ligação** e escolha **PlaidCloud Git**.
2. Atribua à ligação um **Nome da conta** (por exemplo, `Apps Repo`).
3. Defina **Repository Path** como `<org>/apps` — o caminho que anotou no passo 2 — e **Ramo predefinido** como `main`. Deixe **Caminho inicial** em branco, a menos que as suas aplicações estejam num subdiretório.
4. Clique em **Criar**.

Não existe nenhum campo de URL do servidor, utilizador, palavra-passe ou SSL/SSH — o PlaidCloud Git é gerido, pelo que a plataforma trata do anfitrião e da autenticação. Para o formulário completo, incluindo a **Utilização** e o **Modelo de segurança** da ligação (quem na área de trabalho a pode usar), consulte [Ligação PlaidCloud Git](/pt-pt/guides/connections/plaidcloud-git/).

> **Numa versão mais antiga da área de trabalho?** Se o formulário ainda mostrar um URL do servidor ou campos de credenciais, deixe-os em branco — a plataforma autentica-se por si em ambos os casos.

## 4. Publicar a aplicação de servidor

Agora aponte uma implementação de servidor para essa ligação.

1. Abra **As minhas aplicações Panel** e clique em **Nova aplicação de servidor**.
2. Em **Definições do diretório**, defina um **Nome da aplicação** e um **Slug de URL** — o slug é o URL e o nome interno da aplicação, pelo que deve usar letras minúsculas, dígitos e hífenes, começando por uma letra, com 40 carateres ou menos (por exemplo, `hello-panel`).
3. Em **Ligação Git e monitor de publicação**:
   - **Ligação Git** — a ligação PlaidCloud Git que criou no passo 3.
   - **Ramo** — `main`. As submissões para este ramo recompilam e voltam a implementar a aplicação automaticamente.
   - **Ponto de entrada** — `app.py`.
4. Em **Tempo de execução**, escolha a **CPU**, a **Memória**, o **Design** (**FAST** para o aspeto moderno do PlaidCloud) e a janela de **Inatividade**. Assinale **Permitir acesso público** apenas se a aplicação deve estar acessível sem iniciar sessão.
5. Clique em **Publicar**.

Todos os campos desta caixa de diálogo estão descritos em [Criar uma aplicação Panel](/pt-pt/guides/panel-apps/creating/#publicar-a-aplicação).

## 5. Abrir a aplicação — e ler os registos se não arrancar

Depois de publicar, a aplicação é **compilada**: o PlaidCloud clona o ramo, instala o seu `requirements.txt` (o da raiz do repositório e o da pasta da sua aplicação, se existirem) e compila uma imagem de contentor. O seu **Estado** é mostrado na lista **As minhas aplicações Panel** e atualiza-se automaticamente.

- Quando o Estado é **Pronta**, abra a aplicação em `https://<your-tenant-host>/serve/<slug>/`. O primeiro pedido depois de estar inativa reativa-a (cerca de 15 segundos).
- Se a compilação falhar, abra a aplicação e consulte os registos de **Criar** — uma dependência em falta ou um erro de importação aparece aí. Consulte [Utilizar uma aplicação Panel](/pt-pt/guides/panel-apps/using/) para saber o que significa cada estado, como ler os registos e como acionar uma recompilação.

A partir daqui, **cada envio para o ramo da ligação recompila e volta a implementar a aplicação automaticamente** — edite `app.py`, faça `git push` e a sua alteração entra em produção. (A menos que a aplicação esteja **bloqueada** — consulte [Bloquear uma aplicação](/pt-pt/guides/panel-apps/using/#bloquear-uma-aplicação) — caso em que os envios são ignorados até a desbloquear.)

## Passos seguintes

- [Criar uma aplicação Panel](/pt-pt/guides/panel-apps/creating/) — exemplos mais completos, dependências e temas claro/escuro
- [Ligação PlaidCloud Git](/pt-pt/guides/connections/plaidcloud-git/) — o formulário de ligação completo, a utilização e o modelo de segurança
- [Ler dados e o utilizador com sessão iniciada](/pt-pt/guides/panel-apps/accessing-data/) — consulte dados do PlaidCloud como a pessoa que está a ver a aplicação
- [Repositórios](/pt-pt/guides/git/repositories/) — ramos, tokens e colaboração no PlaidCloud Git
