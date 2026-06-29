def get_investment_result(min_amount: int, mike_amount: int, ivan_amount: int) -> str:
    mike_can_invest = mike_amount >= min_amount
    ivan_can_invest = ivan_amount >= min_amount

    if mike_can_invest and ivan_can_invest:
        return "2"

    if mike_can_invest:
        return "Mike"

    if ivan_can_invest:
        return "Ivan"

    if mike_amount + ivan_amount >= min_amount:
        return "1"

    return "0"


def main():
    min_amount = int(input("Минимальная сумма инвестиций: "))
    mike_amount = int(input("Сумма Майкла: "))
    ivan_amount = int(input("Сумма Ивана: "))

    print(get_investment_result(min_amount, mike_amount, ivan_amount))


if __name__ == "__main__":
    main()
