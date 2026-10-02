import csv


def get_video_game():
    name = input("Nombre: ")
    genre = input("Género: ")
    developer = input("Desarrollador: ")
    classification = input("Clasificación ESRB: ")

    return [name, genre, developer, classification]


def write_csv(video_games):
    with open("videojuegos.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["nombre", "genero", "desarrollador", "clasificacion"])

        for video_game in video_games:
            writer.writerow(video_game)


n = int(input("¿Cuántos videojuegos desea ingresar? "))

video_games = []

for i in range(n):
    print(f"\nVideojuego {i + 1}")
    video_game = get_video_game()
    video_games.append(video_game)

write_csv(video_games)