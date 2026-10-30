---
title: ODBC
description: Configure uma ligação ODBC no PlaidCloud através de um DSN de sistema ou de um driver ODBC na máquina de um agente PlaidLink, em Windows ou Linux.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/odbc.md
---

O **ODBC (Open Database Connectivity)** chega a uma base de dados através da configuração ODBC da máquina onde é executado um [agente PlaidLink](/pt-pt/reference/cli/plaidlink/). Utilize-o para uma base de dados que não tenha um conector dedicado do PlaidCloud, a partir de passos de agente como [Agent Remote Export of SQL Result](/pt-pt/reference/workflow-steps/agent/agent-remote-export-of-sql-result/). Para criar uma, escolha **ODBC** como tipo de ligação.

:::note
Uma ligação ODBC requer o PlaidLink 1.2.31 ou posterior no agente. Consulte [Upgrade](/pt-pt/reference/cli/plaidlink/upgrade/).
:::

Uma ligação ODBC funciona de uma de duas formas:

- **Através de um DSN.** Deixe **Driver ODBC** em branco e indique uma origem de dados (DSN) configurada na máquina do agente. O DSN contém o driver, o servidor, a base de dados e quaisquer outras definições do driver, e os **Atributos da ligação** podem substituí-los. Funciona com qualquer driver ODBC.
- **Através de um driver.** Escolha ou escreva um **Driver ODBC** instalado na máquina do agente e indique depois o servidor e a base de dados. O PlaidCloud transmite ao driver uma definição `Server` e uma definição `Database`, seguidas de quaisquer **Atributos da ligação**. Funciona com os drivers do SQL Server da Microsoft. Para qualquer outro driver, incluindo os restantes sugeridos pela lista, utilize um DSN.

## Documentação do fabricante
O driver ODBC de cada base de dados tem as suas próprias definições. Consulte a documentação do fabricante do driver para saber que palavras-chave aceita, tanto ao criar um DSN como ao escrever atributos de ligação.

## Criar o DSN na máquina do agente

Configure o DSN na máquina onde o agente é executado, como DSN de sistema, para que o agente o encontre independentemente da conta com que é executado.

### No Windows

1. Abra **ODBC Data Sources (64-bit)**.
2. No separador **System DSN**, adicione uma origem de dados que utilize o driver ODBC da base de dados e introduza o servidor, a base de dados e quaisquer outras definições que o driver peça.
3. Tome nota do **Nome da origem de dados**. Vai introduzi-lo na ligação.

:::caution
O DSN tem de ser um **System DSN** de 64 bits. No Windows, o agente é executado como um serviço, que não consegue ver um User DSN nem um DSN criado no administrador ODBC de 32 bits. O passo falha então com `ODBC data source '<name>' is not defined on the agent machine`.
:::

### No Linux

No Linux, o agente acede ao ODBC através do unixODBC.

1. Instale o unixODBC e o driver ODBC da base de dados.
2. Verifique se o driver está registado em `odbcinst.ini`, com o seu nome entre parênteses retos. A maioria dos pacotes de drivers regista-se a si própria na instalação, e `odbcinst -q -d` lista os drivers registados.
3. Adicione a origem de dados ao `odbc.ini` do sistema, como uma secção com o nome do DSN. Defina `Driver` com o nome do driver registado e adicione o servidor, a base de dados e quaisquer outras definições que o driver peça:

   ```ini
   [Sales]
   Driver=ODBC Driver 18 for SQL Server
   Server=sales-db.example.com
   Database=Sales
   ```

4. Tome nota do nome da secção, `Sales` neste caso. Vai introduzi-lo na ligação.

O comando `odbcinst -j` mostra onde estão o `odbcinst.ini` e o `odbc.ini` do sistema, normalmente em `/etc`. Um DSN no `~/.odbc.ini` de um utilizador só é encontrado quando o agente é executado como esse utilizador.

### Num contentor

A imagem de contentor do PlaidLink inclui o unixODBC, mas nenhum driver ODBC. Para utilizar o ODBC a partir de um agente executado em Docker ou Kubernetes, crie uma imagem a partir dela que instale o driver e adicione à imagem o `odbc.ini` do sistema com o DSN, ou monte-o no contentor. A imagem é executada com o utilizador `plaid`, pelo que deve mudar para `root` para instalar o driver e voltar a `plaid` depois.

## Configuração

### Ligação à base de dados

