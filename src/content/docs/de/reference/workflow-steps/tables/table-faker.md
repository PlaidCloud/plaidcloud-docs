---
title: Table Faker (Schritt)
description: Erzeugen Sie in einem PlaidCloud-Workflow-Schritt mit Faker synthetische Testdaten, um realistische Beispieldatensätze für die Entwicklung zu erstellen.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-faker.md
---

## Beschreibung


Table Faker erzeugt Testdaten.



### Adresse




| Generator | Optionale Argumente |
| Hausnummer |  |
| Stadt |  |
| Stadtsuffix |  |
| Land |  |
| Ländercode | “representation”=”alpha-2” |
| Vollständige Adresse |  |
| Breitengrad |  |
| Längengrad |  |
| Militär-DPO |  |
| Postleitzahl |  |
| Postleitzahl Plus 4 |  |
| Bundesstaat |  |
| Abkürzung des Bundesstaats |  |
| Straßenadresse |  |
| Straßenname |  |
| Straßensuffix |  |

### Automobil




| Generator | Optionale Argumente |
| Kfz-Kennzeichen |  |

### Barcode




| Generator | Optionale Argumente |
| EAN13 |  |
| EAN8 |  |

### Farben




| Generator | Optionale Argumente |
| Farbname |  |
| Hex-Farbe |  |
| RGB-Farbe |  |
| RGB-CSS-Farbe |  |
| Sicherer Farbname |  |
| Sichere Hex-Farbe |  |

### Unternehmen




| Generator | Optionale Argumente |
| Firmenslogan |  |
| Firmenname |  |
| Firmensuffix |  |

### Kreditkarte




| Generator | Optionale Argumente |
| Ablaufdatum | “start”=”now”“end”=”+10y”## ‘12/20’ |
| Vollständig | “card_type”=null |
| Nummer | “card_type”=null |
| Anbieter | “card_type”=null |
| Sicherheitscode | “card_type”=null |

### Währung




| Generator | Optionale Argumente |
| Code |  |

### Datum und Uhrzeit




| Generator | Optionale Argumente |
| AM/PM |  |
| Jahrhundert |  |
| Datum | “pattern”:”%Y-%m-%d”“end_datetime”:null |
| Datum und Uhrzeit | “tzinfo”:null“end_datetime”=null |
| Datum und Uhrzeit in diesem Jahrhundert | “before_now”=true“after_now”=false“tzinfo”=null |
| Datum und Uhrzeit in diesem Jahrzehnt | “before_now”=true“after_now”=false“tzinfo”=null |
| Datum und Uhrzeit in diesem Monat | “before_now”=true“after_now”=false“tzinfo”=null |
| Datum und Uhrzeit in diesem Jahr | “before_now”=true“after_now”=false“tzinfo”=null |
| Tag des Monats |  |
| Wochentag |  |
| ISO8601-Datum und -Uhrzeit | “tzinfo”=null“end_datetime”=null |
| Monat |  |
| Monatsname |  |
| Vergangenes Datum (letzte 30 Tage) | “start_date”=”-30d”“tzinfo”=null |
| Zeitzone |  |
| Unix-Zeit | “end_datetime”=null“start_datetime”=null |
| Jahr |  |

### Datei




| Generator | Optionale Argumente |
| Dateierweiterung | “category”=null |
| Dateiname | “category”=null“extension”=null |
| Dateipfad | “depth”=”1”“category”=null“extension”=null |
| MIME-Typ | “category”=null |

### Internet




| Generator | Optionale Argumente |
| Firmen-E-Mail |  |
| Domainname |  |
| Domainwort |  |
| E-Mail |  |
| Kostenlose E-Mail |  |
| Domain für kostenlose E-Mail |  |
| Bild-URL | “width”=null“height”=null |
| IPv4 | “network”=false“address_class”=”no”“private”=null |
| IPv6 | “network”=false |
| MAC-Adresse |  |
| Sichere E-Mail |  |
| Slug |  |
| TLD |  |
| URI |  |
| URL | “schemes”=null |
| URL-Erweiterung |  |
| URL-Seite |  |
| Benutzername |  |

### ISBN




| Generator | Optionale Argumente |
| ISBN10 | “eparator”=”-“ |
| ISBN13 | “eparator”=”-“ |

### Beruf




| Generator | Optionale Argumente |
| Berufsbezeichnung |  |

### Lorem




| Generator | Optionale Argumente |
| Absatz | “nb_sentences”=”3”“variable_nb_sentences”=true“ext_word_list”=null |
| Absätze | “nb”=”3”“ext_word_list”=null |
| Satz | “nb_words”=”6”“variable_nb_words”=true“ext_word_list”=null |
| Sätze | “nb”=”3”“ext_word_list”=null |
| Text | “max_nb_chars”=”200”“ext_word_list”=null |
| Wort | “ext_word_list”=null |
| Wörter | “nb”=”3”“ext_word_list”=null |

### Sonstiges




| Generator | Optionale Argumente |
| Binärdaten | “length”=”1048576” |
| Boolesch | “chance_of_getting_true”=”50” |
| Boolesch (Null möglich) |  |
| Gebietsschema |  |
| Sprachcode |  |
| MD5 | “raw_output”=false |
| Passwort | “length”=”10”“special_chars”=true“digits”=true“upper_case”=true“lower_case”=true |
| Zufällige Zeichenfolge |  |
| SHA1 | “raw_output”=false |
| SHA256 | “raw_output”=false |
| UUID4 |  |

