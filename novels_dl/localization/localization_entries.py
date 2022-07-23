localization_entries = {
    "pl": {
        "MAIN_INTERRUPT_SIGNAL": "Przechwycono żądanie wyłączenia. Zamykam skrypt...",
        
        "MAIN_WRONG_PYVERSION": "Nieprawidłowa wersja Pythona. Wymagana jest wersja {1} lub wyższa.",

        "MAIN_AUTH": "Strona novelki.pl udostępnia zasoby wyłącznie zalogowanym użytkownikom.\n"
                     "Podaj swój email i hasło, aby dokonać logowania.\n"
                     "Dane logowania są wysyłane wyłącznie na serwer novelki.pl.",
        "MAIN_AUTH_EMAIL": "Podaj adres email do konta: ",
        "MAIN_AUTH_PASSWORD": "Podaj hasło do konta: ",
        "MAIN_AUTH_OK": "Logowanie przebiegło pomyślnie!",
        "MAIN_AUTH_ERR": "Logowanie nie przebiegło pomyślnie.\nSprawdź czy dane logowania są poprawne.",

        "MAIN_NOVEL_KEY": "Aby wygenerować plik EPUB, musisz znać kod URL nowelki.\n"
                          "Kod URL wygląda następująco: to-jest-przykladowy-kod-nowelki\n"
                          "Kod nowelki znajdziesz w pasku URL przeglądarki podczas czytania nowelki.",
        "MAIN_NOVEL_KEY_INPUT": "Podaj kod URL nowelki: ",
        "MAIN_NOVEL_KEY_INVALID": "Nie wykryto nowelki o takim kodzie. Sprawdź, czy kod jest poprawny.",
        "MAIN_NOVEL_KEY_OK": "Podano poprawny kod nowelki. Metadane zostały załadowane.",
        "MAIN_NOVEL_KEY_DETECTED": "Wykryta nowelka: ",

        "MAIN_EPUB_OUTPUT": "Teraz podaj ścieżkę, pod którą chcesz zapisać plik EPUB. Na przykład,\n"
                            "jeśli chcesz zapisać go w katalogu Pobrane, wpisz /home/my_user/Pobrane/nazwapliku.epub",
        "MAIN_EPUB_OUTPUT_PROMPT": "Ścieżka: ",

        "MAIN_CONVERT_HYPHENS": "Wybierz styl wprowadzania dialogów:",
        "MAIN_CONVERT_HYPHENS_OPTION_1": "[1] Pozostaw oryginalny styl pobrany ze strony",
        "MAIN_CONVERT_HYPHENS_OPTION_2": "[2] Konwertuj cudzysłowy na myślniki (styl polski)",
        "MAIN_CONVERT_HYPHENS_PROMPT": "Podaj numer wybranego stylu (1 lub 2): ",

        "MAIN_PARAGRAPH_SEPARATION": "Wybierz metodę oddzielania akapitów:",
        "MAIN_PARAGRAPH_SEPARATION_OPTION_1": "[1] Oddzielaj marginesami (styl angielski)",
        "MAIN_PARAGRAPH_SEPARATION_OPTION_2": "[2] Oddzielaj wcięciami, bez marginesów (styl polski)",
        "MAIN_PARAGRAPH_SEPARATION_OPTION_3": "[3] Połącz style (używaj zarówno wcięć, jak i marginesów)",
        "MAIN_PARAGRAPH_SEPARATION_PROMPT": "Podaj numer wybranego stylu (1, 2 lub 3): ",

        "MAIN_INDENTS_SIZE_SUGGESTION": "Sugerowany rozmiar wcięć dla czytnika Kindle i konwersji Calibre/mobi to\n"
                                        "1.25em (jeśli lubisz małe wcięcia) lub 1.5em (jeśli lubisz duże)",
        "MAIN_INDENTS_SIZE": "Skonfigurowałeś wcięcia, więc konieczne jest podanie rozmiaru wcięć.\n"
                             "Rozmiar powinien być wyrażony w jednostce CSS, na przykład 1cm albo 0.5rem",
        "MAIN_INDENTS_SIZE_PROMPT": "Podaj rozmiar wcięć w jednostkach CSS: ",
        "MAIN_MARGIN_SIZE_SUGGESTION": "Sugerowany rozmiar marginesów dla czytnika Kindle i konwersji Calibre/mobi to\n"
                                        "0.7em (jeśli lubisz małe marginesy) lub 1em (jeśli lubisz duże)",
        "MAIN_MARGIN_SIZE": "Skonfigurowałeś marginesy, więc konieczne jest podanie rozmiaru marginesów.\n"
                            "Rozmiar powinien być wyrażony w jednostce CSS, na przykład 1cm albo 0.5rem\n",
        "MAIN_MARGIN_SIZE_PROMPT": "Podaj rozmiar marginesów w jednostkach CSS: ",

        "FETCH_CHAPTER_HTTP429": "Otrzymano odpowiedź HTTP/429, czekam {1} sekund",

        "CHAPTER_WRITER_BEGIN": "Rozpoczynam pobieranie rozdziałów.",
        "CHAPTER_WRITER_END": "Zakończono pobieranie rozdziałów.",
        "CHAPTER_WRITER_ANALYZING": "Pobrano rozdział",
        "CHAPTER_WRITER_SAVING_METADATA": "Zapisuję wygenerowane dane rozdziałów do metadanych pliku epub.",

        "CLEANUP_WRITER_BEGIN": "Rozpoczynam czyszczenie katalogu epub.",
        "CLEANUP_WRITER_END": "Zakończono czyszczenie katalogu epub.",

        "COVER_WRITER_BEGIN": "Rozpoczynam pobieranie okładki.",
        "COVER_WRITER_ERR": "Nie odnaleziono okładki do pobrania.",
        "COVER_WRITER_END": "Pobieranie i zapisywanie danych okładki zakończone.",

        "FIX_WRITER_BEGIN": "Rozpoczynam naprawianie formatowania książki.",
        "FIX_WRITER_END": "Zakończono naprawianie formatowania książki.",
        "FIX_WRITER_HYPHENS": "Zamieniam minusy na półpauzy w pliku: ",
        "FIX_WRITER_REDUNDANT_BRS": "Kasuję nadmiarowe znaczniki końca linii w pliku: ",

        "IMAGE_WRITER_VOLUME_TAG": "Nałożono oznaczenie tomu na obrazie okładki",
        "IMAGE_WRITER_BEGIN": "Rozpoczynam pobieranie i zapisywanie obrazków.",
        "IMAGE_WRITER_END": "Zakończono pobieranie i zapisywanie obrazków.",
        "IMAGE_WRITER_METADATA": "Zapisuję informacje o obrazkach w metadanych e-booka.",
        "IMAGE_WRITER_ERR": "Wystąpił błąd przy pobieraniu obrazka, podmieniono obrazek na placeholder.",
        "IMAGE_WRITER_CHECKING": "Sprawdzam, czy są jakieś obrazki do pobrania: ",
        "IMAGE_WRITER_DOWNLOADING": "Pobieram: ",

        "METADATA_WRITER_BEGIN": "Rozpoczynam zapisywanie metadanych książki.",
        "METADATA_WRITER_END": "Zakończyłem zapisywanie metadanych książki.",

        "STYLE_WRITER_BEGIN": "Rozpoczynam modyfikację wyglądu nowelki.",
        "STYLE_WRITER_END": "Zakończono modyfikację wyglądu nowelki.",
        "STYLE_WRITER_INDENTS": "Dodaję metodę oddzielenia paragrafów: wcięcia",
        "STYLE_WRITER_MARGINS": "Dodaję metodę oddzielenia paragrafów: paragrafy blokowe",
        "STYLE_WRITER_REPLACING_QUOTES": "Podmieniam cudzysłowy na myślniki w pliku: ",

        "GENERATOR_BEGIN_GENERATION": "Rozpoczynam generowanie ebooka: ",
        "GENERATOR_END_GENERATION": "Zakończono generowanie ebooka: ",

        "GENERATION_BEGIN_MULTIPLE_GENERATIONS": "Rozpoczynam generowanie serii ebooków",
        "GENERATION_END_MULTIPLE_GENERATIONS": "Zakończono generowanie serii ebooków",

        "CLI_VOL_SPLIT_ASK": "Czy chcesz włączyć dzielenie tomów?\n"
                            "[1] Wygeneruj jeden duży plik .epub ze wszystkimi tomami light novel\n"
                            "[2] Wygeneruj tyle plików .epub, ile jest tomów light novel",
        "CLI_VOL_SPLIT_WARN": "\nUwaga! Jeśli wybierzesz opcję 2, obraz okładki dla poszczególnych tomów się nie "
                              "zmieni.\nStrona novelki.pl nie udostępnia obrazów okładek dla poszczególnych tomów.\n"
                              "Dla rozróżnienia, na każdą z okładek zostanie naniesiony prostokąt z numerem tomu.\n",

        "CLI_ROTATE_LONG_ASK": "Czy chcesz włączyć obracanie długich ilustracji?\n"
                               "[1] Zostaw ilustracje bez zmian\n"
                               "[2] Obracaj ilustracje\n",

        "CLI_ROTATE_LONG_EXPLANATION": "Jeśli włączysz tę opcję, obrazki których szerokość jest większa niż wysokość\n"
                                       "zostaną obrócone o 90 stopni, tak aby lepiej wykorzystywać ekran e-czytników.",

        "UTIL_CHOOSE_1_2": "Wybierz 1 lub 2: "
    },

    "en": {
        "MAIN_INTERRUPT_SIGNAL": "Interrupt signal received. Exiting...",

        "MAIN_WRONG_PYVERSION": "Wrong Python version. Python {1} or higher is required.",

        "MAIN_AUTH": "Website novelki.pl makes its resources available only to logged-in users.\n"
                     "Enter your email and password to log in.\n"
                     "The login data will be send only to the novelki.pl server.",

        "MAIN_AUTH_EMAIL": "Enter your email: ",
        "MAIN_AUTH_PASSWORD": "Enter your password: ",
        "MAIN_AUTH_OK": "Authentication was performed correctly.",
        "MAIN_AUTH_ERR": "Authentication was not performed correctly.\nCheck if your credentials are correct.",

        "MAIN_NOVEL_KEY": "To generate an EPUB file, you need to know the URL code of the novel you want to download.\n"
                          "The URL code looks like this: to-is-an-example-novel-code\n"
                          "You will find the novel code in the URL bar of your browser when reading the novel.",
        "MAIN_NOVEL_KEY_INPUT": "Please type novel URL code: ",
        "MAIN_NOVEL_KEY_INVALID": "Could not find light novel with specified URL code.\n"
                                  "Check if specified URL code is correct.",
        "MAIN_NOVEL_KEY_OK": "Novel's URL code is correct. Metadata has been fetched correctly.",
        "MAIN_NOVEL_KEY_DETECTED": "Detected novel: ",

        "MAIN_EPUB_OUTPUT": "Now enter the path under which you want to save the EPUB file. For example, if you\n"
                            "want to save it in the Downloads directory, type /home/my_user/Downloads/filename.epub",
        "MAIN_EPUB_OUTPUT_PROMPT": "Output path: ",

        "MAIN_CONVERT_HYPHENS": "Choose dialogue introduction method:",
        "MAIN_CONVERT_HYPHENS_OPTION_1": "[1] Dont modify dialogue introduction method",
        "MAIN_CONVERT_HYPHENS_OPTION_2": "[2] Convert quotes to hyphens (Polish style)",
        "MAIN_CONVERT_HYPHENS_PROMPT": "Please enter style number (1 or 2): ",

        "MAIN_PARAGRAPH_SEPARATION": "Choose paragraph separation method:",
        "MAIN_PARAGRAPH_SEPARATION_OPTION_1": "[1] Use margins (English style)",
        "MAIN_PARAGRAPH_SEPARATION_OPTION_2": "[2] Use text-indent (Polish style)",
        "MAIN_PARAGRAPH_SEPARATION_OPTION_3": "[3] Combine both styles (use both indents and margins)",
        "MAIN_PARAGRAPH_SEPARATION_PROMPT": "Please enter style number (1, 2 or 3): ",

        "MAIN_INDENTS_SIZE_SUGGESTION": "Suggested indents size for Kindle readers and Calibre/mobi conversion is\n"
                                        "1.25em (if you like small indents) or 1.5em (if you like bigger indents)",
        "MAIN_INDENTS_SIZE": "You have chosen indentation, so it is necessary to specify the size of the indents.\n"
                             "The size should be expressed in a CSS unit, for example 1cm or 0.5rem",
        "MAIN_INDENTS_SIZE_PROMPT": "Specify the indent size in CSS units: ",
        "MAIN_MARGIN_SIZE_SUGGESTION": "Suggested margin size for Kindle readers and Calibre/mobi conversion is\n"
                                       "0.7em (if you like small margins) lub 1em (if you like bigger margins)",
        "MAIN_MARGIN_SIZE": "You have chosen margins, so it is necessary to specify the size of the margins.\n"
                            "The size should be expressed in a CSS unit, for example 1cm or 0.5rem\n",
        "MAIN_MARGIN_SIZE_PROMPT": "Specify the margin size in CSS units: ",

        "FETCH_CHAPTER_HTTP429": "Got HTTP/429 response, waiting {1} seconds",

        "CHAPTER_WRITER_BEGIN": "Starting to download chapters.",
        "CHAPTER_WRITER_END": "Finished downloading all chapters.",
        "CHAPTER_WRITER_ANALYZING": "Downloaded chapter",
        "CHAPTER_WRITER_SAVING_METADATA": "Saving chapter information to epub metadata.",

        "CLEANUP_WRITER_BEGIN": "Starting epub cleanup.",
        "CLEANUP_WRITER_END": "Finished epub cleanup.",

        "COVER_WRITER_BEGIN": "Starting to download ebook cover.",
        "COVER_WRITER_ERR": "Could not find cover to download",
        "COVER_WRITER_END": "Ebook cover downloaded and registered in epub metadata.",

        "FIX_WRITER_BEGIN": "Starting to fix e-book formatting.",
        "FIX_WRITER_END": "Finished formatting fixing.",
        "FIX_WRITER_HYPHENS": "Fixing typography of hyphens in file: ",
        "FIX_WRITER_REDUNDANT_BRS": "Deleting redundant break line tags in file: ",

        "IMAGE_WRITER_VOLUME_TAG": "Drawn volume tag on the cover image",
        "IMAGE_WRITER_BEGIN": "Starting to download novel images.",
        "IMAGE_WRITER_END": "Finished downloading all images.",
        "IMAGE_WRITER_METADATA": "Saving image information to epub metadata.",
        "IMAGE_WRITER_ERR": "Image downloading error: swapped image to a placeholder.",
        "IMAGE_WRITER_CHECKING": "Checking if there are some images to download: ",
        "IMAGE_WRITER_DOWNLOADING": "Downloading: ",

        "METADATA_WRITER_BEGIN": "Starting to write epub metadata.",
        "METADATA_WRITER_END": "Finished writing epub metadata.",

        "STYLE_WRITER_BEGIN": "Starting to modify epub CSS.",
        "STYLE_WRITER_END": "Finished modifying epub CSS.",
        "STYLE_WRITER_INDENTS": "Adding paragraph separation method: indents",
        "STYLE_WRITER_MARGINS": "Adding paragraph separation method: margins",
        "STYLE_WRITER_REPLACING_QUOTES": "Swapping quotation marks to hyphens in: ",

        "GENERATOR_BEGIN_GENERATION": "Starting to generate ebook: ",
        "GENERATOR_END_GENERATION": "Finished ebook generation: ",

        "GENERATION_BEGIN_MULTIPLE_GENERATIONS": "Starting ebook multiple volumes generation.",
        "GENERATION_END_MULTIPLE_GENERATIONS": "Finished ebook multiple volumes generation.",

        "CLI_VOL_SPLIT_ASK": "Do you want to enable volume splitting?\n"
                             "[1] Generate one large .epub file with all the light novel volumes\n"
                             "[2] Generate as many .epub files as there are light novel volumes",
        "CLI_VOL_SPLIT_WARN": "\nWarning: if you select option 2, the cover image for individual volumes will not "
                              "change.\nThe novelki.pl website does not provide cover images for individual volumes.\n"
                              "For differentiation, a rectangle with volume number will be drawn on each cover image.\n",

        "CLI_ROTATE_LONG_ASK": "Do you want to enable rotation of long images?\n"
                               "[1] Leave images unchanged\n"
                               "[2] Rotate images\n",
        "CLI_ROTATE_LONG_EXPLANATION": "If you enable this option, images which width is greater than the height\n"
                                       "will be rotated by 90 degrees to make better use of the e-reader screen.",

        "UTIL_CHOOSE_1_2": "Type 1 or 2: "
    }
}
