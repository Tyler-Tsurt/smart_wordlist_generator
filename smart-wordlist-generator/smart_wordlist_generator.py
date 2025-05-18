import os

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print("=" * 60)
    print("\U0001F512 Smart Wordlist Generator v2.0")
    print("\U0001F3AF Mimics real human password habits")
    print("\U0001F6E0️  By: Ty-Tech")
    print("=" * 60)

def get_input(prompt):
    try:
        response = input(prompt)
        if response is None:
            return "-"
        return response.strip() or "-"
    except (KeyboardInterrupt, EOFError):
        print("\n\n\u26D4 Exiting.")
        exit()
    except Exception as e:
        print(f"\n[!] Error getting input: {e}\nDefaulting to '-' for this field.")
        return "-"

def gather_data():
    print("\n\U0001F4CB Enter Target Profile Info (press Enter to skip any):\n")
    data = {
        "name": get_input("\U0001F464 Real Name: "),
        "nickname": get_input("\U0001F9D1 Nickname: "),
        "username": get_input("\U0001F4BB Username / Handle: "),
        "birth_year": get_input("\U0001F382 Birth year (e.g., 1997): "),
        "birth_day": get_input("\U0001F389 Birth day (e.g., 14): "),
        "birth_month": get_input("\U0001F5D3️ Birth month (June or 06): "),
        "partner_name": get_input("\U0001F491 Partner's name: "),
        "partner_birth_day": get_input("\U0001F381 Partner's birth day: "),
        "mother_name": get_input("\U0001F475 Mother's name: "),
        "mother_birth_year": get_input("\U0001F5D3️ Mother's birth year: "),
        "father_name": get_input("\U0001F474 Father's name: "),
        "father_birth_year": get_input("\U0001F5D3️ Father's birth year: "),
        "pet_name": get_input("\U0001F436 Pet's name: "),
        "phone_number": get_input("\U0001F4DE Phone number (last 4 digits): "),
        "location": get_input("\U0001F4CD Location (city, town): "),
        "interests": get_input("\U0001F3AF Interests (e.g., football): "),
        "fav_phrase": get_input("\U0001F4AC Favorite phrase or word: ")
    }
    return data

def generate_wordlist(data):
    specials = ["@", "!", "#", "123", ".", "01"]
    common_numbers = ["123", "1234", "123456", "0000", "007", "786", "1122", "1999", "2000", "2020", "2023", "2024", "789", "786786", "999", "1212"]

    names = [data[k] for k in ["name", "nickname", "partner_name", "mother_name", "father_name", "pet_name", "username"] if data[k] != "-"]
    extras = [data[k] for k in ["birth_year", "mother_birth_year", "father_birth_year", "birth_day", "birth_month", "partner_birth_day", "phone_number", "location", "interests", "fav_phrase"] if data[k] != "-"]

    combos = set()

    for name in names:
        for extra in extras + common_numbers:
            combos.update([
                f"{name}{extra}", f"{name}@{extra}", f"{extra}{name}",
                f"{name.capitalize()}{extra}", f"{name}{extra}!", f"{name}_{extra}",
                f"{name.lower()}#{extra}", f"{name}{extra[::-1]}"
            ])

    for name1 in names:
        for name2 in names:
            if name1 != name2:
                for num in common_numbers:
                    combos.update([
                        f"{name1}{name2}", f"{name1}@{name2}", f"{name1}{name2}{num}",
                        f"{name1.capitalize()}{name2.capitalize()}", f"{name2}{name1}!",
                        f"{name1}{num}{name2}"
                    ])

    for item in list(combos):
        for sp in specials:
            combos.add(item + sp)
            combos.add(sp + item)

    return combos

def save_wordlist(wordlist):
    filename = "smart_wordlist.txt"
    with open(filename, "w") as f:
        for word in sorted(wordlist):
            f.write(word + "\n")
    print(f"\n\u2705 Wordlist saved as: {filename}")
    print(f"\U0001F4C2 Total passwords generated: {len(wordlist)}")

def main():
    banner()
    profile = gather_data()
    print("\n\U0001F9E0 Generating smart wordlist...\n")
    wordlist = generate_wordlist(profile)
    save_wordlist(wordlist)

if __name__ == "__main__":
    main()

