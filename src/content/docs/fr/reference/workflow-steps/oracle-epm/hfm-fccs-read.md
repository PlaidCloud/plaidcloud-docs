---
title: "HFM/FCCS : lire les données (ad hoc)"
description: "Obtenez en libre-service une tranche de données d'Oracle FCCS en construisant un point de vue dans le formulaire de l'étape : la grille renvoyée arrive automatiquement sous forme de table, les extractions répétées sont mises en cache, la colonne Entity est prête pour la sécurité au niveau des lignes, et une cible liée facultative la transforme en chargement récurrent planifié."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/hfm-fccs-read.md
---

## Description

Lit une tranche de données ad hoc depuis Oracle **FCCS** (Financial Consolidation and Close, EPM Cloud) via votre [connexion HFM/FCCS](/fr/guides/connections/hfm-fccs/), par **point de vue (POV)** plutôt qu'en écrivant une requête. Un utilisateur de la finance choisit une application, construit un POV à partir des dimensions FCCS et exécute l'étape ; la grille renvoyée arrive automatiquement sous forme de table de projet (schéma à la lecture : la table est créée à partir des colonnes de la grille). L'étape donne l'impression d'une requête en direct, mais en réalité elle soumet un job d'export à FCCS, le **sonde** jusqu'à son achèvement, puis récupère et dépose le résultat : une tranche de longue durée ne bloque donc rien, et aucun ticket auprès de l'équipe HFM n'est nécessaire.

Cette étape apparaît dans le menu des étapes sous **Oracle EPM (HFM/FCCS)**.

:::note[Limiter la dimension Entité]
Gardez la sélection **Entité** bornée : une extraction sans limite peut verrouiller l'application FCCS pendant longtemps pendant l'exécution du job d'export.
:::

## Configuration

### Source et cible

| Champ | Obligatoire | Remarques |
|---|---|---|
| Connexion HFM/FCCS | Oui | La [connexion HFM/FCCS](/fr/guides/connections/hfm-fccs/) à utiliser pour la lecture. |
| Environnement | Oui | L'environnement de la connexion. |
| Application | Oui | L'application FCCS à lire. Utilise par défaut l'Application par défaut de la connexion, si elle est définie. Le choix de l'application déclenche la découverte en direct des membres pour le POV. |
| Table cible | Oui | La table de projet dans laquelle arrive la grille renvoyée. |

### Point de vue

Construisez la tranche à partir des dimensions FCCS. Sur les pods pris en charge, les listes de membres se remplissent automatiquement à partir de la découverte des métadonnées en direct dès qu'une connexion et une application sont choisies ; sur les pods plus anciens, vous saisissez les noms de membres manuellement.

| Dimension | Obligatoire | Remarques |
|---|---|---|
| Scénario | Oui | |
| Année | Oui | |
| Période | Oui | |
| Entité | Bornée | Doit désigner une tranche bornée : le formulaire rejette une sélection vide, « all » ou une sélection de plus de 500 membres. Gardez-la limitée pour que l'export ne verrouille pas l'application. |
| Compte | Non | |
| Custom1–Custom4 | Non | Les dimensions personnalisées de l'application. |
| ICP | Non | Intersociétés. |
| Vue | Non | |
| Valeur | Non | |

Une dimension facultative non définie n'applique aucun filtre sur cet axe (le membre par défaut de FCCS est utilisé).

### Cible liée

Désactivée par défaut : chaque exécution dépose une tranche ad hoc qui écrase la table cible.

| Champ | Remarques |
|---|---|
| Cible liée (chargement récurrent planifié) | Lorsqu'elle est cochée, la cible devient une table **persistante** : l'étape y fusionne les données par un upsert à clé au lieu de l'écraser, et le schéma s'enrichit de façon additive lorsqu'une grille ultérieure apporte de nouvelles colonnes (une nouvelle colonne déclenche un avertissement, jamais un échec). Placer l'étape dans un workflow planifié donne alors un chargement récurrent qui accumule les données au lieu de les effacer. |
| Colonnes clés | Activé uniquement lorsque Cible liée est activée. Colonnes séparées par des virgules qui forment la clé de fusion (par exemple `Entity, Account`). **Laissez-le vide** pour utiliser comme clé de fusion les colonnes de dimensions du POV présentes dans la grille déposée. |

