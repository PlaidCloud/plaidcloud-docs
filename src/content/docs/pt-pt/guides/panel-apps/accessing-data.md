---
title: Ler dados e o utilizador com sessão iniciada
description: Ligue uma aplicação Panel de servidor ao PlaidCloud como a pessoa que a está a ver — leia dados do projeto e use a identidade do visualizador para comportamentos por utilizador e segurança ao nível da linha.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/accessing-data.md
---

Uma aplicação Panel de servidor pode ler os seus dados do PlaidCloud — e fá-lo **como a pessoa que a está a ver**. Quando alguém abre a aplicação, o PlaidCloud inicia a sessão dessa pessoa com o mesmo início de sessão único usado no resto da plataforma, e cada chamada feita pela aplicação é executada com **as permissões do próprio visualizador**. Não existe nenhuma conta de serviço partilhada, e a aplicação nunca pode ver dados que o visualizador não conseguiria ver por si.

Isto aplica-se apenas às aplicações de **Servidor**. As aplicações WASM são executadas inteiramente no navegador e não têm ligação do lado do servidor.

## Ligar ao PlaidCloud

Use `PlaidConnection`, indicando o projeto cujos dados pretende ler:

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection(project_id="<your-project-id>")
```

Esta é toda a configuração de que precisa. **Não** fornece um token, nome de utilizador ou palavra-passe — a ligação autentica-se automaticamente como o visualizador com sessão iniciada. Encontre o id do seu projeto no URL do projeto ou na respetiva página de definições.

> **Atribua um projeto à aplicação.** Uma aplicação publicada com um projeto no seletor **Projeto** lê esse projeto por predefinição, e a [Data API](/pt-pt/guides/panel-apps/data-api/) usa-o para `table("name")`. Para uma aplicação sem projeto, passe `project_id` a `PlaidConnection` como acima; um `PlaidConnection()` simples não tem nenhum projeto para ler.

### Ler uma tabela

Com uma ligação, carregue uma tabela para um DataFrame do pandas pelo nome:

```python
df = conn.get_dataframe("Sales Ledger")
```

Como a ligação é o visualizador, isto devolve apenas as linhas que o visualizador pode ver, e gera um erro de permissão se não tiver qualquer acesso ao projeto.

> **Leia as tabelas pelo nome, não escrevendo SQL.** Num projeto em que um administrador ativou o [Acesso a linhas](/pt-pt/administration/access/managing-security-groups-and-assignments/#acesso-a-linhas-e-consultas-que-escreve-por-si), a leitura pelo nome aplica as concessões de linhas de cada visualizador, enquanto uma consulta composta pela própria aplicação é recusada para quem não seja Arquiteto do projeto — não existe uma única tabela que as concessões possam filtrar. Ler pelo nome mantém a sua aplicação a funcionar em ambos os casos.

## Identificar o visualizador

Para adaptar o que a aplicação mostra a **quem a está a ver** — uma saudação personalizada, ocultar um separador ou segurança ao nível da linha — leia o utilizador com sessão iniciada a partir do Panel:

```python
import panel as pn

viewer = pn.state.user          # the viewer's email address
token  = pn.state.access_token  # their JWT, if you need claims or group membership
```

`pn.state.user` é o correio eletrónico do visualizador, obtido a partir do seu início de sessão verificado — pode confiar nele como a identidade da pessoa. `pn.state.access_token` é o respetivo token de acesso em bruto, útil se precisar de descodificar declarações de grupo ou de função para regras mais granulares.

### Segurança ao nível da linha

Combine os dois: leia o visualizador e depois filtre cada consulta por ele. Por exemplo, para mostrar a cada gestor regional apenas a sua própria região:

```python
import panel as pn
from plaidcloud.utilities.connect import PlaidConnection

pn.extension()

viewer = pn.state.user
conn = PlaidConnection(project_id="<your-project-id>")

sales = conn.get_dataframe("Regional Sales")
mine = sales[sales["manager_email"] == viewer]

pn.Column(
    f"# Sales for {viewer}",
    pn.pane.DataFrame(mine, index=False),
).servable()
```

Como a ligação já impõe as permissões do projeto do visualizador, esta filtragem é uma modelação *adicional* sobre aquilo que a pessoa pode ver — não substitui o controlo de acesso do próprio PlaidCloud.

> **Faça as chamadas de dados a partir do fluxo principal da aplicação.** O visualizador com sessão iniciada está disponível enquanto o código da aplicação é executado para a sua sessão (que é onde o trabalho de `.servable()` acontece). Se enviar uma chamada bloqueante para uma thread em segundo plano, use `asyncio.to_thread` — um conjunto de threads simples não transporta a identidade da sessão, e a ligação falhará de forma explícita em vez de ler os dados errados.

## Aplicações públicas

Se publicou com **Permitir acesso público**, a aplicação é disponibilizada sem início de sessão, pelo que não há nenhum visualizador a representar — `pn.state.user` está vazio e um `PlaidConnection()` não tem ninguém para autenticar. Limite as aplicações públicas a dados que sejam seguros para qualquer pessoa, ou deixe o acesso público desativado para que os visualizadores iniciem sessão e se aplique o modelo por utilizador descrito acima.
