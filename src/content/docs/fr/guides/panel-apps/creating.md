---
title: Créer une application Panel
description: "Créez une application Panel dans Panel Studio, à partir d'une application vierge, d'une table, d'une vue ou de la galerie, ou publiez une application serveur depuis git ou une application WASM statique pour des besoins sur mesure."
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/creating.md
---

Commencez par Panel Studio. Il ne nécessite ni dépôt ni configuration : vous construisez l'application dans PlaidCloud, vous la prévisualisez et vous la publiez lorsque vous êtes prêt. Ne choisissez un environnement d'exécution sur mesure que lorsque Studio ne convient pas.

## Créer une application Studio

Ouvrez **Mes applications Panel**. **Nouvelle application Studio** est le premier bouton de la barre d'outils. Vous pouvez aussi choisir **Nouvelle application Studio** dans la zone **Applications Panel** de l'onglet **Accueil** d'un projet, ou [partir d'une table](#partir-dune-table).

1. Choisissez **Nouvelle application Studio**.
2. Saisissez un **Nom**. Le **Slug d'URL** se remplit à partir de celui-ci.
3. Sélectionnez le **Projet** propriétaire de l'application. Vous devez disposer d'un accès en modification au projet.
4. Sous **Partir de**, choisissez le point de départ de l'application :

   | Partir de | Vous obtenez |
   |---|---|
   | **Application vierge** | Une application minimale avec un `app.py` et un `requirements.txt`. |
   | **À partir d’une table** | Une application construite sur la table que vous sélectionnez. |
   | **À partir d’une vue** | La même, construite sur une vue du projet. |
   | **À partir d’une autre application Studio** | Une copie de l'une de vos applications Studio. |
   | **À partir de la galerie** | Une copie d'une application que votre espace de travail a [listée dans la galerie](#partir-de-la-galerie). |

5. Choisissez **Créer**. Studio ouvre la nouvelle application. Pour une table ou une vue, l'invite de Weave pour construire la première page est prête à être envoyée.

Consultez [Panel Studio](/fr/guides/panel-apps/studio/) pour modifier, prévisualiser et publier l'application.

### Partir d'une table

Vous pouvez aussi commencer depuis l'onglet **Tables** d'un projet. Sélectionnez une table ou une vue, puis choisissez **Créer une application Panel** dans le menu **Nouveau** ou dans le menu contextuel. La boîte de dialogue **Nouvelle application Studio** s'ouvre avec le projet et la table déjà choisis. La commande est disponible lorsque vous disposez d'un accès en modification au projet et que celui-ci n'est pas en lecture seule.

### Partir de la galerie

Choisissez **Galerie** dans la barre d'outils **Mes applications Panel** pour parcourir les applications que votre espace de travail a listées, puis **Créer une application à partir de ceci…** pour en faire votre propre copie. Ou choisissez **À partir de la galerie** dans la boîte de dialogue **Nouvelle application Studio**. Consultez [La galerie d'applications](/fr/guides/panel-apps/gallery/), y compris la façon de lister votre propre application.

## Autres environnements d'exécution

Les applications Studio couvrent la plupart des tableaux de bord et des outils. Pour un besoin sur mesure, publiez avec l'un des autres [environnements d'exécution](/fr/guides/panel-apps/) depuis la barre d'outils **Mes applications Panel** :

- **Ajouter une application WASM** : publiez une application statique exécutée dans le navigateur à partir d'un fichier.
- **Nouvelle application serveur** : construisez et exécutez une application à partir d'un dépôt git que vous gérez, par exemple pour réutiliser du code existant ou votre propre processus de compilation.
- **Nouvelle application Dash** : publiez une application Plotly Dash. Consultez [Applications Dash](/fr/guides/dash-apps/).

## Créer une application serveur

Une application serveur est construite à partir d'un dépôt git et servie à l'adresse `https://<your-tenant-host>/serve/<slug>/`. Vous indiquez à PlaidCloud une branche d'un dépôt ; il compile le code dans un conteneur, exécute `panel serve` dessus et recompile automatiquement chaque fois que vous poussez des modifications vers cette branche.

### Préparer le dépôt de votre application