| Campo | Obrigatório | Descrição |
|---|---|---|
| Driver ODBC | Não | Deixe em branco para ligar através de um DSN. Caso contrário, o nome de um driver ODBC instalado na máquina do agente, exatamente como essa máquina o regista: no Windows, tal como o **ODBC Data Sources (64-bit)** o lista no separador **Drivers**, e no Linux, como o nome da sua secção em `odbcinst.ini`. A lista oferece drivers comuns e pode escrever qualquer outro. Aqui só funcionam os drivers do SQL Server da Microsoft. Para qualquer outro driver, incluindo os restantes que a lista oferece, deixe em branco e utilize um DSN. O nome de um driver não pode conter chavetas nem pontos e vírgulas. |
| Nome da origem de dados (DSN) ou servidor | Sim | Sem driver, o nome do System DSN na máquina do agente. Com driver, o nome do anfitrião do servidor de base de dados, ou `host,port` para o SQL Server numa porta não predefinida. |
| Base de dados | Com driver | A base de dados a abrir. Não está disponível sem driver, porque o DSN indica a sua própria base de dados, e a gravação recusa uma base de dados sem driver. |
| Atributos da ligação | Não | Outras definições para o driver, como pares `KEY=value` separados por `;`. Consulte [Atributos da ligação](#atributos-da-ligação). |

A ligação não tem campo de porta. Para o SQL Server numa porta não predefinida, adicione-a ao servidor como `host,port`, porque os drivers do SQL Server da Microsoft não têm palavra-chave de porta. Com um DSN, defina a porta no DSN ou substitua-a por um atributo como `PORT=5433`, para um driver que a aceite.

### Atributos da ligação

Os **Atributos da ligação** transmitem definições ODBC ao driver em qualquer dos modos, escritas da forma como o ODBC as escreve:

- Com um driver, são adicionados após as definições da própria ligação. Utilize-os para tudo o resto de que o driver precise, como `ApplicationIntent=ReadOnly` para ligar a uma réplica só de leitura.
- Com um DSN, substituem as definições do próprio DSN, como `PORT=5433`, ou `DBQ=MYLIB` para a biblioteca predefinida do IBM i.

Separe os pares com `;`, como em `Encrypt=yes;ApplicationIntent=ReadOnly`. Coloque entre chavetas um valor que contenha `;`, como em `KEY={first;second}`, e dentro das chavetas escreva `}` como `}}`. As palavras-chave chegam ao driver em maiúsculas; as palavras-chave do ODBC não dependem da distinção entre maiúsculas e minúsculas.

A gravação recusa:

- texto que não seja constituído por pares `KEY=value`, incluindo uma chaveta que nunca é fechada e uma palavra-chave sem valor;
- uma palavra-chave indicada mais do que uma vez, em qualquer combinação de maiúsculas e minúsculas;
- uma palavra-chave que a ligação define a partir dos seus próprios campos: `DRIVER`, `DSN`, `SERVER`, `DATABASE`, `UID`, `PWD`, `USER`, `USERID`, `USERNAME` e `PASSWORD`;
- `FILEDSN` e `SAVEFILE`, que fariam o agente ler as definições da ligação de um ficheiro na sua máquina, ou escrevê-las num ficheiro.

As listas de ligações ocultam os atributos, porque um driver pode aceitar aí a sua própria palavra-chave de credencial; o formulário da própria ligação mostra-os. Limpe o campo para os remover. Introduza o utilizador e a palavra-passe em **Credenciais de autenticação**.

:::note
O **ODBC Driver 18 for SQL Server** encripta a ligação e verifica o certificado do servidor por predefinição. Para um servidor com um certificado autoassinado, adicione `TrustServerCertificate=yes` aos atributos.
:::

### Credenciais de autenticação

| Campo | Descrição |
|---|---|
| Utilizador | O utilizador com o qual estabelecer a ligação. Através de um DSN, deixe em branco para iniciar sessão como o DSN está configurado, ou, no SQL Server, adicione `TRUSTED_CONNECTION=Yes` aos atributos para iniciar sessão com a conta do próprio agente. Com um driver do SQL Server e sem utilizador, a ligação inicia sessão com a conta do próprio agente: a sua conta Windows ou, no Linux, o seu bilhete Kerberos. |
| Usar autenticação por início de sessão único (sem palavra-passe, utilizador opcional) | Liga sem uma palavra-passe guardada. |
| Palavra-passe | A palavra-passe do utilizador (só de escrita). Deixe em branco ao editar para manter a palavra-passe guardada. |

### Configuração SSL e Configuração SSH

Estes separadores não se aplicam a uma ligação ODBC. Defina a encriptação e outras opções do driver no DSN ou nos atributos da ligação.

## Ligações guardadas por uma versão anterior

As versões anteriores deste formulário exigiam uma **Base de dados** e um driver escolhido de uma lista fixa, e preenchiam uma **Porta**, mas nunca transmitiam o driver, pelo que essas ligações não conseguiam ligar. Abra a ligação e faça uma das seguintes ações:

- **Ligar através de um DSN:** limpe o **Driver ODBC**, introduza o DSN e guarde. A gravação limpa a antiga base de dados.
- **Ligar através de um driver do SQL Server:** verifique se o **Driver ODBC** corresponde a um driver do SQL Server instalado na máquina do agente. Muitos nomes da lista antiga não eram os nomes com que os drivers se registam.

Uma ligação que mantenha um driver da lista antiga abre-se como ligação por driver. Falha ao ligar até que o driver seja um driver do SQL Server instalado na máquina do agente; para qualquer outra base de dados, ligue através de um DSN.

A gravação limpa também a antiga porta. Uma ligação que só teve um DSN, sem base de dados, abre-se com o **Driver ODBC** em branco.
