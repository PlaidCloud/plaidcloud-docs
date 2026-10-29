---
title: Requête REST
description: Appelez une API REST dans une étape de workflow — importez des points de terminaison depuis Postman, OpenAPI ou HAR, et dirigez la réponse vers une table ou vers des variables de workflow.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/rest-request.md
---

## Description

L'étape **Requête REST** appelle une API REST et dirige la réponse vers une table cible ou vers des variables de workflow. Elle remplace les anciennes étapes de type REST par une étape unique, de style Postman : choisissez un point de terminaison (manuel, Postman, OpenAPI/Swagger ou HAR), modifiez les en-têtes, la requête et le corps, envoyez une requête de test, puis enregistrez.

Pour une présentation complète, consultez le [guide de l'étape Requête REST](/fr/guides/workflows/rest-request-step/).

Pendant la modification, le navigateur conserve un brouillon local de l'étape. Si vous fermez ou rechargez la page avant d'enregistrer, la réouverture de l'étape propose de restaurer ce brouillon non enregistré.

## Configuration

### Requête

* **Source du point de terminaison** — `Manual`, `From the connection's API definition`, `Postman collection (file/URL)`, `OpenAPI / Swagger (URL/file)` ou `HAR archive (file)`. Utilisez **Charger le catalogue** pour lister les points de terminaison d'une source importée ; en choisir un renseigne sa méthode, son URL, ses en-têtes, ses paramètres de requête et son corps, après confirmation si vous avez modifié la requête. Les trois sources de type fichier proposent aussi **Coller…**, qui vous permet de fournir directement la collection ou la spécification au lieu de choisir un fichier.
* **Connexion** *(facultatif)* — une connexion REST pour l'authentification et l'URL de base ; omettez-la pour appeler directement une URL complète. Le raccourci de modification à côté du sélecteur ouvre l'éditeur de la connexion sélectionnée pour la consulter ou la modifier.
* **Méthode** — `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.
* **Point de terminaison** — chemin (avec une connexion) ou URL complète.
* **En-têtes** / **Paramètres de requête** — lignes nom/valeur avec un interrupteur activé/désactivé.
* **Corps** — charge utile de la requête (JSON, formulaire ou brut).
* **Envoyer une requête de test** / **Copier en curl** / **Importer depuis curl** — envoient la requête et permettent d'inspecter la réponse sur place ; copient une commande curl équivalente (secrets masqués) ; ou collent une commande curl pour renseigner la méthode, l'URL, les en-têtes et le corps.
* **Envoyer** — `One request` (par défaut), ou `One request per table row` pour répartir la requête sur une table d'inducteurs.

L'enregistrement de modifications de la requête sortante avant un **Envoyer une requête de test** réussi demande une confirmation. En mode de répartition, **Tester la ligne 1** est le test réussi qui supprime l'avertissement.

Lorsque **Envoyer** vaut `One request per table row`, choisissez une **Table d'inducteurs** (avec le sélecteur de table ou en saisissant un nom) et utilisez des jetons `{{row.column}}` dans le point de terminaison, la requête, les en-têtes ou le corps pour substituer les valeurs de chaque ligne. Les menus d'insertion de variables du point de terminaison et du corps incluent les colonnes de la table d'inducteurs sélectionnée. Facultatifs : **Filtre d'inducteur** (une clause SQL `WHERE`), **Colonnes clés** (reportées sur chaque ligne de sortie), **Limite de lignes**, **Simultanéité**, **Req/s max.** (plafond de la vitesse de démarrage des requêtes sur l'ensemble des workers, indépendamment de la simultanéité ; accepte les fractions, donc 0.5 envoie une requête toutes les deux secondes ; 0 = aucune limite ; une valeur supérieure à 1 000 est plafonnée à 1 000 avec un avertissement), **Add Idempotency-Key header** (envoie un `Idempotency-Key` stable par ligne sur un POST/PUT/PATCH unique sans pagination, afin que les réexécutions ne créent pas de doublons ; ignoré avec un avertissement dans les autres cas), **Continue on error** (consigne une ligne en échec et avertit au lieu d'interrompre) et **Réponse** (`Parsed records` par défaut ; `Text (one row per request)` écrit chaque réponse sous forme de ligne avec les colonnes `DownloadData` et `DownloadHeaders` ; `Raw text, errors as rows` fait de même avec le corps exactement tel que le serveur l'a envoyé, ajoute une colonne `DownloadStatus` et conserve une erreur HTTP ou de transport sous forme de ligne, avec les identifiants masqués dans le corps, les en-têtes et le texte d'erreur). **Tester la ligne 1** envoie la requête pour la première ligne d'inducteur afin que vous puissiez prévisualiser la répartition avant de l'exécuter. La répartition écrit dans la table cible ; elle ne peut pas capturer vers des variables.

Lorsque **Réponse** vaut `Text (one row per request)`, deux autres options de répartition s'appliquent :

* **Corps de la réponse** — `As returned` (par défaut) ; `Visible page text` écrit dans `DownloadData` le texte visible d'une page HTML plutôt que son balisage ; `Raw bytes (Base64)` écrit les octets du corps exactement tels que le serveur les a envoyés, encodés en base64, pour un fichier ou une autre réponse binaire.
* **Continuer l'interrogation tant que la réponse correspond** — pour une API qui répond « toujours en cours » jusqu'à la fin d'une tâche. Indiquez un **chemin de la réponse** (`$` pour toute la réponse, puis `.name`, `[0]`, `['name']` ou `["name"]`), un opérateur (`==`, `!=`, `<`, `<=`, `>` ou `>=`) et une valeur avec son type (`Text`, `Number`, `True/False` ou `Empty`). La requête de chaque ligne est renvoyée tant que sa réponse correspond, toutes les **N seconds** (de 1 à 600, 5 par défaut) pendant au plus **M requests per row** (de 1 à 1 000, 60 par défaut) ; une ligne qui correspond encore après la dernière requête échoue.

Pour envoyer du contenu binaire, tel qu'un fichier ou un audio stocké sous forme de texte base64 dans une colonne, activez **Le corps est du texte base64 : envoyer les octets décodés** (`body_base64`). Avec une requête par ligne de table, le corps, une fois ses jetons `{{row.column}}` renseignés, est lu comme du texte base64 et les octets décodés sont envoyés.

Les sections **Options de réponse texte** et **Connexion, proxy et TLS** comportent les champs suivants. Les workflows KNIME convertis les utilisent aussi.

Avec une requête par ligne de table et **Réponse** défini sur `Text (one row per request)` :

* **Ajouter le statut HTTP de chaque réponse dans une colonne DownloadStatus** (`include_status`) — ajoute le statut HTTP de chaque réponse dans une colonne `DownloadStatus`. **Colonne de statut** (`status_column`) nomme cette colonne à la place, et la définir ajoute la colonne.
* **Conserver la ligne d'une requête échouée, avec DownloadStatus et DownloadError** (`keep_error_rows`) — une requête échouée conserve sa ligne, avec le corps manquant et `DownloadStatus` et `DownloadError` renseignés.
* **Conserver la ligne d'une requête échouée** (`keep_failed_rows`) — une requête ayant reçu une réponse HTTP 400 ou supérieure conserve sa ligne avec le statut, les en-têtes de la réponse et le corps de l'erreur dans `DownloadError` ; une requête sans réponse ne conserve que ses colonnes clés. Un échec arrête quand même l'étape lorsque **Continue on error** est désactivé. **Faire échouer l'étape selon le statut de la réponse** (`fail_on_status`) liste les familles de statuts, comme `5xx`, qui font échouer l'étape ; une réponse d'une autre famille est conservée sous forme de ligne.
* `document` *(à définir avec un assistant IA ou l'API REST)* — enregistre chaque réponse sous forme de fichier dans ce dossier Document, `{account, path, file_name}`, où `file_name` correspond par défaut au dernier segment de l'URL. La ligne contient `FilePath` au lieu du corps.
* **Écrire le corps comme un document de page web** (`html_document`) — écrit chaque corps comme un document HTML normalisé (`html`) ou sous sa forme XML (`xml`). **Rendre absolues les valeurs relatives de href et src** (`html_absolute_urls`, true par défaut) rend absolues, par rapport à l'URL de la requête, les valeurs relatives de `href` et `src`.
* **Typer la colonne du corps d'après la première réponse réussie** (`typed_body`) — type la colonne du corps d'après la première réponse réussie : JSON, texte ou binaire selon son `Content-Type`. Une réponse ultérieure d'un autre type, un JSON qui ne s'analyse pas et un corps vide sont manquants.
* **Ajouter une colonne par en-tête de réponse** (`all_headers`) — ajoute une colonne de texte pour chaque en-tête de réponse, après la colonne de statut ; un en-tête qu'une réponse n'a pas envoyé est manquant.
* **Ajouter les cookies de la réponse (DownloadCookies)** (`cookies`) — ajoute `DownloadCookies`, les cookies de chaque réponse.

Avec une requête par ligne de table :

* **Ignorer une ligne dont l'URL n'est pas une URL http(s) absolue** (`skip_invalid_urls`) — une ligne dont l'URL n'est pas une URL HTTP ou HTTPS absolue n'envoie aucune requête et n'écrit aucune ligne. **Faire échouer l'étape si l'URL d'une ligne n'est pas une URL http(s) absolue** (`fail_invalid_urls`) fait échouer l'étape pour une telle ligne.
* **Ne pas envoyer un en-tête dont la valeur de ligne est NULL** (`skip_null_headers`) — un en-tête dont la valeur `{{row.column}}` est NULL n'est pas envoyé. **Faire échouer l'étape si la valeur de ligne d'un en-tête est NULL** (`fail_null_headers`) fait échouer l'étape à la place.
* **Opération SOAP** (`soap`) — appelle une opération du WSDL nommé par le point de terminaison, une fois par ligne : `service`, `port` et `operation` (le premier lorsqu'ils sont vides), `inputs` associant chaque paramètre à une colonne ou à une constante, `outputs` nommant les éléments de la réponse à écrire sous forme de colonnes (une colonne par élément feuille lorsqu'il est vide) et `xml` pour ajouter l'élément de réponse sous forme de XML. Le WSDL et l'adresse du service doivent être des URL HTTP ou HTTPS publiques.

Pour toute requête :

* **Répondre à un défi HTTP Digest** (`digest_auth`) — répond à un défi HTTP Digest avec le nom d'utilisateur et le mot de passe Basic Auth de la connexion. **Répondre à un défi NTLM** (`ntlm_auth`) répond de la même manière à un défi NTLM ; écrivez le nom d'utilisateur sous la forme `DOMAIN\user` pour indiquer un domaine.
* `proxy` — envoie les requêtes via un proxy HTTP ou SOCKS, défini avec le **Protocole du proxy** (`protocol` : `http`, `https`, `socks`, `socks4` ou `socks5`), l'**Hôte du proxy** (`host`), le **Port du proxy** (`port`), les **Hôtes joints directement** (motifs d'hôtes `excluded`) et le **Nom d'utilisateur du proxy** (`username`). Le mot de passe est le `proxy_password` de la connexion, utilisé uniquement lorsque le `proxy_host` de la connexion correspond à cet hôte.

Les références `{{name}}` aux variables de workflow (également `{{var.name}}` / `{{project_var.name}}`) sont substituées dans le point de terminaison, les en-têtes, les valeurs de requête et le corps au moment de l'exécution. Seules les doubles accolades sont substituées ; les accolades simples d'un corps JSON sont donc laissées littérales. Les exécutions déclenchées par capteur ou webhook exposent aussi `{{trigger_sensor_id}}`, `{{trigger_sensor_type}}`, `{{trigger_fired_at}}` et `{{trigger_payload_json}}` (vides lors des exécutions non déclenchées).

L'éditeur met en évidence les jetons `{{...}}` détectés dans le point de terminaison, les tableaux d'en-têtes et de requête, et l'éditeur du corps.

Les **Nouvelles tentatives** ne s'appliquent qu'aux méthodes idempotentes (GET/HEAD/OPTIONS/DELETE) ; un POST/PUT/PATCH n'est toujours envoyé qu'une fois, afin qu'un corps non idempotent ne soit jamais renvoyé. Les **Nouvelles tentatives** acceptent de 0 à 100. Le **Délai d'expiration (s)** est la limite par requête, de 1 à 600 s ; les requêtes de test attendent au plus 300 s. Consultez [Étape Requête REST](/fr/guides/workflows/rest-request-step/) pour le filtre de catalogue, le collage et le glisser-déposer, les outils JSON, les avertissements de requête et les résultats de test.

### Destination de la réponse

* **Table** *(par défaut)* — analyse la réponse dans la **Table cible** (obligatoire ; tables uniquement, pas de vues). Contrôles : Format de ligne (`Object` ou `Array` ; une requête par ligne de table exige `Object`), Chemin des éléments, Mode de pagination (`No Paging`, `Offset Paging`, `Page Number Paging`, `Next Page URL Paging`, `Cursor Paging` ou `Link Header Paging (RFC 5988)`), Paramètres du mode, Chemins du mode, « Dump raw JSON instead of parsing rows », Nouvelles tentatives, Délai d'expiration. L'onglet **Sélection des données de la table** associe les champs de la réponse aux colonnes ; **Inspecter la source → Populate** le remplit à partir d'une réponse réelle, ce qui exige une connexion et demande une confirmation avant d'envoyer une méthode autre que GET, HEAD ou OPTIONS. Résumer et Distinct ne sont pas proposés.
* **Variables du workflow** — envoie une seule requête et définit `{prefix}_status`, `{prefix}_body`, `{prefix}_headers` et `{prefix}_elapsed_ms`. Le **Préfixe de variable** doit être un identifiant simple et ne peut pas être `cloud`, `project`, `model` ou `date`.

## Comportement

* En mode variable, l'étape effectue une seule requête ; la pagination et l'analyse des lignes ne s'appliquent pas.
* Les variables capturées sont référencées en aval par leur nom, par exemple `{my_call_status}`.
