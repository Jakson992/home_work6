import sys
from pathlib import Path

CATEGORIES = {
    'images': ['.jpeg', '.png', '.jpg', '.svg'],
    'video': ['.avi', '.mp4', '.mov', '.mkv'],
    'documents': ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'],
    'audio': ['.mp3', '.ogg', '.wav', '.amr'],
    'archives': ['.zip', '.gz', '.tar'],
    'others': []
}

def move_file(file:Path,root_dir:Path,category:str):
    if category == 'Unknown':
        return file.replace(root_dir.joinpath(file.name))

    target_dir = root_dir.joinpath(category)
    if not target_dir.exists():
        target_dir.mkdir()
    return file.replace(target_dir.joinpath(file.name))

def get_categories(file: Path):
    extension = file.suffix.lower()
    for cat, exts in CATEGORIES.items():
        if extension in exts:
            return cat
    return 'Unknown'


def sort_dir(root_dir: Path,current_dir:Path):
    for item in [f for f in current_dir.glob('*') if f.name not in CATEGORIES.keys()]:
       print(item.name)
        # if not item.is_dir():
        #     category = get_categories(item)
        #     new_path = move_file(item,root_dir,category)
        #     print(new_path)
        # else:
        #     sort_dir(root_dir,item)
        #     item.rmdir()

def main():
    try:
        path = Path(sys.argv[1])

    except IndexError:
        return f'No path to folder.Try again later'
    if not path.exists():
        return 'Sorry folder not exists'
    sort_dir(path , path)
    return 'All Ok'


if __name__ == '__main__':
    print(main())
