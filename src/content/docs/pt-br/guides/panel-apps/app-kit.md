---
title: O Panel App Kit
description: Crie aplicativos Panel com a aparência do PlaidCloud usando o kit plaidcloud_panel — a estrutura App, a paleta de comandos, FilterBar, KpiCard, DataGrid, Chart, Form, botões de execução, configurações salvas, impressão e traduções, em modo claro e escuro.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/app-kit.md
---

Todo aplicativo Panel de servidor tem o kit `plaidcloud_panel` instalado. Ele dá ao seu aplicativo a aparência do PlaidCloud — as mesmas cores, tipografia e espaçamento do restante da plataforma, em modo claro e escuro — e um conjunto de componentes prontos para as telas de que a maioria dos aplicativos precisa: filtros, números de destaque, uma grade de dados grande, gráficos e formulários. Seu aplicativo adota automaticamente a [identidade visual do projeto](/pt-br/guides/panel-apps/branding/).

```python
import plaidcloud_panel as pcp
```

Importar o kit também aplica a aparência do PlaidCloud aos gráficos Plotly e Matplotlib.

## Comece a partir de um modelo

O kit inclui um comando que escreve um aplicativo inicial funcional. Execute-o em qualquer pasta e depois edite os nomes de tabela e de colunas:

```bash
plaidcloud-panel new --layout dashboard --title "Sales" --table sales --filters region,year --measure amount
```

| Opção | O que faz |
|---|---|
| `--layout dashboard` | Filtros na barra lateral, dois números de destaque e um gráfico. |
| `--layout explorer` | Filtros na barra lateral, uma contagem de linhas e uma tabela de linhas. |
| `--table` | A tabela do PlaidCloud que o aplicativo lê. |
| `--filters` | Colunas separadas por vírgula para filtrar. A primeira controla o gráfico. |
| `--measure` | A coluna numérica a totalizar. |
| `--dir` | Onde gravar `app.py` e `requirements.txt`. O padrão é a pasta atual. |

O comando é interrompido sem gravar nada se `app.py` já existir. Faça commit dos dois arquivos no seu repositório e [publique o aplicativo](/pt-br/guides/panel-apps/creating/).

## Um aplicativo de exemplo

Este aplicativo filtra uma tabela de vendas por região e ano, mostra dois números de destaque, um gráfico e uma grade paginada com as linhas correspondentes. A grade mostra valores com separadores de milhar e margens como porcentagens. Cada elemento acompanha os filtros.

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

O padrão é o mesmo em todo aplicativo do kit: crie um `FilterBar` sobre uma tabela e depois vincule cada visão a `bar.table`. Uma visão que não está vinculada a `bar.table` (ou a um widget) nunca é atualizada quando os filtros mudam.

## App

`pcp.App(title, nav=None, *, main=None, sidebar=None, theme_toggle=True, theme=None, commands=None, tour=None)` constrói a estrutura do aplicativo: um cabeçalho com o título, o logotipo do projeto e o usuário conectado, uma barra lateral e uma área principal. Chame `.servable()` no resultado.

- **Navegação** — passe `nav=[("Overview", overview_page), ("Detail", detail_page)]` para obter um menu de páginas no topo da barra lateral. Cada página é um objeto Panel ou uma função que retorna um. As funções são executadas quando a página é selecionada.
- **Tema** — o aplicativo abre no tema claro. Passe `theme="dark"` para abrir no tema escuro ou adicione `?theme=dark` à URL. Com `theme_toggle=True` (o padrão), o cabeçalho traz uma chave claro/escuro.
- **Identidade visual** — o aplicativo lê as cores da marca e o logotipo do projeto quando uma sessão começa. Um projeto sem identidade visual recebe os padrões do PlaidCloud.
- **Paleta de comandos** — pressione Ctrl-K (Cmd-K no Mac) para pesquisar e executar comandos. Cada página em `nav` é listada como **Ir para** o nome da página, e `commands={"Refresh data": refresh}` adiciona suas próprias entradas, cada uma com um rótulo e uma função sem argumentos. Escolha uma entrada e o aplicativo a executa.
- **Tour de primeira execução** — `tour=[("Filters", "Narrow the data here."), ("Grid", "Sort and group the rows.")]` mostra uma breve introdução passo a passo, cada passo com um título e uma linha de texto. Ela aparece no topo da página até você concluí-la ou ignorá-la, e não é mostrada novamente.
- **Qualquer outra coisa** — os demais argumentos nomeados são repassados ao `FastListTemplate` do Panel.

