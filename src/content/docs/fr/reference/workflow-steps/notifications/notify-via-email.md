---
title: Notify Via Email
description: Envoyez des notifications par e-mail depuis une étape de workflow PlaidCloud, avec objet, corps, destinataires et options de pièces jointes personnalisables.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-email.md
---

## Description


Envoie des notifications par e-mail. Les messages sont envoyés depuis le compte de messagerie *[info@tartansolutions.com](mailto:info@tartansolutions.com)*. Aucune configuration de messagerie sortante n'est nécessaire.



### Adresses e-mail


Indiquez autant de destinataires que vous le souhaitez. Les séparateurs acceptés comprennent le point-virgule (;) et la virgule (,).



### Cc, Cci et Répondre à

**Cc** (`cc_address`), **Cci** (`bcc_address`) et **Répondre à** (`reply_to`) acceptent des adresses au même format que les destinataires, ainsi que les variables du projet et du workflow. Les destinataires en Cc et en Cci reçoivent le même message, et les réponses sont envoyées à l'adresse Répondre à. Ces champs s'appliquent aux corps en texte brut comme aux corps en modèle Jinja. Définissez-les dans **Autres options d'e-mail**, sous l'onglet **Message**.

### Un e-mail pour chaque ligne

Dans **Autres options d'e-mail**, définissez **Envoyer** (`request_source`) sur **Un e-mail par ligne d'une table** (`table`) et choisissez une **Table d'inducteurs** (`driver_table`) pour envoyer un e-mail pour chaque ligne d'une table au lieu d'un seul e-mail. **Nombre maximal de lignes à envoyer** (`row_limit`) plafonne le nombre de lignes utilisées et vaut 10 000 par défaut. L'inducteur doit être une table, et non une vue.

Utilisez `{{row.column}}` dans les adresses, l'objet, le message et le chemin de la pièce jointe pour insérer la valeur de chaque ligne. Une colonne que la table d'inducteurs ne contient pas fait échouer l'étape. Une ligne sans adresse À n'envoie rien pour cette ligne, et l'étape se termine par un avertissement qui la nomme.

Un chemin de pièce jointe renseigné à partir d'une ligne (`{{row.column}}`) doit désigner un seul fichier existant, jamais un dossier, afin qu'une ligne dont le chemin serait erroné ne puisse pas envoyer les fichiers de quelqu'un d'autre. Une ligne dont la valeur pour ce chemin est vide, dont le chemin sort de son dossier avec `..`, ou dont le fichier est introuvable est envoyée sans la pièce jointe, avec un avertissement qui nomme la ligne. L'envoi par ligne exige un corps en texte brut et n'est pas disponible avec un corps en modèle Jinja.

### Message


Indiquez l'**Objet** et le **Corps** de votre choix.



À noter : les variables du projet et les variables du workflow sont toutes deux disponibles pour cette transformation, dans la ligne d'objet comme dans le corps du message.



De plus, le code HTML standard est autorisé dans le corps pour personnaliser davantage l'apparence des messages e-mail.


### Pièces jointes


Joindre des fichiers aux e-mails est très simple. Sélectionnez un fichier ou un dossier dans Document pour le joindre. Si vous sélectionnez un dossier, son contenu est joint sous forme de fichiers individuels. La substitution de variables fonctionne avec les chemins, pour mieux contrôler les pièces jointes lors de l'envoi d'e-mails personnalisés.



Pour joindre plusieurs documents, cochez **Ajouter une pièce jointe à l'e-mail** et listez-les sous **Autres pièces jointes** (`attachments`) dans **Autres options d'e-mail**, chacun avec un **ID de compte** et un **Chemin du document** ; ils sont envoyés avec la pièce jointe que vous sélectionnez, et un chemin peut utiliser des variables et des jetons de ligne de la même manière.

### Priorité et texte brut

Dans **Autres options d'e-mail**, **Priorité** (`priority`) marque le message comme **Faible**, **Normale** ou **Élevée** (`low`, `normal`, `high`), et **Envoyer en** (`content_type`) défini sur **Texte brut** (`text`) envoie le corps en texte brut au lieu de **HTML** (`html`, valeur par défaut).

### Corps (modèle Jinja)


Le corps de l'étape est rédigé sous forme de **modèle Jinja** rendu sur un ou plusieurs **cadres**, ce qui produit un e-mail HTML enrichi. Chaque cadre est une sélection nommée sur une seule table : un nom de cadre, une table de workflow, et éventuellement une sélection de colonnes, un filtre where et une agrégation (sans jointures). L'éditeur s'ouvre directement sur ce modèle (la liste des cadres, le corps du modèle, un aperçu en direct et un bouton **M'envoyer un test**), sans bascule entre texte brut et modèle. Un bouton **Mettre en forme** et une palette d'insertion (`render_table(...)` pour un cadre, `{{ cloud }}`, une boucle for et les filtres de devise, de milliers, de pourcentage et de date) aident à façonner le modèle.

Référencez chaque cadre dans le modèle sous la forme `frames['<Frame Name>'].rows` et `frames['<Frame Name>'].columns` ; un modèle à un seul cadre peut utiliser `rows` / `columns` au niveau supérieur, qui sont liés au premier cadre. Le modèle est un moteur de rendu distinct, isolé dans un bac à sable : seul `cloud` est résolu comme valeur de l'espace de travail, et les anciens jetons `{project}` / `{model}` / `{date}` ne sont pas résolus à l'intérieur. Les étapes créées avant la rédaction Jinja s'ouvrent avec leur ancien corps converti automatiquement ; un corps qui ne peut pas être converti en toute sécurité reste en mode texte brut de repli et continue d'envoyer avec l'ancienne substitution de jetons `{token}`. Consultez [Send Templated HTML Email Notifications](/fr/guides/workflows/notify-email-templates/) pour connaître les variables de modèle disponibles, l'assistant `render_table`, les balises et attributs HTML qui survivent au nettoyage des e-mails, et la façon dont les corps existants sont migrés.



## Exemples


Dans cet exemple, toutes les variables système sont utilisées. De plus, un peu de HTML met en forme la première ligne du corps. L'exécution de cette transformation envoie l'e-mail suivant :


* À : [info@tartansolutions.com](mailto:info%40tartansolutions.com)
* De : [info@tartansolutions.com](mailto:info%40tartansolutions.com) (n'oubliez pas que tous les messages proviennent de cette adresse)
* Objet : DEMO – Workflow Analyze Demo Running
