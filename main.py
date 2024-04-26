from translate import Translator


try:
    with open('text.txt', mode='r') as my_file:  # to add to the end
        # This added it to the end
        # text = my_file.write('I added it to the end')
        reading = my_file.read()
        translator = Translator(to_lang="de")
        translation = translator.translate(reading)
        with open('output.txt', mode='w') as output:
            output.write(translation)
except FileNotFoundError as e:
    print('check path dummy!!')
