list_of_students = ['Mansi', 'Anshika', 'Avni', 'Rishabh', 'Mahi', 'Anisha']

name = input('Type name to check')

if name in list_of_students:
    print('This student is enrolled')
else:
    print('This student is not enrolled')