import random


def roll_dice() -> int:
    """Бросок шестигранного кубика: возвращает число от 1 до 6."""
    return random.randint(1, 6)


def main() -> None:
    print("Игра в кубики для двух игроков")
    print("Правило: у кого выпадет больше очков, тот выигрывает.\n")

    player1 = input("Введите имя первого игрока: ") or "Игрок 1"
    player2 = input("Введите имя второго игрока: ") or "Игрок 2"

    input(f"\n{player1}, нажмите Enter, чтобы бросить кубик...")
    dice1 = roll_dice()
    print(f"{player1} выбросил(а): {dice1}")

    input(f"\n{player2}, нажмите Enter, чтобы бросить кубик...")
    dice2 = roll_dice()
    print(f"{player2} выбросил(а): {dice2}")

    print("\nРезультат:")
    if dice1 > dice2:
        print(f"Победил(а) {player1}!")
    elif dice2 > dice1:
        print(f"Победил(а) {player2}!")
    else:
        print("Ничья!")


if __name__ == "__main__":
    main()