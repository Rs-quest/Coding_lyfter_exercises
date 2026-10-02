print("Calculadora de notas")

total_grades = int(input("¿Cuántas notas vas a ingresar?"))

approved = 0
not_approved = 0

total_sum = 0
approved_sum = 0
not_approved_sum = 0

for i in range(total_grades):

    grade = int(input("Ingresa una nota: "))

    total_sum = total_sum + grade

    if grade >= 70:
        approved = approved + 1
        approved_sum = approved_sum + grade
    else:
        not_approved = not_approved + 1
        not_approved_sum = not_approved_sum + grade

average = total_sum / total_grades

if approved > 0:
    approved_average = approved_sum / approved
else:
    approved_average = 0

if not_approved > 0:
    not_approved_average = not_approved_sum / not_approved
else:
    not_approved_average = 0

print(f"Notas aprobadas: {approved}")
print(f"Notas desaprobadas: {not_approved}")
print(f"Promedio general: {average}")
print(f"Promedio aprobadas: {approved_average}")
print(f"Promedio desaprobadas: {not_approved_average}")