---
title: Ler dados e o utilizador com sessão iniciada numa aplicação Dash
description: Ligue uma aplicação Dash ao PlaidCloud como a pessoa que a está a ver — leia dados do projeto e use a identidade do leitor para comportamentos por utilizador e segurança ao nível da linha.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/accessing-data.md
---

Uma aplicação Dash pode ler os seus dados do PlaidCloud — e fá-lo **como a pessoa que a está a ver**, tal como uma aplicação Panel de servidor. Quando alguém abre a aplicação, o PlaidCloud inicia a sessão dessa pessoa com o mesmo início de sessão único que o resto da plataforma usa, e cada chamada feita pela aplicação é executada com **as permissões do próprio leitor**. Não existe uma conta de serviço partilhada, e a aplicação nunca pode ver dados que o leitor não pudesse ver por si próprio.

Os auxiliares encontram-se em `plaidcloud_dash`, que faz parte da imagem base do Dash:

```python
from plaidcloud_dash import current_user, get_connection
```

## Ligar ao PlaidCloud

Chame `get_connection()` a partir de dentro de uma função de retorno (callback) do Dash, indicando o projeto cujos dados pretende ler:

```python
from plaidcloud_dash import get_connection

conn = get_connection(project_id="<your-project-id>")
```

Esta é toda a configuração necessária. **Não** é necessário fornecer um token, um nome de utilizador nem uma palavra-passe — `get_connection()` autentica-se automaticamente como o leitor com sessão iniciada, usando o token de acesso da sua sessão atual. O ID do projeto encontra-se no URL do projeto ou na respetiva página de definições.

> **Chame-a a partir de dentro de um callback.** `get_connection()` lê o token do leitor a partir da sessão Flask do pedido atual, que só está disponível enquanto um callback trata do pedido desse leitor. Se enviar uma chamada bloqueante para uma thread em segundo plano, um conjunto de threads simples não transporta a sessão — leia o token dentro do callback e passe-o explicitamente. Chamar `get_connection()` fora de um pedido (ou com a autenticação desativada) gera um `RuntimeError` em vez de devolver silenciosamente uma ligação sem identidade associada.

> **Indique o projeto no código.** Não existe nenhuma definição de projeto na caixa de diálogo de publicação — uma aplicação Dash lê o projeto que indicar em `get_connection(project_id=...)`, tal como o `PlaidConnection(project_id=...)` de uma aplicação Panel de servidor — consulte [Ler dados e o utilizador com sessão iniciada](/pt-pt/guides/panel-apps/accessing-data/). Um `get_connection()` simples, sem `project_id`, é adequado para uma aplicação que nunca acede a dados de projeto (uma que apenas chama `current_user()`, por exemplo); se chamar uma operação ao nível do projeto nessa ligação sem um ID de projeto real e acessível, é gerado o erro `Project Id has not been set`. (Para ler de mais do que um projeto, abra uma ligação por projeto.)

### Ler uma tabela

Com uma ligação, carregue uma tabela para um DataFrame do pandas pelo nome:

```python
df = conn.get_dataframe("Sales Ledger")
```

Como a ligação é o leitor, isto devolve apenas as linhas que o leitor pode ver e gera um erro de permissão se não tiver qualquer acesso ao projeto.

> **Leia as tabelas pelo nome, não escrevendo SQL.** Num projeto em que um administrador tenha ativado o [Acesso a linhas](/pt-pt/administration/access/managing-security-groups-and-assignments/#acesso-a-linhas-e-consultas-que-escreve-por-si), a leitura pelo nome aplica as concessões de linhas de cada leitor, ao passo que uma consulta composta pela própria aplicação é recusada para qualquer pessoa que não seja Arquiteto do projeto — não existe uma única tabela sobre a qual as concessões possam filtrar. Ler pelo nome mantém a aplicação a funcionar em ambos os casos.

## Ler num callback, nunca na importação nem ao nível do processo

Um único processo serve todos os leitores. Garantir o isolamento correto dos dados resume-se a duas regras:

- **Nunca abra uma ligação nem leia uma tabela ao nível do módulo (no momento da importação).** O seu `app.py` e quaisquer módulos que importe são executados **uma vez**, quando o contentor arranca — antes de alguém ter iniciado sessão. Um `get_connection()` ou `PlaidConnection()` aí não tem nenhum leitor com que se autenticar e faz a aplicação falhar no arranque (esta é a causa mais comum de um ciclo de falhas do tipo "a aplicação não arrancou"). Mantenha todas as leituras dentro de um callback, onde o pedido do leitor — e o respetivo token de sessão — está presente.

- **Nunca guarde em cache um resultado por leitor ao nível do módulo ou do processo.** O worker gunicorn com várias threads partilha um único processo Python por todos os leitores em simultâneo, pelo que um DataFrame guardado numa variável ao nível do módulo, num dicionário global ou num `lru_cache` fica visível para *todos* os outros leitores — as linhas de uma pessoa passam para a vista de outra. Calcule os dados por leitor dentro do callback e deixe-os sair do âmbito quando o callback terminar:

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

### Dados de referência partilhados

Se vários leitores precisarem realmente dos *mesmos* dados de referência — uma tabela de consulta, uma lista de produtos —, não tente partilhá-los através de uma cache ao nível do processo. Conceda essas tabelas aos utilizadores da aplicação através do [Acesso a linhas / permissões de projeto](/pt-pt/administration/access/managing-security-groups-and-assignments/) habituais do PlaidCloud e deixe cada leitor lê-las com o seu próprio `get_connection()`. Todos obtêm as mesmas linhas de referência porque todos têm o mesmo acesso — e não porque a leitura de um leitor seja reutilizada para outro.

## Identificar o leitor

Para adaptar o que a aplicação mostra a **quem a está a ver** — uma saudação personalizada, ocultar um separador ou segurança ao nível da linha —, chame `current_user()`:

```python
from plaidcloud_dash import current_user

viewer = current_user()  # the viewer's identifier
```

`current_user()` devolve o identificador do leitor com sessão iniciada — o nome de utilizador, recorrendo ao e-mail e depois ao ID da conta se não existir uma indicação de nome de utilizador —, obtido a partir do seu início de sessão verificado, pelo que pode confiar nele como a sua identidade. Nunca gera erros; se for chamado com a autenticação desativada ou fora de um pedido, devolve uma cadeia vazia.

### Segurança ao nível da linha

Combine as duas coisas: leia o leitor e filtre cada consulta por ele. Por exemplo, para mostrar a cada gestor regional apenas a sua própria região:

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

Como a ligação já impõe as permissões de projeto do leitor, esta filtragem é uma modelação *adicional* sobre aquilo que o leitor pode ver — e não um substituto do controlo de acesso do próprio PlaidCloud.

## Aplicações públicas

Se publicou com **Permitir acesso público**, a aplicação é servida sem início de sessão, pelo que não existe nenhum leitor como quem agir — `current_user()` devolve uma cadeia vazia e `get_connection()` não tem nenhum token de sessão com que se autenticar, pelo que gera um erro. Limite as aplicações públicas a dados que sejam seguros para qualquer pessoa ou deixe o acesso público desativado, para que os leitores iniciem sessão e se aplique o modelo por utilizador descrito acima.
