---
title: Table Faker (krok)
description: Generuj syntetyczne dane testowe w kroku przepływu pracy PlaidCloud za pomocą Fakera, aby tworzyć realistyczne przykładowe zbiory danych na potrzeby tworzenia rozwiązań.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-faker.md
---

## Opis


Krok Table Faker generuje fikcyjne dane.



### Adres




| Generator | Argumenty opcjonalne |
| Numer budynku |  |
| Miasto |  |
| Przyrostek miasta |  |
| Kraj |  |
| Kod kraju | “representation”=”alpha-2” |
| Pełny adres |  |
| Szerokość geograficzna |  |
| Długość geograficzna |  |
| Wojskowy DPO |  |
| Kod pocztowy |  |
| Kod pocztowy Plus 4 |  |
| Stan |  |
| Skrót stanu |  |
| Adres ulicy |  |
| Nazwa ulicy |  |
| Przyrostek ulicy |  |

### Motoryzacja




| Generator | Argumenty opcjonalne |
| Tablica rejestracyjna |  |

### Kod kreskowy




| Generator | Argumenty opcjonalne |
| EAN13 |  |
| EAN8 |  |

### Kolory




| Generator | Argumenty opcjonalne |
| Nazwa koloru |  |
| Kolor szesnastkowy |  |
| Kolor RGB |  |
| Kolor RGB CSS |  |
| Nazwa koloru bezpiecznego |  |
| Bezpieczny kolor szesnastkowy |  |

### Firma




| Generator | Argumenty opcjonalne |
| Slogan firmy |  |
| Nazwa firmy |  |
| Przyrostek firmy |  |

### Karta kredytowa




| Generator | Argumenty opcjonalne |
| Data ważności | “start”=”now”“end”=”+10y”## ‘12/20’ |
| Pełne dane | “card_type”=null |
| Numer | “card_type”=null |
| Operator | “card_type”=null |
| Kod bezpieczeństwa | “card_type”=null |

### Waluta




| Generator | Argumenty opcjonalne |
| Kod |  |

### Data i godzina




| Generator | Argumenty opcjonalne |
| AM/PM |  |
| Stulecie |  |
| Data | “pattern”:”%Y-%m-%d”“end_datetime”:null |
| Data i godzina | “tzinfo”:null“end_datetime”=null |
| Data i godzina w tym stuleciu | “before_now”=true“after_now”=false“tzinfo”=null |
| Data i godzina w tej dekadzie | “before_now”=true“after_now”=false“tzinfo”=null |
| Data i godzina w tym miesiącu | “before_now”=true“after_now”=false“tzinfo”=null |
| Data i godzina w tym roku | “before_now”=true“after_now”=false“tzinfo”=null |
| Dzień miesiąca |  |
| Dzień tygodnia |  |
| Data i godzina ISO8601 | “tzinfo”=null“end_datetime”=null |
| Miesiąc |  |
| Nazwa miesiąca |  |
| Data z przeszłości (ostatnie 30 dni) | “start_date”=”-30d”“tzinfo”=null |
| Strefa czasowa |  |
| Czas Unix | “end_datetime”=null“start_datetime”=null |
| Rok |  |

### Plik




| Generator | Argumenty opcjonalne |
| Rozszerzenie pliku | “category”=null |
| Nazwa pliku | “category”=null“extension”=null |
| Ścieżka pliku | “depth”=”1”“category”=null“extension”=null |
| Typ MIME | “category”=null |

### Internet




| Generator | Argumenty opcjonalne |
| Służbowy adres e-mail |  |
| Nazwa domeny |  |
| Słowo domeny |  |
| Adres e-mail |  |
| Darmowy adres e-mail |  |
| Domena darmowej poczty e-mail |  |
| URL obrazu | “width”=null“height”=null |
| IPv4 | “network”=false“address_class”=”no”“private”=null |
| IPv6 | “network”=false |
| Adres MAC |  |
| Bezpieczny adres e-mail |  |
| Slug |  |
| TLD |  |
| URI |  |
| URL | “schemes”=null |
| Rozszerzenie URL |  |
| Strona URL |  |
| Nazwa użytkownika |  |

### ISBN




| Generator | Argumenty opcjonalne |
| ISBN10 | “eparator”=”-“ |
| ISBN13 | “eparator”=”-“ |

### Stanowisko




| Generator | Argumenty opcjonalne |
| Nazwa stanowiska |  |

### Lorem




| Generator | Argumenty opcjonalne |
| Akapit | “nb_sentences”=”3”“variable_nb_sentences”=true“ext_word_list”=null |
| Akapity | “nb”=”3”“ext_word_list”=null |
| Zdanie | “nb_words”=”6”“variable_nb_words”=true“ext_word_list”=null |
| Zdania | “nb”=”3”“ext_word_list”=null |
| Tekst | “max_nb_chars”=”200”“ext_word_list”=null |
| Słowo | “ext_word_list”=null |
| Słowa | “nb”=”3”“ext_word_list”=null |

### Różne




| Generator | Argumenty opcjonalne |
| Dane binarne | “length”=”1048576” |
| Wartość logiczna | “chance_of_getting_true”=”50” |
| Wartość logiczna z null |  |
| Ustawienia regionalne |  |
| Kod języka |  |
| MD5 | “raw_output”=false |
| Hasło | “length”=”10”“special_chars”=true“digits”=true“upper_case”=true“lower_case”=true |
| Losowy ciąg znaków |  |
| SHA1 | “raw_output”=false |
| SHA256 | “raw_output”=false |
| UUID4 |  |

