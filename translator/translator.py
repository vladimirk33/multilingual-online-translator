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

    print("Translations")

    translations = []
    for translation in soup.select('[class*="translation ltr dict"]'):
        translation = translation.get_text().strip()
        translations.append(translation)

    sent_translations = []
    for translation in soup.find_all('div', {'class': ['src ltr', 'trg ltr']}):
        translation = translation.get_text().strip()
        sent_translations.append(translation)

    print(translations)
    print(sent_translations)


if __name__ == "__main__":
    main()