## Fonctionnement

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 130" role="img" aria-label="L'étape soumet un job d'export à FCCS, le sonde jusqu'à son achèvement, récupère la grille et la dépose sous forme de table ; un point de vue répété est servi à partir de la table en cache." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="hf-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="58" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Soumettre</text>
<rect x="150" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="198" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Sonder</text>
<rect x="290" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="338" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Récupérer</text>
<rect x="430" y="46" width="120" height="40" rx="7" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" /><text x="490" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Créer la table</text>
<path d="M106 66 L150 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M246 66 L290 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M386 66 L430 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<text x="198" y="34" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">pendant l'exécution…</text>
<rect x="590" y="46" width="120" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="650" y="64" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">POV répété</text><text x="650" y="78" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">servi depuis le cache</text>
<path d="M550 82 C570 100 630 100 650 88" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="4 3" marker-end="url(#hf-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Une exécution soumet un job d'export, le sonde, récupère la grille et dépose une table. Le même point de vue demandé de nouveau est servi à partir de la copie déjà déposée.</figcaption>
</figure>

Pendant l'exécution du job, l'étape affiche un état d'interrogation. Lorsque le résultat est déposé, la table est créée à partir des colonnes de la grille : aucun schéma à définir au préalable.

## Mise en cache

Le même POV demandé de nouveau est **servi à partir de la table déjà déposée**, instantanément, au lieu de soumettre à nouveau l'export à FCCS. Une exécution est identifiée par l'application, la table cible, le point de vue et une étiquette **as-of** (valeur par défaut `latest`) ; une répétition qui correspond à une tranche déjà déposée signale que la table a été laissée en place plutôt que réécrite. Modifiez l'étiquette as-of pour forcer une nouvelle extraction du même POV.

## Sécurité au niveau des lignes

L'axe des entités de la grille déposée est normalisé dans une colonne nommée exactement **`Entity`** : la table est donc **prête pour la sécurité au niveau des lignes**. Un administrateur peut la gouverner avec l'[Accès aux lignes](/fr/administration/access/managing-security-groups-and-assignments/) afin que les utilisateurs en libre-service ne voient que les entités auxquelles ils ont droit.

Cette gouvernance est **placée sous le contrôle d'un administrateur et n'est pas automatique**. Comme l'extraction s'exécute sous le compte de service de la connexion, PlaidCloud ne laisse pas l'étape déclarer sa propre sécurité. Un administrateur suit le workflow standard d'accès aux lignes :

1. **Publier** la table déposée pour le reporting.
2. **Déclarer** la colonne `Entity` comme attribut de gouvernance (refus par défaut).
3. **Approuver** la première écriture gouvernée.
4. **Réconcilier** pour que les autorisations prennent effet.

Tant qu'un administrateur n'a pas effectué ces opérations, la table n'est pas filtrée. Consultez [Gestion des groupes de sécurité et des affectations](/fr/administration/access/managing-security-groups-and-assignments/).

## Limites des fonctionnalités

| Limitation | Signification |
|---|---|
| Lecture seule | Extrait une tranche de FCCS. N'écrit pas de données de consolidation, n'exécute pas de consolidations et ne comptabilise rien en retour. |
| Entité bornée obligatoire | Le formulaire rejette une sélection d'entités vide, « all » ou de plus de 500 membres, et un membre agrégé unique peut tout de même s'étendre côté serveur : gardez la tranche limitée. |
| Membres manuels sur les pods plus anciens | Lorsqu'un pod n'expose pas le point de terminaison des métadonnées, les listes de membres ne se remplissent pas automatiquement ; saisissez les noms de membres à la main. |
| Sécurité au niveau des lignes gouvernée par un administrateur | La colonne `Entity` est prête pour la sécurité au niveau des lignes, mais un administrateur doit publier, déclarer, approuver la première écriture et réconcilier avant que la table ne soit filtrée. |

## Voir aussi

- [Extraire depuis HFM / FCCS (guide)](/fr/guides/connections/hfm-fccs/) : la procédure complète.
- [Connecteur HFM / FCCS](/fr/reference/connectors/rest/hfm-fccs/) : référence des champs de connexion.
- [Étapes Oracle EPM (HFM / FCCS)](/fr/reference/workflow-steps/oracle-epm/)
- [Gestion des groupes de sécurité et des affectations](/fr/administration/access/managing-security-groups-and-assignments/)
