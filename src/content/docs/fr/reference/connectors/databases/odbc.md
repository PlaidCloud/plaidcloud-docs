---
title: ODBC
description: Configurez une connexion ODBC dans PlaidCloud via un DSN système ou un pilote ODBC sur la machine d'un agent PlaidLink, sous Windows ou Linux.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/odbc.md
---

**ODBC (Open Database Connectivity)** atteint une base de données grâce à la configuration ODBC de la machine sur laquelle s'exécute un [agent PlaidLink](/fr/reference/cli/plaidlink/). Utilisez-la pour une base de données qui n'a pas de connecteur PlaidCloud dédié, depuis des étapes d'agent comme [Agent Remote Export of SQL Result](/fr/reference/workflow-steps/agent/agent-remote-export-of-sql-result/). Pour en créer une, choisissez **ODBC** comme type de connexion.

:::note
Une connexion ODBC nécessite PlaidLink 1.2.31 ou une version ultérieure sur l'agent. Consultez [Upgrade](/fr/reference/cli/plaidlink/upgrade/).
:::

Une connexion ODBC fonctionne de l'une des deux façons suivantes :

- **Via un DSN.** Laissez **Pilote ODBC** vide et indiquez le nom d'une source de données (DSN) configurée sur la machine de l'agent. Le DSN contient le pilote, le serveur, la base de données et tous les autres paramètres du pilote, et les **Attributs de connexion** peuvent les remplacer. Cela fonctionne avec n'importe quel pilote ODBC.
- **Via un pilote.** Choisissez ou saisissez un **Pilote ODBC** installé sur la machine de l'agent, puis indiquez le serveur et la base de données. PlaidCloud transmet au pilote un paramètre `Server` et un paramètre `Database`, suivis des éventuels **Attributs de connexion**. Cela fonctionne avec les pilotes SQL Server de Microsoft. Pour tout autre pilote, y compris les autres pilotes suggérés par la liste, utilisez un DSN.

## Documentation officielle
Le pilote ODBC de chaque base de données a ses propres paramètres. Consultez la documentation de l'éditeur du pilote pour connaître les mots-clés qu'il accepte, que ce soit pour créer un DSN ou pour écrire des attributs de connexion.

## Créer le DSN sur la machine de l'agent

Configurez le DSN sur la machine où s'exécute l'agent, sous la forme d'un DSN système, afin que l'agent le trouve quel que soit le compte sous lequel il s'exécute.

### Sous Windows

1. Ouvrez **Sources de données ODBC (64 bits)**.
2. Dans l'onglet **DSN système**, ajoutez une source de données qui utilise le pilote ODBC de la base de données, puis saisissez le serveur, la base de données et tous les autres paramètres que le pilote demande.
3. Notez le **Nom de la source de données**. Vous le saisirez dans la connexion.

:::caution
Le DSN doit être un **DSN système** 64 bits. Sous Windows, l'agent s'exécute comme un service, qui ne peut pas voir un DSN utilisateur ni un DSN créé dans l'administrateur ODBC 32 bits. L'étape échoue alors avec l'erreur `ODBC data source '<name>' is not defined on the agent machine`.
:::

### Sous Linux

Sous Linux, l'agent accède à ODBC via unixODBC.

1. Installez unixODBC et le pilote ODBC de la base de données.
2. Vérifiez que le pilote est enregistré dans `odbcinst.ini`, sous son nom entre crochets. La plupart des paquets de pilotes s'enregistrent eux-mêmes à l'installation, et `odbcinst -q -d` liste les pilotes enregistrés.
3. Ajoutez la source de données au fichier système `odbc.ini`, dans une section portant le nom du DSN. Définissez `Driver` avec le nom du pilote enregistré, puis ajoutez le serveur, la base de données et tous les autres paramètres que le pilote demande :

   ```ini
   [Sales]
   Driver=ODBC Driver 18 for SQL Server
   Server=sales-db.example.com
   Database=Sales
   ```

4. Notez le nom de la section, ici `Sales`. Vous le saisirez dans la connexion.

`odbcinst -j` indique où se trouvent les fichiers système `odbcinst.ini` et `odbc.ini`, généralement dans `/etc`. Un DSN situé dans le fichier `~/.odbc.ini` d'un utilisateur n'est trouvé que si l'agent s'exécute sous cet utilisateur.

### Dans un conteneur

L'image de conteneur PlaidLink inclut unixODBC mais aucun pilote ODBC. Pour utiliser ODBC depuis un agent qui s'exécute dans Docker ou Kubernetes, créez à partir de cette image une image qui installe le pilote, puis ajoutez à l'image le fichier système `odbc.ini` contenant le DSN, ou montez-le dans le conteneur. L'image s'exécute sous l'utilisateur `plaid` : passez donc à `root` pour installer le pilote, puis revenez à `plaid` ensuite.

## Configuration

### Connexion à la base de données

