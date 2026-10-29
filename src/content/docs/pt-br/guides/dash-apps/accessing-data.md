---
title: Leitura de dados e do usuário conectado em um aplicativo Dash
description: Conecte um aplicativo Dash ao PlaidCloud como a pessoa que o está visualizando — leia dados do projeto e use a identidade do visualizador para comportamento por usuário e segurança em nível de linha.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/accessing-data.md
---

Um aplicativo Dash pode ler seus dados do PlaidCloud — e faz isso **como a pessoa que o está visualizando**, exatamente como um aplicativo Panel de servidor. Quando alguém abre o aplicativo, o PlaidCloud conecta essa pessoa com o mesmo logon único usado no restante da plataforma, e cada chamada que seu aplicativo faz é executada com **as permissões do próprio visualizador**. Não há conta de serviço compartilhada, e o aplicativo nunca pode ver dados que o visualizador não poderia ver por conta própria.

Os auxiliares ficam em `plaidcloud_dash`, parte da imagem base do Dash:

```python
from plaidcloud_dash import current_user, get_connection
```

## Conectar ao PlaidCloud

Chame `get_connection()` de dentro de um callback do Dash, indicando o projeto cujos dados você quer ler:

```python
from plaidcloud_dash import get_connection

conn = get_connection(project_id="<your-project-id>")
```

Essa é toda a configuração necessária. Você **não** informa token, nome de usuário nem senha — `get_connection()` se autentica automaticamente como o visualizador conectado, usando o token de acesso da sessão atual dele. Encontre o ID do seu projeto na URL do projeto ou na página de configurações dele.

> **Chame-a de dentro de um callback.** `get_connection()` lê o token do visualizador na sessão Flask da solicitação atual, que só está disponível enquanto um callback trata a solicitação desse visualizador. Se você transferir uma chamada bloqueante para uma thread em segundo plano, um pool de threads simples não leva a sessão consigo — leia o token dentro do callback e passe-o explicitamente. Chamar `get_connection()` fora de uma solicitação (ou com a autenticação desativada) gera um `RuntimeError` em vez de devolver silenciosamente uma conexão sem nenhuma identidade por trás.

> **Informe seu projeto no código.** Não há uma configuração de projeto na caixa de diálogo de publicação — um aplicativo Dash lê o projeto que você informar em `get_connection(project_id=...)`, assim como o `PlaidConnection(project_id=...)` de um aplicativo Panel de servidor — consulte [Leitura de dados e do usuário conectado](/pt-br/guides/panel-apps/accessing-data/). Um `get_connection()` simples, sem `project_id`, funciona para um aplicativo que nunca acessa dados de projeto (um que apenas chama `current_user()`, por exemplo); se você chamar uma operação com escopo de projeto nessa conexão sem um ID de projeto real e acessível, ocorre o erro `Project Id has not been set`. (Para ler de mais de um projeto, abra uma conexão por projeto.)

### Ler uma tabela

Com uma conexão, carregue uma tabela em um DataFrame do pandas pelo nome:

```python
df = conn.get_dataframe("Sales Ledger")
```

Como a conexão é o visualizador, isso retorna apenas as linhas que ele tem permissão para ver e gera um erro de permissão se ele não tiver nenhum acesso ao projeto.