## FilterBar

`pcp.FilterBar(table, "region", "year", amount=pn.widgets.IntInput(name="Amount"))` cria uma caixa de múltipla escolha pesquisável para cada coluna que você nomear, listando os valores distintos dessa coluna (até 1.000, com um aviso quando a lista é cortada). Uma caixa mostra **Todos** quando nada está selecionado. Passe seus próprios widgets pelo nome da coluna para qualquer outro caso.

- `bar.table` é a tabela restringida pelas seleções atuais. Um widget em branco não restringe os dados.
- As seleções são salvas na URL da página (`?region=EU`), então uma visão filtrada pode ser compartilhada como link.

## KpiCard

`pcp.KpiCard(label, source, column=None, fn="sum", fmt="{:,.0f}", drill_to=None)` mostra um número de destaque. `fn` é `sum`, `count`, `avg`, `min` ou `max`, calculado sobre a tabela inteira pelo servidor. Sem `column`, ele mostra a contagem de linhas. Passe `bar.table` como origem para que o número acompanhe os filtros.

Passe `drill_to=grid`, um `DataGrid`, para adicionar um botão **View rows** abaixo do número. Escolhê-lo aponta a grade para a tabela do próprio cartão, de modo que a grade lista as linhas por trás do número.

## DataGrid

`pcp.DataGrid(source, key="id", totals={"amount": "sum"})` é uma visão de tabela para dados de qualquer tamanho. Somente a página atual é enviada ao navegador; paginação, ordenação, totais e exportação são todos executados no servidor.

