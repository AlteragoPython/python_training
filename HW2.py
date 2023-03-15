
def transform(legacy_data: dict[int, list[str]]) -> dict[str, int]:
    new_data = {}
    for key, value in legacy_data.items():
        for letter in value:
            if letter in new_data:
                new_data[letter] += key
            else:
                new_data[letter] = key
    print(new_data)

legacy_data = {1: ["A", "E"], 2: ["D", "G"]}
transform(legacy_data)