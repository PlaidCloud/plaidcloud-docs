---
title: O kit de aplicações Panel
description: Crie aplicações Panel com o aspeto do PlaidCloud com o kit plaidcloud_panel — a estrutura App, a paleta de comandos, FilterBar, KpiCard, DataGrid, Chart, Form, botões de execução, definições guardadas, impressão e traduções, em tema claro e escuro.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

Todas as aplicações Panel de servidor têm o kit `plaidcloud_panel` instalado. Dá à sua aplicação o aspeto do PlaidCloud — as mesmas cores, tipos de letra e espaçamento do resto da plataforma, em tema claro e escuro — e um conjunto de componentes prontos a usar para os ecrãs de que a maioria das aplicações precisa: filtros, números de destaque, uma grelha de dados grande, gráficos e formulários. A sua aplicação adota automaticamente a [identidade visual do projeto](/pt-pt/guides/panel-apps/branding/).

```python
import plaidcloud_panel as pcp
```

Importar o kit também aplica o aspeto do PlaidCloud aos gráficos Plotly e Matplotlib.

## Começar a partir de um modelo

No [Panel Studio](/pt-pt/guides/panel-apps/studio/), **Nova aplicação Studio** começa a partir de uma aplicação em branco, de uma tabela ou vista, de outra aplicação do Studio ou de uma aplicação da [galeria](/pt-pt/guides/panel-apps/gallery/), sem nenhum comando para executar.

Para uma aplicação que mantém num repositório git, o kit inclui um comando que escreve uma aplicação inicial funcional. Execute-o a partir de qualquer pasta e depois edite os nomes da tabela e das colunas:

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| Opção | O que faz |
|---|---|
| `--layout dashboard` | Filtros na barra lateral, dois números de destaque e um gráfico. |
| `--layout explorer` | Filtros na barra lateral, uma contagem de linhas e uma tabela de linhas. |
| `--table` | A tabela do PlaidCloud que a aplicação lê. |
| `--filters` | Colunas separadas por vírgulas pelas quais filtrar. A primeira controla o gráfico. |
| `--measure` | A coluna numérica a totalizar. |
| `--dir` | Onde escrever `app.py` e `requirements.txt`. Por predefinição, a pasta atual. |

O comando termina sem escrever nada se `app.py` já existir. Faça commit dos dois ficheiros no seu repositório e [publique-o como aplicação de servidor](/pt-pt/guides/panel-apps/creating/#criar-uma-aplicação-de-servidor).

## Uma aplicação de exemplo

Esta aplicação filtra uma tabela de vendas por região e ano, mostra dois números de destaque, um gráfico e uma grelha com paginação das linhas correspondentes. A grelha mostra os montantes com separadores de milhares e as margens em percentagem. Cada elemento acompanha os filtros.

```python
import panel as pn
import plaidcloud_panel as pcp
from bokeh.plotting import figure
from plaidcloud.utilities.panel_data import table

pn.extension("tabulator")

sales = table("sales")
bar = pcp.FilterBar(sales, "region", "year")


def by_region(t):
    df = t.aggregate(by=["region"], total=("amount", "sum"))
    regions = df["region"].astype(str).tolist()
    fig = figure(x_range=regions, height=320, toolbar_location=None)
    fig.vbar(x=regions, top=df["total"].astype(float).tolist(), width=0.8, color=pcp.series()[0])
    return fig


def grid(t):
    return pcp.DataGrid(t, key="id", totals={"amount": "sum"}, formats={"amount": "0,0", "margin": "0.0%"})


pcp.App(
    "Sales",
    sidebar=[bar],
    main=[
        pn.Row(
            pcp.KpiCard("Total amount", bar.table, "amount"),
            pcp.KpiCard("Orders", bar.table),
        ),
        pcp.Chart(pn.bind(by_region, bar.table), title="Amount by region"),
        pcp.Section("Orders", pn.bind(grid, bar.table)),
    ],
).servable()
```

O padrão é o mesmo em todas as aplicações do kit: crie uma `FilterBar` sobre uma tabela e depois associe cada vista a `bar.table`. Uma vista que não esteja associada a `bar.table` (ou a um widget) nunca é atualizada quando os filtros mudam.

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)` cria a estrutura da aplicação: um cabeçalho com o título, o logótipo do projeto e o utilizador com sessão iniciada, uma barra lateral e uma área principal. Chame `.servable()` sobre o resultado.

- **Navegação** — transmita `nav=[("Overview", overview_page), ("Detail", detail_page)]` para obter um menu de páginas no topo da barra lateral. Cada página é um objeto Panel ou uma função que devolve um. As funções são executadas quando a página é selecionada.
- **Tema** — a aplicação abre no tema claro. Transmita `theme="dark"` para abrir no tema escuro ou acrescente `?theme=dark` ao URL. Com `theme_toggle=True` (o valor predefinido), o cabeçalho inclui um comutador claro/escuro.
- **Identidade visual** — a aplicação lê as cores e o logótipo da marca do respetivo projeto quando uma sessão começa. Um projeto sem identidade visual recebe os valores predefinidos do PlaidCloud.
- **Paleta de comandos** — prima Ctrl-K (Cmd-K num Mac) para pesquisar e executar comandos. Cada página em `nav` é listada como **Ir para** o nome da página, e `commands={"Refresh data": refresh}` acrescenta entradas suas, cada uma com uma etiqueta e uma função que não recebe argumentos. Escolha uma entrada e a aplicação executa-a.
- **Visita guiada na primeira execução** — `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]` mostra uma breve introdução passo a passo, em que cada passo é um título e uma linha de texto. Aparece no topo da página até a concluir ou ignorar, e não volta a ser mostrada.
- **Qualquer outra coisa** — os restantes argumentos nomeados são transmitidos ao `FastListTemplate` do Panel.

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` cria uma caixa de escolha múltipla com pesquisa por cada coluna que indicar, listando os valores distintos dessa coluna (até 1000, com um aviso quando a lista é cortada). Uma caixa mostra **Todos** quando nada está escolhido. Transmita os seus próprios widgets por nome de coluna para tudo o resto.