### Liczby




| Generator | Argumenty opcjonalne |
| Big Serial (autoinkrementacja) |  |
| Losowa liczba zmiennoprzecinkowa |  |
| Losowa liczba zmiennoprzecinkowa z zakresu |  |
| Losowa liczba całkowita |  |
| Losowa liczba całkowita z zakresu |  |
| Losowa liczba |  |
| Losowy procent (0 – 1) |  |
| Losowy procent (0 – 100) |  |
| Serial (autoinkrementacja) |  |

### Osoba




| Generator | Argumenty opcjonalne |
| Imię |  |
| Imię żeńskie |  |
| Imię męskie |  |
| Imię i nazwisko |  |
| Imię i nazwisko (kobieta) |  |
| Imię i nazwisko (mężczyzna) |  |
| Nazwisko |  |
| Nazwisko żeńskie |  |
| Nazwisko męskie |  |
| Tytuł |  |
| Tytuł (kobieta) |  |
| Tytuł (mężczyzna) |  |
| Przyrostek |  |
| Przyrostek (kobieta) |  |
| Przyrostek (mężczyzna) |  |

### Telefon




| Generator | Argumenty opcjonalne |
| Numer telefonu |  |
| ISDN |  |

### Podatki




| Generator | Argumenty opcjonalne |
| EIN |  |
| Pełny SSN |  |
| ITIN |  |

### Agent użytkownika




| Generator | Argumenty opcjonalne |
| Chrome | “version_from”=”13”“version_to”=”63”“build_from”=”800”“build_to”=”899” |
| Firefox |  |
| Pełny agent użytkownika |  |
| Internet Explorer |  |
| Token platformy Linux |  |
| Procesor Linux |  |
| Token platformy Mac |  |
| Procesor Mac |  |
| Opera |  |
| Safari |  |
| Token platformy Windows |  |

### Generatory specjalne


Te dwa generatory nie mają argumentów, ale oferowane przez nie opcje działają podobnie do argumentów.



**Generator wzorca**:




| Liczba | Format | Wynik | Opis |
| 3.1415926 | \{:.2f} | 3.14 | 2 miejsca po przecinku |
| 3.1415926 | \{:+.2f} | +3.14 | 2 miejsca po przecinku ze znakiem |
| -1 | \{:+.2f} | -1.00 | 2 miejsca po przecinku ze znakiem |
| 2.71828 | \{:.0f} | 3 | Bez miejsc po przecinku |
| 5 | \{:0>2d} | 05 | Dopełnienie liczby zerami (z lewej strony, szerokość 2) |
| 5 | \{:x&lt;4d} | 5xxx | Dopełnienie liczby znakami x (z prawej strony, szerokość 4) |
| 10 | \{:x&lt;4d} | 10xx | Dopełnienie liczby znakami x (z prawej strony, szerokość 4) |
| 1000000 | \{:,} | 1,000,000 | Format liczby z przecinkiem jako separatorem |
| 0.25 | \{:.2%} | 25.00% | Format procentowy |
| 1000000000 | \{:.2e} | 1.00e+09 | Notacja wykładnicza |
| 13 | \{:10d} | 13 | Wyrównanie do prawej (domyślne, szerokość 10) |
| 13 | \{:&lt;10d} | 13 | Wyrównanie do lewej (szerokość 10) |
| 13 | \{:^10d} | 13 | Wyrównanie do środka (szerokość 10) |

**Losowy wybór**:


Aby podać opcje losowego wyboru, umieść je w cudzysłowach i oddziel przecinkami. Ciąg opcji losowego wyboru wygląda więc tak: “x”,”y”,”z”



W tym przykładzie kolumna „Key Word Args/Pattern/Choices” w wierszu „pattern” zawiera zdanie z kilkoma odwołaniami. Pierwsze odwołanie ( \{percentage0-100:.2f}% ) wskazuje wiersz „percentage0-100”, który wygeneruje losową wartość. Losowy procent wygenerowany przez wiersz „percentage0-100” zostanie więc automatycznie wstawiony do zdania. Odwołanie \{first_name} wskazuje wiersz o nazwie „first_name”, który losowo wygeneruje imię, a to imię zostanie automatycznie wstawione do zdania. Ostatnie odwołanie ( \{randomn_choice} ) działa tak samo jak dwa pozostałe.



Po uruchomieniu generatora wzorca otrzymasz następujące wyniki.


## Liczba wierszy z tabeli

Aby pobrać liczbę wierszy z danych, ustaw **Tabela z liczbą** (`rows_source`) i **Kolumna z liczbą** (`rows_column`). Krok odczytuje liczbę z pierwszego wiersza tabeli, z tej kolumny, w chwili uruchomienia, zamiast ustawionej przez Ciebie liczby wierszy. Brakująca wartość lub wartość mniejsza niż 1 nie generuje żadnych wierszy.

## Co jest sprawdzane przy zapisie

Każdy wiersz sekcji **Kolumny danych fikcyjnych i typy danych** staje się kolumną wygenerowanej tabeli, więc każdy musi mieć własną nazwę. Zapis jest odrzucany z komunikatem *Every fake data column needs a name.*, gdy nazwa jest pusta, oraz z komunikatem *Fake data column name 'city' is used more than once; each needs its own.*, gdy dwa wiersze mają tę samą nazwę.
