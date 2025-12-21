import flet as ft


def on_picked_file(e: ft.FilePickerResultEvent, name_list, page):
    if not e.files:
        return None, None, None
    
    name_list.controls.clear()
    
    video_name = [f.name.rsplit('.', 1)[0] for f in e.files]
    video_path = [f.path for f in e.files]
    
    for name in video_name:
        name_list.controls.append(ft.Text(f"{name} - Not converted"))

    page.update()

    return video_path, video_name, name_list

def carpeta(e: ft.FilePickerResultEvent, directorio, page):
    if not e.path:
        return None

    files_path = e.path
    directorio.value = f"Output: {e.path}"
    page.update()

    return files_path