---
title: Créer une application Panel
description: Publiez dans PlaidCloud une application HoloViz Panel côté serveur à partir d'un dépôt Git (avec un exemple « hello world »), ou une application WASM statique à partir d'un fichier.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Ouvrez **Mes applications Panel**. La barre d'outils propose deux façons de publier, une par [environnement d'exécution](/fr/guides/panel-apps/) :

- **Nouvelle application serveur** : construire et exécuter une application à partir d'un dépôt Git.
- **Ajouter une application WASM** : publier une application statique, exécutée dans le navigateur, à partir d'un fichier.

Pour écrire l'application directement dans PlaidCloud, sans dépôt à configurer, utilisez [Panel Studio](/fr/guides/panel-apps/studio/).

## Créer une application serveur

Une application serveur est construite à partir d'un dépôt Git et servie à l'adresse `https://<your-tenant-host>/serve/<slug>/`. Vous indiquez à PlaidCloud une branche d'un dépôt ; il construit le code dans un conteneur, y exécute `panel serve` et le reconstruit automatiquement chaque fois que vous poussez des modifications vers cette branche.

### Préparer le dépôt de votre application

Votre dépôt a besoin de deux éléments : un **point d'entrée** (un fichier Python qui construit une application Panel et la marque `.servable()`) et, éventuellement, un fichier **`requirements.txt`** listant les paquets supplémentaires, placé à la racine du dépôt ou à côté de votre point d'entrée.

```
my-panel-app/
├── app.py            # entry point — calls .servable()
└── requirements.txt  # optional; extra dependencies (repo root or next to app.py)
```

#### Hello World

Créez `app.py` :

```python
import panel as pn

pn.extension()

pn.pane.Markdown("# Hello, PlaidCloud 👋\n\nYour first server-side Panel app is running.").servable()
```

C'est une application complète. L'appel à `.servable()` est ce que PlaidCloud sert : tout ce que vous voulez afficher doit être marqué comme servable (directement, ou en faisant partie d'une mise en page servable).

#### Un exemple un peu plus riche

Les applications Panel sont interactives. Celle-ci ajoute un curseur qui met à jour une table en direct :

```python
import pandas as pd
import panel as pn

pn.extension()

multiplier = pn.widgets.IntSlider(name="Multiplier", start=1, end=10, value=3)

@pn.depends(multiplier)
def times_table(m):
    df = pd.DataFrame({"n": range(1, 6)})
    df["result"] = df["n"] * m
    return pn.pane.DataFrame(df, index=False)

pn.Column(
    "# Times Table",
    multiplier,
    times_table,
).servable()
```

#### Ajouter des dépendances

Ce deuxième exemple importe `pandas`, qui ne fait pas partie de l'image de base : ajoutez donc un `requirements.txt` (à la racine du dépôt, ou à côté de votre point d'entrée) :

```text
pandas
```

PlaidCloud les installe avec `pip` lors de la construction de l'image. Les bibliothèques de visualisation courantes (`plotly`, `holoviews`, `hvplot`) ne font pas non plus partie de l'image de base : listez donc ici celles que votre application importe.

> **Ce que la plateforme fournit, et ce qu'elle attend.** Gardez ces hypothèses à l'esprit lorsque vous écrivez votre application :
>
> - **`panel` et `bokeh` sont préinstallés** par l'image de base de la plateforme. Ne les listez pas dans `requirements.txt` et évitez d'épingler une version plus ancienne de Panel : la reconnexion de la mise à jour en direct repose sur une version récente.
> - **Les bibliothèques clientes PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) sont préinstallées.** Importez directement `plaidcloud.rpc` ou `plaidcloud.utilities` ; ne les listez pas dans `requirements.txt`.
> - **`requirements.txt` peut se trouver à la racine du dépôt ou à côté de votre point d'entrée.** Dans un dépôt partagé (monodépôt), conservez les dépendances de chaque application dans son propre dossier. Un fichier à la racine, s'il existe, est également installé : placez-y les dépendances partagées et placez les dépendances propres à l'application à côté d'elle.
> - **L'application s'exécute en tant qu'utilisateur non root sur un système de fichiers en lecture seule.** Seul `/tmp` est accessible en écriture : écrivez-y donc tous les fichiers temporaires (la plupart des bibliothèques respectent déjà `$TMPDIR`).
> - **Ne codez pas en dur le port, le préfixe d'URL ou l'hôte.** PlaidCloud les attribue et les injecte au moment du déploiement : appelez simplement `.servable()`.