Votre dépôt a besoin de deux éléments : un **point d'entrée** — un fichier Python qui construit une application Panel et la marque `.servable()` — et, facultativement, un fichier **`requirements.txt`** listant les paquets supplémentaires, soit à la racine du dépôt, soit à côté de votre point d'entrée.

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

Voilà une application complète. L'appel `.servable()` est ce que PlaidCloud sert : tout ce que vous voulez afficher doit être marqué comme servable (directement, ou en se trouvant dans une disposition servable).

#### Un exemple un peu plus riche

Les applications Panel sont interactives. Celle-ci ajoute un curseur qui met à jour une table en direct :

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

Ce deuxième exemple importe `pandas`, qui ne fait pas partie de l'image de base ; ajoutez donc un `requirements.txt` (à la racine du dépôt, ou à côté de votre point d'entrée) :

```text
pandas
```

PlaidCloud les installe avec `pip` lors de la compilation de l'image. Les bibliothèques de visualisation courantes — `plotly`, `holoviews`, `hvplot` — ne figurent pas non plus dans l'image de base ; listez donc ici celles que votre application importe.

> **Ce que la plateforme fournit — et attend.** Gardez ces hypothèses à l'esprit lorsque vous écrivez votre application :
>
> - **`panel` et `bokeh` sont préinstallés** par l'image de base de la plateforme. Ne les listez pas dans `requirements.txt` et évitez d'épingler une version plus ancienne de Panel — la reconnexion de mise à jour en direct repose sur une version récente.
> - **Les bibliothèques clientes PlaidCloud (`plaidcloud-rpc`, `plaidcloud-utilities`) sont préinstallées.** Importez directement `plaidcloud.rpc` ou `plaidcloud.utilities` — ne les listez pas dans `requirements.txt`.
> - **`requirements.txt` peut se trouver à la racine du dépôt ou à côté de votre point d'entrée.** Dans un dépôt partagé (monorepo), conservez les dépendances de chaque application dans son propre dossier. Un fichier à la racine, s'il existe, est également installé — placez-y les dépendances partagées et placez celles propres à l'application à côté de celle-ci.
> - **L'application s'exécute sous un utilisateur non root sur un système de fichiers en lecture seule.** Seul `/tmp` est accessible en écriture ; écrivez-y donc tous les fichiers temporaires (la plupart des bibliothèques respectent déjà `$TMPDIR`).
> - **Ne codez pas en dur le port, le préfixe d'URL ni l'hôte.** PlaidCloud les attribue et les injecte au moment du déploiement — appelez simplement `.servable()`.

