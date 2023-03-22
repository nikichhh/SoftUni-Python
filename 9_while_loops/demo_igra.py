import random

questions = [
    'От кой език идва думата "пенкилер"?',
    'Изразът "желязната завеса" добива популярност сред реч на Чърчил от 1946г. Кои от градовете са в двата и края?',
    'Коя европейска столица носиимето на  един от най-известните магистри от ордена на йоаните?'
]

questions_asked = []

while True:
    current_question = random.choice(questions)

    if current_question not in questions_asked:
        print(current_question)
        questions_asked.append(current_question)