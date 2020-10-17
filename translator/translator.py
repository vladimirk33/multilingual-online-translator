import string
import requests
from bs4 import BeautifulSoup


def choose_language():
    lang = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:\n')
    if lang == "fr":
        return "english-french", "fr"
    elif lang == "en":
        return "french-english", "en"


def main():
    language, lang = choose_language()
    print('Type the word you want to translate:')
    word = input()
    print(f'You chose "{language}" as a language to translate "{word}".')
    user_agent = 'Mozilla/5.0'
    url = f"https://context.reverso.net/translation/{language}/{word}"
    response = requests.get(url, headers={'User-Agent': user_agent})
    soup = BeautifulSoup(response.content, "lxml")

    if response.status_code == 200:
        print(response.status_code, "OK")

    print("\nContext examples:")

    translations = []
    print("\nFrench Translations:")
    for translation in soup.select('[class*="translation ltr dict"]'):
        translation = translation.get_text().strip()
        translation = ''.join([i if ord(i) < 128 else '?' for i in translation])
        translations.append(translation)

    for translation in translations[:5]:
        print(translation)

    french_examples = []
    print("\nFrench Examples:")
    for translation in soup.find_all('div', {'class': ['src ltr', 'trg ltr']}):
        translation = translation.get_text().strip()
        translation = ''.join([i if ord(i) < 128 else '?' for i in translation])
        french_examples.append(translation)

    for i in range(1, 10, 2):
        print(f"{french_examples[i-1]}:\n{french_examples[i]}\n")

    #print(translations)
    #print(sent_translations)


if __name__ == "__main__":
    main()
