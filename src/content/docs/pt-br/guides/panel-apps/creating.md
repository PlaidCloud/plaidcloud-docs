---
title: Criando um aplicativo Panel
description: Publique no PlaidCloud um aplicativo HoloViz Panel do lado do servidor a partir de um repositório git (com um exemplo hello-world) ou um aplicativo WASM estático a partir de um arquivo.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Abra **Meus aplicativos Panel**. A barra de ferramentas oferece duas formas de publicar, uma para cada [tempo de execução](/pt-br/guides/panel-apps/):

- **Novo aplicativo de servidor** — compile e execute um aplicativo a partir de um repositório git.
- **Adicionar aplicativo WASM** — publique um aplicativo estático, no navegador, a partir de um arquivo.

Para escrever o aplicativo no próprio PlaidCloud, sem repositório para configurar, use o [Panel Studio](/pt-br/guides/panel-apps/studio/).

## Criando um aplicativo de servidor

Um aplicativo de servidor é compilado a partir de um repositório git e servido em `https://<your-tenant-host>/serve/<slug>/`. Você aponta o PlaidCloud para um branch de um repositório; ele compila o código em um contêiner, executa `panel serve` nele e o recompila automaticamente sempre que você envia alterações para esse branch.

### Prepare o repositório do seu aplicativo

Seu repositório precisa de duas coisas: um **ponto de entrada** — um arquivo Python que constrói um aplicativo Panel e o marca como `.servable()` — e, opcionalmente, um **`requirements.txt`** que liste os pacotes extras, na raiz do repositório ou ao lado do ponto de entrada.

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

#### Hello World

Crie `app.py`:

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

Esse é um aplicativo completo. A chamada `.servable()` é o que o PlaidCloud serve — tudo o que você quer exibir deve ser marcado como servable (diretamente ou por estar dentro de um layout servable).

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

Este segundo exemplo importa `pandas`, que não faz parte da imagem base, então adicione um `requirements.txt` (na raiz do repositório ou ao lado do ponto de entrada):

```text
pandas
```

O PlaidCloud instala esses pacotes com `pip` ao construir a imagem. Bibliotecas de visualização comuns — `plotly`, `holoviews`, `hvplot` — também não estão na imagem base, então liste aqui as que o seu aplicativo importa.

> **O que a plataforma fornece — e espera.** Tenha estas premissas em mente ao escrever seu aplicativo:
>
> - **`panel` e `bokeh` vêm pré-instalados** pela imagem base da plataforma. Não os liste em `requirements.txt` e evite fixar uma versão mais antiga do Panel — a reconexão de atualização ao vivo depende de uma versão recente.
> - **As bibliotecas cliente do PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) vêm pré-instaladas.** Importe `plaidcloud.rpc` ou `plaidcloud.utilities` diretamente — não as liste em `requirements.txt`.
> - **O `requirements.txt` pode ficar na raiz do repositório ou ao lado do seu ponto de entrada.** Em um repositório compartilhado (monorepo), mantenha as dependências de cada aplicativo na própria pasta. Um arquivo no nível da raiz, se existir, também é instalado — coloque ali as dependências compartilhadas e, ao lado do aplicativo, as específicas dele.
> - **O aplicativo é executado como um usuário não root em um sistema de arquivos somente leitura.** Somente `/tmp` permite gravação, então grave ali quaisquer arquivos temporários (a maioria das bibliotecas já respeita `$TMPDIR`).
> - **Não fixe no código a porta, o prefixo da URL nem o host.** O PlaidCloud os atribui e os injeta no momento da implantação — basta chamar `.servable()`.

Para obter a aparência do PlaidCloud e filtros, grades e gráficos prontos, crie seu aplicativo com [o kit de aplicativos Panel](/pt-br/guides/panel-apps/app-kit/).

### Defina o tema: claro, escuro ou alternável

