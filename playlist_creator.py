#replace:   disk:/path_to_the_folder_with_files     line 5
#replace:   playlist_name                           line 6
#replace:   path_to_files_on_flipper                line 11
from pathlib import Path
directory = Path(r'disk:/path_to_the_folder_with_files')
output_file = Path('playlist_name.txt')
sub_files = list(directory.rglob('*.sub'))
with output_file.open('w') as file:
    for file_path in sub_files:
        relative_path = file_path.relative_to(directory)
        formatted_line = f"sub: /ext/subghz/path_to_files_on_flipper/{relative_path.as_posix()}\n"
        file.write(formatted_line)
print(relative_path.as_posix())
print(f"Write to {output_file.resolve()}")
