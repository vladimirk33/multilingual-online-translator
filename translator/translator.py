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


def choose_language():
    for i in range(len(LANGUAGES)):
        print(f"{i+1}. {LANGUAGES[i].title()}")
    first_language_number = int(input("Type the number of your language:\n"))
    second_language_number = int(input("Type the number of language you want to translate to:\n"))
    return LANGUAGES[first_language_number-1], LANGUAGES[second_language_number-1]


def main():
    print("Hello, you're welcome to the translator. Translator supports:")
    first_language, second_language = choose_language()
    word = input("Type the word you want to translate:\n")

    user_agent = 'Mozilla/5.0'
    url = f"https://context.reverso.net/translation/{first_language}-{second_language}/{word}"
    response = requests.get(url, headers={'User-Agent': user_agent})
    soup = BeautifulSoup(response.content, "lxml")

    # if response.status_code == 200:
    #     print(response.status_code, "OK")

    translations = []
    print(f"\n{second_language.title()} Translations:")
    for translation in soup.select('[class*="translation ltr dict"]'):
        translation = translation.get_text().strip()
        translation = ''.join([i if ord(i) < 128 else '?' for i in translation])
        translations.append(translation)

    for translation in translations[:5]:
        print(translation)

    french_examples = []
    print(f"\n{second_language.title()} Examples:")
    for translation in soup.find_all('div', {'class': ['src ltr', 'trg ltr']}):
        translation = translation.get_text().strip()
        translation = ''.join([i if ord(i) < 128 else '?' for i in translation])
        french_examples.append(translation)

    for i in range(1, 10, 2):
        print(f"{french_examples[i-1]}:\n{french_examples[i]}\n")


if __name__ == "__main__":
    main()
