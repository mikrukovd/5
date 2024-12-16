import file_operations
import random
import os
from faker import Faker


def main():
    letters = {
        'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
        'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
        'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
        'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
        'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
        'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
        'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
        'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
        'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
        'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
        'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
        'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
        'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
        'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
        'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
        'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
        'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
        'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
        'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
        'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
        'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
        'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
        ' ': ' '
    }
    skills = ['Удар кулаком', 'Удар молнией', 'Удар огнем', 'Ледяная ловушка']
    fake = Faker('ru_RU')
    svg = 'svg/5.svg'
    os.makedirs('result')
    runic_skills = []
    for skill in skills:
        text_letter = ''
        for s in skill:
            s = letters[s]
            text_letter += s
        runic_skills.append(text_letter)
    for i in range(1, 11):
        first_name = fake.first_name()
        last_name = fake.last_name()
        job = fake.job()
        town = fake.city()
        strength = random.randint(3, 18)
        agility = random.randint(3, 18)
        endurance = random.randint(3, 18)
        intelligence = random.randint(3, 18)
        luck = random.randint(3, 18)
        skill_1, skill_2, skill_3 = random.sample(runic_skills, 3)
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'job': job,
            'town': town,
            'strength': strength,
            'agility': agility,
            'endurance': endurance,
            'intelligence': intelligence,
            'luck': luck,
            'skill_1': skill_1,
            'skill_2': skill_2,
            'skill_3': skill_3
        }
        result = 'result/result_{i}.svg'.format(i=i)
        file_operations.render_template(svg, result, context)


if __name__ == '__main__':
    main()