> **Leia tabelas pelo nome, sem escrever SQL.** Em um projeto em que um administrador ativou o [Acesso a linhas](/pt-br/administration/access/managing-security-groups-and-assignments/#acesso-a-linhas-e-consultas-que-você-mesmo-escreve), a leitura pelo nome aplica as concessões de linha de cada visualizador, enquanto uma consulta composta pelo próprio aplicativo é recusada para qualquer pessoa que não seja Arquiteto do projeto — não existe uma tabela única para as concessões filtrarem. Ler pelo nome mantém seu aplicativo funcionando nos dois casos.

## Leia em um callback, nunca na importação ou no escopo do processo

Um único processo atende todos os visualizadores. Isolar bem os dados se resume a duas regras:

- **Nunca abra uma conexão nem leia uma tabela no escopo do módulo (no momento da importação).** Seu `app.py` e quaisquer módulos que ele importa são executados **uma vez**, quando o contêiner inicia — antes de qualquer pessoa se conectar. Um `get_connection()` ou `PlaidConnection()` ali não tem visualizador com quem se autenticar e faz o aplicativo falhar na inicialização (a causa mais comum de um loop de falhas de "o aplicativo não iniciou"). Mantenha toda leitura dentro de um callback, onde a solicitação do visualizador — e o token de sessão dele — está presente.

- **Nunca armazene em cache um resultado por visualizador no escopo do módulo ou do processo.** O worker gunicorn com várias threads compartilha um único processo Python entre todos os visualizadores simultâneos, de modo que um DataFrame guardado em uma variável de módulo, em um dicionário global ou em um `lru_cache` fica visível para *todos* os outros visualizadores — as linhas de uma pessoa vazam para a visão de outra. Calcule os dados por visualizador dentro do callback e deixe-os saírem de escopo quando o callback retornar:

  ```python
  # WRONG — a module/process-global cache is shared across all viewers
  _CACHE = {}

  @app.callback(...)
  def _load(n):
      viewer = current_user()
      if viewer not in _CACHE:                      # still process-global; leaks under load
          _CACHE[viewer] = get_connection(project_id="…").get_dataframe("Sales")
      return _CACHE[viewer].to_dict("records")

  # RIGHT — read inside the callback, no shared state
  @app.callback(...)
  def _load(n):
      conn = get_connection(project_id="…")          # this viewer, this request
      return conn.get_dataframe("Sales").to_dict("records")
  ```

### Dados de referência compartilhados

Se vários visualizadores realmente precisam dos *mesmos* dados de referência — uma tabela de consulta, uma lista de produtos —, não tente compartilhá-los por meio de um cache no nível do processo. Conceda essas tabelas aos usuários do aplicativo por meio do [Acesso a linhas / permissões de projeto](/pt-br/administration/access/managing-security-groups-and-assignments/) normais do PlaidCloud e deixe cada visualizador lê-las com o próprio `get_connection()`. Todos recebem as mesmas linhas de referência porque todos têm o mesmo acesso concedido — não porque a leitura de um visualizador foi reaproveitada para outro.

## Identificar o visualizador

Para adaptar o que o aplicativo mostra a **quem o está vendo** — uma saudação personalizada, ocultar uma guia ou segurança em nível de linha —, chame `current_user()`:

```python
from plaidcloud_dash import current_user

viewer = current_user()  # the viewer's identifier
```

`current_user()` retorna o identificador do visualizador conectado — o nome de usuário dele, recorrendo ao e-mail e depois ao ID da conta se não houver declaração de nome de usuário —, extraído do logon verificado, de modo que você pode confiar nele como a identidade da pessoa. Ela nunca gera exceção; chamada com a autenticação desativada ou fora de uma solicitação, retorna uma string vazia.

### Segurança em nível de linha

Combine as duas coisas: leia o visualizador e depois filtre cada consulta por ele. Por exemplo, para mostrar a cada gerente regional apenas a própria região:

```python
from dash import Input, Output
from plaidcloud_dash import current_user, get_connection


@app.callback(Output("sales-table", "children"), Input("load-btn", "n_clicks"))
def _load_my_region(n_clicks):
    viewer = current_user()
    conn = get_connection(project_id="<your-project-id>")

    sales = conn.get_dataframe("Regional Sales")
    mine = sales[sales["manager_email"] == viewer]

    return mine.to_dict("records")
```

Como a conexão já aplica as permissões de projeto do visualizador, essa filtragem é uma moldagem *adicional* sobre o que ele já pode ver — não um substituto para o controle de acesso do próprio PlaidCloud.

## Aplicativos públicos

Se você publicou com **Permitir acesso público**, o aplicativo é servido sem logon, portanto não há visualizador a representar — `current_user()` retorna uma string vazia e `get_connection()` não tem token de sessão com o qual se autenticar, então gera um erro. Limite os aplicativos públicos a dados seguros para qualquer pessoa ou deixe o acesso público desativado, para que os visualizadores se conectem e o modelo por usuário descrito acima se aplique.
