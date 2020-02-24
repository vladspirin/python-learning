# Строки
# words = 'Hello, world!'
# words = "Hello, \"test\" 'world'!"
# print(words)

# verse = ' Jürgen Klopp is relishing the opportunity for Liverpool to ‘immediately strike back’ upon tonight’s welcome return to Anfield.\n \
# The Reds’ pursuit of the Premier League title resumes against West Ham United on Monday, with Klopp’s side heading into the game on the back of a rare defeat.\n \
# A 1-0 loss to Atletico Madrid at Estadio Metropolitano last Tuesday leaves their hopes of Champions League progression in the balance, but the focus within the home dressing room this evening will be solely on domestic matters and the chance to get back to winning ways.'

# print(verse)

# verse = '''\
# Jürgen Klopp is relishing the opportunity for Liverpool to ‘immediately strike back’ upon tonight’s welcome return to Anfield.

# The Reds’ pursuit of the Premier League title resumes against West Ham United on Monday, with Klopp’s side heading into the game on the back of a rare defeat.

#A 1-0 loss to Atletico Madrid at Estadio Metropolitano last Tuesday leaves their hopes of Champions League progression in the balance, but the focus within the home dressing room this evening will be solely on domestic matters and the chance to get back to winning ways.\
#'''

#print(verse)

# s = r'C:\d\new.txt'
# print(s)

# r - перед строкой, говорит что эта строка сырая и Python не будет обрабатывать спец.символы и последовательности в этой строке

st = 'Py' 'thon'
print(st)

s1 = 'Hello, '
s2 = 'world!'
s3 = s1 + s2
print(s3)

print('hi' * 5)

# индексация
# s = 'Hello world!'
# print(s[6])
# print(s[-2])

# срезы
# '''
# +---+---+---+---+---+---+---+---+---+---+---+---+
# | H | e | l | l | o |   | w | o | r | l | d | ! |
# +---+---+---+---+---+---+---+---+---+---+---+---+
# 0   1   2   3   4   5   6   7   8   9  10  11  12
# -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1 0
# '''
# [X:Y:Z] X -начало среза, Y - конец среза, Z - шаг среза

s = 'Hello world!'

#print(s[6:])
#print(s[::2]) #шаг

# перевернуть строку
print(s[::-1])
# слить строку
print(s[:5] + s[6:])