Por padrão, os aplicativos de servidor são renderizados no design moderno **Fast** do PlaidCloud — um visual limpo, no estilo Fluent, aplicado em toda a plataforma. Na caixa de diálogo de publicação, **Design** controla essa camada da plataforma:

- **FAST** — o padrão do PlaidCloud. Use-o para aplicativos novos e aplicativos criados com modelos Fast.
- **Padrão** — a estilização padrão do Panel. Use-o quando o CSS ou os elementos visuais de um aplicativo existente quebrarem com FAST.

O que você controla no código do seu aplicativo é o **tema**: claro, escuro ou uma chave que o visualizador pode alternar.

O tema é uma propriedade do **modelo** que você serve. Os modelos Fast — `FastListTemplate` (uma única coluna) e `FastGridTemplate` (uma grade responsiva) — aceitam duas configurações para isso:

- **`theme`** — `"default"` para claro ou `"dark"`. Defini-la fixa o aplicativo nesse tema, mesmo que um visualizador adicione `?theme=dark` à URL.
- **`theme_toggle`** — `True` mostra uma chave claro/escuro no cabeçalho; `False` a oculta. O padrão é `True`. Ocultar a chave não fixa o tema por si só — fixe-o com `theme` (acima); defina `theme_toggle=False` depois, para que os visualizadores não vejam uma chave que não altera nada.

Escolha o padrão que se adapta ao seu aplicativo.

**Somente claro** — o melhor para relatórios densos e tabelas financeiras, que geralmente são estilizados à mão para um fundo claro:

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

**Deixe o visualizador escolher** — o padrão é claro, com uma chave no cabeçalho. Omita `theme` para que ele siga a chave:

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **Se você permitir o modo escuro, deixe suas tabelas compatíveis com ele.** Um `Tabulator` fixado em um tema de tabela claro (`theme="bootstrap"`), ou um CSS personalizado com cores claras fixas no código, como `background: #fff`, é renderizado como um bloco branco ilegível em uma página escura. Use um tema de tabela que siga o aplicativo — `pn.widgets.Tabulator(..., theme="fast")` — e evite cores claras fixas no código. Se um relatório é muito estilizado à mão para o modo claro, fixe-o no claro (o primeiro padrão acima).

Um aplicativo simples sem modelo — `pn.Column(...).servable()` — segue o padrão do Panel e não é afetado por essas configurações; recorra a um modelo quando quiser controle explícito.

Seu repositório precisa estar acessível por meio de uma **conexão git** no PlaidCloud. Se o seu código está no [PlaidCloud Git](/pt-br/guides/git/), crie uma conexão gerenciada do **PlaidCloud Git** em **Tools > Connections** — ela não precisa de URL de servidor nem de credenciais. Para o caminho completo de um repositório vazio até um aplicativo servido, veja [Implante um aplicativo Panel a partir do PlaidCloud Git](/pt-br/guides/panel-apps/deploy-from-git/).

### Publique o aplicativo

