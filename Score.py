import Utils

def add_score(diff):
    current_score = 0
    try:
        read_file = open(Utils.SCORES_FILE_NAME, 'r')
        current_score = int(read_file.readline())
        read_file.close()
    except (ValueError, FileNotFoundError):
        print(f"{Utils.SCORES_FILE_NAME} was empty / not found, continuing anyway")

    new_score = current_score + ((diff * 3) + 5)

    write_file = open(Utils.SCORES_FILE_NAME, 'w')
    write_file.write(str(new_score))
    write_file.close()