### Numerisch




| Generator | Optionale Argumente |
| Big Serial (Auto-Inkrement) |  |
| Zufällige Gleitkommazahl |  |
| Zufällige Gleitkommazahl in Bereich |  |
| Zufällige Ganzzahl |  |
| Zufällige Ganzzahl in Bereich |  |
| Zufällige Dezimalzahl |  |
| Zufälliger Prozentsatz (0 – 1) |  |
| Zufälliger Prozentsatz (0 – 100) |  |
| Serial (Auto-Inkrement) |  |

### Person




| Generator | Optionale Argumente |
| Vorname |  |
| Vorname weiblich |  |
| Vorname männlich |  |
| Vollständiger Name |  |
| Vollständiger Name weiblich |  |
| Vollständiger Name männlich |  |
| Nachname |  |
| Nachname weiblich |  |
| Nachname männlich |  |
| Präfix |  |
| Präfix weiblich |  |
| Präfix männlich |  |
| Suffix |  |
| Suffix weiblich |  |
| Suffix männlich |  |

### Telefon




| Generator | Optionale Argumente |
| Telefonnummer |  |
| ISDN |  |

### Steuer




| Generator | Optionale Argumente |
| EIN |  |
| Vollständige SSN |  |
| ITIN |  |

### User-Agent




| Generator | Optionale Argumente |
| Chrome | “version_from”=”13”“version_to”=”63”“build_from”=”800”“build_to”=”899” |
| Firefox |  |
| Vollständiger User-Agent |  |
| Internet Explorer |  |
| Linux-Plattform-Token |  |
| Linux-Prozessor |  |
| Mac-Plattform-Token |  |
| Mac-Prozessor |  |
| Opera |  |
| Safari |  |
| Windows-Plattform-Token |  |

### Spezielle Generatoren


Diese beiden Generatoren haben zwar keine Argumente, die Optionen, die sie bieten, wirken jedoch ähnlich wie Argumente.



**Pattern-Generator**:




| Zahl | Format | Ausgabe | Beschreibung |
| 3.1415926 | \{:.2f} | 3.14 | 2 Nachkommastellen |
| 3.1415926 | \{:+.2f} | +3.14 | 2 Nachkommastellen mit Vorzeichen |
| -1 | \{:+.2f} | -1.00 | 2 Nachkommastellen mit Vorzeichen |
| 2.71828 | \{:.0f} | 3 | Keine Nachkommastellen |
| 5 | \{:0>2d} | 05 | Zahl mit Nullen auffüllen (Auffüllung links, Breite 2) |
| 5 | \{:x&lt;4d} | 5xxx | Zahl mit x auffüllen (Auffüllung rechts, Breite 4) |
| 10 | \{:x&lt;4d} | 10xx | Zahl mit x auffüllen (Auffüllung rechts, Breite 4) |
| 1000000 | \{:,} | 1,000,000 | Zahlenformat mit Komma als Tausendertrennzeichen |
| 0.25 | \{:.2%} | 25.00% | Prozentwert formatieren |
| 1000000000 | \{:.2e} | 1.00e+09 | Exponentialschreibweise |
| 13 | \{:10d} | 13 | Rechtsbündig (Standard, Breite 10) |
| 13 | \{:&lt;10d} | 13 | Linksbündig (Breite 10) |
| 13 | \{:^10d} | 13 | Zentriert (Breite 10) |

**Zufallsauswahl**:


Um die Optionen für die Zufallsauswahl anzugeben, setzen Sie Ihre Optionen einfach in Anführungszeichen und trennen Sie sie durch Kommas. Eine Zeichenfolge mit Optionen für die Zufallsauswahl sieht dann so aus: “x”,”y”,”z”



Hier enthält die Spalte “Key Word Args/Pattern/Choices” der Zeile “pattern” einen Satz mit mehreren Verweisen. Die erste Verweisgleichung ( \{percentage0-100:.2f}% ) verweist auf die Zeile “percentage0-100”, die eine zufällige Gleichung erzeugt. Der von der Zeile “percentage0-100” erzeugte zufällige Prozentsatz wird daher automatisch in den Satz eingefügt. Die Verweisgleichung \{first_name} verweist auf die Zeile “first_name”, die zufällig einen Vornamen erzeugt, und dieser Name wird automatisch in den Satz eingefügt. Die letzte Verweisgleichung ( \{randomn_choice} ) funktioniert genauso wie die beiden anderen.



Wenn der Pattern-Generator ausgeführt wird, erhalten Sie damit die folgenden Ergebnisse.


## Zeilenanzahl aus einer Tabelle

Um die Zeilenanzahl aus Daten zu übernehmen, legen Sie **Tabelle mit der Anzahl** (`rows_source`) und **Spalte mit der Anzahl** (`rows_column`) fest. Der Schritt liest die Zahl bei der Ausführung aus der ersten Zeile der Tabelle in dieser Spalte und verwendet sie anstelle der von Ihnen festgelegten **Zeilenanzahl**. Fehlt ein Wert oder ist er kleiner als 1, werden keine Zeilen erzeugt.

## Was beim Speichern geprüft wird

Jede Zeile von **Testdatenspalten und Datentypen** wird zu einer Spalte der erzeugten Tabelle, daher braucht jede einen eigenen Namen. Das Speichern wird mit *Every fake data column needs a name.* abgelehnt, wenn ein Name leer ist, und mit *Fake data column name 'city' is used more than once; each needs its own.*, wenn zwei denselben Namen haben.
