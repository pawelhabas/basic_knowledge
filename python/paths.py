import os
from pathlib import Path

from python_basic_utils import line_separator as ls

if __name__ == '__main__':
    print_parts = {'old_way': 0,
                   'new_way': 0,
                   'file_exists': 0,
                   'set_file_path': 0,
                   'creating_dir_and_file': 0,
                   }

    if print_parts['old_way']:
        old_way_path = os.path.join("data", "files", "example.txt")
        print(f"Old way: {old_way_path}")
        ls()

    if print_parts['new_way']:
        #   more useful cross-platform

        new_way_path = Path("data") / "files" / "example.txt"
        print(f"New way: {new_way_path}")
        ls()

    if print_parts['file_exists']:
        #   Sprawdzenie, czy plik istnieje; jego parametry

        config_file = Path("config") / "settings.json"

        if config_file.exists():
            print(f"Config file exists at: {config_file}")

        print(f"Parent: {config_file.parent}")
        print(f"Filename: {config_file.name}")
        print(f"Extension: {config_file.suffix}")
        ls()

    if print_parts['set_file_path']:
        # Ustawienie bezwzględnej ścieżki do pliku konfiguracyjnego
        path = Path(__file__)
        print("Current file path: ", path)
        path_settings = (Path(__file__).resolve().parent / "config" / "settings.json")
        print("Setting path: ", path_settings)
        ls()

    if print_parts['creating_dir_and_file']:
        # utworzenie katalogu, utworzenie pliku, zapis i odczyt z pliku
        data_dir = Path("data") / "output"
        data_dir.mkdir(parents=True, exist_ok=True)

        output_file = data_dir / "results.txt"
        output_file.write_text("Hello, pathlib!")
        print(f"Wrote to: {output_file}")
        print(f"Read: {output_file.read_text()}")
        ls()
