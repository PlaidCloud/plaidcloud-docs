---
title: Aplicativos Dash
description: Crie e implante aplicativos de dados Plotly Dash do lado do servidor no PlaidCloud, publicados a partir de um repositório Git e servidos com autenticação por usuário e escalonamento a zero, em paridade com os aplicativos Panel de servidor.
sidebar:
  label: Aplicativos Dash
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/index.md
---

Os Aplicativos Dash permitem publicar aplicativos interativos [Plotly Dash](https://dash.plotly.com/), com callbacks, gráficos e grades de dados (`dash-ag-grid`, `dash-mantine-components`), diretamente do PlaidCloud. Você os gerencia na tela **Meus aplicativos Panel**, junto com seus aplicativos Panel, onde cada linha mostra o runtime, o status da compilação e a URL.

## Onde o Dash se encaixa

Um aplicativo Dash é hospedado exatamente como um **aplicativo Panel de servidor**: você aponta o PlaidCloud para um branch de um repositório Git, ele compila seu código em um contêiner, e o contêiner fica ocioso com zero réplicas, desperta na primeira solicitação, atende e volta a zero quando fica ocioso. Não existe um runtime "WASM" separado para o Dash: todo aplicativo Dash é um aplicativo de servidor.

Use um aplicativo Dash quando seu aplicativo for escrito com Plotly Dash em vez de HoloViz Panel, por exemplo, uma base de código Dash existente ou uma equipe que prefere o modelo de callbacks do Dash e o ecossistema `dash-ag-grid` / `dash-mantine-components`. Se você está começando do zero e não tem preferência, consulte [Aplicativos Panel](/pt-br/guides/panel-apps/) para conhecer a alternativa.

Tudo o que um aplicativo Panel de servidor recebe, um aplicativo Dash também recebe:

- **Identidade por usuário.** Cada visualizador entra com o logon único da plataforma, e toda chamada que o aplicativo faz para ler dados é executada como *aquele visualizador*, o mesmo modelo de [Leitura de dados e do usuário conectado](/pt-br/guides/panel-apps/accessing-data/), usando a API auxiliar própria do Dash. Consulte [Leitura de dados e do usuário conectado em um aplicativo Dash](/pt-br/guides/dash-apps/accessing-data/).
- **Escalonamento a zero.** O aplicativo fica ocioso com zero réplicas após a janela de inatividade configurada e desperta na próxima solicitação, com uma breve tela de carregamento do PlaidCloud durante a inicialização a frio. Consulte [Usar um aplicativo Dash](/pt-br/guides/dash-apps/using/#abrir-um-aplicativo-dash).
- **Recompilações automáticas.** Cada push no branch conectado recompila e reimplanta o aplicativo.
- **Logs de runtime e de compilação**, cada um identificado com o visualizador cuja sessão gerou a linha.

Duas coisas que um aplicativo Dash **não** tem, ambas por projeto e ambas iguais ao que um aplicativo Panel também não tem:

- **Sem configuração de design/tema.** A opção **Design** na caixa de diálogo de publicação do Panel (FAST vs. Padrão) é uma preocupação específica do Panel: os aplicativos Dash definem seu estilo inteiramente pelos componentes que você escolhe (`dash-mantine-components`, CSS personalizado etc.), portanto o formulário de publicação não tem um campo equivalente.
- **Sem lista de acesso por aplicativo.** O acesso é o portão de SSO do espaço de trabalho: qualquer pessoa conectada ao seu tenant pode abrir o aplicativo (ou, se você ativar **Permitir acesso público**, qualquer pessoa). Não há uma camada separada de ACL por aplicativo para nenhum dos dois tipos de aplicativo.

## Contrato do aplicativo

O arquivo de entrada de um aplicativo Dash deve se chamar `app.py` e deve expor um `server`; esse é todo o contrato:

```python
from dash import Dash

app = Dash(__name__)  # picks up DASH_URL_BASE_PATHNAME from the platform automatically
server = app.server   # the platform imports this and wires per-user sign-in for you
```

- **Nomeie o arquivo como `app.py`.** O inicializador do PlaidCloud importa seu aplicativo como o módulo `app` e lê o objeto `server`; portanto, qualquer que seja o caminho definido em **Ponto de entrada** (raiz do repositório ou uma subpasta), o arquivo nesse caminho deve se chamar `app.py`.
- **Exponha `server = app.server`** no nível do módulo. Esse é o objeto que a plataforma importa.
- **Você não configura o login por conta própria.** A plataforma protege cada solicitação com logon único por usuário automaticamente: você não precisa chamar `init_auth` nem importar `plaidcloud_dash` só para obter a identidade. (Um aplicativo antigo que *chama* `plaidcloud_dash.init_auth(server, url_base_pathname=os.environ["DASH_URL_BASE_PATHNAME"])` continua funcionando sem alterações: essa chamada é idempotente, então convive com a configuração da própria plataforma.)
- **Não defina `requests_pathname_prefix` nem `url_base_pathname` em `Dash(__name__)`.** Todo aplicativo Dash é servido sob um prefixo de URL obrigatório (`/serve/<slug>/`), e a plataforma o define para você por meio da variável de ambiente `DASH_URL_BASE_PATHNAME`, que é a variável de configuração nativa do próprio Dash, lida antes de qualquer argumento do construtor. Passar o prefixo explicitamente também entra em conflito com a configuração do Dash e o aplicativo não inicia.
- **`Entry Point` pode apontar para uma subpasta.** Antes de iniciar o aplicativo, o host define o diretório de trabalho do contêiner como a pasta do próprio arquivo de entrada, de modo que importações de irmãos na mesma pasta (`import data`) e caminhos de arquivo relativos no seu aplicativo são resolvidos a partir dessa pasta, como ao executar `python app.py` de dentro dela.
- **Não leia dados no momento da importação.** Faça as leituras do PlaidCloud dentro de callbacks, não no escopo do módulo. Consulte [Leitura de dados e do usuário conectado em um aplicativo Dash](/pt-br/guides/dash-apps/accessing-data/). O módulo do seu aplicativo é executado uma vez, na inicialização do contêiner, antes de qualquer visualizador ter entrado; uma leitura de conexão ou de tabela nesse momento não tem um visualizador como identidade e faz o aplicativo falhar na inicialização.

O PlaidCloud executa seu aplicativo com **gunicorn com threads**, portanto ele atende visualizadores simultâneos a partir de um único processo: você não precisa fazer nada extra para dar suporte a mais de uma pessoa usando o aplicativo ao mesmo tempo.

## Como escolher entre Panel e Dash

| | Aplicativos Panel | Aplicativos Dash |
|---|---|---|
| Framework | HoloViz Panel | Plotly Dash |
| Runtimes | WASM (no navegador) ou servidor | Somente servidor |
| Modelo de identidade | SSO por usuário (aplicativos de servidor) | SSO por usuário |
| Escalonamento a zero | Somente aplicativos de servidor | Sim |
| Configuração de design/tema | Sim (FAST / Padrão) | Não: defina o estilo pelos seus próprios componentes |
| Lista de acesso por aplicativo | Não: portão de SSO do espaço de trabalho | Não: portão de SSO do espaço de trabalho |

## Próximos passos

- [Implantar um aplicativo Dash a partir do PlaidCloud Git](/pt-br/guides/dash-apps/deploy-from-git/): o caminho completo do repositório até um aplicativo servido, usando uma conexão gerenciada sem credenciais.
- [Leitura de dados e do usuário conectado em um aplicativo Dash](/pt-br/guides/dash-apps/accessing-data/): consulte os dados do PlaidCloud como a pessoa que está visualizando o aplicativo.
- [Usar um aplicativo Dash](/pt-br/guides/dash-apps/using/): status da compilação, abertura do aplicativo, logs e remoção.
