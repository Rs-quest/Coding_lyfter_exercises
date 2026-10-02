def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.readlines()


def sort_songs(songs):
    return sorted(songs)


def write_file(path, songs):
    with open(path, "w", encoding="utf-8") as file:
        file.writelines(songs)


songs = read_file("songs.txt")
sorted_songs = sort_songs(songs)
write_file("sorted_songs.txt", sorted_songs)