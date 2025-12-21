import flet as ft
from components.video import convert_video as cnv
from components.ui import select_file as sf


def main(page: ft.Page):

    video_path = None
    files_path = None
    video_name = None
    name_list = ft.ListView(expand=True, spacing=5, auto_scroll=True)

    
    page.title = "Davinci Re-Solver for Linux"
    page.padding = 10
    page.theme_mode = ft.ThemeMode.SYSTEM
    
    """""
    no tiene sentido usar esto todavia
    def open_url():
        page.launch_url('https://github.com/racsuline/Davinci-Solver')

    
    burguer = ft.Container(
        ft.PopupMenuButton(
            tooltip = "Settings",
            icon = ft.Icons.MENU,
            height = 48,
            width = 48,
            items = [
                ft.PopupMenuItem(
                    content = ft.Text("Github Repo", theme_style=ft.TextThemeStyle.LABEL_MEDIUM, text_align = ft.TextAlign.CENTER),
                    on_click = lambda e: open_url()
                )
            ]
        ),
        padding=ft.padding.only(right=-10),
        border_radius=ft.border_radius.all(3),
    )
    """

    directorio = ft.Text("Output Folder: Not selected")
    info_row = ft.Row([directorio], alignment = ft.MainAxisAlignment.CENTER)

    
    suffix = ""
    suffix_field = ft.TextField(
        value = "",
        label = "Add a suffix to the converted file name",
        hint_text = "_Example",
        on_change = lambda e: update_suffix(),
        width = 400,
        border_color = ft.Colors.GREY_800
        )

    def update_suffix():
        nonlocal suffix
        if not suffix_field.value:
            return
        else:
            suffix = suffix_field.value
            return
    
    def on_picked_file(e):
        nonlocal video_path, video_name, name_list
        video_path, video_name, name_list = sf.on_picked_file(e, name_list, page)

    def carpeta(e):
        nonlocal files_path
        files_path = sf.carpeta(e, directorio, page)

    def convertir_video():
        nonlocal name_list
        cnv.convertir_video(video_path, video_name, files_path, progress_bar, progress_text, page, suffix, name_list)
    
    # LISTA DE VIDEOS CARGADOS Y CONVERSIONES COMPLETADAS

    loaded_videos = ft.Container(
        name_list,
        border = ft.border.all(1, ft.Colors.GREY_800),
        border_radius = 2,
        height = 200,
        width = 400,
        bgcolor = ft.Colors.GREY_900,
        padding = 10
    )


    # BARRA DE PROGRESO
    progress_bar = ft.ProgressBar(value=0, visible=True, width = 500)
    progress_text = ft.Text("No conversion is running yet", visible=True)

    progress_container = ft.Container(
        content = ft.Column(
            [
                ft.Text("Progress"),
                progress_text,
                progress_bar
            ],
            alignment = ft.MainAxisAlignment.CENTER
        ),
        border = ft.border.all(1, ft.Colors.GREY_800),
        border_radius = 2,
        width = 400,
        padding = 10
    )
    # PICKERS
    picker = ft.FilePicker(on_result = on_picked_file)
    c_pick = ft.FilePicker(on_result = carpeta)
    page.overlay.append(c_pick)
    page.overlay.append(picker)

    # BOTONES
    select_output = ft.FilledButton(
        "Output Folder",
        icon = ft.Icons.FOLDER,                                                        
        on_click = lambda _: c_pick.get_directory_path(dialog_title = "Choose a folder to save the converted files"),
        color = ft.Colors.WHITE,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),
        bgcolor = ft.Colors.YELLOW_800,
        tooltip = "Where converted videos will be saved"
        
    )

    select_video = ft.FilledButton(
        "Upload Videos",
        icon = ft.Icons.UPLOAD_FILE_ROUNDED,
        on_click = lambda _: picker.pick_files(allowed_extensions = ["mp4", "mov", "avi", "mkv", "flv", "webm", "wmv", "m4v"], allow_multiple= True),
        color = ft.Colors.WHITE,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),
        bgcolor = ft.Colors.RED_800,
        tooltip = "Select video files to convert"
    )

    start_converting = ft.FilledButton(
        "Convert File",
        icon = ft.Icons.VIDEO_CHAT,                                                    
        on_click = lambda v: convertir_video(),
        color = ft.Colors.WHITE,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10),),
        bgcolor = ft.Colors.GREEN_800
        
    )
    page.add(
        ft.Column(
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(
                    "Convert your videos to edit them on Davinci Resolve!",
                    size=20,
                    weight= "bold"
                ),
                ft.Column(
                    [
                        ft.Text("Choose Files"),
                        loaded_videos
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                info_row,
                ft.Row(
                    [
                        suffix_field,
                    ],
                    alignment = ft.MainAxisAlignment.CENTER
                ),
                progress_container,
                ft.Divider(),
                ft.Container(
                    padding=10,
                    content=ft.SafeArea(
                        ft.Row(
                            [
                                select_output,
                                select_video,
                                start_converting
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            wrap=True
                        )
                    )
                )
            ]
        )
    )


ft.app(target = main)