Pour obtenir l'apparence PlaidCloud ainsi que des filtres, des grilles et des graphiques prêts à l'emploi, construisez votre application avec [le kit d'applications Panel](/fr/guides/panel-apps/app-kit/).

### Définir le thème : clair, sombre ou commutable

Les applications serveur s'affichent par défaut avec le design moderne **Fast** de PlaidCloud, un style épuré de type Fluent appliqué à toute la plateforme. Dans la boîte de dialogue de publication, **Conception** contrôle cette couche de plateforme :

- **FAST** : la valeur PlaidCloud par défaut. Utilisez-la pour les nouvelles applications et les applications construites avec des modèles Fast.
- **Par défaut** : le style par défaut de Panel. Utilisez-la lorsque le CSS ou les visuels d'une application existante se dégradent avec FAST.

Ce que vous contrôlez dans le code de votre application, c'est le **thème** : clair, sombre ou un commutateur que le lecteur peut basculer.

Le thème est une propriété du **modèle** que vous servez. Les modèles Fast, `FastListTemplate` (une seule colonne) et `FastGridTemplate` (une grille adaptative), acceptent deux paramètres pour cela :

- **`theme`** : `"default"` pour le thème clair ou `"dark"`. Le définir verrouille l'application sur ce thème, même si un lecteur ajoute `?theme=dark` à l'URL.
- **`theme_toggle`** : `True` affiche un commutateur clair/sombre dans l'en-tête ; `False` le masque. La valeur par défaut est `True`. Masquer le commutateur ne fixe pas le thème à lui seul : verrouillez-le avec `theme` (ci-dessus) ; définissez `theme_toggle=False` une fois cela fait, afin que les lecteurs ne voient pas un commutateur qui ne change rien.

Choisissez le schéma qui convient à votre application.

**Clair uniquement** : idéal pour les rapports denses et les tables financières, qui sont généralement mis en forme à la main pour un fond clair :

```python
import panel as pn

pn.extension("tabulator")

pn.template.FastListTemplate(
    title="Sales Dashboard",
    theme="default",      # light
    theme_toggle=False,   # hide the switch
    main=[...],
).servable()
```

**Sombre uniquement :**

```python
pn.template.FastListTemplate(
    title="Ops Monitor",
    theme="dark",
    theme_toggle=False,
    main=[...],
).servable()
```

**Laisser le lecteur choisir** : clair par défaut, avec un commutateur dans l'en-tête. Omettez `theme` pour qu'il suive le commutateur :

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **Si vous autorisez le mode sombre, adaptez vos tables.** Un `Tabulator` verrouillé sur un thème de table clair (`theme="bootstrap"`), ou un CSS personnalisé avec des couleurs claires codées en dur comme `background: #fff`, s'affiche comme un bloc blanc illisible sur une page sombre. Utilisez un thème de table qui suit l'application (`pn.widgets.Tabulator(..., theme="fast")`) et évitez les couleurs claires codées en dur. Si un rapport est très fortement mis en forme pour un fond clair, verrouillez-le plutôt sur le thème clair (le premier schéma ci-dessus).

Une application simple sans modèle (`pn.Column(...).servable()`) suit le comportement par défaut de Panel et n'est pas affectée par ces paramètres ; utilisez un modèle lorsque vous voulez un contrôle explicite.

Votre dépôt doit être accessible via une **connexion Git** dans PlaidCloud. Si votre code se trouve dans [PlaidCloud Git](/fr/guides/git/), créez une connexion **PlaidCloud Git** gérée sous **Tools > Connections** : elle ne nécessite ni URL de serveur ni identifiants. Pour l'ensemble du parcours, d'un dépôt vide à une application servie, consultez [Déployer une application Panel depuis PlaidCloud Git](/fr/guides/panel-apps/deploy-from-git/).

### Publier l'application

1. Cliquez sur **Nouvelle application serveur** pour ouvrir la boîte de dialogue **Publier une application Panel serveur**. Ses paramètres sont regroupés en sections.
2. Sous **Paramètres du répertoire** :
   - **Nom de l'application** : le nom affiché dans la liste.
   - **Slug d'URL** : à la fois l'URL de l'application et son nom interne ; il doit donc être une étiquette DNS valide : lettres minuscules, chiffres et tirets, commençant par une lettre, 40 caractères au maximum (par exemple, `sales-dashboard`). La boîte de dialogue le vérifie avant la publication.
   - **Mémo** : une description facultative.
   - **Projet** : le projet auquel appartient l'application. Il fournit l'[image de marque](/fr/guides/panel-apps/branding/) de l'application et constitue le projet par défaut pour ses tables. Vous ne pouvez pas le modifier ici après la publication ; utilisez [Affecter](/fr/guides/panel-apps/branding/#pour-les-applications-existantes).
3. Sous **Connexion Git et observateur de publication** :
   - **Connexion Git** : la connexion qui contient le dépôt de votre application.
   - **Branche** : la branche à partir de laquelle construire. Les envois vers cette branche reconstruisent et redéploient automatiquement l'application.
   - **Point d'entrée** : le fichier `.py` que Panel doit servir (votre `app.py`).
4. Sous **Exécution** :
   - **CPU** et **Mémoire** que le conteneur de l'application doit demander.

     > Moins de ressources (CPU / mémoire plus faibles) permettent à l'application d'être planifiée et de démarrer à froid plus rapidement.

   - **Conception** : choisissez **FAST** pour le design moderne de PlaidCloud, ou **Par défaut** si le CSS de l'application attend le style par défaut de Panel.
   - **Inactivité (minutes)** : la durée pendant laquelle l'application reste active sans trafic avant de revenir à zéro. La valeur par défaut est de 5 minutes.
   - **Autoriser l'accès public** : cochez cette option pour autoriser l'accès sans authentification ; sinon, les lecteurs doivent se connecter à votre tenant.
5. Sous **Avancé (diffusion intégrée)** : facultatif. Par défaut, l'application n'est servie que depuis votre tenant PlaidCloud. Pour l'intégrer dans un autre site, cliquez sur **Ajouter un domaine** et saisissez chaque domaine autorisé à la charger, un par ligne : un hôte uniquement, sans schéma ni chemin (par exemple, `example.com` ou `app.example.com:8443`). Laissez la liste vide, sauf si vous intégrez l'application ailleurs.
6. Cliquez sur **Publier**.

Après la publication, l'application est **construite** : son **Statut** s'affiche dans la liste et se met à jour automatiquement. Consultez [Utiliser une application Panel](/fr/guides/panel-apps/using/) pour connaître la signification des statuts, la façon d'ouvrir l'application lorsqu'elle est prête et la façon de déclencher une reconstruction sans la dépublier.

> L'URL de l'application ne fonctionne qu'une fois son statut de build **Prêt**, et la première requête après une période d'inactivité la redémarre (environ 15 secondes).

### Avancé : reproduire PlaidCloud en local

Les utilisateurs techniques peuvent construire et tester l'application avec les mêmes entrées que celles utilisées par PlaidCloud. C'est la vérification locale la plus proche avant de publier ou de cliquer sur **Régénérer**.

PlaidCloud construit à partir de la branche Git sélectionnée avec ce Dockerfile généré. Utilisez le même contenu en local sous le nom `Dockerfile.plaidcloud-panel` :

```dockerfile
FROM us-docker.pkg.dev/plaidcloud-build/panel-base/platform-panel-base:0.5.1
USER root
COPY . /app
RUN if [ -f /app/requirements.txt ]; then pip install --no-cache-dir -r /app/requirements.txt; fi
# If your entry point is in a subfolder, PlaidCloud also installs that folder's requirements.txt,
# after the root one (so a per-app pin wins). Replace <app-folder> with your entry point's folder,
# or drop this line if your app is at the repository root.
RUN if [ -f "/app/<app-folder>/requirements.txt" ]; then pip install --no-cache-dir -r "/app/<app-folder>/requirements.txt"; fi
USER 10001
```

Pour reproduire le build du serveur :

1. Extrayez la même branche que celle que vous sélectionnez dans **Branche**.
2. Lancez le build depuis la racine du dépôt, afin que `COPY . /app` corresponde à PlaidCloud.
3. Placez les dépendances facultatives dans un fichier `requirements.txt`, à la racine du dépôt ou à côté de votre point d'entrée. Les deux sont installés, celui du dossier de l'application en dernier (afin qu'une version épinglée propre à l'application l'emporte).
4. Utilisez le même chemin de point d'entrée que celui que vous sélectionnez dans **Point d'entrée**.

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

L'image déployée ne remplace pas le point d'entrée de l'image de base. Elle exécute `panel serve` à partir de variables d'environnement injectées par PlaidCloud. Testez l'image construite avec le même contrat d'exécution :

```sh
docker run --rm \
  --cpus 0.5 \
  --memory 512m \
  -p 5006:5006 \
  -e APP_PATH=/app/app.py \
  -e PANEL_PREFIX=/serve/local \
  -e PANEL_PORT=5006 \
  -e PANEL_ORIGIN=localhost:5006 \
  -e PANEL_KEEP_ALIVE_MS=25000 \
  -e PLAID_PANEL_DESIGN=fast \
  local-panel-app:plaidcloud
```

Ouvrez `http://localhost:5006/serve/local/`.

Reprenez les paramètres de la boîte de dialogue de publication lorsque vous testez :

- **Point d'entrée** correspond à `APP_PATH=/app/<entry-point>`.
- **CPU** et **Mémoire** correspondent aux limites `--cpus` et `--memory` de Docker.
- **Conception : FAST** correspond à `PLAID_PANEL_DESIGN=fast`.
- **Conception : Par défaut** signifie qu'il faut omettre `PLAID_PANEL_DESIGN`.
- **Inactivité (minutes)** correspond à la fenêtre de réduction d'échelle du déploiement. Elle n'est pas appliquée par Docker en local, mais l'application utilise tout de même les mêmes paramètres de keepalive websocket et de nettoyage des sessions de Panel.
- Les domaines de **diffusion intégrée** correspondent à `PANEL_ORIGIN` ; utilisez une liste séparée par des espaces si vous devez tester plusieurs hôtes.

Si vous n'avez pas besoin d'un conteneur, vous pouvez tout de même tester la couche de service depuis un environnement Python local. Installez le même `requirements.txt`, définissez les variables d'environnement de la plateforme, puis exécutez `panel serve` avec les mêmes options que celles de l'image déployée.

```sh
export APP_PATH=app.py
export PANEL_PREFIX=/serve/local
export PANEL_PORT=5006
export PANEL_ORIGIN=localhost:5006
export PANEL_KEEP_ALIVE_MS=25000
export PLAID_PANEL_DESIGN=fast

panel serve "$APP_PATH" \
  --address 0.0.0.0 \
  --port "$PANEL_PORT" \
  --prefix "$PANEL_PREFIX" \
  --allow-websocket-origin "$PANEL_ORIGIN" \
  --num-procs 1 \
  --keep-alive "$PANEL_KEEP_ALIVE_MS" \
  --unused-session-lifetime 15000 \
  --index "$(basename "$APP_PATH" .py)"
```

Ouvrez `http://localhost:5006/serve/local/`.

Utilisez `PLAID_PANEL_DESIGN=fast` pour reproduire l'apparence déployée par défaut. Pour tester l'option de conception **Par défaut** de la boîte de dialogue de publication, laissez `PLAID_PANEL_DESIGN` non défini et exécutez la même commande. Conservez `PANEL_PREFIX`, `PANEL_ORIGIN`, `--keep-alive` et `--unused-session-lifetime` : ils font partie du contrat d'exécution déployé.

## Créer une application WASM

Une application WASM s'exécute dans le navigateur à partir d'un fichier HTML préconstruit.

1. Cliquez sur **Ajouter une application WASM** pour ouvrir la boîte de dialogue **Publier une application Panel sans serveur**.
2. Saisissez un **Nom de l'application** et une **Version**.
3. Choisissez l'**Emplacement HTML de l'application** : le fichier HTML dans un compte de documents.
4. Saisissez un **Slug d'URL de l'application** et, éventuellement, un **Mémo**.
5. Cliquez sur **Publier**. Une application WASM n'a pas d'étape de build et est servie immédiatement.
