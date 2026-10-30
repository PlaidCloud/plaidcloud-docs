---
title: Table Faker
description: Générez des données de test synthétiques dans une étape de workflow PlaidCloud à l'aide de Faker, pour créer des jeux de données d'exemple réalistes à des fins de développement.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-faker.md
---

## Description


Table Faker génère de fausses données.



### Adresse




| Générateur | Arguments facultatifs |
| Numéro de rue |  |
| Ville |  |
| Suffixe de ville |  |
| Pays |  |
| Code pays | “representation”=”alpha-2” |
| Adresse complète |  |
| Latitude |  |
| Longitude |  |
| DPO militaire |  |
| Code postal |  |
| Code postal plus 4 |  |
| État |  |
| Abréviation de l'état |  |
| Adresse postale |  |
| Nom de rue |  |
| Suffixe de rue |  |

### Automobile




| Générateur | Arguments facultatifs |
| Plaque d'immatriculation |  |

### Code-barres




| Générateur | Arguments facultatifs |
| EAN13 |  |
| EAN8 |  |

### Couleurs




| Générateur | Arguments facultatifs |
| Nom de couleur |  |
| Couleur hexadécimale |  |
| Couleur RVB |  |
| Couleur RVB CSS |  |
| Nom de couleur web-safe |  |
| Couleur hexadécimale web-safe |  |

### Entreprise




| Générateur | Arguments facultatifs |
| Slogan d'entreprise |  |
| Nom d'entreprise |  |
| Suffixe d'entreprise |  |

### Carte de crédit




| Générateur | Arguments facultatifs |
| Date d'expiration | “start”=”now”“end”=”+10y”## ‘12/20’ |
| Complet | “card_type”=null |
| Numéro | “card_type”=null |
| Émetteur | “card_type”=null |
| Code de sécurité | “card_type”=null |

### Devise




| Générateur | Arguments facultatifs |
| Code |  |

### Date et heure




| Générateur | Arguments facultatifs |
| AM/PM |  |
| Siècle |  |
| Date | “pattern”:”%Y-%m-%d”“end_datetime”:null |
| Date et heure | “tzinfo”:null“end_datetime”=null |
| Date et heure de ce siècle | “before_now”=true“after_now”=false“tzinfo”=null |
| Date et heure de cette décennie | “before_now”=true“after_now”=false“tzinfo”=null |
| Date et heure de ce mois | “before_now”=true“after_now”=false“tzinfo”=null |
| Date et heure de cette année | “before_now”=true“after_now”=false“tzinfo”=null |
| Jour du mois |  |
| Jour de la semaine |  |
| Date et heure ISO8601 | “tzinfo”=null“end_datetime”=null |
| Mois |  |
| Nom du mois |  |
| Date passée (30 derniers jours) | “start_date”=”-30d”“tzinfo”=null |
| Fuseau horaire |  |
| Heure Unix | “end_datetime”=null“start_datetime”=null |
| Année |  |

### Fichier




| Générateur | Arguments facultatifs |
| Extension de fichier | “category”=null |
| Nom du fichier | “category”=null“extension”=null |
| Chemin du fichier | “depth”=”1”“category”=null“extension”=null |
| Type MIME | “category”=null |

### Internet




| Générateur | Arguments facultatifs |
| E-mail d'entreprise |  |
| Nom de domaine |  |
| Mot de domaine |  |
| E-mail |  |
| E-mail gratuit |  |
| Domaine d'e-mail gratuit |  |
| URL d'image | “width”=null“height”=null |
| IPv4 | “network”=false“address_class”=”no”“private”=null |
| IPv6 | “network”=false |
| Adresse MAC |  |
| E-mail sûr |  |
| Slug |  |
| TLD |  |
| URI |  |
| URL | “schemes”=null |
| Extension d'URL |  |
| Page d'URL |  |
| Nom d'utilisateur |  |

### ISBN




| Générateur | Arguments facultatifs |
| ISBN10 | “eparator”=”-“ |
| ISBN13 | “eparator”=”-“ |

### Emploi




| Générateur | Arguments facultatifs |
| Intitulé de poste |  |

### Lorem




| Générateur | Arguments facultatifs |
| Paragraphe | “nb_sentences”=”3”“variable_nb_sentences”=true“ext_word_list”=null |
| Paragraphes | “nb”=”3”“ext_word_list”=null |
| Phrase | “nb_words”=”6”“variable_nb_words”=true“ext_word_list”=null |
| Phrases | “nb”=”3”“ext_word_list”=null |
| Texte | “max_nb_chars”=”200”“ext_word_list”=null |
| Mot | “ext_word_list”=null |
| Mots | “nb”=”3”“ext_word_list”=null |

### Divers




| Générateur | Arguments facultatifs |
| Binaire | “length”=”1048576” |
| Booléen | “chance_of_getting_true”=”50” |
| Booléen nul |  |
| Paramètres régionaux |  |
| Code de langue |  |
| MD5 | “raw_output”=false |
| Mot de passe | “length”=”10”“special_chars”=true“digits”=true“upper_case”=true“lower_case”=true |
| Chaîne aléatoire |  |
| SHA1 | “raw_output”=false |
| SHA256 | “raw_output”=false |
| UUID4 |  |

