def calculate_structure_sum(data):
    total_sum = 0

    for element in data:
        if isinstance(element,(int, float)):
            total_sum += element
        elif isinstance(element, str):
            total_sum += len(element)
        elif isinstance(element, (list, tuple)):
           total_sum += calculate_structure_sum(element)
        elif isinstance(element, dict):

            for key, value in element.items():
                if isinstance(key, str):
                    total_sum += len(key)
                if isinstance(value, (int, float)):
                    total_sum += value
                elif isinstance(value, (list, tuple, dict)):
                    total_sum += calculate_structure_sum([value])
        elif isinstance(element, set):
            total_sum += calculate_structure_sum(list(element))
    return total_sum



data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

