from file_operations import render_template
from faker import Faker
from transliterate import slugify
from random import randint, sample
from letters_mapping import letters
import os


def main():
    os.makedirs('output/svg', exist_ok=True)

    persons_amount = 10

    skills = ['Стремительный прыжок',
              'Электрический выстрел',
              'Ледяной удар',
              'Стремительный удар',
              'Кислотный взгляд',
              'Тайный побег',
              'Ледяной выстрел',
              'Огненный заряд']

    fake = Faker('ru_RU')

    for number in range(persons_amount):
        person_skills = sample(skills, 3)
        runic_skills = []
        for person_skill in person_skills:
            runic_skill = ''
            for letter in person_skill:
                runic_skill += letters[letter]
            runic_skills.append(runic_skill)

        person = {'first_name': fake.first_name_male(),
                  'last_name': fake.last_name_male(),
                  'job': fake.job(),
                  'town': fake.city(),
                  'strength': randint(3, 18),
                  'agility': randint(3, 18),
                  'endurance': randint(3, 18),
                  'intelligence': randint(3, 18),
                  'luck': randint(3, 18),
                  'skill_1': runic_skills[0],
                  'skill_2': runic_skills[1],
                  'skill_3': runic_skills[2]}

        file_name = f'{person['first_name']} {person['last_name']}'
        file_path = f'output/svg/{slugify(file_name)}.svg'

        render_template('src/charsheet.svg', file_path, person)


if __name__ == '__main__':
    main()