### Numérique




| Générateur | Arguments facultatifs |
| Grande série (incrément automatique) |  |
| Flottant aléatoire |  |
| Flottant aléatoire dans une plage |  |
| Entier aléatoire |  |
| Entier aléatoire dans une plage |  |
| Nombre aléatoire |  |
| Pourcentage aléatoire (0 – 1) |  |
| Pourcentage aléatoire (0 – 100) |  |
| Série (incrément automatique) |  |

### Personne




| Générateur | Arguments facultatifs |
| Prénom |  |
| Prénom féminin |  |
| Prénom masculin |  |
| Nom complet |  |
| Nom complet féminin |  |
| Nom complet masculin |  |
| Nom de famille |  |
| Nom de famille féminin |  |
| Nom de famille masculin |  |
| Civilité |  |
| Civilité féminine |  |
| Civilité masculine |  |
| Suffixe |  |
| Suffixe féminin |  |
| Suffixe masculin |  |

### Téléphone




| Générateur | Arguments facultatifs |
| Numéro de téléphone |  |
| ISDN |  |

### Fiscalité




| Générateur | Arguments facultatifs |
| EIN |  |
| SSN complet |  |
| ITIN |  |

### Agent utilisateur




| Générateur | Arguments facultatifs |
| Chrome | “version_from”=”13”“version_to”=”63”“build_from”=”800”“build_to”=”899” |
| Firefox |  |
| Agent utilisateur complet |  |
| Internet Explorer |  |
| Jeton de plateforme Linux |  |
| Processeur Linux |  |
| Jeton de plateforme Mac |  |
| Processeur Mac |  |
| Opera |  |
| Safari |  |
| Jeton de plateforme Windows |  |

### Générateurs spéciaux


Bien que ces deux générateurs n'aient pas d'arguments, les options qu'ils proposent jouent un rôle similaire.



**Générateur de motif** :




| Nombre | Format | Sortie | Description |
| 3.1415926 | \{:.2f} | 3.14 | 2 décimales |
| 3.1415926 | \{:+.2f} | +3.14 | 2 décimales avec signe |
| -1 | \{:+.2f} | -1.00 | 2 décimales avec signe |
| 2.71828 | \{:.0f} | 3 | Aucune décimale |
| 5 | \{:0>2d} | 05 | Complète le nombre avec des zéros (remplissage à gauche, largeur 2) |
| 5 | \{:x&lt;4d} | 5xxx | Complète le nombre avec des x (remplissage à droite, largeur 4) |
| 10 | \{:x&lt;4d} | 10xx | Complète le nombre avec des x (remplissage à droite, largeur 4) |
| 1000000 | \{:,} | 1,000,000 | Format numérique avec virgule comme séparateur |
| 0.25 | \{:.2%} | 25.00% | Mise en forme d'un pourcentage |
| 1000000000 | \{:.2e} | 1.00e+09 | Notation exponentielle |
| 13 | \{:10d} | 13 | Aligné à droite (par défaut, largeur 10) |
| 13 | \{:&lt;10d} | 13 | Aligné à gauche (largeur 10) |
| 13 | \{:^10d} | 13 | Centré (largeur 10) |

**Choix aléatoire** :


Pour fournir les options du choix aléatoire, placez simplement vos options entre guillemets et séparez-les par une virgule. Une chaîne d'options de choix aléatoire se présente ainsi : “x”,”y”,”z”



Ici, la colonne « Key Word Args/Pattern/Choices » de la ligne « pattern » contient une phrase comportant plusieurs références. La première équation de référence ( \{percentage0-100:.2f}% ) pointe vers la ligne « percentage0-100 », qui génère une équation aléatoire. Le pourcentage aléatoire produit par la ligne « percentage0-100 » est donc automatiquement inséré dans la phrase. L'équation de référence \{first_name} pointe vers la ligne intitulée « first_name », qui génère aléatoirement un prénom, lequel est automatiquement inséré dans la phrase. La dernière équation de référence ( \{randomn_choice} ) fonctionne de la même manière que les deux autres.



Lorsque le générateur de motif est exécuté, vous obtenez alors les résultats suivants.


## Nombre de lignes depuis une table

Pour reprendre le nombre de lignes à partir des données, définissez **Table contenant le nombre** (`rows_source`) et **Colonne contenant le nombre** (`rows_column`). À l'exécution, l'étape lit le nombre dans la première ligne de la table, dans cette colonne, à la place du nombre de lignes que vous avez défini. Une valeur manquante, ou inférieure à 1, ne génère aucune ligne.

## Contrôles effectués à l'enregistrement

Chaque ligne de **Colonnes de données fictives et types de données** devient une colonne de la table générée ; chacune doit donc avoir son propre nom. L'enregistrement est refusé avec le message *Every fake data column needs a name.* lorsqu'un nom est vide, et avec *Fake data column name 'city' is used more than once; each needs its own.* lorsque deux colonnes portent le même nom.
