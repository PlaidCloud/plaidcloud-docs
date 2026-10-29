---
title: Lendo dados e o usuário conectado
description: Conecte um aplicativo Panel do lado do servidor ao PlaidCloud como a pessoa que o está visualizando — leia dados do projeto e use a identidade do visualizador para comportamento por usuário e segurança em nível de linha.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/accessing-data.md
---

Um aplicativo Panel de servidor pode ler os seus dados do PlaidCloud — e faz isso **como a pessoa que o está visualizando**. Quando alguém abre o aplicativo, o PlaidCloud o conecta com o mesmo logon único que o restante da plataforma usa, e cada chamada feita pelo seu aplicativo é executada com **as permissões do próprio visualizador**. Não existe conta de serviço compartilhada, e o aplicativo nunca pode ver dados que o visualizador não poderia ver por conta própria.

Isso se aplica somente a aplicativos do tipo **Servidor**. Aplicativos WASM são executados inteiramente no navegador e não têm conexão do lado do servidor.

## Conectar ao PlaidCloud

Use `PlaidConnection`, informando o projeto cujos dados você quer ler:

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection(project_id="<your-project-id>")
```

Essa é toda a configuração necessária. Você **não** informa token, nome de usuário nem senha — a conexão se autentica automaticamente como o visualizador conectado. Encontre o ID do seu projeto na URL do projeto ou na página de configurações dele.

> **Informe um projeto.** Um aplicativo publicado com um projeto no seletor **Projeto** lê esse projeto por padrão, e a [Data API](/pt-br/guides/panel-apps/data-api/) o usa para `table("name")`. Para um aplicativo sem projeto, passe `project_id` para `PlaidConnection` como acima; um `PlaidConnection()` sem argumentos não tem projeto para ler.

### Ler uma tabela

Com uma conexão, carregue uma tabela em um DataFrame do pandas pelo nome:

```python
df = conn.get_dataframe("Sales Ledger")
```

Como a conexão é o visualizador, isso retorna somente as linhas que ele tem permissão para ver e gera um erro de permissão se ele não tiver nenhum acesso ao projeto.

> **Leia tabelas pelo nome, sem escrever SQL.** Em um projeto no qual um administrador ativou o [Acesso a linhas](/pt-br/administration/access/managing-security-groups-and-assignments/#acesso-a-linhas-e-consultas-que-você-mesmo-escreve), a leitura pelo nome aplica as concessões de linha de cada visualizador, enquanto uma consulta composta pelo próprio aplicativo é recusada para qualquer pessoa que não seja Arquiteto do projeto — não existe uma única tabela para as concessões filtrarem. Ler pelo nome mantém seu aplicativo funcionando nos dois casos.

## Identificar o visualizador

Para adaptar o que o aplicativo mostra a **quem está olhando** — uma saudação personalizada, ocultar uma guia ou segurança em nível de linha — leia o usuário conectado pelo Panel:

```python
import panel as pn

viewer = pn.state.user          # the viewer's email address
token  = pn.state.access_token  # their JWT, if you need claims or group membership
```

`pn.state.user` é o e-mail do visualizador, obtido do logon verificado dele — você pode confiar nele como identidade. `pn.state.access_token` é o token de acesso bruto, útil se você precisar decodificar declarações de grupo ou função para regras mais refinadas.

### Segurança em nível de linha

Combine os dois: leia o visualizador e filtre cada consulta por ele. Por exemplo, para mostrar a cada gerente regional apenas a própria região:

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

Como a conexão já aplica as permissões de projeto do visualizador, essa filtragem é uma moldagem *adicional* sobre o que ele tem permissão para ver — não um substituto para o controle de acesso do próprio PlaidCloud.

> **Faça as chamadas de dados a partir do fluxo principal do aplicativo.** O visualizador conectado está disponível enquanto o código do seu aplicativo é executado para a sessão dele (que é onde o trabalho de `.servable()` acontece). Se você enviar uma chamada bloqueante para uma thread em segundo plano, use `asyncio.to_thread` — um pool de threads simples não carrega a identidade da sessão, e a conexão falhará de forma explícita em vez de ler os dados errados.

## Aplicativos públicos

Se você publicou com **Permitir acesso público**, o aplicativo é servido sem logon, então não há visualizador para representar — `pn.state.user` fica vazio e um `PlaidConnection()` não tem ninguém para autenticar. Limite os aplicativos públicos a dados que sejam seguros para qualquer pessoa, ou deixe o acesso público desativado para que os visualizadores façam logon e o modelo por usuário descrito acima se aplique.
