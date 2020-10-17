import requests
from bs4 import BeautifulSoup

LANGUAGES = ("arabic",
             "german",
             "english",
             "spanish",
             "french",
             "hebrew",
             "japanese",
             "dutch",
             "polish",
             "portuguese",
             "romanian",
             "russian",
             "turkish",
             )


def all_languages_translation(first_language, languages, word, file):
    user_agent = 'Mozilla/5.0'
    for second_language in languages:
        if second_language == first_language:
            continue
        url = f"https://context.reverso.net/translation/{first_language}-{second_language}/{word}"
        response = requests.get(url, headers={'User-Agent': user_agent})
        soup = BeautifulSoup(response.content, "lxml")

        # if response.status_code == 200:
        #     print(response.status_code, "OK")

        print(f"\n{second_language.title()} Translations:")
        file.write(f"{second_language.title()} Translations:\n")
        if second_language == "arabic" or second_language == "hebrew":
            translation = soup.select('[class*="translation rtl dict"]')[0].get_text().strip()
            print(translation)
            file.write(translation + "\n\n")
        else:
            translation = soup.select('[class*="translation ltr dict"]')[0].get_text().strip()
            print(translation)
            file.write(translation + "\n\n")
        print(f"\n{second_language.title()} Examples:")
        file.write(f"{second_language.title()} Examples:\n")
        example = soup.find_all('div', {'class': ['src ltr', 'trg ltr', 'trg rtl arabic']})
        print(f"{example[0].get_text().strip()}:\n{example[1].get_text().strip()}\n")
        file.write(f"{example[0].get_text().strip()}:\n{example[1].get_text().strip()}\n\n\n")


def standard_translation(first_language, second_language, word, file):
    user_agent = 'Mozilla/5.0'
    url = f"https://context.reverso.net/translation/{first_language}-{second_language}/{word}"
    response = requests.get(url, headers={'User-Agent': user_agent})
    soup = BeautifulSoup(response.content, "lxml")

    # if response.status_code == 200:
    #     print(response.status_code, "OK")

    translations = []
    print(f"\n{second_language.title()} Translations:")
    file.write(f"{second_language.title()} Translations:\n")
    if second_language == "arabic" or second_language == "hebrew":
        for translation in soup.select('[class*="translation rtl dict"]'):
            translation = translation.get_text().strip()
            # translation = ''.join([i if ord(i) < 128 else '?' for i in translation])
            translations.append(translation)
    else:
        for translation in soup.select('[class*="translation ltr dict"]'):
            translation = translation.get_text().strip()
            # translation = ''.join([i if ord(i) < 128 else '?' for i in translation])
            translations.append(translation)

    for translation in translations[:5]:
        print(translation)
        file.write(translation + "\n")

    examples = []
    print(f"\n{second_language.title()} Examples:")
    file.write(f"\n{second_language.title()} Examples:\n")
    for translation in soup.find_all('div', {'class': ['src ltr', 'trg ltr', 'trg rtl arabic']}):
        translation = translation.get_text().strip()
        #translation = ''.join([i if ord(i) < 128 else '?' for i in translation])
        examples.append(translation)

    for i in range(1, 10, 2):
        print(f"{examples[i-1]}:\n{examples[i]}\n")
        file.write(f"{examples[i-1]}:\n{examples[i]}\n\n")


def choose_language():
    for i in range(len(LANGUAGES)):
        print(f"{i+1}. {LANGUAGES[i].title()}")
    first_language_number = int(input("Type the number of your language:\n"))
    second_language_number = int(input("Type the number of a language you want to translate to or '0' to translate to all languages:\n"))
    if second_language_number == 0:
        return LANGUAGES[first_language_number-1], LANGUAGES
    return LANGUAGES[first_language_number-1], LANGUAGES[second_language_number-1]


def main():
    print("Hello, you're welcome to the translator. Translator supports:")
    first_language, second_language = choose_language()
    word = input("Type the word you want to translate:\n")
    file = open(f"{word}.txt", "w", encoding="utf-8")
    if isinstance(second_language, tuple):
        all_languages_translation(first_language, second_language, word, file)
    else:
        standard_translation(first_language, second_language, word, file)
    file.close()


if __name__ == "__main__":
    main()