Pour obtenir l'apparence PlaidCloud ainsi que des filtres, des grilles et des graphiques prêts à l'emploi, construisez votre application avec [le kit d'applications Panel](/fr/guides/panel-apps/app-kit/).

### Définir le thème : clair, sombre ou commutateur

Les applications serveur s'affichent par défaut dans le design moderne **Fast** de PlaidCloud — un style épuré de type Fluent appliqué à toute la plateforme. Dans la boîte de dialogue de publication, **Conception** contrôle cette couche de plateforme :

- **FAST** : la valeur par défaut de PlaidCloud. Utilisez-la pour les nouvelles applications et celles construites avec des modèles Fast.
- **Par défaut** : le style par défaut de Panel. Utilisez-le lorsque le CSS ou les visuels d'une application existante se dégradent sous FAST.

Ce que vous contrôlez dans le code de votre application, c'est le **thème** : clair, sombre ou un commutateur que le lecteur peut basculer.

Le thème est une propriété du **modèle** que vous servez. Les modèles Fast — `FastListTemplate` (une seule colonne) et `FastGridTemplate` (une grille adaptative) — acceptent deux paramètres pour cela :

- **`theme`** : `"default"` pour le thème clair ou `"dark"`. Le définir épingle l'application à ce thème, même si un lecteur ajoute `?theme=dark` à l'URL.
- **`theme_toggle`** : `True` affiche un commutateur clair/sombre dans l'en-tête ; `False` le masque. La valeur par défaut est `True`. Masquer le commutateur ne fixe pas le thème à lui seul — épinglez-le avec `theme` (ci-dessus) ; définissez `theme_toggle=False` une fois cela fait, afin que les lecteurs ne voient pas un commutateur qui ne change rien.

Choisissez le schéma qui convient à votre application.

**Clair uniquement** — idéal pour les rapports denses et les tables financières, généralement mis en forme à la main pour un fond clair :

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

**Sombre uniquement :**

```python
pn.template.FastListTemplate(
    title="Ops Monitor",
    theme="dark",
    theme_toggle=False,
    main=[...],
).servable()
```

**Laisser le lecteur choisir** — clair par défaut, avec un commutateur dans l'en-tête. Omettez `theme` pour que l'application suive le commutateur :

```python
pn.template.FastListTemplate(
    title="Explorer",
    theme_toggle=True,
    main=[...],
).servable()
```

> **Si vous autorisez le thème sombre, adaptez vos tables.** Un `Tabulator` épinglé à un thème de table clair (`theme="bootstrap"`), ou un CSS personnalisé avec des couleurs claires codées en dur comme `background: #fff`, s'affiche comme un bloc blanc illisible sur une page sombre. Utilisez un thème de table qui suit l'application — `pn.widgets.Tabulator(..., theme="fast")` — et évitez les couleurs claires codées en dur. Si un rapport est fortement mis en forme à la main pour le thème clair, épinglez-le plutôt au thème clair (le premier schéma ci-dessus).

Une application simple sans modèle — `pn.Column(...).servable()` — suit le comportement par défaut de Panel et n'est pas affectée par ces paramètres ; recourez à un modèle lorsque vous voulez un contrôle explicite.

Votre dépôt doit être accessible via une **connexion git** dans PlaidCloud. Si votre code se trouve dans [PlaidCloud Git](/fr/guides/git/), créez une connexion gérée **PlaidCloud Git** sous **Tools > Connections** — elle ne nécessite ni URL de serveur ni identifiants. Pour le parcours complet, d'un dépôt vide à une application servie, consultez [Déployer une application Panel depuis PlaidCloud Git](/fr/guides/panel-apps/deploy-from-git/).

### Publier l'application

1. Cliquez sur **Nouvelle application serveur** pour ouvrir la boîte de dialogue **Publier une application Panel serveur**. Ses paramètres sont regroupés en sections.
2. Sous **Paramètres du répertoire** :
   - **Nom de l'application** : le nom d'affichage indiqué dans la liste.
   - **Slug d'URL** : à la fois l'URL de l'application et son nom interne ; il doit donc être une étiquette DNS valide : lettres minuscules, chiffres et traits d'union, en commençant par une lettre, 40 caractères au maximum (par exemple, `sales-dashboard`). La boîte de dialogue le vérifie avant la publication.
   - **Mémo** : une description facultative.
   - **Projet** : le projet propriétaire de l'application. Il fournit l'[identité visuelle](/fr/guides/panel-apps/branding/) de l'application et constitue le projet par défaut de ses tables. Vous ne pouvez pas le modifier ici après la publication ; utilisez [Assign](/fr/guides/panel-apps/branding/#pour-les-applications-existantes).
3. Sous **Connexion Git et observateur de publication** :
   - **Connexion Git** : la connexion qui contient le dépôt de votre application.
   - **Branche** : la branche à partir de laquelle compiler. Les poussées vers cette branche recompilent et redéploient automatiquement l'application.
   - **Point d'entrée** : le fichier `.py` que Panel doit servir (votre `app.py`).
4. Sous **Exécution** :
   - **CPU** et **Mémoire** que le conteneur de l'application doit demander.

     > Moins de ressources (CPU / mémoire plus faibles) permettent à l'application d'être planifiée et de démarrer à froid plus rapidement.

   - **Conception** : choisissez **FAST** pour le design moderne de PlaidCloud, ou **Par défaut** si le CSS de l'application attend le style par défaut de Panel.
   - **Inactivité (minutes)** : durée pendant laquelle l'application reste active sans trafic avant de revenir à zéro. La valeur par défaut est de 5 minutes.
   - **Autoriser l'accès public** : cochez cette case pour autoriser l'accès non authentifié ; sinon, les lecteurs doivent se connecter à votre locataire.
5. Sous **Avancé (diffusion intégrée)** — facultatif. Par défaut, l'application n'est servie que depuis votre locataire PlaidCloud. Pour l'intégrer dans un autre site, cliquez sur **Ajouter un domaine** et saisissez chaque domaine autorisé à la charger, un par ligne — un hôte uniquement, sans schéma ni chemin (par exemple, `example.com` ou `app.example.com:8443`). Laissez la liste vide, sauf si vous intégrez l'application ailleurs.
6. Cliquez sur **Publier**.

Après la publication, l'application est **compilée** — son **Statut** s'affiche dans la liste et se met à jour automatiquement. Consultez [Utiliser une application Panel](/fr/guides/panel-apps/using/) pour connaître la signification des statuts, la façon d'ouvrir l'application une fois qu'elle est prête et celle de déclencher une recompilation sans annuler la publication.

> L'URL de l'application ne fonctionne qu'une fois son statut de compilation **Prêt** ; la première requête après une période d'inactivité la réveille (~15 secondes).

### Avancé : reproduire PlaidCloud en local

Les utilisateurs techniques peuvent compiler et tester l'application avec les mêmes entrées que PlaidCloud. C'est la vérification locale la plus proche avant de publier ou de cliquer sur **Régénérer**.

PlaidCloud compile à partir de la branche git sélectionnée avec ce Dockerfile généré. Utilisez le même contenu en local sous le nom `Dockerfile.plaidcloud-panel` :

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

Pour reproduire la compilation du serveur :

1. Extrayez la même branche que celle que vous sélectionnez dans **Branche**.
2. Lancez la compilation depuis la racine du dépôt, afin que `COPY . /app` corresponde à PlaidCloud.
3. Placez les dépendances facultatives dans un `requirements.txt` — à la racine du dépôt ou à côté de votre point d'entrée. Les deux sont installés, celui du dossier de l'application en dernier (ce qui fait prévaloir une version épinglée propre à l'application).
4. Utilisez le même chemin de point d'entrée que celui que vous sélectionnez dans **Point d'entrée**.

```sh
docker build \
  -f Dockerfile.plaidcloud-panel \
  -t local-panel-app:plaidcloud \
  .
```

L'image déployée ne remplace pas le point d'entrée de l'image de base. Elle exécute `panel serve` à partir de variables d'environnement injectées par PlaidCloud. Testez l'image compilée avec le même contrat d'exécution :

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

Faites correspondre les paramètres de la boîte de dialogue de publication lors de vos tests :

- **Point d'entrée** correspond à `APP_PATH=/app/<entry-point>`.
- **CPU** et **Mémoire** correspondent aux limites `--cpus` et `--memory` de Docker.
- **Conception : FAST** correspond à `PLAID_PANEL_DESIGN=fast`.
- **Conception : Par défaut** signifie qu'il faut omettre `PLAID_PANEL_DESIGN`.
- **Inactivité (minutes)** correspond à la fenêtre de réduction d'échelle du déploiement. Docker en local ne l'applique pas, mais l'application utilise tout de même les mêmes paramètres de maintien de connexion websocket et de nettoyage de session de Panel.
- Les domaines de **diffusion intégrée** correspondent à `PANEL_ORIGIN` ; utilisez une liste séparée par des espaces si vous devez tester plusieurs hôtes.

Si vous n'avez pas besoin d'un conteneur, vous pouvez tout de même tester la couche de service depuis un environnement Python local. Installez le même `requirements.txt`, définissez les variables d'environnement de la plateforme, puis exécutez `panel serve` avec les mêmes options que l'image déployée.

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

Une application WASM s'exécute dans le navigateur à partir d'un fichier HTML précompilé.

1. Cliquez sur **Ajouter une application WASM** pour ouvrir la boîte de dialogue **Publier une application Panel sans serveur**.
2. Saisissez un **Nom de l'application** et une **Version**.
3. Choisissez l'**Emplacement HTML de l'application** — le fichier HTML d'un compte de documents.
4. Saisissez un **Slug d'URL de l'application** et un **Mémo** facultatif.
5. Cliquez sur **Publier**. Une application WASM n'a pas d'étape de compilation et est servie immédiatement.
