'''Dado uma entrada onde a primeira linha eh um numero indicando o numero de alunos,
a linha seguinte eh um aluno e na linha seguinte sua respectiva nota e assim por diante.
imprima na tela os nomes dos alunos que tiverem a segunda menor nota da sala. Caso exista mais
de um aluno com a segunda menor nota, imprima ambos em ordem alfabetica, um em cada linha.'''

students_number = int(input())
students_list = []
for student in range(students_number):
    student_name = input()
    student_grade = float(input())
    students_list.append([student_name, student_grade])
minimum = 100
for name, grade in students_list:
    if minimum > grade:
        minimum = grade
        aluno_minimo = [name, grade]
students_list = [student for student in students_list if student[1] != aluno_minimo[1]]
minimum = 100
for name, grade in students_list:
    if minimum > grade:
        minimum = grade
        aluno_minimo = [name, grade]
alunos = [student[0] for student in students_list if student[1] == aluno_minimo[1]]
alunos.sort()
for aluno in alunos:
    print(aluno)
