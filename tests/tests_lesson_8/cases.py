task_1_cases = [
    {
        "numbers": [],
        "result": [],
    },
    {
        "numbers": [1],
        "result": [1],
    },
    {
        "numbers": [1, 2],
        "result": [2, 1],
    },
    {
        "numbers": [1, 2, 3],
        "result": [3, 2, 1],
    },
    {
        "numbers": [5, 4, 3, 2, 1],
        "result": [1, 2, 3, 4, 5],
    },
    {
        "numbers": [0, 0, 0],
        "result": [0, 0, 0],
    },
    {
        "numbers": [-1, -2, -3],
        "result": [-3, -2, -1],
    },
    {
        "numbers": [10, -5, 0, 8],
        "result": [8, 0, -5, 10],
    },
    {
        "numbers": [100000, -100000],
        "result": [-100000, 100000],
    },
    {
        "numbers": [7, 1, 9, 3, 5, 2],
        "result": [2, 5, 3, 9, 1, 7],
    },
]
task_2_cases = [
    {
        "numbers": [],
        "result": [],
    },
    {
        "numbers": [1],
        "result": [1],
    },
    {
        "numbers": [1, 2],
        "result": [2, 1],
    },
    {
        "numbers": [1, 2, 3],
        "result": [3, 1, 2],
    },
    {
        "numbers": [1, 2, 3, 4],
        "result": [4, 1, 2, 3],
    },
    {
        "numbers": [5, 4, 3, 2, 1],
        "result": [1, 5, 4, 3, 2],
    },
    {
        "numbers": [0, 0, 0],
        "result": [0, 0, 0],
    },
    {
        "numbers": [-1, -2, -3],
        "result": [-3, -1, -2],
    },
    {
        "numbers": [10, -5, 0, 8],
        "result": [8, 10, -5, 0],
    },
    {
        "numbers": [1_000_000_000, 1, 2, 3],
        "result": [3, 1_000_000_000, 1, 2],
    },
]
task_3_cases = [
    {
        "max_weight": 100,
        "weights": [50],
        "result": 1,
    },
    {
        "max_weight": 100,
        "weights": [50, 50],
        "result": 1,
    },
    {
        "max_weight": 100,
        "weights": [60, 50],
        "result": 2,
    },
    {
        "max_weight": 100,
        "weights": [40, 60, 50],
        "result": 2,
    },
    {
        "max_weight": 100,
        "weights": [20, 30, 40, 50],
        "result": 2,
    },
    {
        "max_weight": 100,
        "weights": [70, 80, 90],
        "result": 3,
    },
    {
        "max_weight": 100,
        "weights": [20, 20, 80, 80],
        "result": 2,
    },
    {
        "max_weight": 100,
        "weights": [30, 40, 50, 60, 70],
        "result": 3,
    },
    {
        "max_weight": 150,
        "weights": [40, 50, 60, 70, 80],
        "result": 3,
    },
    {
        "max_weight": 200,
        "weights": [100, 90, 80, 70, 60, 50],
        "result": 3,
    },
]