| Champ | Obligatoire | Description |
|---|---|---|
| Pilote ODBC | Non | Laissez le champ vide pour vous connecter via un DSN. Sinon, indiquez le nom d'un pilote ODBC installé sur la machine de l'agent, exactement tel que cette machine l'enregistre : sous Windows, tel que le liste **Sources de données ODBC (64 bits)** dans son onglet **Pilotes**, et sous Linux, tel que son nom de section dans `odbcinst.ini`. La liste propose les pilotes courants, et vous pouvez en saisir un autre. Seuls les pilotes SQL Server de Microsoft fonctionnent ici. Pour tout autre pilote, y compris les autres que propose la liste, laissez ce champ vide et utilisez un DSN. Un nom de pilote ne peut pas contenir d'accolades ni de points-virgules. |
| Nom de la source de données (DSN) ou serveur | Oui | Sans pilote, nom du DSN système sur la machine de l'agent. Avec un pilote, nom d'hôte du serveur de base de données, ou `host,port` pour SQL Server sur un port autre que celui par défaut. |
| Base de données | Avec un pilote | Base de données à ouvrir. Elle n'est pas disponible sans pilote, car le DSN nomme la sienne, et l'enregistrement refuse une base de données sans pilote. |
| Attributs de connexion | Non | Autres paramètres du pilote, sous forme de paires `KEY=value` séparées par `;`. Consultez [Attributs de connexion](#attributs-de-connexion). |

La connexion n'a pas de champ de port. Pour SQL Server sur un port autre que celui par défaut, ajoutez-le au serveur sous la forme `host,port`, car les pilotes SQL Server de Microsoft n'acceptent aucun mot-clé de port. Avec un DSN, définissez le port dans le DSN, ou remplacez-le par un attribut tel que `PORT=5433` pour un pilote qui en accepte un.

### Attributs de connexion

Les **Attributs de connexion** transmettent des paramètres ODBC au pilote dans les deux modes, écrits comme le fait ODBC :

- Avec un pilote, ils sont ajoutés après les paramètres propres à la connexion. Utilisez-les pour tout ce dont le pilote a besoin par ailleurs, par exemple `ApplicationIntent=ReadOnly` pour se connecter à un réplica en lecture seule.
- Avec un DSN, ils remplacent les paramètres propres du DSN, par exemple `PORT=5433`, ou `DBQ=MYLIB` pour la bibliothèque par défaut d'IBM i.

Séparez les paires par `;`, comme dans `Encrypt=yes;ApplicationIntent=ReadOnly`. Placez entre accolades une valeur qui contient `;`, comme dans `KEY={first;second}`, et, à l'intérieur des accolades, écrivez `}` sous la forme `}}`. Les mots-clés parviennent au pilote en majuscules ; les mots-clés ODBC ne dépendent pas de la casse.

L'enregistrement refuse :

- un texte qui n'est pas composé de paires `KEY=value`, y compris une accolade jamais fermée et un mot-clé sans valeur ;
- un mot-clé donné plusieurs fois, quelle que soit la casse ;
- un mot-clé que la connexion définit à partir de ses propres champs : `DRIVER`, `DSN`, `SERVER`, `DATABASE`, `UID`, `PWD`, `USER`, `USERID`, `USERNAME` et `PASSWORD` ;
- `FILEDSN` et `SAVEFILE`, qui feraient lire par l'agent les paramètres de la connexion depuis un fichier de sa machine, ou les y feraient écrire.

Les listes de connexions masquent les attributs, car un pilote peut y accepter son propre mot-clé d'identifiant ; le formulaire de la connexion les affiche. Videz le champ pour les supprimer. Saisissez l'utilisateur et le mot de passe sous **Identifiants d'authentification**.

:::note
**ODBC Driver 18 for SQL Server** chiffre la connexion et vérifie par défaut le certificat du serveur. Pour un serveur doté d'un certificat auto-signé, ajoutez `TrustServerCertificate=yes` aux attributs.
:::

### Identifiants d'authentification

| Champ | Description |
|---|---|
| Utilisateur | Utilisateur avec lequel se connecter. Avec un DSN, laissez le champ vide pour vous connecter comme le DSN est configuré, ou, pour SQL Server, ajoutez `TRUSTED_CONNECTION=Yes` aux attributs pour vous connecter avec le compte propre de l'agent. Avec un pilote SQL Server et sans utilisateur, la connexion s'ouvre avec le compte propre de l'agent : son compte Windows, ou son ticket Kerberos sous Linux. |
| Utiliser l'authentification unique (sans mot de passe, utilisateur facultatif) | Se connecter sans mot de passe enregistré. |
| Mot de passe | Mot de passe de l'utilisateur (en écriture seule). Laissez le champ vide lors d'une modification pour conserver le mot de passe enregistré. |

### Configuration SSL et configuration SSH

Ces onglets ne s'appliquent pas à une connexion ODBC. Définissez le chiffrement et les autres options du pilote dans le DSN ou dans les attributs de connexion.

## Connexions enregistrées par une version antérieure

Les versions antérieures de ce formulaire exigeaient une **Base de données** et un pilote choisi dans une liste fixe, et renseignaient un **Port**, mais ne transmettaient jamais le pilote : ces connexions ne pouvaient donc pas se connecter. Ouvrez la connexion et procédez de l'une des deux façons suivantes :

- **Se connecter via un DSN :** videz **Pilote ODBC**, saisissez le DSN, puis enregistrez. L'enregistrement efface l'ancienne base de données.
- **Se connecter via un pilote SQL Server :** vérifiez que **Pilote ODBC** correspond à un pilote SQL Server installé sur la machine de l'agent. De nombreux noms de l'ancienne liste n'étaient pas ceux sous lesquels les pilotes s'enregistrent.

Une connexion qui conserve un pilote de l'ancienne liste s'ouvre comme une connexion par pilote. Elle ne parvient pas à se connecter tant que le pilote n'est pas un pilote SQL Server installé sur la machine de l'agent ; pour toute autre base de données, connectez-vous via un DSN.

L'enregistrement efface aussi l'ancien port. Une connexion qui n'a jamais eu qu'un DSN, sans base de données, s'ouvre avec **Pilote ODBC** vide.
