# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).


def print_operation_table(operation, num_rows=6, num_columns=6):
    for rows in range(1, num_rows+1):
        list = []
        for i in range(1, num_columns+1):
            list.append(operation(i, rows))
        print (*list)

print_operation_table(lambda x, y: x * y)

