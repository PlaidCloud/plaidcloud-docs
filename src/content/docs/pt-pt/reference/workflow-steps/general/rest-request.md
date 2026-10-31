---
title: Pedido REST
description: Chame uma API REST num passo de fluxo de trabalho — importe endpoints do Postman, OpenAPI ou HAR e encaminhe a resposta para uma tabela ou para variáveis do fluxo de trabalho.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/rest-request.md
---

## Descrição

O passo **Pedido REST** chama uma API REST e encaminha a resposta para uma tabela de destino ou para variáveis do fluxo de trabalho. Substitui os passos mais antigos de estilo REST por um único passo unificado, ao estilo do Postman: escolha um endpoint (manual, Postman, OpenAPI/Swagger ou HAR), edite os cabeçalhos, a consulta e o corpo, envie um pedido de teste e guarde.

Para um guia completo, consulte o [guia do passo Pedido REST](/pt-pt/guides/workflows/rest-request-step/).

Enquanto edita, o navegador mantém um rascunho local do passo. Se fechar ou recarregar antes de guardar, ao voltar a abrir o passo é-lhe oferecida a opção de restaurar esse rascunho por guardar.

## Configuração

### Pedido

* **Origem dos pontos finais** — `Manual`, `From the connection's API definition`, `Postman collection (file/URL)`, `OpenAPI / Swagger (URL/file)` ou `HAR archive (file)`. Utilize **Carregar catálogo** para listar os endpoints de uma origem importada; ao escolher um, preenche o respetivo método, URL, cabeçalhos, parâmetros de consulta e corpo, perguntando primeiro se editou o pedido. As três origens de ficheiro oferecem também **Colar…**, que permite fornecer diretamente a coleção ou a especificação em vez de escolher um ficheiro.
* **Ligação** *(opcional)* — uma ligação REST para autenticação e URL de base; omita-a para chamar diretamente um URL completo. O atalho de edição junto ao seletor abre o editor da ligação selecionada para consulta ou edição.
* **Método** — `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.
* **Endpoint** — caminho (com uma ligação) ou URL completo.
* **Cabeçalhos** / **Parâmetros de consulta** — linhas de nome/valor com um interruptor de ativação.
* **Corpo** — conteúdo do pedido (JSON, formulário ou texto simples).
* **Enviar pedido de teste** / **Copiar como curl** / **Importar de curl** — dispara o pedido e inspeciona a resposta no local; copia um comando curl equivalente (com os segredos ocultados); ou cola um comando curl para preencher o método, o URL, os cabeçalhos e o corpo.
* **Enviar** — `One request` (predefinição), ou `One request per table row` para distribuir o pedido por uma tabela de indutores.

Guardar alterações a um pedido de saída antes de um **Enviar pedido de teste** bem-sucedido pede confirmação. No modo de distribuição, **Testar linha 1** é o teste bem-sucedido que elimina o aviso.

Quando **Enviar** é `One request per table row`, escolha uma **Tabela de indutores** (selecione-a com o seletor de tabelas ou escreva um nome) e utilize tokens `{{row.column}}` no endpoint, na consulta, nos cabeçalhos ou no corpo para substituir os valores de cada linha. Os menus de inserção de variáveis do endpoint e do corpo incluem as colunas da tabela de indutores selecionada. Opcionais: **Filtro do driver** (uma cláusula SQL `WHERE`), **Colunas-chave** (transportadas para cada linha de saída), **Limite de linhas**, **Simultaneidade**, **Máx. pedidos/seg.** (limite à rapidez com que os pedidos arrancam em todos os trabalhadores, independentemente da simultaneidade; aceita frações, pelo que 0,5 envia um pedido a cada dois segundos; 0 = sem limite; um valor acima de 1000 é limitado a 1000 com um aviso), **Add Idempotency-Key header** (envia um `Idempotency-Key` estável por linha num único POST/PUT/PATCH sem paginação, para que as reexecuções não dupliquem a criação; ignorado com um aviso nos restantes casos), **Continue on error** (regista uma linha falhada e avisa em vez de abortar) e **Resposta** (`Parsed records` por predefinição; `Text (one row per request)` escreve cada resposta como uma linha com as colunas `DownloadData` e `DownloadHeaders`; `Raw text, errors as rows` faz o mesmo com o corpo exatamente como o servidor o enviou, acrescenta uma coluna `DownloadStatus` e mantém um erro HTTP ou de transporte como uma linha, com as credenciais ocultadas no corpo, nos cabeçalhos e no texto do erro). **Testar linha 1** dispara o pedido para a primeira linha da tabela de indutores, para que possa pré-visualizar a distribuição antes de a executar. A distribuição escreve na tabela de destino; não pode capturar para variáveis.

Com **Resposta** definida como `Text (one row per request)`, aplicam-se mais duas opções de distribuição:

* **Corpo da resposta** — `As returned` (predefinição); `Visible page text` escreve em `DownloadData` o texto visível de uma página HTML em vez do respetivo código; e `Raw bytes (Base64)` escreve os bytes do corpo exatamente como o servidor os enviou, codificados em base64, para uma resposta de ficheiro ou outra resposta binária.
* **Continuar a consultar enquanto a resposta corresponder** — para uma API que responde «ainda em curso» até uma tarefa terminar. Indique um **Caminho da resposta** (`$` para a resposta inteira, seguido de `.name`, `[0]`, `['name']` ou `["name"]`), um operador (`==`, `!=`, `<`, `<=`, `>` ou `>=`) e um valor com o seu tipo (`Text`, `Number`, `True/False` ou `Empty`). O pedido de cada linha é enviado de novo enquanto a respetiva resposta corresponder, a cada **N seconds** (1 a 600, 5 por predefinição) até um máximo de **M requests per row** (1 a 1000, 60 por predefinição); uma linha que ainda corresponda após o último pedido falha.

Para enviar conteúdo binário, como um ficheiro ou áudio guardado como texto base64 numa coluna, ative **O corpo é texto base64: enviar os bytes descodificados** (`body_base64`). Com um pedido por linha da tabela, o corpo, depois de os tokens `{{row.column}}` serem preenchidos, é lido como texto base64 e são enviados os bytes que ele descodifica.

As secções **Opções de resposta de texto** e **Início de sessão, proxy e TLS** têm estes campos. Os fluxos de trabalho KNIME convertidos também os utilizam.

Com um pedido por linha da tabela e **Resposta** definida como `Text (one row per request)`:

* **Adicionar o estado HTTP de cada resposta como coluna DownloadStatus** (`include_status`) — adiciona o estado HTTP de cada resposta como uma coluna `DownloadStatus`. **Coluna de status** (`status_column`) dá nome a essa coluna em alternativa, e defini-la adiciona a coluna.
* **Manter a linha de um pedido falhado, com DownloadStatus e DownloadError** (`keep_error_rows`) — um pedido falhado mantém a sua linha, com o corpo em falta e `DownloadStatus` e `DownloadError` preenchidos.
* **Manter a linha de uma solicitação com falha** (`keep_failed_rows`) — um pedido que obteve resposta HTTP 400 ou superior mantém a sua linha com o estado, os cabeçalhos da resposta e o corpo do erro em `DownloadError`; um pedido sem resposta mantém apenas as colunas-chave. Uma falha continua a interromper o passo quando **Continue on error** está desativado. **Fazer a etapa falhar conforme o status da resposta** (`fail_on_status`) lista as famílias de estados, como `5xx`, que fazem o passo falhar; uma resposta de qualquer outra família é mantida como linha.
* `document` *(definido com um assistente de IA ou com a API REST)* — guarda cada resposta como um ficheiro nesta pasta de documentos, `{account, path, file_name}`, em que `file_name` assume por predefinição o último segmento do URL. A linha contém `FilePath` em vez do corpo.
* **Escrever o corpo como documento de página da web** (`html_document`) — escreve cada corpo como um documento HTML normalizado (`html`) ou na sua forma XML (`xml`). **Tornar absolutos os valores relativos de href e src** (`html_absolute_urls`, predefinição true) torna absolutos, em relação ao URL do pedido, os valores relativos de `href` e `src`.
* **Tipar a coluna de corpo pela primeira resposta bem-sucedida** (`typed_body`) — tipa a coluna de corpo pela primeira resposta bem-sucedida: JSON, texto ou binário, segundo o seu `Content-Type`. Uma resposta posterior de outro tipo, JSON que não é analisável e um corpo vazio ficam em falta.
* **Adicionar uma coluna por cabeçalho de resposta** (`all_headers`) — adiciona uma coluna de texto por cada cabeçalho de resposta, depois da coluna de estado; um cabeçalho que uma resposta não enviou fica em falta.
* **Adicionar os cookies da resposta (DownloadCookies)** (`cookies`) — adiciona `DownloadCookies`, os cookies de cada resposta.

Com um pedido por linha da tabela:

* **Ignorar uma linha cuja URL não é uma URL http(s) absoluta** (`skip_invalid_urls`) — uma linha cujo URL não é um URL HTTP ou HTTPS absoluto não envia nenhum pedido e não escreve nenhuma linha. **Fazer a etapa falhar se a URL de uma linha não for uma URL http(s) absoluta** (`fail_invalid_urls`) faz o passo falhar numa linha dessas.
* **Não enviar um cabeçalho cujo valor de linha seja NULL** (`skip_null_headers`) — um cabeçalho cujo valor `{{row.column}}` é NULL não é enviado. **Fazer a etapa falhar se o valor de linha de um cabeçalho for NULL** (`fail_null_headers`) faz o passo falhar em alternativa.
* **Operação SOAP** (`soap`) — chama uma operação do WSDL indicado pelo endpoint, uma vez por linha: `service`, `port` e `operation` (o primeiro de cada quando em branco), `inputs`, que mapeia cada parâmetro para uma coluna ou uma constante, `outputs`, que nomeia os elementos da resposta a escrever como colunas (uma coluna por elemento folha quando vazio), e `xml` para adicionar o elemento de resposta como XML. O WSDL e o endereço do serviço têm de ser URL HTTP ou HTTPS públicos.

Para qualquer pedido:

* **Responder a um desafio HTTP Digest** (`digest_auth`) — responde a um desafio HTTP Digest com o nome de utilizador e a palavra-passe de Basic Auth da ligação. **Responder a um desafio NTLM** (`ntlm_auth`) responde a um desafio NTLM da mesma forma; escreva o nome de utilizador como `DOMAIN\user` para indicar um domínio.
* `proxy` — envia os pedidos através de um proxy HTTP ou SOCKS, definido com **Protocolo do proxy** (`protocol`: `http`, `https`, `socks`, `socks4` ou `socks5`), **Host do proxy** (`host`), **Porta do proxy** (`port`), **Hosts acessados diretamente** (padrões de hosts `excluded`) e **Nome de utilizador do proxy** (`username`). A palavra-passe é o `proxy_password` da ligação, utilizado apenas quando o `proxy_host` da ligação é este host.

As referências `{{name}}` a variáveis do fluxo de trabalho (também `{{var.name}}` / `{{project_var.name}}`) são substituídas no endpoint, nos cabeçalhos, nos valores da consulta e no corpo no momento da execução. Só são substituídas chavetas duplas, pelo que as chavetas simples num corpo JSON são deixadas tal como estão. As execuções de sensor/webhook expõem também `{{trigger_sensor_id}}`, `{{trigger_sensor_type}}`, `{{trigger_fired_at}}` e `{{trigger_payload_json}}` (vazios em execuções não acionadas).

O editor realça os tokens `{{...}}` detetados no endpoint, nas tabelas de cabeçalhos e de consulta e no editor do corpo.

As **Novas tentativas** aplicam-se apenas a métodos idempotentes (GET/HEAD/OPTIONS/DELETE); um POST/PUT/PATCH é sempre enviado uma só vez, para que um corpo não idempotente nunca seja reenviado. **Novas tentativas** aceita de 0 a 100. **Tempo limite (s)** é o limite por pedido, de 1 a 600 s; os pedidos de teste esperam no máximo 300 s. Consulte [passo Pedido REST](/pt-pt/guides/workflows/rest-request-step/) para o filtro do catálogo, colar e largar, ferramentas JSON, avisos de pedidos e resultados de testes.

### Destino da resposta

* **Tabela** *(predefinição)* — analisa a resposta para a **Tabela de destino** (obrigatória; apenas tabelas, não vistas). Controlos: Formato da linha (`Object` ou `Array`; um pedido por linha da tabela exige `Object`), Caminho dos itens, Modo de paginação (`No Paging`, `Offset Paging`, `Page Number Paging`, `Next Page URL Paging`, `Cursor Paging` ou `Link Header Paging (RFC 5988)`), Parâmetros do modo, Caminhos do modo, "Dump raw JSON instead of parsing rows", Novas tentativas, Tempo limite. O separador **Seleção de dados da tabela** mapeia os campos da resposta para colunas; **Inspecionar origem → Populate** preenche-o a partir de uma resposta em direto, o que requer uma ligação e pergunta primeiro antes de enviar um método que não seja GET, HEAD ou OPTIONS. Resumir e Distinto não são oferecidos.
* **Variáveis do fluxo de trabalho** — dispara um pedido e define `{prefix}_status`, `{prefix}_body`, `{prefix}_headers` e `{prefix}_elapsed_ms`. O **Prefixo da variável** tem de ser um identificador simples e não pode ser um de `cloud`, `project`, `model`, `date`.

## Comportamento

* No modo de variáveis, o passo faz um único pedido; a paginação e a análise de linhas não se aplicam.
* As variáveis capturadas são referenciadas a jusante pelo nome, por exemplo `{my_call_status}`.
