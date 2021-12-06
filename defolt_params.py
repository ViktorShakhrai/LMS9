def greet(name, word="-") -> str:
    a = (f"{name.capitalize()} ты сегодня {word}!")
    return a


assert greet("111", "2") == "111 ты сегодня 2!"
assert greet("игорь", "молодец") == "Игорь ты сегодня молодец!"
assert greet(name="ольга", word="супер") == "Ольга ты сегодня супер!"
assert greet("николай") == "Николай ты сегодня -!"
