---
title: Panel Studio
description: Créez, modifiez, prévisualisez et publiez des applications Panel sans quitter PlaidCloud, puis restaurez une version antérieure, consultez l'utilisation et la rapidité de l'application, configurez des alertes et des résumés, référencez-la dans la galerie et épinglez-la à Accueil.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/studio.md
---

Panel Studio est l'éditeur d'applications Panel dans PlaidCloud. Il affiche les fichiers de l'application à côté d'un éditeur, construit un aperçu privé que vous pouvez ouvrir et publie l'application lorsque vous êtes prêt. Vous n'avez pas besoin d'un dépôt Git pour commencer.

## Ouvrir Panel Studio

- Sur le tableau **Accueil** d'un projet, choisissez **Open in Studio** sur une application Panel.
- Dans **Mes applications Panel**, choisissez **Open in Studio** sur la ligne d'une application.

Pour démarrer une nouvelle application, choisissez **Create app** à l'un ou l'autre de ces endroits.

## Créer une application

La boîte de dialogue **Create app** vous propose de partir de l'une de cinq sources :

| Partir de | Vous obtenez |
|---|---|
| **Vierge** | Une application minimale avec un `app.py` et un `requirements.txt`. |
| **Table** | Une application construite sur la table que vous choisissez. |
| **Vue** | La même chose, construite sur une vue du projet. |
| **Modèle** | Une application prête à l'emploi issue du [kit d'applications Panel](/fr/guides/panel-apps/app-kit/#partir-dun-modèle). |
| **Depuis la galerie** | Une copie d'une application que votre espace de travail a référencée dans la [galerie d'applications](/fr/guides/panel-apps/gallery/). |

Nommez l'application, choisissez son **Projet** et choisissez **Créer**. Studio ouvre la nouvelle application, avec ses fichiers listés à gauche.

## Modifier

Choisissez un fichier dans la liste pour le modifier dans l'éditeur. Listez vos dépendances Python dans `requirements.txt`, un paquet par ligne. Elles sont installées lorsque l'application est construite.

Choisissez **Ask Weave** pour que Weave écrive ou modifie l'application à votre place. Consultez [Créer des applications Panel avec Weave](/fr/guides/panel-apps/build-with-weave/).

## Enregistrer, prévisualiser et publier

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 150" role="img" aria-label="L'enregistrement conserve un brouillon que vous seul pouvez voir. L'aperçu construit une copie privée du brouillon pour l'éditeur. La publication remplace l'application en ligne après votre confirmation." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="ps-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="10" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="95" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Enregistrer</text>
  <text x="95" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">brouillon uniquement</text>
  <path d="M180 70 L238 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="240" y="40" width="170" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="325" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Aperçu</text>
  <text x="325" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">éditeur uniquement</text>
  <path d="M410 70 L468 70" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#ps-arrow)" />
  <rect x="470" y="40" width="170" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="555" y="66" text-anchor="middle" font-size="13" fill="var(--sl-color-text)">Publier</text>
  <text x="555" y="86" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">l'application en ligne</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Vos modifications n'atteignent les lecteurs que lorsque vous publiez.</figcaption>
</figure>

### Enregistrer

**Enregistrer** stocke vos modifications sous forme de brouillon. L'application en ligne ne change pas, et personne d'autre ne voit le brouillon.

### Aperçu

**Aperçu** construit votre brouillon enregistré sous forme de copie privée et l'ouvre. Seuls les éditeurs de l'application peuvent ouvrir un aperçu.

- Un aperçu est supprimé après 24 heures sans enregistrement.
- Un espace de travail peut avoir jusqu'à 10 aperçus à la fois.
- Enregistrez de nouveau et choisissez **Aperçu** pour voir vos dernières modifications.

### Publier

**Publier** remplace l'application en ligne par votre brouillon enregistré. Cela nécessite l'autorisation de modification sur le projet de l'application, et Studio vous demande d'abord de confirmer.

Si quelqu'un d'autre a publié une modification après que vous avez ouvert l'application, Studio signale un conflit au lieu d'écraser son travail. Rechargez l'application, reportez vos modifications et publiez de nouveau.

## Statut de build et erreurs

