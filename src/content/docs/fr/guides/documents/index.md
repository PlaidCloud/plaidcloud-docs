---
title: Gestion des fichiers
description: Gérez dans PlaidCloud les comptes de stockage de fichiers servant à importer et exporter des données aux formats CSV, Excel, Parquet et autres.
sidebar:
  label: Vue d'ensemble
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/index.md
---

PlaidCloud Documents — stockez, organisez, recherchez et partagez des fichiers aux côtés de vos données et de vos workflows. Les documents peuvent provenir de n'importe quel compte de stockage connecté et être référencés dans les workflows.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="Des comptes de stockage connectés, tels que S3, Google Cloud Storage et OneDrive, alimentent PlaidCloud Documents, où les fichiers sont stockés, organisés, recherchés et partagés. Les étapes de workflow référencent ensuite ces fichiers pour importer et exporter des données." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="dc-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">comptes de stockage</text>
  <rect x="16" y="40" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="60" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">S3</text>
  <rect x="16" y="82" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Cloud Storage</text>
  <rect x="16" y="124" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">OneDrive</text>
  <path d="M136 55 C186 55 206 92 246 96" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 97 L246 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 139 C186 139 206 108 246 104" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="248" y="70" width="180" height="64" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="338" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Documents</text>
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">stocker · organiser · rechercher · partager</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">étapes de workflow</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">importer · exporter des fichiers</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Les fichiers arrivent dans Documents depuis n'importe quel compte de stockage connecté, où vous les stockez, organisez, recherchez et partagez, puis vous les référencez dans des étapes de workflow pour importer et exporter des données.</figcaption>
</figure>

## L'espace Documents

**Document** s'ouvre avec un rail à gauche et, à côté, la page que vous choisissez. Le rail regroupe ses pages sous **Documents** (**Vue d'ensemble** et **Parcourir**) et **Comptes** (**Vos comptes** et **Gérer**). Les membres qui ne peuvent pas ouvrir une page ne voient pas l'élément correspondant. Les pages ont un titre en haut, souvent accompagné d'un court sous-titre, et leurs actions dans l'en-tête à côté.

| Élément du rail | Contenu affiché |
|---|---|
| **Vue d'ensemble** | Des vignettes pour vos comptes (**Comptes**, qui ouvre **Vos comptes**, **Buckets gérés**, **Services externes** et **Désactivé**, qui porte l'étiquette **Nécessite une attention** et ouvre **Gérer** lorsqu'un compte dont vous êtes propriétaire est désactivé), les fichiers **Épinglés**, **Comptes par service** et **Qui peut les utiliser**. Sélectionnez un fichier épinglé pour ouvrir **Parcourir** dans son dossier, avec le fichier sélectionné. |
| **Parcourir** | L'explorateur de fichiers. Il ouvre votre compte favori (celui dont vous avez épinglé le dossier racine), ou le compte par défaut de l'espace de travail, et vous pouvez choisir un autre compte dans la liste de l'en-tête de la page. Consultez [Utiliser les comptes de documents](/fr/guides/documents/using-document/). |
| **Vos comptes** | Tous les comptes que vous pouvez utiliser, dans une seule liste. Une pastille **Partagés** ou **Privé** sur chaque ligne indique si le compte est partagé avec vous ou s'il n'est qu'à vous. Double-cliquez sur une ligne pour la parcourir. |
| **Gérer** | Les comptes dont vous êtes propriétaire, avec **Nom**, **Service**, **Type de sécurité**, **Statut** et **Description**. Un administrateur de l'espace de travail voit ici tous les comptes de documents et peut gérer tout compte qu'il peut par ailleurs gérer ; les comptes gérés par le système sont refusés et les comptes de bucket géré ne peuvent pas être clonés. |

Le rail affiche un nombre à côté de **Vos comptes**. La vue d'ensemble propose les boutons **Parcourir les fichiers** et **Nouveau compte** pour démarrer rapidement.

### Actions sur les lignes dans Gérer

Ouvrez le menu **⋯** d'une ligne, cliquez avec le bouton droit sur la ligne ou utilisez le menu **Actions** de la barre d'outils pour accéder à :

- **Ouvrir** et **Modifier**, qui ouvrent la page du compte.
- **Cloner…**, **Historique des versions** et **Où utilisé…**. Consultez [Où utilisé et redirection](/fr/guides/documents/account-management/document-account-used-by/).
- **Qui peut l'utiliser**, avec **Membres**, **Groupes**, **Agents** et **Propriétaires**. Consultez [Contrôler l'accès aux comptes de documents](/fr/guides/documents/account-management/control-document-account-access/).
- **Activer** ou **Désactiver**, et **Supprimer**.

### La page du compte

**Nouveau compte**, **Ouvrir** et **Modifier** affichent le compte sous forme de page, avec **Gérer les comptes** en haut pour revenir en arrière. Elle comporte des cartes pour :

- **Général** : le nom du compte, son service, son bucket et son chemin de départ.
- **Accès** : le modèle de sécurité et les personnes autorisées à utiliser le compte. **Membres**, **Groupes**, **Agents** et **Propriétaires** disposent chacun d'un lien **Modifier** qui ouvre le même sélecteur que le menu de la ligne.
- **Identifiants** : des champs en écriture seule pour le service choisi. Une mention **Identifiants enregistrés** indique que les identifiants sont définis ; les valeurs enregistrées ne sont jamais affichées. Laissez un champ vide pour conserver la valeur enregistrée. Les comptes SFTP disposent également de **Tester la connexion**.
- **SSH** : les paramètres de clé, pour les comptes SFTP uniquement.

L'en-tête comporte **Parcourir**, **Où utilisé** et un menu **Actions** avec **Cloner**, **Historique des versions**, **Activer** ou **Désactiver** et **Supprimer**. Si vous quittez une page dont les modifications ne sont pas enregistrées, PlaidCloud vous demande s'il faut les abandonner.

Les anciens liens et favoris vers les écrans Document ouvrent toujours la page correspondante.
