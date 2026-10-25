import random


def roll_dice() -> int:
    """Бросок шестигранного кубика: возвращает число от 1 до 6."""
    return random.randint(1, 6)


def main() -> None:
    print("Игра в кубики для трех игроков")
    print("Правило: побеждает игрок с наибольшим числом очков.\n")

    player1 = input("Введите имя первого игрока: ") or "Игрок 1"
    player2 = input("Введите имя второго игрока: ") or "Игрок 2"
    player3 = input("Введите имя третьего игрока: ") or "Игрок 3"

    input(f"\n{player1}, нажмите Enter, чтобы бросить кубик...")
    dice1 = roll_dice()
    print(f"{player1} выбросил(а): {dice1}")

    input(f"\n{player2}, нажмите Enter, чтобы бросить кубик...")
    dice2 = roll_dice()
    print(f"{player2} выбросил(а): {dice2}")

    input(f"\n{player3}, нажмите Enter, чтобы бросить кубик...")
    dice3 = roll_dice()
    print(f"{player3} выбросил(а): {dice3}")

    print("\nРезультат:")

    max_score = max(dice1, dice2, dice3)

    if dice1 == max_score and dice2 != max_score and dice3 != max_score:
        print(f"Победил(а) {player1}!")
    elif dice2 == max_score and dice1 != max_score and dice3 != max_score:
        print(f"Победил(а) {player2}!")
    elif dice3 == max_score and dice1 != max_score and dice2 != max_score:
        print(f"Победил(а) {player3}!")
    else:
        print("Ничья!")


if __name__ == "__main__":
    main()