L'onglet **Build** affiche le statut du dernier build et se met à jour pendant son exécution. Lorsqu'un build échoue, l'onglet liste chaque erreur avec son fichier et son numéro de ligne, ce qui vous permet d'aller directement à la ligne concernée. Les problèmes de dépendances dans `requirements.txt` s'accompagnent d'une indication pour les corriger.

Les erreurs et les avertissements sont aussi signalés sur leurs lignes dans l'éditeur : vous voyez ainsi un problème là où il se trouve.

Pour la signification de chaque statut une fois l'application publiée, consultez [Utiliser une application Panel](/fr/guides/panel-apps/using/#état-de-génération-applications-serveur).

## Historique et restauration

L'onglet **Historique** liste chaque version publiée de l'application, de la plus récente à la plus ancienne, avec son statut de build. Choisissez **Charger plus** pour voir les plus anciennes.

Pour revenir à une version antérieure, choisissez **Restaurer** sur celle-ci et confirmez. La version restaurée devient l'application en ligne et est reconstruite. Votre brouillon non enregistré n'est pas perdu : il reste dans le brouillon et sera mis en ligne par-dessus la version restaurée à votre prochaine publication. Si l'application correspond déjà à cette version, Studio l'indique et ne change rien. Si quelqu'un a publié pendant que vous restauriez, Studio ne restaure rien et vous demande de réessayer.

## Analyses

L'onglet **Analyses** montre comment les gens utilisent l'application et avec quelle rapidité elle répond. Choisissez les 7, 14 ou 30 derniers jours.

| Section | Affiche |
|---|---|
| **Vues par jour** | Combien de fois l'application a été ouverte chaque jour. |
| **Chargement de page** | Le temps de chargement médian, et le temps que 95 % des chargements ne dépassent pas, à partir des chargements de page de la période. |
| **Requêtes les plus lentes** | Les requêtes qui ont pris le plus de temps, avec leur fréquence d'exécution et leurs temps médian, de fin de distribution et maximal. |
| **Erreurs** | Ce qui s'est mal passé durant la période, par type d'erreur et par endroit de l'application où cela s'est produit. |

Lorsqu'une période contient plus d'activité que ce que les Analyses peuvent lire, elles indiquent que les chiffres sont partiels. Lorsque des chargements de page dépassent le [budget de performance](/fr/guides/panel-apps/app-kit/#budgets-de-performance) de l'application, les Analyses vous avertissent du nombre de chargements concernés et des requêtes lentes. Les Analyses n'affichent jamais les données renvoyées par une requête ni les noms des personnes qui ont ouvert l'application.

Les deux onglets nécessitent que l'application soit affectée à un projet ; une application non affectée affiche une invite pour l'affecter.

## Alertes et résumés

Choisissez **Alerts & Digests** pour configurer des notifications qui surveillent un chiffre dans les données de l'application et vous préviennent lorsqu'il franchit un seuil, ou qui envoient un résumé selon une planification. Consultez [Alertes et résumés](/fr/guides/panel-apps/alerts-and-digests/).

## Référencer une application dans la galerie

Choisissez **Gallery…** pour référencer l'application comme modèle à partir duquel toute personne pouvant consulter son projet peut créer sa propre application, ou pour la retirer de la galerie. Consultez [La galerie d'applications](/fr/guides/panel-apps/gallery/).

## Épingler à Accueil

Choisissez **Pin to Home** pour ajouter l'application au tableau **Accueil** du projet, et **Unpin from Home** pour la retirer.

## Supprimer une application

La suppression d'une application Panel vous demande d'abord de confirmer. Dans **Mes applications Panel**, utilisez l'icône **moins** sur la ligne de l'application. Dépublier demande également une confirmation.

## Étapes suivantes

- [Créer des applications Panel avec Weave](/fr/guides/panel-apps/build-with-weave/) : décrivez l'application et approuvez la modification exacte.
- [Le kit d'applications Panel](/fr/guides/panel-apps/app-kit/) : les composants utilisés par les démarrages de Studio à partir d'une table, d'une vue et d'un modèle.
- [Alertes et résumés](/fr/guides/panel-apps/alerts-and-digests/) : prévenez les utilisateurs lorsqu'un chiffre franchit un seuil, ou selon une planification.
- [La galerie d'applications](/fr/guides/panel-apps/gallery/) : partagez une application comme point de départ pour d'autres.
- [Utiliser une application Panel](/fr/guides/panel-apps/using/) : journaux, utilisation et reconstructions après la publication.
