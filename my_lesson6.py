import sys
from pathlib import Path

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
    "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

BAD_SYMBOLS = ('%','*',' ','-')

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

for i in BAD_SYMBOLS:
    TRANS[ord(i)] = '_'

CATEGORIES = {
    'images': ['.jpeg', '.png', '.jpg', '.svg'],
    'video': ['.avi', '.mp4', '.mov', '.mkv'],
    'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    'audio': ['.mp3', '.ogg', '.wav', '.amr'],
    'archives': ['.zip', '.gz', '.tar'],
    'others': []
}

def normalize(name: str) -> str:
    trans_name = name.translate(TRANS)
    return trans_name

def move_file(file: Path, root_dir: Path, category: str):
    if category == 'Unknown':
        return file.replace(root_dir.joinpath(normalize(file.name)))

    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir()
    return file.replace(target_dir.joinpath(normalize(file.name)))

def get_categories(file: Path):
    extension = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if extension in exts:
            return cat
    return 'Unknown'

def sort_dir(root_dir: Path, current_dir: Path):
    for item in [f for f in current_dir.glob('*') if f.name not in CATEGORIES.keys()]:
        if not item.is_dir():
            category = get_categories(item)
            new_path = move_file(item, root_dir, category)
            print(new_path)
        else:
            sort_dir(root_dir, item)
            item.rmdir()

def main():
    try:
        path = Path(sys.argv[1])

    except IndexError:
        return f'No path to folder. Try again later'

    if not path.exists():
        return 'Sorry, folder does not exist'

    sort_dir(path, path)
    return 'All Ok'

if __name__ == '__main__':
    print(main())