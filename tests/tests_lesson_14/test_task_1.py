import ast
import inspect

from src.lesson_14 import task_1


def test_print_list_recursively(capsys) -> None:
    task_1.print_list_recursively([0, 1, 2])

    assert capsys.readouterr().out.splitlines() == [
        "0",
        "1",
        "2",
        "Конец списка",
    ]


def test_print_list_recursively_does_not_use_loops() -> None:
    source = inspect.getsource(task_1.print_list_recursively)
    tree = ast.parse(source)

    assert not any(isinstance(node, ast.For | ast.While) for node in ast.walk(tree))
