---
title: Criar uma aplicação Panel
description: Crie uma aplicação Panel no Panel Studio, a partir de uma aplicação em branco, de uma tabela, de uma vista ou da galeria, ou publique uma aplicação de servidor a partir do git ou uma aplicação WASM estática para necessidades específicas.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Comece pelo Panel Studio. Não precisa de repositório nem de configuração: cria a aplicação no PlaidCloud, pré-visualiza-a e publica-a quando estiver pronto. Escolha um tempo de execução à medida apenas quando o Studio não servir.

## Criar uma aplicação Studio

Abra **Aplicações** e abra o menu **Novo app**. Sob o título **Panel app**, **Studio** escreve e publica a aplicação no editor do PlaidCloud com a disposição padrão e guarda o código por si. Também pode escolher **Nova aplicação Studio** na linha **Aplicações Studio** do cartão **Aplicações e identidade visual** do separador **Início** de um projeto, ou [começar a partir de uma tabela](#começar-a-partir-de-uma-tabela).

1. Escolha **Novo app** > **Studio**.
2. Introduza um **Nome**. O **Slug do URL** é preenchido a partir dele.
3. Escolha o **Projeto** a que a aplicação pertence. Precisa de acesso de edição ao projeto.
4. Em **Começar a partir de**, escolha onde a aplicação começa:

   | Começar a partir de | Obtém |
   |---|---|
   | **Aplicação em branco** | Uma aplicação mínima com um `app.py` e um `requirements.txt`. |
   | **A partir de uma tabela** | Uma aplicação criada sobre a tabela que escolher. |
   | **A partir de uma vista** | O mesmo, criado sobre uma vista do projeto. |
   | **A partir de outra aplicação Studio** | Uma cópia de uma das suas aplicações Studio. |
   | **A partir da galeria** | Uma cópia de uma aplicação que a sua área de trabalho [listou na galeria](#começar-a-partir-da-galeria). |

5. Escolha **Criar**. O Studio abre a nova aplicação. Para uma tabela ou uma vista, o pedido do Weave para criar a primeira página fica pronto a enviar.

Consulte o [Panel Studio](/pt-pt/guides/panel-apps/studio/) para editar, pré-visualizar e publicar a aplicação.

### Começar a partir de uma tabela

Também pode começar no separador **Tabelas** de um projeto. Selecione uma tabela ou vista e escolha **Criar aplicação Panel** no menu **Novo** ou no menu de contexto. A caixa de diálogo **Nova aplicação Studio** abre com o projeto e a tabela já escolhidos. O comando está disponível quando tem acesso de edição ao projeto e o projeto não é só de leitura.

### Começar a partir da galeria

Escolha **Novo app** > **Da galeria…** para navegar pelas aplicações que a sua área de trabalho listou e, depois, **Criar aplicação a partir disto…** para fazer a sua própria cópia. Ou escolha **A partir da galeria** na caixa de diálogo **Nova aplicação Studio**. Consulte [A galeria de aplicações](/pt-pt/guides/panel-apps/gallery/), incluindo como listar a sua própria aplicação.

## Outros tempos de execução

As aplicações Studio cobrem a maioria dos painéis de controlo e ferramentas. Para uma necessidade específica, publique com um dos outros [tempos de execução](/pt-pt/guides/panel-apps/) a partir do menu **Novo app**:

- **Apenas navegador** — o seu próprio repositório; a aplicação é executada no navegador do espectador.
- **Baseada em servidor** — o seu próprio repositório; a aplicação é executada num servidor do PlaidCloud, por exemplo para reutilizar código existente ou o seu próprio processo de compilação.
- **Aplicação Dash** — publique uma aplicação Plotly Dash. Consulte [Aplicações Dash](/pt-pt/guides/dash-apps/).

## Criar uma aplicação de servidor

Uma aplicação de servidor é criada a partir de um repositório git e disponibilizada em `https://<your-tenant-host>/serve/<slug>/`. Aponta o PlaidCloud para um ramo de um repositório; este compila o código num contentor, executa `panel serve` sobre ele e volta a compilar automaticamente sempre que faz push para esse ramo.

### Preparar o repositório da aplicação

O repositório precisa de duas coisas: um **ponto de entrada** — um ficheiro Python que cria uma aplicação Panel e a marca com `.servable()` — e, opcionalmente, um **`requirements.txt`** a listar quaisquer pacotes adicionais, na raiz do repositório ou junto ao ponto de entrada.

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

É uma aplicação completa. A chamada `.servable()` é o que o PlaidCloud disponibiliza — tudo o que pretende que seja apresentado tem de ser marcado como servable (diretamente ou por estar dentro de uma disposição servable).

#### Um exemplo ligeiramente mais completo

As aplicações Panel são interativas. Esta acrescenta um controlo deslizante que atualiza uma tabela em direto:

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

#### Adicionar dependências

Este segundo exemplo importa `pandas`, que não faz parte da imagem base, pelo que deve adicionar um `requirements.txt` (na raiz do repositório ou junto ao ponto de entrada):

```text
pandas
```

O PlaidCloud instala estes pacotes com `pip` quando cria a imagem. As bibliotecas de visualização comuns — `plotly`, `holoviews`, `hvplot` — também não estão na imagem base, pelo que deve listar aqui as que a sua aplicação importa.

> **O que a plataforma fornece — e espera.** Tenha estes pressupostos presentes quando escrever a sua aplicação:
>
> - **`panel` e `bokeh` estão pré-instalados** pela imagem base da plataforma. Não os liste em `requirements.txt` e evite fixar uma versão mais antiga do Panel — a reconexão de atualização em direto depende de uma versão recente.
> - **As bibliotecas cliente do PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) estão pré-instaladas.** Importe `plaidcloud.rpc` ou `plaidcloud.utilities` diretamente — não as liste em `requirements.txt`.
> - **O `requirements.txt` pode estar na raiz do repositório ou junto ao ponto de entrada.** Num repositório partilhado (monorepo), mantenha as dependências de cada aplicação na sua própria pasta. Um ficheiro ao nível da raiz, se existir, também é instalado — coloque aí as dependências partilhadas e as específicas da aplicação junto a ela.
> - **A aplicação é executada como utilizador sem privilégios de root num sistema de ficheiros só de leitura.** Apenas `/tmp` é gravável, pelo que deve escrever aí quaisquer ficheiros temporários (a maioria das bibliotecas já respeita `$TMPDIR`).
> - **Não fixe no código a porta, o prefixo do URL nem o anfitrião.** O PlaidCloud atribui-os e injeta-os no momento da implementação — basta chamar `.servable()`.

Para obter o aspeto do PlaidCloud e filtros, grelhas e gráficos prontos a usar, crie a sua aplicação com [o kit de aplicações Panel](/pt-pt/guides/panel-apps/app-kit/).

### Definir o tema: claro, escuro ou um interruptor

As aplicações de servidor são apresentadas, por predefinição, com o design moderno **Fast** do PlaidCloud — um aspeto limpo, ao estilo Fluent, aplicado em toda a plataforma. Na caixa de diálogo de publicação, **Design** controla essa camada da plataforma:

- **FAST** — a predefinição do PlaidCloud. Utilize-a para novas aplicações e para aplicações criadas com modelos Fast.
- **Predefinição** — o estilo predefinido do Panel. Utilize-a quando o CSS ou os elementos visuais de uma aplicação existente deixarem de funcionar com FAST.

O que controla no código da aplicação é o **tema**: claro, escuro ou um interruptor que o espectador pode alternar.

O tema é uma propriedade do **modelo** que disponibiliza. Os modelos Fast — `FastListTemplate` (uma única coluna) e `FastGridTemplate` (uma grelha responsiva) — aceitam duas definições para o efeito:

- **`theme`** — `"default"` para claro ou `"dark"`. Defini-lo fixa a aplicação nesse tema, mesmo que um espectador acrescente `?theme=dark` ao URL.
- **`theme_toggle`** — `True` mostra um interruptor claro/escuro no cabeçalho; `False` oculta-o. Por predefinição é `True`. Ocultar o interruptor não fixa o tema por si só — fixe-o com `theme` (acima); defina `theme_toggle=False` depois de o fazer, para que os espectadores não vejam um interruptor que não consegue alterar nada.

Escolha o padrão que se adequa à sua aplicação.

**Apenas claro** — ideal para relatórios densos e tabelas financeiras, que normalmente são estilizadas à mão para um fundo claro:

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

**Apenas escuro:**

```python
pn.template.FastListTemplate(
    title="Ops Monitor",
    theme="dark",
    theme_toggle=False,
    main=[...],
).servable()
```

**Deixar o espectador escolher** — começa em claro, com um interruptor no cabeçalho. Omita `theme` para que siga o interruptor:

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **Se permitir o modo escuro, torne as suas tabelas compatíveis com ele.** Um `Tabulator` fixado a um tema de tabela claro (`theme="bootstrap"`), ou CSS personalizado com cores claras fixas no código, como `background: #fff`, é apresentado como um bloco branco ilegível numa página escura. Utilize um tema de tabela que acompanhe a aplicação — `pn.widgets.Tabulator(..., theme="fast")` — e evite cores claras fixas no código. Se um relatório estiver muito estilizado à mão para claro, fixe-o em claro (o primeiro padrão acima).

Uma aplicação simples sem modelo — `pn.Column(...).servable()` — segue a predefinição do Panel e não é afetada por estas definições; recorra a um modelo quando pretender controlo explícito.

O seu repositório tem de estar acessível através de uma **ligação git** no PlaidCloud. Se o seu código estiver no [PlaidCloud Git](/pt-pt/guides/git/), crie uma ligação **PlaidCloud Git** gerida em **Tools > Connections** — não precisa de URL de servidor nem de credenciais. Para o percurso completo desde um repositório vazio até uma aplicação disponibilizada, consulte [Implementar uma aplicação Panel a partir do PlaidCloud Git](/pt-pt/guides/panel-apps/deploy-from-git/).

### Publicar a aplicação

1. Escolha **Novo app** > **Baseada em servidor** para abrir a caixa de diálogo **Publicar aplicação Panel de servidor**. As suas definições estão agrupadas em secções.
2. Em **Definições do diretório**:
   - **Nome da aplicação** — o nome de apresentação mostrado na lista.
   - **Slug do URL** — tanto o URL da aplicação como o seu nome interno, pelo que tem de ser uma etiqueta DNS válida: letras minúsculas, dígitos e hífenes, começando por uma letra, com 40 caracteres ou menos (por exemplo, `sales-dashboard`). A caixa de diálogo verifica-o antes de publicar.
   - **Memorando** — uma descrição opcional.
   - **Projeto** — o projeto a que a aplicação pertence. Fornece a [identidade visual](/pt-pt/guides/panel-apps/branding/) da aplicação e é o projeto predefinido das suas tabelas. Não o pode alterar aqui depois de publicar; utilize [Assign](/pt-pt/guides/panel-apps/branding/#para-aplicações-existentes).
3. Em **Ligação Git e monitor de publicação**:
   - **Ligação Git** — a ligação que contém o repositório da sua aplicação.
   - **Ramo** — o ramo a partir do qual compilar. Os pushes para este ramo recompilam e voltam a implementar a aplicação automaticamente.
   - **Ponto de entrada** — o ficheiro `.py` que o Panel deve disponibilizar (o seu `app.py`).
4. Em **Tempo de execução**:
   - **CPU** e **Memória** que o contentor da aplicação deve solicitar.

     > Menos recursos (menos CPU / memória) permitem à aplicação ser agendada e arrancar a frio mais depressa.

   - **Design** — escolha **FAST** para o design moderno do PlaidCloud ou **Predefinição** se o CSS da aplicação esperar o estilo predefinido do Panel.
   - **Inatividade (minutos)** — durante quanto tempo a aplicação se mantém ativa sem tráfego antes de voltar a escalar para zero. A predefinição é 5 minutos.
   - **Permitir acesso público** — assinale para permitir acesso não autenticado; caso contrário, os espectadores têm de iniciar sessão no seu tenant.
5. Em **Avançado (disponibilização incorporada)** — opcional. Por predefinição, a aplicação é disponibilizada apenas a partir do seu tenant do PlaidCloud. Para a incorporar noutro site, clique em **Adicionar domínio** e introduza cada domínio autorizado a carregá-la, um por linha — apenas o anfitrião, sem esquema nem caminho (por exemplo, `example.com` ou `app.example.com:8443`). Deixe a lista vazia, a menos que esteja a incorporar a aplicação noutro local.
6. Clique em **Publicar**.

Depois de publicar, a aplicação é **compilada** — o seu **Estado** é mostrado na lista e atualiza-se automaticamente. Consulte [Utilizar uma aplicação Panel](/pt-pt/guides/panel-apps/using/) para saber o que significam os estados, como abrir a aplicação quando estiver pronta e como desencadear uma recompilação sem anular a publicação.

> O URL da aplicação só funciona quando o estado da compilação for **Pronta**, e o primeiro pedido depois de ter estado inativa arranca-a (~15 segundos).

### Avançado: reproduzir o PlaidCloud localmente

Os utilizadores técnicos podem compilar e testar a aplicação com as mesmas entradas que o PlaidCloud usa. Esta é a verificação local mais próxima antes de publicar ou de clicar em **Recompilar**.

O PlaidCloud compila a partir do ramo git selecionado com este Dockerfile gerado. Utilize o mesmo conteúdo localmente como `Dockerfile.plaidcloud-panel`:

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

1. Faça checkout do mesmo ramo que seleciona em **Ramo**.
2. Execute a compilação a partir da raiz do repositório, para que `COPY . /app` corresponda ao PlaidCloud.
3. Coloque as dependências opcionais num `requirements.txt` — na raiz do repositório ou junto ao ponto de entrada. Ambos são instalados, o da pasta da aplicação em último lugar (para que prevaleça a fixação por aplicação).
4. Utilize o mesmo caminho do ponto de entrada que seleciona em **Ponto de entrada**.

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

A imagem implementada não substitui o ponto de entrada da imagem base. Executa `panel serve` a partir de variáveis de ambiente injetadas pelo PlaidCloud. Teste a imagem compilada com o mesmo contrato de execução:

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

Faça corresponder as definições da caixa de diálogo de publicação ao testar:

- **Ponto de entrada** corresponde a `APP_PATH=/app/<entry-point>`.
- **CPU** e **Memória** correspondem aos limites `--cpus` e `--memory` do Docker.
- **Design: FAST** corresponde a `PLAID_PANEL_DESIGN=fast`.
- **Design: Predefinição** significa omitir `PLAID_PANEL_DESIGN`.
- **Inatividade (minutos)** corresponde à janela de redução de escala da implementação. Não é imposta pelo Docker local, mas a aplicação continua a usar as mesmas definições de keepalive de websocket e de limpeza de sessões do Panel.
- Os domínios de **Disponibilização incorporada** correspondem a `PANEL_ORIGIN`; utilize uma lista separada por espaços se precisar de testar mais do que um anfitrião.

Se não precisar de um contentor, pode na mesma testar a camada de disponibilização a partir de um ambiente Python local. Instale o mesmo `requirements.txt`, defina as variáveis de ambiente da plataforma e execute `panel serve` com as mesmas opções que a imagem implementada usa.

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

Utilize `PLAID_PANEL_DESIGN=fast` para corresponder ao aspeto implementado por predefinição. Para testar a opção de design **Predefinição** da caixa de diálogo de publicação, deixe `PLAID_PANEL_DESIGN` por definir e execute o mesmo comando. Mantenha `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive` e `--unused-session-lifetime` no lugar; fazem parte do contrato de execução implementado.

## Criar uma aplicação WASM

Uma aplicação WASM é executada no navegador a partir de um ficheiro HTML pré-compilado.

1. Escolha **Novo app** > **Apenas navegador** para abrir a caixa de diálogo **Publicar aplicação Panel sem servidor**.
2. Introduza um **Nome da aplicação** e uma **Versão**.
3. Escolha a **Localização HTML da aplicação** — o ficheiro HTML numa conta de documentos.
4. Introduza um **Slug de URL da aplicação** e um **Memorando** opcional.
5. Clique em **Publicar**. Uma aplicação WASM não tem passo de compilação e é disponibilizada imediatamente.
