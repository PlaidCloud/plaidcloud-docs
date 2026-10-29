---
title: Dépannage
description: Problèmes courants de connexion des agents IA au serveur MCP de PlaidCloud et comment les résoudre.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/troubleshooting.md
---

## Cursor (ou un autre client strict) ne se connecte pas du tout

Symptôme : le serveur n'établit jamais de session dans Cursor et les clients stricts similaires, alors que le même espace de travail fonctionne dans Claude Code.

Cause : une **barre oblique finale** dans l'URL du serveur. Utilisez `https://<your-workspace>.plaid.cloud/mcp`, et non `.../mcp/`. Les clients stricts rejettent une URL avec barre oblique finale (ou ne suivent pas la redirection émise par l'ancien chemin), tandis que les clients tolérants comme Claude Code l'acceptent.

Solution : supprimez la barre oblique finale de l'`url` dans votre configuration, puis reconnectez-vous. Tous les exemples de ces guides utilisent la forme sans barre oblique.

## « failed to Connect » / « session Not Found »

Symptôme : la configuration du client semble correcte, mais le serveur apparaît en échec dans le panneau d'état MCP du client. Les journaux du serveur affichent des erreurs 404 `Session not found`.

Cause : un bogue connu de certains clients MCP (notamment Claude Code 2.1.111 avec des en-têtes `Authorization` statiques) qui ne conservent pas `mcp-session-id` entre des requêtes HTTP successives. Le serveur MCP de PlaidCloud fonctionne en mode HTTP sans état pour contourner ce problème. Si vous le constatez sur un tenant qui n'a pas été redéployé depuis le correctif, demandez à votre administrateur de le redéployer.

En attendant le redéploiement, le flux OAuth (sans en-têtes `Authorization` statiques) fonctionne toujours, car il emprunte un autre chemin de code dans le client.

## La page « application Access Request »

Symptôme : après vous être connecté à PlaidCloud lors d'une autorisation OAuth, vous arrivez sur une page intitulée **Application Access Request** qui indique une application et un URI de redirection, et vous devez cliquer sur Approve pour que le flux continue.

Cause : c'est le comportement attendu. Chaque autorisation OAuth via le serveur MCP de PlaidCloud affiche cette page afin que vous puissiez confirmer ce que vous connectez avant l'émission d'un jeton. Elle indique l'application demandeuse et l'URI de redirection vers lequel les identifiants seront envoyés. Vérifiez que les deux correspondent bien au client que vous connectez, et n'approuvez pas une demande que vous n'avez pas initiée.

Un client déjà connecté ne revoit pas cette page lors de l'actualisation du jeton : seule une nouvelle autorisation (première connexion, ou après l'expiration ou la révocation du jeton d'actualisation) la fait réapparaître.

Solution : il n'y a rien à corriger, approuvez la page pour continuer. Si vous avez lancé l'autorisation dans un navigateur (ou un profil) et que la page s'affiche dans un autre, elle ne pourra pas aboutir : le consentement est lié au navigateur qui a démarré le flux. Relancez l'autorisation depuis le navigateur dans lequel vous êtes connecté à PlaidCloud.

## « oauth Flow is Not in Progress » lors de la connexion à Claude Code

Symptôme : vous autorisez l'accès dans le navigateur, collez l'URL de rappel dans Claude Code, et celui-ci indique qu'aucun flux n'est en cours.

Cause : l'état OAuth en mémoire du pont est propre à chaque port et peut être perdu entre les appels d'outil `authenticate` et `complete_authentication`, en particulier dans les sessions distantes/SSH où le rappel du navigateur ne peut pas atteindre `localhost`.

Solution : passez au flux Bearer statique. Ouvrez `https://<your-workspace>.plaid.cloud/mcp/setup/token` dans un navigateur où vous êtes connecté à PlaidCloud, copiez l'extrait dans votre `.mcp.json`, puis redémarrez Claude Code.

## Jeton expiré

Symptôme : des outils qui fonctionnaient hier renvoient maintenant 401 Unauthorized.

Cause : les jetons Bearer statiques suivent la politique de durée de vie des jetons d'accès de votre realm Keycloak (généralement de quelques heures à une journée).

Solution : rechargez `https://<your-workspace>.plaid.cloud/mcp/setup/token` pour générer un nouveau jeton, puis collez-le dans votre configuration. Pour les sessions de longue durée, privilégiez OAuth : les clients qui le prennent en charge actualisent automatiquement les jetons.

## « no `access_token` in Session »

Symptôme : l'ouverture de `/mcp/setup/token` affiche « Sign-in required » ou « No access_token in session » alors que vous êtes connecté à PlaidCloud.

Cause : votre session a été établie par un chemin de connexion qui n'a pas mis en cache le jeton Keycloak (rare, mais possible).

