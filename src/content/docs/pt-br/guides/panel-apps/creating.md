---
title: Criar um aplicativo Panel
description: Crie um aplicativo Panel no Panel Studio, a partir de um aplicativo em branco, de uma tabela, de uma visão ou da galeria, ou publique um aplicativo de servidor a partir do git ou um aplicativo WASM estático para necessidades específicas.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Comece pelo Panel Studio. Ele não exige repositório nem configuração: você cria o aplicativo no PlaidCloud, visualiza-o e o publica quando estiver pronto. Escolha um tempo de execução personalizado somente quando o Studio não atender.

## Criar um aplicativo Studio

Abra **Aplicativos** e abra o menu **Novo app**. Sob o título **App Panel**, **Studio** escreve e publica o aplicativo no editor do PlaidCloud com o layout padrão e guarda o código para você. Você também pode escolher **Novo aplicativo Studio** na linha **Aplicativos Studio** do cartão **Aplicativos e identidade visual** na guia **Início** de um projeto ou [começar a partir de uma tabela](#começar-a-partir-de-uma-tabela).

1. Escolha **Novo app** > **Studio**.
2. Informe um **Nome**. O **Slug da URL** é preenchido a partir dele.
3. Escolha o **Projeto** proprietário do aplicativo. Você precisa de acesso de edição ao projeto.
4. Em **Começar de**, escolha o ponto de partida do aplicativo:

   | Começar de | O que você recebe |
   |---|---|
   | **Aplicativo em branco** | Um aplicativo mínimo com um `app.py` e um `requirements.txt`. |
   | **A partir de uma tabela** | Um aplicativo criado a partir da tabela que você escolher. |
   | **A partir de uma visualização** | O mesmo, criado a partir de uma visão do projeto. |
   | **A partir de outro aplicativo Studio** | Uma cópia de um de seus aplicativos Studio. |
   | **A partir da galeria** | Uma cópia de um aplicativo que seu espaço de trabalho [listou na galeria](#começar-a-partir-da-galeria). |

5. Escolha **Criar**. O Studio abre o novo aplicativo. No caso de uma tabela ou de uma visão, o prompt do Weave para criar a primeira página já está pronto para ser enviado.

Consulte o [Panel Studio](/pt-br/guides/panel-apps/studio/) para editar, visualizar e publicar o aplicativo.

### Começar a partir de uma tabela

Você também pode começar na guia **Tabelas** de um projeto. Selecione uma tabela ou uma visão e escolha **Criar aplicativo Panel** no menu **Novo** ou no menu de contexto (clique com o botão direito). A caixa de diálogo **Novo aplicativo Studio** é aberta com o projeto e a tabela já escolhidos. O comando fica disponível quando você tem acesso de edição ao projeto e o projeto não é somente leitura.

### Começar a partir da galeria

Escolha **Novo app** > **Da galeria…** para navegar pelos aplicativos que seu espaço de trabalho listou e, em seguida, **Criar aplicativo a partir disto…** para criar sua própria cópia. Ou escolha **Da galeria** na caixa de diálogo **Novo aplicativo Studio**. Consulte [A galeria de aplicativos](/pt-br/guides/panel-apps/gallery/), inclusive como listar seu próprio aplicativo.

## Outros tempos de execução

Os aplicativos Studio cobrem a maioria dos painéis e ferramentas. Para uma necessidade específica, publique com um dos outros [tempos de execução](/pt-br/guides/panel-apps/) no menu **Novo app**:

- **Somente navegador** — seu próprio repositório; o aplicativo é executado no navegador de quem o visualiza.
- **Baseado em servidor** — seu próprio repositório; o aplicativo é executado em um servidor do PlaidCloud, por exemplo, para reutilizar código existente ou seu próprio processo de compilação.
- **App Dash** — publique um aplicativo Plotly Dash. Consulte [Aplicativos Dash](/pt-br/guides/dash-apps/).

## Criar um aplicativo de servidor

Um aplicativo de servidor é criado a partir de um repositório git e servido em `https://<your-tenant-host>/serve/<slug>/`. Você aponta o PlaidCloud para um branch de um repositório; ele compila o código em um contêiner, executa `panel serve` nele e o recompila automaticamente sempre que você faz push nesse branch.

### Prepare o repositório do aplicativo

Seu repositório precisa de duas coisas: um **ponto de entrada** — um arquivo Python que cria um aplicativo Panel e o marca como `.servable()` — e, opcionalmente, um **`requirements.txt`** listando os pacotes extras, na raiz do repositório ou ao lado do ponto de entrada.

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

#### Olá, mundo

Crie o `app.py`:

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

Esse é um aplicativo completo. A chamada `.servable()` é o que o PlaidCloud serve — tudo o que você quiser exibir precisa estar marcado como servable (diretamente ou por estar dentro de um layout servable).

#### Um exemplo um pouco mais completo

Os aplicativos Panel são interativos. Este adiciona um controle deslizante que atualiza uma tabela ao vivo:

```python
import pandas as pd
import panel as pn

pn.extension()

multiplier = pn.widgets.IntSlider(name="Multiplier", start=1, end=10, value=3)

@pn.depends(multiplier)
def times_table(m):
    df = pd.DataFrame({"n": range(1, 6)})
    df["result"] = df["n"] * m
    return pn.pane.DataFrame(df, index=False)

pn.Column(
    "# Times Table",
    multiplier,
    times_table,
).servable()
```

#### Adicione dependências

Este segundo exemplo importa o `pandas`, que não faz parte da imagem base; portanto, adicione um `requirements.txt` (na raiz do repositório ou ao lado do ponto de entrada):

```text
pandas
```

O PlaidCloud instala esses pacotes com o `pip` ao compilar a imagem. Bibliotecas de visualização comuns — `plotly`, `holoviews`, `hvplot` — também não estão na imagem base; portanto, liste aqui as que seu aplicativo importa.

> **O que a plataforma fornece — e espera.** Tenha estas premissas em mente ao escrever seu aplicativo:
>
> - **`panel` e `bokeh` vêm pré-instalados** na imagem base da plataforma. Não os liste no `requirements.txt` e evite fixar uma versão mais antiga do Panel — a reconexão das atualizações ao vivo depende de uma versão recente.
> - **As bibliotecas cliente do PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) vêm pré-instaladas.** Importe `plaidcloud.rpc` ou `plaidcloud.utilities` diretamente — não as liste no `requirements.txt`.
> - **O `requirements.txt` pode ficar na raiz do repositório ou ao lado do ponto de entrada.** Em um repositório compartilhado (monorepo), mantenha as dependências de cada aplicativo na própria pasta. Um arquivo na raiz, se existir, também é instalado — coloque ali as dependências compartilhadas e, ao lado do aplicativo, as específicas dele.
> - **O aplicativo é executado como usuário não root em um sistema de arquivos somente leitura.** Apenas `/tmp` é gravável; portanto, grave ali quaisquer arquivos temporários (a maioria das bibliotecas já respeita `$TMPDIR`).
> - **Não fixe a porta, o prefixo de URL nem o host no código.** O PlaidCloud os atribui e os injeta no momento da implantação — basta chamar `.servable()`.

Para ter a aparência do PlaidCloud e filtros, grades e gráficos prontos, crie seu aplicativo com o [Panel App Kit](/pt-br/guides/panel-apps/app-kit/).

### Defina o tema: claro, escuro ou alternável

Por padrão, os aplicativos de servidor são exibidos no design moderno **Fast** do PlaidCloud — uma aparência limpa, no estilo Fluent, aplicada em toda a plataforma. Na caixa de diálogo de publicação, **Design** controla essa camada da plataforma:

- **FAST** — o padrão do PlaidCloud. Use-o em aplicativos novos e em aplicativos criados com modelos Fast.
- **Padrão** — o estilo padrão do Panel. Use-o quando o CSS ou os elementos visuais de um aplicativo existente deixarem de funcionar com FAST.

O que você controla no código do aplicativo é o **tema**: claro, escuro ou uma chave que quem visualiza pode alternar.

O tema é uma propriedade do **modelo** que você serve. Os modelos Fast — `FastListTemplate` (uma única coluna) e `FastGridTemplate` (uma grade responsiva) — aceitam duas configurações para isso:

- **`theme`** — `"default"` para claro ou `"dark"`. Defini-lo fixa o aplicativo nesse tema, mesmo que quem visualiza adicione `?theme=dark` à URL.
- **`theme_toggle`** — `True` exibe uma chave claro/escuro no cabeçalho; `False` a oculta. O padrão é `True`. Ocultar a chave não fixa o tema por si só — fixe-o com `theme` (acima); defina `theme_toggle=False` depois de fazer isso, para que as pessoas não vejam uma chave que não altera nada.

Escolha o padrão que melhor se adapta ao seu aplicativo.

**Somente claro** — o melhor para relatórios densos e tabelas financeiras, que geralmente são estilizados manualmente para um fundo claro:

```python
import panel as pn

pn.extension("tabulator")

pn.template.FastListTemplate(
    title="Sales Dashboard",
    theme="default",      # light
    theme_toggle=False,   # hide the switch
    main=[...],
).servable()
```

**Somente escuro:**

```python
pn.template.FastListTemplate(
    title="Ops Monitor",
    theme="dark",
    theme_toggle=False,
    main=[...],
).servable()
```

**Deixe quem visualiza escolher** — o padrão é claro, com uma chave no cabeçalho. Omita `theme` para que ele acompanhe a chave:

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **Se você permitir o tema escuro, deixe suas tabelas preparadas para ele.** Um `Tabulator` fixado em um tema de tabela claro (`theme="bootstrap"`), ou um CSS personalizado com cores claras fixas, como `background: #fff`, aparece como um bloco branco ilegível em uma página escura. Use um tema de tabela que acompanhe o aplicativo — `pn.widgets.Tabulator(..., theme="fast")` — e evite cores claras fixas. Se um relatório é muito estilizado manualmente para o tema claro, fixe-o no claro (o primeiro padrão acima).

Um aplicativo simples sem modelo — `pn.Column(...).servable()` — segue o padrão do Panel e não é afetado por essas configurações; use um modelo quando quiser controle explícito.

Seu repositório precisa estar acessível por meio de uma **conexão git** no PlaidCloud. Se seu código está no [PlaidCloud Git](/pt-br/guides/git/), crie uma conexão gerenciada **PlaidCloud Git** em **Tools > Connections** — ela não precisa de URL de servidor nem de credenciais. Para todo o caminho de um repositório vazio até um aplicativo servido, consulte [Implantar um aplicativo Panel a partir do PlaidCloud Git](/pt-br/guides/panel-apps/deploy-from-git/).

### Publique o aplicativo

1. Escolha **Novo app** > **Baseado em servidor** para abrir a caixa de diálogo **Publicar aplicativo Panel de servidor**. As configurações dela são agrupadas em seções.
2. Em **Configurações do diretório**:
   - **Nome do aplicativo** — o nome de exibição mostrado na lista.
   - **Slug de URL** — é a URL do aplicativo e também o nome interno dele; portanto, deve ser um rótulo DNS válido: letras minúsculas, dígitos e hifens, começando com uma letra, com no máximo 40 caracteres (por exemplo, `sales-dashboard`). A caixa de diálogo verifica isso antes de você publicar.
   - **Memorando** — uma descrição opcional.
   - **Projeto** — o projeto proprietário do aplicativo. Ele fornece a [identidade visual](/pt-br/guides/panel-apps/branding/) do aplicativo e é o projeto padrão das tabelas dele. Não é possível alterá-lo aqui após a publicação; use [Atribuir](/pt-br/guides/panel-apps/branding/#para-aplicativos-existentes).
3. Em **Conexão Git e monitor de publicação**:
   - **Conexão Git** — a conexão que contém o repositório do seu aplicativo.
   - **Branch** — o branch a partir do qual compilar. Os pushes nesse branch recompilam e reimplantam o aplicativo automaticamente.
   - **Ponto de entrada** — o arquivo `.py` que o Panel deve servir (seu `app.py`).
4. Em **Tempo de execução**:
   - **CPU** e **Memória** que o contêiner do aplicativo deve solicitar.

     > Menos recursos (menor CPU / memória) permitem que o aplicativo seja agendado e inicializado a frio mais rapidamente.

   - **Design** — escolha **FAST** para o design moderno do PlaidCloud ou **Padrão** se o CSS do aplicativo espera o estilo padrão do Panel.
   - **Inatividade (minutos)** — por quanto tempo o aplicativo permanece ativo sem tráfego antes de voltar a zero. O padrão é 5 minutos.
   - **Permitir acesso público** — marque para permitir acesso sem autenticação; caso contrário, quem visualiza precisa fazer login em seu tenant.
5. Em **Avançado (exibição incorporada)** — opcional. Por padrão, o aplicativo é servido somente a partir do seu tenant do PlaidCloud. Para incorporá-lo em outro site, clique em **Adicionar domínio** e informe cada domínio autorizado a carregá-lo, um por linha — somente o host, sem esquema nem caminho (por exemplo, `example.com` ou `app.example.com:8443`). Deixe a lista vazia, a menos que você esteja incorporando o aplicativo em outro lugar.
6. Clique em **Publicar**.

Depois de publicar, o aplicativo é **compilado** — o **Status** dele aparece na lista e é atualizado automaticamente. Consulte [Usar um aplicativo Panel](/pt-br/guides/panel-apps/using/) para saber o que significam os status, como abrir o aplicativo quando ele estiver pronto e como acionar uma recompilação sem cancelar a publicação.

> A URL do aplicativo só funciona quando o status da compilação é **Pronto**, e a primeira solicitação depois de um período de inatividade ativa o aplicativo (~15 segundos).

### Avançado: reproduza o PlaidCloud localmente

Usuários técnicos podem compilar e testar o aplicativo com as mesmas entradas que o PlaidCloud usa. Essa é a verificação local mais próxima antes de publicar ou de clicar em **Recompilar**.

O PlaidCloud compila a partir do branch git selecionado com este Dockerfile gerado. Use o mesmo conteúdo localmente como `Dockerfile.plaidcloud-panel`:

```dockerfile
FROM us-docker.pkg.dev/plaidcloud-build/panel-base/platform-panel-base:0.5.1
USER root
COPY . /app
RUN if [ -f /app/requirements.txt ]; then pip install --no-cache-dir -r /app/requirements.txt; fi
# If your entry point is in a subfolder, PlaidCloud also installs that folder's requirements.txt,
# after the root one (so a per-app pin wins). Replace <app-folder> with your entry point's folder,
# or drop this line if your app is at the repository root.
RUN if [ -f "/app/<app-folder>/requirements.txt" ]; then pip install --no-cache-dir -r "/app/<app-folder>/requirements.txt"; fi
USER 10001
```

Para reproduzir a compilação do servidor:

1. Faça checkout do mesmo branch que você seleciona em **Branch**.
2. Execute a compilação a partir da raiz do repositório, para que `COPY . /app` corresponda ao PlaidCloud.
3. Coloque as dependências opcionais em um `requirements.txt` — na raiz do repositório ou ao lado do ponto de entrada. Ambos são instalados, o da pasta do aplicativo por último (para que uma versão fixada por aplicativo prevaleça).
4. Use o mesmo caminho de ponto de entrada que você seleciona em **Ponto de entrada**.

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

A imagem implantada não substitui o ponto de entrada da imagem base. Ela executa `panel serve` a partir de variáveis de ambiente injetadas pelo PlaidCloud. Teste a imagem compilada com o mesmo contrato de tempo de execução:

```sh
docker run --rm \
  --cpus 0.5 \
  --memory 512m \
  -p 5006:5006 \
  -e APP_PATH=/app/app.py \
  -e PANEL_PREFIX=/serve/local \
  -e PANEL_PORT=5006 \
  -e PANEL_ORIGIN=localhost:5006 \
  -e PANEL_KEEP_ALIVE_MS=25000 \
  -e PLAID_PANEL_DESIGN=fast \
  local-panel-app:plaidcloud
```

Abra `http://localhost:5006/serve/local/`.

Reproduza as configurações da caixa de diálogo de publicação ao testar:

- **Ponto de entrada** corresponde a `APP_PATH=/app/<entry-point>`.
- **CPU** e **Memória** correspondem aos limites `--cpus` e `--memory` do Docker.
- **Design: FAST** corresponde a `PLAID_PANEL_DESIGN=fast`.
- **Design: Padrão** significa omitir `PLAID_PANEL_DESIGN`.
- **Inatividade (minutos)** corresponde à janela de redução de escala da implantação. Ela não é aplicada pelo Docker local, mas o aplicativo ainda usa as mesmas configurações de keepalive do websocket do Panel e de limpeza de sessão.
- Os domínios de **exibição incorporada** correspondem a `PANEL_ORIGIN`; use uma lista separada por espaços se precisar testar mais de um host.

Se você não precisa de um contêiner, ainda pode testar a camada de serviço em um ambiente Python local. Instale o mesmo `requirements.txt`, defina as variáveis de ambiente da plataforma e execute `panel serve` com os mesmos flags que a imagem implantada usa.

```sh
export APP_PATH=app.py
export PANEL_PREFIX=/serve/local
export PANEL_PORT=5006
export PANEL_ORIGIN=localhost:5006
export PANEL_KEEP_ALIVE_MS=25000
export PLAID_PANEL_DESIGN=fast

panel serve "$APP_PATH" \
  --address 0.0.0.0 \
  --port "$PANEL_PORT" \
  --prefix "$PANEL_PREFIX" \
  --allow-websocket-origin "$PANEL_ORIGIN" \
  --num-procs 1 \
  --keep-alive "$PANEL_KEEP_ALIVE_MS" \
  --unused-session-lifetime 15000 \
  --index "$(basename "$APP_PATH" .py)"
```

Abra `http://localhost:5006/serve/local/`.

Use `PLAID_PANEL_DESIGN=fast` para reproduzir a aparência padrão implantada. Para testar a opção de design **Padrão** da caixa de diálogo de publicação, deixe `PLAID_PANEL_DESIGN` sem definir e execute o mesmo comando. Mantenha `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive` e `--unused-session-lifetime`; eles fazem parte do contrato de tempo de execução implantado.

## Criar um aplicativo WASM

Um aplicativo WASM é executado no navegador a partir de um arquivo HTML já compilado.

1. Escolha **Novo app** > **Somente navegador** para abrir a caixa de diálogo **Publicar aplicativo Panel serverless**.
2. Informe um **Nome do aplicativo** e uma **Versão**.
3. Escolha o **Local do HTML do aplicativo** — o arquivo HTML em uma conta de documentos.
4. Informe um **Slug de URL do aplicativo** e um **Memorando** opcional.
5. Clique em **Publicar**. Um aplicativo WASM não tem etapa de compilação e é servido imediatamente.
