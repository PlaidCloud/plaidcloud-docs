---
title: Aplicações Dash
description: Crie e implemente aplicações de dados Plotly Dash do lado do servidor no PlaidCloud — publicadas a partir de um repositório Git e disponibilizadas com autenticação por utilizador e escala até zero, em paridade com as aplicações Panel de servidor.
sidebar:
  label: Aplicações Dash
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/index.md
---

As aplicações Dash permitem-lhe publicar aplicações interativas [Plotly Dash](https://dash.plotly.com/) — callbacks, gráficos e grelhas de dados (`dash-ag-grid`, `dash-mantine-components`) — diretamente a partir do PlaidCloud. Gere-as no ecrã **As minhas aplicações Panel**, juntamente com as suas aplicações Panel, onde cada linha mostra o respetivo tempo de execução, estado da compilação e URL.

## Onde o Dash se enquadra

Uma aplicação Dash é alojada exatamente como uma **aplicação Panel de servidor**: aponta o PlaidCloud para um ramo de um repositório Git, este compila o código num contentor, e o contentor fica em repouso com zero réplicas, acorda no primeiro pedido, serve e volta a reduzir para zero quando está inativo. Não existe um tempo de execução "WASM" separado para o Dash — todas as aplicações Dash são aplicações de servidor.

Opte por uma aplicação Dash quando a sua aplicação for escrita com Plotly Dash em vez de HoloViz Panel — por exemplo, uma base de código Dash existente ou uma equipa que prefira o modelo de callbacks do Dash e o ecossistema `dash-ag-grid` / `dash-mantine-components`. Se está a começar de raiz e não tem uma preferência, consulte [Aplicações Panel](/pt-pt/guides/panel-apps/) para conhecer a alternativa.

Tudo o que uma aplicação Panel de servidor obtém, uma aplicação Dash também obtém:

- **Identidade por utilizador.** Cada leitor inicia sessão com o início de sessão único da plataforma, e cada chamada que a aplicação faz para ler dados é executada como *esse leitor* — o mesmo modelo de [Ler dados e o utilizador com sessão iniciada](/pt-pt/guides/panel-apps/accessing-data/), usando a API de auxiliares própria do Dash. Consulte [Ler dados e o utilizador com sessão iniciada numa aplicação Dash](/pt-pt/guides/dash-apps/accessing-data/).
- **Escala até zero.** A aplicação fica em repouso com zero réplicas após a janela de inatividade configurada e acorda no pedido seguinte, com um breve ecrã de carregamento do PlaidCloud durante o arranque a frio — consulte [Utilizar uma aplicação Dash](/pt-pt/guides/dash-apps/using/#abrir-uma-aplicação-dash).
- **Recompilações automáticas.** Cada envio para o ramo ligado recompila e volta a implementar a aplicação.
- **Registos de execução e de compilação**, cada um identificado com o leitor cuja sessão produziu uma linha.

Existem duas coisas que uma aplicação Dash **não** tem, ambas por desenho e ambas em linha com o que uma aplicação Panel também não tem:

- **Nenhuma definição de design/temas.** A opção **Design** na caixa de diálogo de publicação do Panel (FAST vs. predefinido) é específica do Panel — as aplicações Dash definem o seu estilo inteiramente através dos componentes que escolher (`dash-mantine-components`, CSS personalizado, etc.), pelo que o formulário de publicação não tem um campo equivalente.
- **Nenhuma lista de acesso por aplicação.** O acesso é a porta de SSO da área de trabalho — qualquer pessoa com sessão iniciada no seu inquilino pode abrir a aplicação (ou, se ativar **Permitir acesso público**, qualquer pessoa). Não existe uma camada de ACL separada por aplicação para nenhum dos tipos de aplicação.

## Contrato da aplicação

O ficheiro de entrada de uma aplicação Dash tem de se chamar `app.py` e tem de expor um `server` — esse é todo o contrato:

```python
from dash import Dash

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you
```

- **Dê ao ficheiro o nome `app.py`.** O iniciador do PlaidCloud importa a sua aplicação como o módulo `app` e lê o respetivo objeto `server`, pelo que, seja qual for o caminho que definir em **Ponto de entrada** (raiz do repositório ou uma subpasta), o ficheiro nesse caminho tem de se chamar `app.py`.
- **Exponha `server = app.server`** ao nível do módulo. É o objeto que a plataforma importa.
- **Não precisa de configurar o início de sessão.** A plataforma protege automaticamente cada pedido com início de sessão único por utilizador — não chame `init_auth` nem importe `plaidcloud_dash` apenas para obter a identidade. (Uma aplicação mais antiga que *chame* `plaidcloud_dash.init_auth(server, url_base_pathname=os.environ["DASH_URL_BASE_PATHNAME"])` continua a funcionar sem alterações — essa chamada é idempotente, pelo que coexiste com a configuração da própria plataforma.)
- **Não defina `requests_pathname_prefix` nem `url_base_pathname` em `Dash(__name__)`.** Cada aplicação Dash é servida sob um prefixo de URL obrigatório (`/serve/<slug>/`), e a plataforma define-o por si através da variável de ambiente `DASH_URL_BASE_PATHNAME` — que é a variável de configuração nativa do próprio Dash, lida antes de qualquer argumento do construtor. Passar também o prefixo explicitamente entra em conflito com a configuração do Dash e a aplicação não arranca.
- **`Entry Point` pode apontar para uma subpasta.** Antes de arrancar a aplicação, o anfitrião define o diretório de trabalho do contentor como a pasta do próprio ficheiro de entrada — pelo que as importações de ficheiros irmãos na mesma pasta (`import data`) e os caminhos de ficheiros relativos na aplicação são resolvidos em relação a essa pasta, tal como ao executar `python app.py` a partir de dentro dela.
- **Não leia dados no momento da importação.** Faça as leituras do PlaidCloud dentro de callbacks, não ao nível do módulo — consulte [Ler dados e o utilizador com sessão iniciada numa aplicação Dash](/pt-pt/guides/dash-apps/accessing-data/). O módulo da aplicação é executado uma vez, no arranque do contentor, antes de qualquer leitor ter iniciado sessão; uma ligação ou leitura de tabela aí não tem nenhum leitor como quem agir e faz a aplicação falhar no arranque.

O PlaidCloud executa a aplicação sob **gunicorn com várias threads**, pelo que serve leitores em simultâneo a partir de um único processo — não precisa de fazer nada adicional para suportar mais do que uma pessoa a usar a aplicação ao mesmo tempo.

## Escolher entre Panel e Dash

| | Aplicações Panel | Aplicações Dash |
|---|---|---|
| Framework | HoloViz Panel | Plotly Dash |
| Tempos de execução | WASM (no navegador) ou servidor | Apenas servidor |
| Modelo de identidade | SSO por utilizador (aplicações de servidor) | SSO por utilizador |
| Escala até zero | Apenas aplicações de servidor | Sim |
| Definição de design/temas | Sim (FAST / predefinido) | Não — defina o estilo através dos seus próprios componentes |
| Lista de acesso por aplicação | Não — porta de SSO da área de trabalho | Não — porta de SSO da área de trabalho |

## Passos seguintes

- [Implementar uma aplicação Dash a partir do PlaidCloud Git](/pt-pt/guides/dash-apps/deploy-from-git/) — o percurso completo desde o repositório até uma aplicação disponibilizada, usando uma ligação gerida sem credenciais.
- [Ler dados e o utilizador com sessão iniciada numa aplicação Dash](/pt-pt/guides/dash-apps/accessing-data/) — consulte dados do PlaidCloud como a pessoa que está a ver a aplicação.
- [Utilizar uma aplicação Dash](/pt-pt/guides/dash-apps/using/) — estado da compilação, abrir a aplicação, registos e remoção.
