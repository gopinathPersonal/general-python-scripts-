from translate import Translator

translator = Translator(to_lang="ja")
try:
    with open('C:\python\eng.txt', mode='r')as myfile:
        engText = myfile.read()
        print(engText)
        translation = translator.translate(engText)
        print(translation)
        with open('C:\python\ja.txt', mode='w') as translatedfile:
            translatedfile.write(translation)
except FileNotFoundError:
    print('check your file path ')