- `bar.table` é a tabela restringida pelas seleções atuais. Um widget em branco não restringe os dados.
- As seleções são guardadas no URL da página (`?region=EU`), pelo que uma vista filtrada pode ser partilhada como ligação.

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)` mostra um número de destaque. `fn` é `sum`, `count`, `avg`, `min` ou `max`, calculado pelo servidor sobre a tabela inteira. Sem `column`, mostra a contagem de linhas. Transmita `bar.table` como origem para que o número acompanhe os filtros.

Transmita `drill_to=grid`, uma `DataGrid`, para acrescentar um botão **View rows** sob o número. Ao escolhê-lo, a grelha passa a apontar para a própria tabela do cartão, pelo que a grelha lista as linhas que estão por trás do número.

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` é uma vista de tabela para dados de qualquer dimensão. Apenas a página atual é enviada para o navegador; a paginação, a ordenação, os totais e a exportação são todos executados no servidor.

- **Paginação** — 200, 500 ou 1000 linhas por página, com botões Anterior e Seguinte e um contador de linhas.
- **Ordenação** — clique no cabeçalho de uma coluna. A ordenação aplica-se à tabela inteira, não apenas à página visível.
- **Totais** — `totals` associa uma coluna a `sum`, `count`, `avg`, `min` ou `max`. O servidor calcula cada um sobre todas as linhas correspondentes e fixa o resultado como última linha da grelha.
- **Exportar** — os botões **CSV** e **XLSX** transferem todas as linhas correspondentes na ordenação atual, até `export_cap` linhas (100 000 por predefinição). Quando a tabela é maior, um aviso indica que deve restringir os filtros. As células de texto que começam por `=`, `+`, `-` ou `@` recebem um apóstrofo como prefixo para que uma folha de cálculo as leia como texto.
- **Formatos numéricos** — `formats={"margin": "0.0%", "amount": "0,0"}` define um formato de apresentação por coluna, usando cadeias de formato [numbro](https://numbrojs.com/format.html). Um formato `%` multiplica por 100. A linha Total usa o mesmo formato. As colunas de vírgula flutuante sem formato mostram até duas casas decimais com separadores de milhares. **Copiar**, **CSV** e **XLSX** mantêm os valores em bruto.
- **Chave** — `key` é a coluna, ou a lista de colunas, que identifica uma linha de forma única. Transmita-a sempre. Consulte [Paginação estável](/pt-pt/guides/panel-apps/data-api/#paginação-estável).

- **Agrupar por** — `group_by=["region"]` mostra uma linha por grupo, com as medidas de `totals` e uma contagem `rows`, todas calculadas pelo servidor, e uma linha **Total** sobre todas as linhas correspondentes. Transmita `groupable=["region", "year"]` para acrescentar um seletor **Agrupar por** para que os leitores escolham as colunas. Uma grelha mostra até 1000 grupos e avisa quando cortou a lista. As linhas de grupo não têm ligações **Abrir**.
- **Formatação condicional** — `rules` colore as células por valor. Cada regra indica uma `column`, uma `op` (`>`, `>=`, `<`, `<=`, `==`, `!=` ou `between`), um `value` (`[low, high]` para `between`) e um `token` (`success`, `warning`, `error` ou `info`), por exemplo `{"column": "margin", "op": "<", "value": 0, "token": "error"}`. A linha Total nunca é colorida.
- **Copiar** — o botão **Copiar** coloca a página atual, com as colunas visíveis e a linha Total, na área de transferência como texto separado por tabulações que se cola no Excel.
- **Open in PlaidCloud** — quando a origem é uma tabela do PlaidCloud, uma ligação **Open in PlaidCloud** abre essa tabela.
- **Disposição de colunas guardada** — `layout_key="orders"` acrescenta os seletores **Colunas** e **Pinned** para escolher e ordenar colunas e fixar algumas delas. A escolha de cada leitor é guardada sob esse nome e restaurada na vez seguinte em que abre a aplicação.
- **Ligações de linha** — `row_link` é uma função que recebe uma linha, como dicionário, e devolve um endereço web, ou `None` para nenhuma ligação. A grelha acrescenta uma coluna **Abrir** com uma ligação em cada linha que a tenha. Apenas os endereços `http` e `https` e os caminhos no mesmo site são ligados.
- **Atualizar** — `grid.refresh()` consulta novamente a mesma origem e mantém a página, a ordenação e o agrupamento. Chame-o depois de uma [execução](#botões-de-execução-e-atualidade) terminar de escrever a tabela.

`source` é o nome de uma tabela ou uma tabela da [API de dados](/pt-pt/guides/panel-apps/data-api/). Para voltar a filtrar uma grelha, defina `grid.source` como uma tabela filtrada ou crie uma nova grelha a partir de `bar.table`, como faz o exemplo.

A grelha está sujeita à segurança ao nível da linha do leitor: lê através da ligação do próprio leitor.

## Chart

`pcp.Chart(obj, title=None, height=320)` coloca um gráfico num cartão com título. `obj` pode ser uma figura Bokeh, um gráfico hvPlot ou HoloViews, uma figura Plotly, uma figura Matplotlib ou um `pn.bind(...)` que devolva qualquer um deles. Os eixos numéricos das figuras Bokeh mostram separadores de milhares, pelo que 800000 se lê 800 000.

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")` dispõe widgets de entrada como um único formulário com um botão de envio. `form.values()` devolve `{widget.name: widget.value}` para cada widget com nome, e `on_submit` recebe esse dicionário quando o botão é clicado.

## Section, Card, Tabs e Loading

| Componente | Para que serve |
|---|---|
| `pcp.Section(title, *objects)` | Um grupo com título diretamente sobre o fundo da página. |
| `pcp.Card(title, *objects)` | Um grupo com título numa superfície elevada. |
| `pcp.Tabs(Overview=obj, Detail=obj)` | Separadores que carregam o conteúdo de um separador quando este é selecionado. O separador ativo assume a cor da marca. |
| `pcp.Loading(height=200)` | Um marcador cintilante a mostrar enquanto os dados são carregados. |

## StatusBanner

`pcp.StatusBanner(message, kind="info")` mostra um aviso em linha. `kind` é `error`, `warning`, `success` ou `info`.

## Botões de execução e atualidade

`pcp.run_workflow_button(workflow_id, label=None)` acrescenta um botão que executa um fluxo de trabalho do PlaidCloud como a pessoa que abriu a aplicação, e mostra **Em execução…**, depois **Concluído** ou **Falhou**. Uma falha nomeia os passos que falharam, até cinco. O fluxo de trabalho pertence ao projeto da aplicação, a menos que transmita `project_id`.

`pcp.RunButton(label, start, status)` faz o mesmo para qualquer tarefa. `start` inicia-a e devolve um id de execução; `status(run_id)` devolve `"running"`, `"succeeded"` ou `"failed"`, ou `("failed", reason)` para mostrar um motivo. Ambas são funções normais, como chamadas a uma API REST. O valor `runs` do botão aumenta uma unidade de cada vez que uma execução é bem-sucedida, pelo que uma vista que tenha de ser atualizada depois se associa a ele:

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)` mostra quando uma tabela foi escrita pela última vez, como **Updated 5 min ago**. A idade vai avançando enquanto a página permanece aberta. Transmita `stale_after=datetime.timedelta(hours=24)` para assinalar com um aviso dados mais antigos, e chame `.refresh()` depois de uma execução. Uma tabela cuja data não é possível determinar mostra **Last update unknown**; isso nunca é um erro. `pcp.Freshness(fetch)` faz o mesmo para qualquer origem, em que `fetch` devolve quando os dados mudaram pela última vez.

## Definições guardadas

`pcp.user_state` memoriza as escolhas de cada pessoa entre visitas, para que uma aplicação abra como a pessoa a deixou.

- `pcp.user_state.persist(widget, "region")` restaura o valor guardado no widget e guarda-o a cada alteração. Um valor guardado que o widget já não oferece é ignorado.
- A página escolhida em `nav` é guardada automaticamente.
- Uma chave que começa por `filters.`, como `pcp.user_state.persist(widget, "filters.region")`, contém uma escolha de filtro. O PlaidCloud ajusta-a ao acesso atual às linhas da pessoa sempre que é lida, pelo que um filtro guardado nunca traz de volta valores que a pessoa já não pode ver.
- `pcp.user_state.get(key, default)` e `pcp.user_state.set(key, value)` guardam qualquer outro valor pequeno.

As definições guardadas pertencem a uma pessoa numa aplicação, até 8 KB. As definições nunca são partilhadas entre pessoas. Se não for possível contactar o PlaidCloud quando uma definição é guardada, a aplicação mantém-na até ao fim da sessão.

## Imprimir e guardar como PDF

`pcp.PrintButton()` abre a caixa de diálogo de impressão do navegador, onde o destino pode ser **Guardar como PDF**. A página é impressa com a barra lateral e os controlos ocultos e com a identidade visual do seu projeto aplicada. Cada `DataGrid` imprime a sua página atual inteira, até 1000 linhas, com a linha Total no fim. Uma aplicação escura imprime com a paleta clara.

## Idiomas

O texto do próprio kit, como botões, avisos, a paleta de comandos, a visita guiada, as mensagens de execução e de atualidade e o rodapé da grelha, aparece em inglês, alemão ou francês. O idioma é `?lang=de` ou `?lang=fr` no endereço da página, caso contrário o idioma do navegador. Os números usam os separadores do idioma. Os seus dados, nomes de colunas e quaisquer etiquetas que escreva nunca são traduzidos.

## Orçamentos de desempenho

Um carregamento de página cuja primeira pintura demore mais de 3000 ms, ou que execute uma consulta mais lenta do que 2000 ms, escreve um aviso no registo da aplicação a indicar o que excedeu o limite. Os mesmos valores aparecem no separador **Análises** do [Panel Studio](/pt-pt/guides/panel-apps/studio/#análises). Para definir limites diferentes para uma aplicação, defina estas variáveis de ambiente:

| Variável | Predefinição | Define |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | Milissegundos até à primeira pintura. |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | Milissegundos para uma consulta. |

Um valor que não seja um número inteiro é ignorado e aplica-se o valor predefinido.

## Cores para os seus próprios gráficos

`pcp.series()` devolve a paleta de gráficos do PlaidCloud como uma lista de cores, por ordem. Use-a para que os gráficos que desenha corresponham aos componentes do próprio kit, como o exemplo faz para o gráfico de barras.

## Passos seguintes

- [A API de dados](/pt-pt/guides/panel-apps/data-api/) — filtre, pagine, conte e agregue tabelas do PlaidCloud a partir da sua aplicação.
- [Alertas e resumos](/pt-pt/guides/panel-apps/alerts-and-digests/) — envie alertas de KPI e resumos agendados a partir de uma aplicação.
- [Identidade visual do projeto](/pt-pt/guides/panel-apps/branding/) — defina as suas cores e o logótipo uma só vez para todas as aplicações de um projeto.
