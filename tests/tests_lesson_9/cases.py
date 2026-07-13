task_1_cases = [
    {
        "numbers": [],
        "result": 0,
    },
    {
        "numbers": [1],
        "result": 1,
    },
    {
        "numbers": [1, 1],
        "result": 1,
    },
    {
        "numbers": [1, 2],
        "result": 2,
    },
    {
        "numbers": [1, 2, 3, 4, 5],
        "result": 5,
    },
    {
        "numbers": [1, 2, 2, 3, 3, 4],
        "result": 4,
    },
    {
        "numbers": [7, 7, 7, 7, 7],
        "result": 1,
    },
    {
        "numbers": [-1, -2, -2, 0, 1],
        "result": 4,
    },
    {
        "numbers": [10**9, -(10**9), 10**9],
        "result": 2,
    },
    {
        "numbers": [5, 3, 5, 2, 3, 1, 2, 4],
        "result": 5,
    },
]
task_2_cases = [
    {
        "first_numbers": [],
        "second_numbers": [],
        "result": 0,
    },
    {
        "first_numbers": [1],
        "second_numbers": [1],
        "result": 1,
    },
    {
        "first_numbers": [1],
        "second_numbers": [2],
        "result": 0,
    },
    {
        "first_numbers": [1, 2, 3],
        "second_numbers": [2, 3, 4],
        "result": 2,
    },
    {
        "first_numbers": [1, 2, 3],
        "second_numbers": [4, 5, 6],
        "result": 0,
    },
    {
        "first_numbers": [1, 2, 3],
        "second_numbers": [1, 2, 3],
        "result": 3,
    },
    {
        "first_numbers": [1, 1, 2, 2, 3],
        "second_numbers": [2, 2, 3, 3, 4],
        "result": 2,
    },
    {
        "first_numbers": [-1, 0, 1],
        "second_numbers": [-1, 2, 3],
        "result": 1,
    },
    {
        "first_numbers": [10**9, -(10**9)],
        "second_numbers": [10**9],
        "result": 1,
    },
    {
        "first_numbers": [5, 4, 3, 2, 1],
        "second_numbers": [1, 2, 3, 4, 5],
        "result": 5,
    },
]
task_3_cases = [
    {
        "numbers": [],
        "result": [],
    },
    {
        "numbers": [1],
        "result": ["NO"],
    },
    {
        "numbers": [1, 1],
        "result": ["NO", "YES"],
    },
    {
        "numbers": [1, 2, 3],
        "result": ["NO", "NO", "NO"],
    },
    {
        "numbers": [1, 2, 1],
        "result": ["NO", "NO", "YES"],
    },
    {
        "numbers": [1, 2, 2, 1],
        "result": ["NO", "NO", "YES", "YES"],
    },
    {
        "numbers": [5, 5, 5, 5],
        "result": ["NO", "YES", "YES", "YES"],
    },
    {
        "numbers": [-1, 0, -1, 1, 0],
        "result": ["NO", "NO", "YES", "NO", "YES"],
    },
    {
        "numbers": [10**9, -(10**9), 10**9],
        "result": ["NO", "NO", "YES"],
    },
    {
        "numbers": [3, 1, 4, 1, 5, 9, 2, 6, 5],
        "result": ["NO", "NO", "NO", "YES", "NO", "NO", "NO", "NO", "YES"],
    },
]
