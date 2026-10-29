---
title: Conector REST Salesforce
description: Configure uma ligação à API REST do Salesforce no PlaidCloud com o fluxo de credenciais de cliente OAuth 2.0, teste-a e extraia objetos de CRM para tabelas do projeto com o passo Salesforce Query Object.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/salesforce.md
---

## Documentação da API

A [referência da API REST do Salesforce](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.html) documenta os pontos de acesso de registos e de metadados, e o [Bulk API 2.0 Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm) documenta as tarefas de consulta em que se baseia o passo [Salesforce: Consultar objeto](/pt-pt/reference/workflow-steps/salesforce/query-salesforce-object/).

Para um passo a passo completo — a aplicação no lado do Salesforce, o utilizador Run As, a criação da ligação e o respetivo teste — siga o guia [Ligar ao Salesforce](/pt-pt/guides/connections/salesforce/). Esta página é a referência de campos que o sustenta.

## Como funciona a autenticação

O conector inicia sessão com **credenciais de cliente OAuth 2.0**: o PlaidCloud troca a consumer key e o segredo da aplicação por um token de acesso no ponto de acesso de tokens da própria organização e chama a API como o utilizador que a aplicação indica na definição **Run As**. Não existe início de sessão interativo, nem token de atualização, nem certificado para gerir.

Duas propriedades dessa troca são importantes na prática:

- **Um único token cobre uma extração inteira.** O PlaidCloud guarda o token de acesso em cache por ligação e ambiente até pouco antes de expirar, pelo que uma leitura paginada grande não volta a autenticar-se em cada página. Um token que o Salesforce deixe de aceitar antes do tempo — revogado, uma restrição de IP, uma política de sessão alterada — é descartado e substituído uma vez, automaticamente.
- **Os pedidos vão para onde o Salesforce indica.** A resposta do token indica a instância da organização, e todas as chamadas seguintes são feitas a essa instância e não ao anfitrião que escreveu, pelo que uma ligação continua a funcionar depois de uma alteração de My Domain ou de instância.

A versão da API REST é fixada por ligação em vez de flutuar, para que uma atualização da organização não possa alterar silenciosamente a estrutura das respostas por baixo de um passo guardado. As novas ligações utilizam uma versão atualmente suportada; uma ligação pode ser fixada a uma versão diferente através da API de configuração da ligação e, se uma versão fixada chegar ao fim de vida, o Salesforce responde com HTTP 410 e o PlaidCloud indica qual a versão que foi descontinuada.

## Configuração

Estes campos aparecem ao criar ou editar uma ligação Salesforce em **Tools > Connections**.

### Descrição da conta

| Campo | Tipo | Descrição |
|---|---|---|
| Nome da conta | Texto | Nome de apresentação desta ligação. |
| Memo | Texto (várias linhas) | Notas opcionais sobre a ligação. |

### Ligação

| Campo | Tipo | Descrição |
|---|---|---|
| Anfitrião ou endereço IP | Texto | O anfitrião My Domain da organização — `mycompany.my.salesforce.com` para produção e Developer Edition, `mycompany--uat.sandbox.my.salesforce.com` para um sandbox. O PlaidCloud acrescenta `https://` se o omitir. |

### Credenciais de autenticação

| Campo | Tipo | Descrição |
|---|---|---|
| ID do cliente | Texto | A consumer key da aplicação. |
| Segredo do cliente | Palavra-passe | O consumer secret da aplicação. Guardado cifrado; escreva um novo valor para o alterar ou deixe em branco para manter o valor armazenado. |

### Utilização e segurança

| Campo | Tipo | Descrição |
|---|---|---|
| Ativa (permitir acesso) | Comutador | Indica se a ligação pode ser utilizada. Desmarque-a para suspender o acesso sem eliminar a ligação. |
| Modelo de segurança | Seleção | Quem pode utilizar a ligação — privada para os seus proprietários, membros específicos, grupos de segurança específicos ou todos os membros da área de trabalho. |

Cada ligação guarda um conjunto destes valores por ambiente, pelo que uma ligação pode apontar para um sandbox no seu ambiente de desenvolvimento e para produção no seu ambiente de produção. Teste e defina as credenciais por ambiente.

## Testar ligação

**Testar ligação** executa a troca de tokens real e indica com que identidade as credenciais se autenticam:

| Indicado | Porque é importante |
|---|---|
| ID da organização | Confirma a que organização as credenciais chegam — a forma mais rápida de detetar uma credencial de sandbox guardada num ambiente de produção. |
| Versão da API | A versão mais alta que esta organização suporta. As leituras são executadas na versão fixada à ligação — `v61.0`, a menos que `salesforce_api_version` esteja definido — e não nesta. |
| Utilizador Run As | O utilizador a quem estão limitadas todas as linhas e campos que esta ligação alguma vez devolve. Verifique-o antes de confiar nas contagens de linhas de uma extração. |

Um teste falhado indica a causa. As falhas de autenticação comunicam o estado HTTP e pedem-lhe que volte a introduzir o ID e o segredo do cliente, porque um segredo de cliente não pode ser lido depois de guardado.

## Limitações conhecidas

- **O utilizador Run As limita todas as leituras, de duas formas diferentes.** As linhas que esse utilizador não consegue ver estão simplesmente ausentes, sem erro nem contagem. Um campo que esse utilizador não consegue ler faz falhar a consulta inteira. Ambos os casos são abordados em [O utilizador Run As limita tudo](/pt-pt/guides/connections/salesforce/#o-utilizador-run-as-limita-tudo).
- **Apenas leitura.** Este conector extrai dados; não escreve registos de volta no Salesforce.
- **Alguns tipos de campo não podem ser extraídos** — campos compostos de morada e de geolocalização, blobs `base64`, `encryptedstring` e `anyType`. O seletor de campos do passo assinala cada um e indica o motivo. Consulte [Campos que o passo recusa](/pt-pt/reference/workflow-steps/salesforce/query-salesforce-object/#campos-que-o-passo-recusa).
- **Uma extração não é uma sincronização.** Um registo eliminado no Salesforce permanece na tabela de destino.

## Relacionado

- [Ligar ao Salesforce](/pt-pt/guides/connections/salesforce/) — passo a passo
- [Salesforce: Consultar objeto](/pt-pt/reference/workflow-steps/salesforce/query-salesforce-object/)
- [Criar e gerir uma ligação](/pt-pt/guides/connections/create-connection/)
