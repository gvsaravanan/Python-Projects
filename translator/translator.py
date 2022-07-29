from translate import Translator

translator = Translator(to_lang = "ta")

try:
    with open('translator/text.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
except FileNotFoundError as e:
    print("check file location")