def main():
    print('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
    lang = input()
    print('Type the word you want to translate:')
    word = input()
    print(f'You chose "{lang}" as the language to translate "{word}" to.')


if __name__ == "__main__":
    main()