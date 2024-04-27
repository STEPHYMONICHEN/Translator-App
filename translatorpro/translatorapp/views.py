from django.shortcuts import render
from translate import Translator


def translator(request):
    translated_text = None

    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        language = request.POST.get('language')

        translates = Translator(to_lang=language)
        translated_text = translates.translate(input_text)

    return render(request, 'translator.html', {'translated_text': translated_text})