Solution : déconnectez-vous de PlaidCloud, puis reconnectez-vous via la page de connexion standard. La nouvelle session contiendra le jeton d'accès.

## Outils manquants ou catalogue incomplet

Symptôme : `mcp_introspect` renvoie moins d'outils que prévu, ou certains outils dont vous avez besoin sont absents.

Cause 1, les portées : les outils exigent des portées PlaidCloud spécifiques (par exemple `analyze.workflow.write`). Si votre compte n'a pas la portée requise, l'outil refuse de s'exécuter. Exécutez `mcp_introspect(name='<tool>')` pour voir `required_scopes`. Demandez à l'administrateur de votre espace de travail d'accorder la portée, ou exécutez l'opération avec un compte qui la possède.

Cause 2, une version différente : un ancien déploiement peut ne pas disposer de tous les outils décrits dans la dernière documentation. Comparez le nombre d'outils renvoyé par `mcp_introspect()` aux notes de version de votre version actuelle, et demandez un redéploiement si nécessaire.

## Multi-tenant : quel tenant l'agent vient-il d'interroger ?

Symptôme : plusieurs tenants PlaidCloud sont configurés et la réponse de l'agent pourrait provenir de n'importe lequel d'entre eux.

Solution : indiquez explicitement le tenant dans votre invite (« dans le tenant **dev**, liste les workflows… »). Les noms de serveur MCP que vous avez choisis dans votre configuration (par exemple `plaidcloud-prod`, `plaidcloud-dev`) servent aussi d'identifiants que le modèle peut utiliser pour lever l'ambiguïté. Pour les opérations à enjeux élevés, laissez la production désactivée dans le sélecteur de connecteurs jusqu'à ce que vous en ayez réellement besoin.

## Limites de débit et quota

La surface REST de PlaidCloud est limitée en nombre de requêtes par minute, par le même intergiciel que celui qui précède l'interface. Les appels MCP partagent cette limite. Si un agent envoie une longue rafale d'appels `find` (par exemple pour énumérer tous les projets, workflows et étapes), vous risquez d'atteindre la limite. Utilisez la pagination (`cursor`, `limit`) et `count_only=True` pour estimer la taille, plutôt que de récupérer l'ensemble des résultats.

Notez qu'un find renvoie 25 lignes par page par défaut (`step_find` en renvoie 50) : énumérer un grand ensemble coûte donc plus d'appels qu'auparavant. Augmentez `limit` pour un balayage volontaire plutôt que de paginer à la valeur par défaut. À l'inverse, si vous atteignez régulièrement la limite, `count_only=True` et une projection `fields=[...]` plus ciblée signifient généralement que vous n'aviez pas besoin du balayage.

## Une liste semble courte, ou un agent dit « c'est tout »

Symptôme : un find a renvoyé moins de lignes que prévu, ou l'agent a conclu qu'un projet comptait 25 tables alors qu'il en compte 300.

Solution : examinez l'enveloppe. Une page tronquée renseigne `next_cursor`, et un outil find nomme aussi la liste tronquée dans `truncated` : l'un comme l'autre signifie qu'il reste des résultats à récupérer. `total` indique le nombre complet dans tous les cas ; comparez-le aux lignes obtenues. Demandez à l'agent de paginer avec le curseur, ou de relancer avec une valeur de `limit` plus élevée.

## Un résultat ressemble à `{"_fmt": "cols", ...}`

Symptôme : un outil a renvoyé `{"_fmt": "cols", "cols": [...], "rows": [[...]]}` au lieu de la liste d'objets attendue.

C'est la forme voulue pour un gros résultat dont toutes les lignes portent les mêmes champs : les noms de champs sont envoyés une seule fois au lieu d'être répétés sur chaque ligne. La ligne *i* est `dict(zip(cols, rows[i]))`. Les agents en sont informés à la connexion et la gèrent sans qu'il soit nécessaire de le leur demander ; si vous lisez ces réponses depuis votre propre code, décodez les deux formes, car les résultats petits ou irréguliers arrivent toujours sous forme de tableaux d'objets ordinaires. Rien d'autre ne change dans l'enveloppe et aucune valeur n'est modifiée. Consultez [Premiers pas avec les agents de codage IA](/fr/integrations/ai-coding-agents/getting-started/#résultats-orientés-colonnes).

## Obtenir de l'aide

Pour les problèmes côté serveur (échecs d'authentification, outils renvoyant des erreurs sans cause évidente, outils manquants), examinez d'abord l'enveloppe `error` de la réponse. Chaque échec inclut `code`, `retryable`, `message` et souvent un `hint`. Si l'indication ne suffit pas, contactez votre administrateur PlaidCloud ou ouvrez un ticket de support avec l'ID de la requête (renvoyé dans l'en-tête de réponse `X-Request-Id`).
