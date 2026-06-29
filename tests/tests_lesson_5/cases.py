task_1_cases = [
    {
        "input_value": "0",
        "result": "нулевое число",
    },
    {
        "input_value": "1",
        "result": "положительное нечетное число",
    },
    {
        "input_value": "-1",
        "result": "отрицательное нечетное число",
    },
    {
        "input_value": "2",
        "result": "положительное четное число",
    },
    {
        "input_value": "-2",
        "result": "отрицательное четное число",
    },
    {
        "input_value": "190",
        "result": "положительное четное число",
    },
    {
        "input_value": "-999999",
        "result": "отрицательное нечетное число",
    },
    {
        "input_value": "",
        "result": "не является целым числом",
    },
    {
        "input_value": "Привет",
        "result": "не является целым числом",
    },
    {
        "input_value": "😀",
        "result": "не является целым числом",
    },
]
task_2_cases = [
    {
        "word": "",
        "result": "Количество согласных: 0\n"
        "Количество гласных: 0\n"
        "a: False\n"
        "e: False\n"
        "i: False\n"
        "o: False\n"
        "u: False",
    },
    {
        "word": "a",
        "result": "Количество согласных: 0\n"
        "Количество гласных: 1\n"
        "a: 1\n"
        "e: False\n"
        "i: False\n"
        "o: False\n"
        "u: False",
    },
    {
        "word": "e",
        "result": "Количество согласных: 0\nКоличество гласных: 1\na: False\ne: 1\ni: False\no: False\nu: False",
    },
    {
        "word": "i",
        "result": "Количество согласных: 0\nКоличество гласных: 1\na: False\ne: False\ni: 1\no: False\nu: False",
    },
    {
        "word": "o",
        "result": "Количество согласных: 0\nКоличество гласных: 1\na: False\ne: False\ni: False\no: 1\nu: False",
    },
    {
        "word": "u",
        "result": "Количество согласных: 0\nКоличество гласных: 1\na: False\ne: False\ni: False\no: False\nu: 1",
    },
    {
        "word": "b",
        "result": "Количество согласных: 1\nКоличество гласных: 0\na: False\ne: False\ni: False\no: False\nu: False",
    },
    {
        "word": "hello",
        "result": "Количество согласных: 3\nКоличество гласных: 2\na: False\ne: 1\ni: False\no: 1\nu: False",
    },
    {
        "word": "education",
        "result": "Количество согласных: 4\nКоличество гласных: 5\na: 1\ne: 1\ni: 1\no: 1\nu: 1",
    },
    {
        "word": "aeiou",
        "result": "Количество согласных: 0\nКоличество гласных: 5\na: 1\ne: 1\ni: 1\no: 1\nu: 1",
    },
    {
        "word": "aaaa",
        "result": "Количество согласных: 0\nКоличество гласных: 4\na: 4\ne: False\ni: False\no: False\nu: False",
    },
    {
        "word": "bbb",
        "result": "Количество согласных: 3\nКоличество гласных: 0\na: False\ne: False\ni: False\no: False\nu: False",
    },
    {
        "word": "queue",
        "result": "Количество согласных: 1\nКоличество гласных: 4\na: False\ne: 2\ni: False\no: False\nu: 2",
    },
    {
        "word": "rhythm",
        "result": "Количество согласных: 6\nКоличество гласных: 0\na: False\ne: False\ni: False\no: False\nu: False",
    },
    {
        "word": "Apple",
        "result": "Количество согласных: 3\nКоличество гласных: 2\na: 1\ne: 1\ni: False\no: False\nu: False",
    },
    {
        "word": "AEIOU",
        "result": "Количество согласных: 0\nКоличество гласных: 5\na: 1\ne: 1\ni: 1\no: 1\nu: 1",
    },
    {
        "word": "Python",
        "result": "Количество согласных: 5\nКоличество гласных: 1\na: False\ne: False\ni: False\no: 1\nu: False",
    },
    {
        "word": "mississippi",
        "result": "Количество согласных: 7\nКоличество гласных: 4\na: False\ne: False\ni: 4\no: False\nu: False",
    },
    {
        "word": "substitution",
        "result": "Количество согласных: 7\nКоличество гласных: 5\na: False\ne: False\ni: 2\no: 1\nu: 2",
    },
    {
        "word": "abcdefghijklmnopqrstuvwxyz",
        "result": "Количество согласных: 21\nКоличество гласных: 5\na: 1\ne: 1\ni: 1\no: 1\nu: 1",
    },
]
task_3_cases = [
    {
        "min_amount": 100,
        "mike_amount": 150,
        "ivan_amount": 200,
        "result": "2",
    },
    {
        "min_amount": 100,
        "mike_amount": 100,
        "ivan_amount": 100,
        "result": "2",
    },
    {
        "min_amount": 100,
        "mike_amount": 150,
        "ivan_amount": 50,
        "result": "Mike",
    },
    {
        "min_amount": 100,
        "mike_amount": 100,
        "ivan_amount": 99,
        "result": "Mike",
    },
    {
        "min_amount": 100,
        "mike_amount": 50,
        "ivan_amount": 150,
        "result": "Ivan",
    },
    {
        "min_amount": 100,
        "mike_amount": 99,
        "ivan_amount": 100,
        "result": "Ivan",
    },
    {
        "min_amount": 100,
        "mike_amount": 60,
        "ivan_amount": 40,
        "result": "1",
    },
    {
        "min_amount": 100,
        "mike_amount": 70,
        "ivan_amount": 29,
        "result": "0",
    },
    {
        "min_amount": 1,
        "mike_amount": 0,
        "ivan_amount": 1,
        "result": "Ivan",
    },
    {
        "min_amount": 1_000_000,
        "mike_amount": 700_000,
        "ivan_amount": 500_000,
        "result": "1",
    },
]