1. Clique em **Novo aplicativo de servidor** para abrir a caixa de diálogo **Publicar aplicativo Panel de servidor**. Suas configurações são agrupadas em seções.
2. Em **Configurações do diretório**:
   - **Nome do aplicativo** — o nome de exibição mostrado na lista.
   - **Slug de URL** — a URL do aplicativo e também o nome interno dele, então deve ser um rótulo DNS válido: letras minúsculas, dígitos e hifens, começando com uma letra, com 40 caracteres ou menos (por exemplo, `sales-dashboard`). A caixa de diálogo verifica isso antes de você publicar.
   - **Memorando** — uma descrição opcional.
   - **Projeto** — o projeto proprietário do aplicativo. Ele fornece a [identidade visual](/pt-br/guides/panel-apps/branding/) do aplicativo e é o projeto padrão das tabelas dele. Você não pode alterá-lo aqui depois de publicar; use [Atribuir](/pt-br/guides/panel-apps/branding/#para-aplicativos-existentes).
3. Em **Conexão Git e monitor de publicação**:
   - **Conexão Git** — a conexão que guarda o repositório do seu aplicativo.
   - **Branch** — o branch a partir do qual compilar. Envios para esse branch recompilam e reimplantam o aplicativo automaticamente.
   - **Ponto de entrada** — o arquivo `.py` que o Panel deve servir (seu `app.py`).
4. Em **Tempo de execução**:
   - **CPU** e **Memória** que o contêiner do aplicativo deve solicitar.

     > Menos recursos (menos CPU / memória) permitem que o aplicativo seja agendado e inicie a frio mais rápido.

   - **Design** — escolha **FAST** para o design moderno do PlaidCloud ou **Padrão** se o CSS do aplicativo espera a estilização padrão do Panel.
   - **Inatividade (minutos)** — por quanto tempo o aplicativo permanece ativo sem tráfego antes de voltar a zero. O padrão é 5 minutos.
   - **Permitir acesso público** — marque para permitir acesso sem autenticação; caso contrário, os visualizadores precisam fazer logon no seu tenant.
5. Em **Avançado (exibição incorporada)** — opcional. Por padrão, o aplicativo é servido apenas a partir do seu tenant do PlaidCloud. Para incorporá-lo em outro site, clique em **Adicionar domínio** e informe cada domínio autorizado a carregá-lo, um por linha — apenas o host, sem esquema nem caminho (por exemplo, `example.com` ou `app.example.com:8443`). Deixe a lista vazia, a menos que você esteja incorporando o aplicativo em outro lugar.
6. Clique em **Publicar**.

Depois que você publica, o aplicativo é **compilado** — o **Status** dele aparece na lista e é atualizado automaticamente. Veja [Usando um aplicativo Panel](/pt-br/guides/panel-apps/using/) para saber o que significam os status, como abrir o aplicativo quando ele estiver pronto e como disparar uma recompilação sem cancelar a publicação.

> A URL do aplicativo só funciona quando o status de compilação dele é **Pronto**, e a primeira solicitação depois de um período ocioso o inicia (~15 segundos).

### Avançado: reproduza o PlaidCloud localmente

Usuários técnicos podem compilar e testar o aplicativo com as mesmas entradas que o PlaidCloud usa. Esta é a verificação local mais próxima antes de publicar ou clicar em **Recompilar**.

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
- **Inatividade (minutos)** corresponde à janela de redução de escala da implantação. Ela não é imposta pelo Docker local, mas o aplicativo ainda usa as mesmas configurações de keepalive de websocket e de limpeza de sessão do Panel.
- Os domínios de exibição incorporada correspondem a `PANEL_ORIGIN`; use uma lista separada por espaços se precisar testar mais de um host.

Se você não precisa de um contêiner, ainda pode testar a camada de serviço a partir de um ambiente Python local. Instale o mesmo `requirements.txt`, defina as variáveis de ambiente da plataforma e execute `panel serve` com as mesmas flags que a imagem implantada usa.

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

Use `PLAID_PANEL_DESIGN=fast` para reproduzir o visual padrão implantado. Para testar a opção de design **Padrão** da caixa de diálogo de publicação, deixe `PLAID_PANEL_DESIGN` sem definir e execute o mesmo comando. Mantenha `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive` e `--unused-session-lifetime` no lugar; eles fazem parte do contrato de tempo de execução implantado.

## Criando um aplicativo WASM

Um aplicativo WASM é executado no navegador a partir de um arquivo HTML pré-compilado.

1. Clique em **Adicionar aplicativo WASM** para abrir a caixa de diálogo **Publicar aplicativo Panel serverless**.
2. Informe um **Nome do aplicativo** e uma **Versão**.
3. Escolha o **Local do HTML do aplicativo** — o arquivo HTML em uma conta de documentos.
4. Informe um **Slug de URL do aplicativo** e um **Memorando** opcional.
5. Clique em **Publicar**. Um aplicativo WASM não tem etapa de compilação e é servido imediatamente.
