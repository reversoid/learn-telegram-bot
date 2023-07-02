import os

BOOK_PATH = 'book_bot/book/book.txt'
PAGE_SIZE = 100

Page = int
Content = str

book: dict[Page, Content] = {}


PUNCTUATION = [',', '.', '!', ':', ';', '?']


def find_last_punctuation_interval(text: str) -> tuple[int, int]:
    index_from: int = None
    index_to: int = None

    i = len(text) - 1
    while i > 0:
        letter = text[i]
        if letter in PUNCTUATION:
            if (index_to == None):
                index_to = i
            index_from = i
        elif index_to != None:
            break

        i -= 1

    return index_from, index_to


def get_correct_text_slice(text: str):
    start_index, end_index = find_last_punctuation_interval(text=text)
    if (start_index == None):
        return ''
    return text[:end_index + 1]


def get_end_text_slice_index(text_len: int, start: int, size: int) -> int:
    expected_end = start + size
    if text_len >= expected_end:
        return expected_end
    return text_len


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    end = get_end_text_slice_index(len(text), start, size)

    unprepared_text_part = text[start:end]
    headroom = text[end] if end != len(text) else ''

    startIndex, endIndex = find_last_punctuation_interval(
        unprepared_text_part)

    unprepared_text_ends_with_punctuation = endIndex == len(
        unprepared_text_part) - 1

    if (unprepared_text_ends_with_punctuation and headroom and headroom[0] in PUNCTUATION):
        result = get_correct_text_slice(text=unprepared_text_part[:startIndex])
        return result, len(result)

    else:
        result = get_correct_text_slice(text=unprepared_text_part)
        return result, len(result)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path) as f:
        full_book = f.read()
        start_index = 0
        page_counter = 1
        while start_index < len(full_book):
            part_of_text = full_book[start_index: start_index + PAGE_SIZE]
            print(part_of_text)

            correct_part_of_text, size = _get_part_text(
                part_of_text, start_index, PAGE_SIZE)

            if (size == 0):
                continue

            book[page_counter] = correct_part_of_text

            page_counter += 1
            start_index += size


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))


print(book)
