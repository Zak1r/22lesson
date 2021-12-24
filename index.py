# таблица умножения
# 10 x 1 = 10
# 10 x 2 = 20
# 10 x 3 = 30
# 10 x 4 = 40
# 10 x 5 = 50
# 10 x 6 = 60
# 10 x 7 = 70
# 10 x 8 = 80
# 10 x 9 = 90
# 10 x 10 = 100

# with open('./table.txt', 'w') as wf:
#     for i in range(1,11):
#         wf.write(f'10 x {i} = {10 * i}\n')

'''нужно ( Создание Телеграм бота ) ДЗ'''

'''e-commerce ()
fintech ()
edtech ()

Бизнес и IT
1) продать себя = продать время
2) открыть стартап'''


# for example
# dad - Murad
#  mum - Dilfuza
#  Me - Zakir
# with open('./data.txt', 'w') as wf:
#     familyMembers = int(input('How many members in your family? '))
#     for i in range(1, familyMembers):
#         relation = input(f' What is {i} person\'s relation to you? ')
#         name = input(f'What is your {relation}\' name? ')
#         wf.write(f'{relation} - {name}\n ')
#     name = input('What is your name? ')
#     wf.write(f'Me - {name}')



# task
# names = ['Timur', 'Shukhrat', 'Sanjar']
# TiMuR
# ShUkHrAt
# SaNjAr

# names = ['Timur', 'Shukhrat', 'Sanjar']

# with open('upperlower.txt', 'w') as wf:
#     for name in names:
#         newName = ''
#         for i, char in enumerate(name):
#             if i % 2 == 0:  newName += char.upper()
#             else:   newName += char
#         wf.write(f'{newName}\n')




# nums = [123, 1000, 654, 12, 10093]
# digits.txt
# 1 + 2 + 3 = 6
# 1 + 0 + 0 + 0 = 1
# 6 + 5 + 4 = 15

nums = [123, 1000, 654, 12, 10093]
with open('digits.txt', 'w') as wf:
    for num in nums:
        digitList = []
        while num > 0:
            digit = num % 10
            num = num // 10
        digitList