- **Paginação** — 200, 500 ou 1.000 linhas por página, com botões Anterior e Próxima e um contador de linhas.
- **Ordenação** — clique no cabeçalho de uma coluna. A ordenação se aplica à tabela inteira, não apenas à página visível.
- **Totais** — `totals` associa uma coluna a `sum`, `count`, `avg`, `min` ou `max`. O servidor calcula cada um sobre todas as linhas correspondentes e fixa o resultado como a última linha da grade.
- **Exportação** — os botões **CSV** e **XLSX** baixam todas as linhas correspondentes na ordenação atual, até `export_cap` linhas (100.000 por padrão). Quando a tabela é maior, um aviso orienta você a restringir os filtros. As células de texto que começam com `=`, `+`, `-` ou `@` recebem um apóstrofo como prefixo para que uma planilha as leia como texto.
- **Formatos de número** — `formats={"margin": "0.0%", "amount": "0,0"}` define um formato de exibição por coluna, usando strings de formato do [numbro](https://numbrojs.com/format.html). Um formato `%` multiplica por 100. A linha Total usa o mesmo formato. Colunas de ponto flutuante sem formato mostram até duas casas decimais com separadores de milhar. **Copiar**, **CSV** e **XLSX** mantêm os valores brutos.
- **Chave** — `key` é a coluna, ou a lista de colunas, que identifica uma linha de forma exclusiva. Sempre informe-a. Veja [Paginação estável](/pt-br/guides/panel-apps/data-api/#paginação-estável).

- **Agrupar por** — `group_by=["region"]` mostra uma linha por grupo, com as medidas de `totals` e uma contagem `rows`, tudo calculado pelo servidor, e uma linha **Total** sobre todas as linhas correspondentes. Passe `groupable=["region", "year"]` para adicionar um seletor **Agrupar por** para que os visualizadores escolham as colunas. Uma grade mostra até 1.000 grupos e avisa quando cortou a lista. As linhas de grupo não têm links **Abrir**.
- **Formatação condicional** — `rules` colore células por valor. Cada regra nomeia uma `column`, um `op` (`>`, `>=`, `<`, `<=`, `==`, `!=` ou `between`), um `value` (`[low, high]` para `between`) e um `token` (`success`, `warning`, `error` ou `info`), por exemplo `{"column": "margin", "op": "<", "value": 0, "token": "error"}`. A linha Total nunca é colorida.
- **Copiar** — o botão **Copiar** coloca na área de transferência a página atual, com as colunas visíveis e a linha Total, como texto separado por tabulações que pode ser colado no Excel.
- **Open in PlaidCloud** — quando a origem é uma tabela do PlaidCloud, um link **Open in PlaidCloud** abre essa tabela.
- **Layout de colunas salvo** — `layout_key="orders"` adiciona seletores **Colunas** e **Pinned** para escolher e ordenar colunas e fixar algumas delas. A escolha de cada visualizador é salva com esse nome e restaurada na próxima vez que ele abrir o aplicativo.
- **Links de linha** — `row_link` é uma função que recebe uma linha, como um dicionário, e retorna um endereço web, ou `None` para nenhum link. A grade adiciona uma coluna **Abrir** com um link em cada linha que tiver um. Somente endereços `http` e `https` e caminhos no mesmo site recebem link.
- **Atualizar** — `grid.refresh()` consulta a mesma origem novamente e mantém a página, a ordenação e o agrupamento. Chame-o depois que uma [execução](#botões-de-execução-e-atualidade) terminar de gravar a tabela.

`source` é um nome de tabela ou uma tabela da [Data API](/pt-br/guides/panel-apps/data-api/). Para refiltrar uma grade, defina `grid.source` como uma tabela filtrada ou crie uma nova grade a partir de `bar.table`, como faz o exemplo.

A grade está sujeita à segurança em nível de linha do visualizador: ela lê pela conexão do próprio visualizador.

## Chart

`pcp.Chart(obj, title=None, height=320)` coloca um gráfico em um cartão com título. `obj` pode ser uma figura Bokeh, um gráfico hvPlot ou HoloViews, uma figura Plotly, uma figura Matplotlib ou um `pn.bind(...)` que retorne qualquer um deles. Os eixos numéricos das figuras Bokeh mostram separadores de milhar, então 800000 aparece como 800.000.

## Form

`pcp.Form(*widgets, on_submit=save, submit="Save")` organiza widgets de entrada como um único formulário com um botão de envio. `form.values()` retorna `{widget.name: widget.value}` para cada widget nomeado, e `on_submit` recebe esse dicionário quando o botão é clicado.

## Section, Card, Tabs e Loading

| Componente | Use para |
|---|---|
| `pcp.Section(title, *objects)` | Um grupo com título diretamente no fundo da página. |
| `pcp.Card(title, *objects)` | Um grupo com título em uma superfície elevada. |
| `pcp.Tabs(Overview=obj, Detail=obj)` | Guias que carregam o conteúdo de uma guia quando ela é selecionada. A guia ativa assume a cor da marca. |
| `pcp.Loading(height=200)` | Um espaço reservado cintilante para exibir enquanto os dados carregam. |

## StatusBanner

`pcp.StatusBanner(message, kind="info")` mostra um aviso em linha. `kind` é `error`, `warning`, `success` ou `info`.

## Botões de execução e atualidade

`pcp.run_workflow_button(workflow_id, label=None)` adiciona um botão que executa um fluxo de trabalho do PlaidCloud como a pessoa que abriu o aplicativo e mostra **Em execução…**, depois **Concluído** ou **Falhou**. Uma falha nomeia as etapas que falharam, até cinco. O fluxo de trabalho pertence ao projeto do aplicativo, a menos que você passe `project_id`.

`pcp.RunButton(label, start, status)` faz o mesmo para qualquer tarefa. `start` a inicia e retorna um ID de execução; `status(run_id)` retorna `"running"`, `"succeeded"` ou `"failed"`, ou `("failed", reason)` para mostrar um motivo. Ambas são funções comuns, como chamadas a uma API REST. O valor `runs` do botão aumenta em um cada vez que uma execução é bem-sucedida, então uma visão que precisa ser atualizada depois se vincula a ele:

```python
run = pcp.run_workflow_button("monthly_load")
grid = pcp.DataGrid("sales", key="id")
run.param.watch(lambda _: grid.refresh(), "runs")
```

`pcp.table_freshness(table_id)` mostra quando uma tabela foi gravada pela última vez, como **Updated 5 min ago**. A idade continua avançando enquanto a página permanece aberta. Passe `stale_after=datetime.timedelta(hours=24)` para sinalizar dados mais antigos com um aviso e chame `.refresh()` depois de uma execução. Uma tabela cuja data não pode ser determinada mostra **Last update unknown**; isso nunca é um erro. `pcp.Freshness(fetch)` faz o mesmo para qualquer origem, em que `fetch` retorna quando os dados mudaram pela última vez.

## Configurações salvas

`pcp.user_state` lembra as escolhas de cada pessoa entre visitas, para que um aplicativo abra do jeito que ela o deixou.

- `pcp.user_state.persist(widget, "region")` restaura o valor salvo no widget e o salva a cada alteração. Um valor salvo que o widget não oferece mais é ignorado.
- A página escolhida em `nav` é salva automaticamente.
- Uma chave que começa com `filters.`, como `pcp.user_state.persist(widget, "filters.region")`, guarda uma escolha de filtro. O PlaidCloud a ajusta ao acesso atual às linhas da pessoa sempre que é lida, então um filtro salvo nunca traz de volta valores que ela não pode mais ver.
- `pcp.user_state.get(key, default)` e `pcp.user_state.set(key, value)` salvam qualquer outro valor pequeno.

As configurações salvas pertencem a uma pessoa em um aplicativo, até 8 KB. As configurações nunca são compartilhadas entre pessoas. Se o PlaidCloud não puder ser alcançado quando uma configuração for salva, o aplicativo a mantém até o fim da sessão.

## Impressão e Salvar como PDF

`pcp.PrintButton()` abre a caixa de diálogo de impressão do navegador, em que o destino pode ser **Salvar como PDF**. A página é impressa com a barra lateral e os controles ocultos e com a identidade visual do seu projeto aplicada. Cada `DataGrid` imprime toda a sua página atual, até 1.000 linhas, com a linha Total por último. Um aplicativo escuro é impresso com a paleta clara.

## Idiomas

O texto próprio do kit, como botões, avisos, a paleta de comandos, o tour, as mensagens de execução e atualidade e o rodapé da grade, aparece em inglês, alemão ou francês. O idioma é `?lang=de` ou `?lang=fr` no endereço da página; caso contrário, é o idioma do navegador. Os números usam os separadores do idioma. Seus dados, nomes de colunas e quaisquer rótulos que você escrever nunca são traduzidos.

## Orçamentos de desempenho

Um carregamento de página cuja primeira renderização leva mais de 3.000 ms, ou que executa uma consulta mais lenta que 2.000 ms, grava um aviso no log do aplicativo nomeando o que ultrapassou o limite. Os mesmos valores aparecem na guia **Insights** no [Panel Studio](/pt-br/guides/panel-apps/studio/#insights). Para definir limites diferentes para um aplicativo, defina estas variáveis de ambiente:

| Variável | Padrão | Define |
|---|---|---|
| `PLAID_PANEL_BUDGET_FIRST_PAINT_MS` | `3000` | Milissegundos até a primeira renderização. |
| `PLAID_PANEL_BUDGET_QUERY_MS` | `2000` | Milissegundos para uma consulta. |

Um valor que não seja um número inteiro é ignorado, e o padrão se aplica.

## Cores para os seus próprios gráficos

`pcp.series()` retorna a paleta de gráficos do PlaidCloud como uma lista de cores, em ordem. Use-a para que os gráficos que você desenha correspondam aos componentes do próprio kit, como o exemplo faz no gráfico de barras.

## Próximas etapas

- [A Data API](/pt-br/guides/panel-apps/data-api/) — filtre, pagine, conte e agregue tabelas do PlaidCloud a partir do seu aplicativo.
- [Alertas e resumos](/pt-br/guides/panel-apps/alerts-and-digests/) — envie alertas de KPI e resumos agendados a partir de um aplicativo.
- [Identidade visual do projeto](/pt-br/guides/panel-apps/branding/) — defina suas cores e logotipo uma vez para todos os aplicativos de um projeto.
