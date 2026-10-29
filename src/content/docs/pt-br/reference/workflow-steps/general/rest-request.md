---
title: Solicitação REST
description: Chame uma API REST em uma etapa de fluxo de trabalho — importe endpoints do Postman, OpenAPI ou HAR e direcione a resposta para uma tabela ou para variáveis do fluxo de trabalho.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/rest-request.md
---

## Descrição

A etapa **Solicitação REST** chama uma API REST e direciona a resposta para uma tabela de destino ou para variáveis do fluxo de trabalho. Ela substitui as etapas mais antigas no estilo REST por uma única etapa unificada, no estilo Postman: escolha um endpoint (manual, Postman, OpenAPI/Swagger ou HAR), edite cabeçalhos/consulta/corpo, envie uma solicitação de teste e salve.

Para um passo a passo completo, consulte o [guia da etapa Solicitação REST](/pt-br/guides/workflows/rest-request-step/).

Enquanto você edita, o navegador mantém um rascunho local da etapa. Se você fechar ou recarregar a página antes de salvar, ao reabrir a etapa será oferecida a opção de restaurar esse rascunho não salvo.

## Configuração

### Solicitação

* **Origem do endpoint** — `Manual`, `From the connection's API definition`, `Postman collection (file/URL)`, `OpenAPI / Swagger (URL/file)` ou `HAR archive (file)`. Use **Carregar catálogo** para listar os endpoints de uma origem importada; ao escolher um, o método, a URL, os cabeçalhos, os parâmetros de consulta e o corpo são preenchidos, com uma confirmação antes se você tiver editado a solicitação. As três origens de arquivo também oferecem **Colar…**, que permite fornecer a coleção ou a especificação diretamente em vez de escolher um arquivo.
* **Conexão** *(opcional)* — uma conexão REST para autenticação e URL base; omita para chamar uma URL completa diretamente. O atalho de edição ao lado do seletor abre o editor da conexão selecionada para visualização ou edição.
* **Método** — `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.
* **Endpoint** — caminho (com uma conexão) ou URL completa.
* **Cabeçalhos** / **Parâmetros de consulta** — linhas de nome/valor com uma chave de ativar/desativar.
* **Corpo** — carga da solicitação (JSON, formulário ou bruto).
* **Enviar solicitação de teste** / **Copiar como curl** / **Importar de curl** — dispara a solicitação e inspeciona a resposta na própria tela; copia um comando curl equivalente (segredos mascarados); ou cola um comando curl para preencher o método, a URL, os cabeçalhos e o corpo.
* **Enviar** — `One request` (padrão) ou `One request per table row` para distribuir a solicitação por uma tabela de direcionadores.

Salvar alterações na solicitação de saída antes de um **Enviar solicitação de teste** bem-sucedido pede confirmação. No modo de distribuição, **Testar linha 1** é o teste bem-sucedido que limpa o aviso.

Quando **Enviar** é `One request per table row`, escolha uma **Tabela de direcionadores** (selecione-a com o seletor de tabelas ou digite um nome) e use tokens `{{row.column}}` no endpoint, na consulta, nos cabeçalhos ou no corpo para substituir os valores de cada linha. Os menus de inserção de variáveis do endpoint e do corpo incluem as colunas da tabela de direcionadores selecionada. Opcionais: **Filtro do direcionador** (uma cláusula SQL `WHERE`), **Colunas-chave** (levadas para cada linha de saída), **Limite de linhas**, **Simultaneidade**, **Máx. solic./s** (limite de quão rápido as solicitações são iniciadas em todos os workers, independentemente da simultaneidade; aceita frações, portanto 0,5 envia uma solicitação a cada dois segundos; 0 = sem limite; um valor acima de 1000 é limitado a 1000, com um aviso), **Add Idempotency-Key header** (envia um `Idempotency-Key` estável por linha em um único POST/PUT/PATCH sem paginação, para que novas execuções não dupliquem a criação; ignorado com um aviso nos demais casos) e **Continue on error** (registra uma linha com falha e emite um aviso em vez de abortar), e **Resposta** (`Parsed records` por padrão; `Text (one row per request)` grava cada resposta como uma linha com as colunas `DownloadData` e `DownloadHeaders`; `Raw text, errors as rows` faz o mesmo com o corpo exatamente como o servidor o enviou, adiciona uma coluna `DownloadStatus` e mantém um erro HTTP ou de transporte como uma linha, com as credenciais mascaradas no corpo, nos cabeçalhos e no texto do erro). **Testar linha 1** dispara a solicitação para a primeira linha do direcionador, para que você visualize a distribuição antes de executá-la. A distribuição grava na tabela de destino; ela não pode capturar para variáveis.

Com **Resposta** definida como `Text (one row per request)`, mais duas opções de distribuição se aplicam:

* **Corpo da resposta** — `As returned` (padrão), `Visible page text` grava em `DownloadData` o texto visível de uma página HTML em vez de sua marcação, e `Raw bytes (Base64)` grava os bytes do corpo exatamente como o servidor os enviou, codificados em base64, para uma resposta de arquivo ou outra resposta binária.
* **Continuar consultando enquanto a resposta corresponder** — para uma API que responde "ainda em andamento" até um job terminar. Informe um **caminho da resposta** (`$` para a resposta inteira, depois `.name`, `[0]`, `['name']` ou `["name"]`), um operador (`==`, `!=`, `<`, `<=`, `>` ou `>=`) e um valor com seu tipo (`Text`, `Number`, `True/False` ou `Empty`). A solicitação de cada linha é enviada novamente enquanto a resposta corresponder, a cada **N seconds** (1 a 600, 5 por padrão) por até **M requests per row** (1 a 1000, 60 por padrão); uma linha que ainda corresponde após a última solicitação falha.

Para enviar conteúdo binário, como um arquivo ou áudio armazenado como texto base64 em uma coluna, ative **O corpo é texto base64: enviar os bytes decodificados** (`body_base64`). Com uma solicitação por linha da tabela, o corpo, depois de preenchidos seus tokens `{{row.column}}`, é lido como texto base64 e os bytes decodificados são enviados.

As seções **Opções de resposta de texto** e **Login, proxy e TLS** têm estes campos. Fluxos de trabalho do KNIME convertidos também os usam.

Com uma solicitação por linha da tabela e **Resposta** definida como `Text (one row per request)`:

* **Adicionar o status HTTP de cada resposta como coluna DownloadStatus** (`include_status`) — adiciona o status HTTP de cada resposta como uma coluna `DownloadStatus`. **Coluna de status** (`status_column`) dá nome a essa coluna, e defini-la adiciona a coluna.
* **Manter a linha de uma solicitação com falha, com DownloadStatus e DownloadError** (`keep_error_rows`) — uma solicitação com falha mantém sua linha, com o corpo ausente e `DownloadStatus` e `DownloadError` preenchidos.
* **Manter a linha de uma solicitação com falha** (`keep_failed_rows`) — uma solicitação que respondeu HTTP 400 ou superior mantém sua linha com o status, os cabeçalhos da resposta e o corpo do erro em `DownloadError`; uma solicitação sem resposta mantém apenas suas colunas-chave. Uma falha ainda interrompe a etapa quando **Continue on error** está desativado. **Fazer a etapa falhar conforme o status da resposta** (`fail_on_status`) lista as famílias de status, como `5xx`, que fazem a etapa falhar; uma resposta de qualquer outra família é mantida como uma linha.
* `document` *(definido com um assistente de IA ou pela API REST)* — salva cada resposta como um arquivo nesta pasta de Document, `{account, path, file_name}`, em que `file_name` assume por padrão o último segmento da URL. A linha contém `FilePath` em vez do corpo.
* **Gravar o corpo como documento de página da web** (`html_document`) — grava cada corpo como um documento HTML normalizado (`html`) ou sua forma XML (`xml`). **Tornar absolutos os valores relativos de href e src** (`html_absolute_urls`, padrão true) torna absolutos, em relação à URL da solicitação, os valores relativos de `href` e `src`.
* **Tipar a coluna de corpo pela primeira resposta bem-sucedida** (`typed_body`) — tipa a coluna de corpo pela primeira resposta bem-sucedida: JSON, texto ou binário, conforme seu `Content-Type`. Uma resposta posterior de outro tipo, um JSON que não pode ser analisado e um corpo vazio são ausentes.
* **Adicionar uma coluna por cabeçalho de resposta** (`all_headers`) — adiciona uma coluna de texto para cada cabeçalho de resposta, depois da coluna de status; um cabeçalho que uma resposta não enviou é ausente.
* **Adicionar os cookies da resposta (DownloadCookies)** (`cookies`) — adiciona `DownloadCookies`, os cookies de cada resposta.

Com uma solicitação por linha da tabela:

* **Ignorar uma linha cuja URL não é uma URL http(s) absoluta** (`skip_invalid_urls`) — uma linha cuja URL não é uma URL HTTP ou HTTPS absoluta não envia solicitação e não grava linha. **Fazer a etapa falhar se a URL de uma linha não for uma URL http(s) absoluta** (`fail_invalid_urls`) faz a etapa falhar para essa linha.
* **Não enviar um cabeçalho cujo valor de linha seja NULL** (`skip_null_headers`) — um cabeçalho cujo valor `{{row.column}}` é NULL não é enviado. **Fazer a etapa falhar se o valor de linha de um cabeçalho for NULL** (`fail_null_headers`) faz a etapa falhar.
* **Operação SOAP** (`soap`) — chama uma operação do WSDL indicado pelo endpoint, uma vez por linha: `service`, `port` e `operation` (cada um assume o primeiro quando em branco), `inputs` mapeando cada parâmetro para uma coluna ou uma constante, `outputs` nomeando os elementos da resposta a gravar como colunas (uma coluna por elemento folha quando vazio) e `xml` para adicionar o elemento da resposta como XML. O WSDL e o endereço do serviço devem ser URLs HTTP ou HTTPS públicas.

Para qualquer solicitação:

* **Responder a um desafio HTTP Digest** (`digest_auth`) — responde a um desafio HTTP Digest com o nome de usuário e a senha de Basic Auth da conexão. **Responder a um desafio NTLM** (`ntlm_auth`) responde a um desafio NTLM da mesma forma; escreva o nome de usuário como `DOMAIN\user` para informar um domínio.
* `proxy` — envia as solicitações por um proxy HTTP ou SOCKS, definido com **Protocolo do proxy** (`protocol`: `http`, `https`, `socks`, `socks4` ou `socks5`), **Host do proxy** (`host`), **Porta do proxy** (`port`), **Hosts acessados diretamente** (padrões de host em `excluded`) e **Nome de usuário do proxy** (`username`). A senha é o `proxy_password` da conexão, usado somente quando o `proxy_host` da conexão é este host.

Referências `{{name}}` a variáveis do fluxo de trabalho (também `{{var.name}}` / `{{project_var.name}}`) são substituídas no endpoint, nos cabeçalhos, nos valores de consulta e no corpo em tempo de execução. Somente chaves duplas são substituídas, portanto chaves simples em um corpo JSON são mantidas literalmente. Execuções por sensor/webhook também expõem `{{trigger_sensor_id}}`, `{{trigger_sensor_type}}`, `{{trigger_fired_at}}` e `{{trigger_payload_json}}` (vazios em execuções não disparadas).

O editor destaca os tokens `{{...}}` detectados no endpoint, nas tabelas de cabeçalhos e de consulta e no editor do corpo.

**Novas tentativas** se aplicam apenas a métodos idempotentes (GET/HEAD/OPTIONS/DELETE); um POST/PUT/PATCH é sempre enviado uma única vez, para que um corpo não idempotente nunca seja reenviado. **Novas tentativas** aceita de 0 a 100. **Tempo limite (s)** é o limite por solicitação, de 1 a 600 s; as solicitações de teste esperam no máximo 300 s. Consulte [Etapa Solicitação REST](/pt-br/guides/workflows/rest-request-step/) para o filtro do catálogo, colar e soltar, ferramentas de JSON, avisos de solicitação e resultados de teste.

### Destino da resposta

* **Tabela** *(padrão)* — analisa a resposta e a grava na **Tabela de destino** (obrigatória; somente tabelas, não visões). Controles: Formato da linha (`Object` ou `Array`; uma solicitação por linha da tabela exige `Object`), Caminho dos itens, Modo de paginação (`No Paging`, `Offset Paging`, `Page Number Paging`, `Next Page URL Paging`, `Cursor Paging` ou `Link Header Paging (RFC 5988)`), Parâmetros do modo, Caminhos do modo, "Dump raw JSON instead of parsing rows", Novas tentativas, Tempo limite. A guia **Seleção de dados da tabela** mapeia campos da resposta para colunas; **Inspecionar origem → Populate** a preenche a partir de uma resposta real, o que exige uma conexão e pede confirmação antes de enviar um método diferente de GET, HEAD ou OPTIONS. Resumir e Distintos não são oferecidos.
* **Variáveis do fluxo de trabalho** — dispara uma solicitação e define `{prefix}_status`, `{prefix}_body`, `{prefix}_headers` e `{prefix}_elapsed_ms`. O **Prefixo da variável** deve ser um identificador simples e não pode ser `cloud`, `project`, `model` nem `date`.

## Comportamento

* No modo de variáveis, a etapa faz uma única solicitação; a paginação e a análise de linhas não se aplicam.
* As variáveis capturadas são referenciadas downstream pelo nome, por exemplo `{my_call_status}`.
