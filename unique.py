from typing import Sequence, Dict, List, Tuple


def humanize_list(items: Sequence[str]) -> str:
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + ", and " + items[-1]


def resolve_duplicates(character: str, characters: Sequence[str]) -> List[int]:
    occurances: List[int] = []
    for idx, char in enumerate(characters, start=1):
        if char == character:
            occurances.append(idx)
    return occurances


def map_duplicates(characters: Sequence[str]) -> Tuple[Dict[str, List[int]], bool]:
    book: Dict[str, List[int]] = {
    }
    has_duplicates: bool = False
    for char in characters:
        if char in book.keys():
            continue
        else:
            book[char] = resolve_duplicates(char, characters)
            if not has_duplicates and len(book[char]) > 1:
                has_duplicates = True
    return book, has_duplicates


while True:
    input_string = input("enter a string: ")
    if len(set(input_string)) == len(input_string):
        print("The string contains only unique characters")
        continue
    else:
        data, has_dupl = map_duplicates(input_string)
        if not has_dupl:
            print("The string contains only unique characters")
        else:
            end = ['the following characters: \n']
            for k, v in data.items():
                if len(v) == 1:
                    continue
                end.append(f"the character {k} which is found at positions {humanize_list(list(map(str, v)))}")
            end = '\n'.join(end)
            print(
                f"The string does not contain only unique characters as it contains multiple copies of {end}"
            )
