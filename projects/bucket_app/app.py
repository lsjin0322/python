#리스트 응용 라인편집기 

import flet as ft
import httpx

BASE_URL = "http://127.0.0.1:8000"

GREEN = "#00FF41"
DIM_GREEN = "#00AA22"
DARK_GREEN = "#003300"
BLACK = "#0A0A0A"
PANEL = "#0F1A0F"
RED = "#FF4444"


def main(page: ft.Page):
    page.title = "BUCKET LIST 2025"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = BLACK
    page.padding = 20
    page.fonts = {
        "pixel": "https://fonts.gstatic.com/s/pressstart2p/v15/e3t4euO8T-267oIAQAu6jDQyK3nVivM.woff2"
    }

    editing_id = {"value": None}

    # ── API ──────────────────────────────────────────────
    def api_get(url, params=None):
        try:
            r = httpx.get(url, params=params, timeout=5)
            r.raise_for_status()
            return r.json()
        except Exception as ex:
            set_status(f"ERROR: {ex}")
            return None

    def api_post(url, data):
        try:
            r = httpx.post(url, json=data, timeout=5)
            r.raise_for_status()
            return r.json()
        except Exception as ex:
            set_status(f"ERROR: {ex}")
            return None

    def api_put(url, data):
        try:
            r = httpx.put(url, json=data, timeout=5)
            r.raise_for_status()
            return r.json()
        except Exception as ex:
            set_status(f"ERROR: {ex}")
            return None

    def api_delete(url):
        try:
            r = httpx.delete(url, timeout=5)
            r.raise_for_status()
            return r.json()
        except Exception as ex:
            set_status(f"ERROR: {ex}")
            return None

    # ── 상태바 ───────────────────────────────────────────
    status_text = ft.Text("> SYSTEM READY", size=14, color=DIM_GREEN, italic=True)

    def set_status(msg):
        status_text.value = f"> {msg}"
        page.update()

    # ── 진행률 ───────────────────────────────────────────
    progress_bar = ft.ProgressBar(value=0, bgcolor=DARK_GREEN, color=GREEN, height=12, border_radius=0)
    progress_text = ft.Text("0 / 0  (0%)", size=14, color=GREEN)

    def update_progress():
        data = api_get(f"{BASE_URL}/bucketlist/progress")
        if data:
            progress_bar.value = data["rate"] / 100
            progress_text.value = f"{data['done']} / {data['total']}  ({data['rate']}%) ACHIEVED"

    # ── 입력창 ───────────────────────────────────────────
    new_input = ft.TextField(
        hint_text="> 새 목표를 입력하세요...",
        hint_style=ft.TextStyle(color=DARK_GREEN),
        border_color=DIM_GREEN,
        focused_border_color=GREEN,
        color=GREEN,
        bgcolor=PANEL,
        border_radius=0,
        text_size=16,
        cursor_color=GREEN,
        expand=True,
        content_padding=ft.Padding(left=14, top=10, right=14, bottom=10),
        on_submit=lambda e: add_item(),
    )

    search_input = ft.TextField(
        hint_text="> 검색...",
        hint_style=ft.TextStyle(color=DARK_GREEN),
        border_color=DIM_GREEN,
        focused_border_color=GREEN,
        color=GREEN,
        bgcolor=PANEL,
        border_radius=0,
        text_size=16,
        cursor_color=GREEN,
        expand=True,
        content_padding=ft.Padding(left=14, top=10, right=14, bottom=10),
        on_submit=lambda e: refresh(search_input.value),
    )

    # ── 수정 다이얼로그 ──────────────────────────────────
    edit_input = ft.TextField(
        color=GREEN,
        bgcolor=PANEL,
        border_color=GREEN,
        border_radius=0,
        text_size=16,
        cursor_color=GREEN,
        content_padding=ft.Padding(left=14, top=10, right=14, bottom=10),
        width=340,
    )

    def close_dialog(e=None):
        page.dialog.open = False
        editing_id["value"] = None
        page.update()

    def save_edit(e=None):
        new_title = edit_input.value.strip()
        if new_title and editing_id["value"] is not None:
            api_put(f"{BASE_URL}/bucketlist", {"id": editing_id["value"], "title": new_title})
            set_status(f"UPDATED: {new_title}")
        close_dialog()
        refresh(search_input.value)

    edit_dialog = ft.AlertDialog(
        modal=True,
        bgcolor=BLACK,
        shape=ft.RoundedRectangleBorder(radius=0),
        title=ft.Text("// EDIT MISSION", color=GREEN, size=14),
        content=edit_input,
        actions=[
            ft.TextButton("CANCEL", style=ft.ButtonStyle(color=DIM_GREEN), on_click=close_dialog),
            ft.TextButton("SAVE", style=ft.ButtonStyle(color=GREEN), on_click=save_edit),
        ],
    )
    page.dialog = edit_dialog

    def open_edit(item_id, title):
        editing_id["value"] = item_id
        edit_input.value = title
        edit_dialog.open = True
        page.update()

    # ── 카드 생성 ─────────────────────────────────────────
    def build_card(item: dict, num: int):
        item_id = item["id"]
        is_done = item["done"]
        num_str = str(num).zfill(2)

        badge = ft.Container(
            content=ft.Text(
                "CLEAR!" if is_done else "TODO",
                size=11, color=GREEN if is_done else DARK_GREEN,
            ),
            border=ft.border.all(1, GREEN if is_done else DARK_GREEN),
            padding=ft.Padding(left=6, top=2, right=6, bottom=2),
        )

        def on_toggle(e):
            api_put(f"{BASE_URL}/bucketlist", {"id": item_id, "done": not is_done})
            set_status("MISSION CLEAR! 🎉" if not is_done else "BACK TO TODO")
            refresh(search_input.value)

        def on_edit(e):
            open_edit(item_id, item["title"])

        def on_delete(e):
            api_delete(f"{BASE_URL}/bucketlist/{item_id}")
            set_status(f"DELETED: {item['title']}")
            refresh(search_input.value)

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text(num_str, size=11, color=DARK_GREEN),
                    ft.Text(
                        item["title"],
                        size=16,
                        color=DIM_GREEN if is_done else GREEN,
                        style=ft.TextStyle(
                            decoration=ft.TextDecoration.LINE_THROUGH if is_done else None
                        ),
                        expand=True,
                    ),
                    ft.Row(
                        controls=[
                            badge,
                            ft.Row(
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.CHECK if not is_done else ft.Icons.UNDO,
                                        icon_color=GREEN,
                                        icon_size=16,
                                        tooltip="완료 토글",
                                        on_click=on_toggle,
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.EDIT,
                                        icon_color=DIM_GREEN,
                                        icon_size=16,
                                        tooltip="수정",
                                        on_click=on_edit,
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.CLOSE,
                                        icon_color=RED,
                                        icon_size=16,
                                        tooltip="삭제",
                                        on_click=on_delete,
                                    ),
                                ],
                                spacing=0,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                ],
                spacing=8,
            ),
            bgcolor=PANEL if not is_done else "#050F05",
            border=ft.border.all(1, DIM_GREEN if not is_done else DARK_GREEN),
            border_radius=0,
            padding=14,
            expand=True,
        )

    # ── 그리드 ───────────────────────────────────────────
    grid = ft.GridView(
        expand=True,
        runs_count=3,
        max_extent=280,
        child_aspect_ratio=1.2,
        spacing=10,
        run_spacing=10,
    )

    def refresh(search_text=""):
        params = {"search": search_text} if search_text else None
        data = api_get(f"{BASE_URL}/bucketlist", params=params)
        grid.controls.clear()
        if data is not None:
            if len(data) == 0:
                grid.controls.append(
                    ft.Container(
                        content=ft.Text(
                            "목표가 없습니다.\n새 목표를 추가해보세요!",
                            size=16, color=DARK_GREEN,
                            text_align=ft.TextAlign.CENTER,
                        ),
                        alignment=ft.Alignment(0, 0),
                        expand=True,
                    )
                )
            else:
                for i, item in enumerate(data):
                    grid.controls.append(build_card(item, i + 1))
        update_progress()
        page.update()

    def add_item():
        title = new_input.value.strip()
        if not title:
            set_status("ERROR: 내용을 입력하세요")
            return
        result = api_post(f"{BASE_URL}/bucketlist", {"title": title})
        if result:
            new_input.value = ""
            set_status(f"ADDED: {result['title']}")
            refresh(search_input.value)

    # ── 버튼 스타일 ───────────────────────────────────────
    def pixel_btn(label, on_click):
        return ft.OutlinedButton(
            label,
            style=ft.ButtonStyle(
                color=GREEN,
                side=ft.BorderSide(1, DIM_GREEN),
                shape=ft.RoundedRectangleBorder(radius=0),
                padding=ft.Padding(left=16, top=10, right=16, bottom=10),
            ),
            on_click=on_click,
        )

    # ── 레이아웃 ─────────────────────────────────────────
    header = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("👾 👾", size=28, text_align=ft.TextAlign.CENTER),
                ft.Text(
                    "2026년 버킷리스트",
                    size=22, color=GREEN,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "> 한번사는 인생 멋있게 살자",
                    size=14, color=DIM_GREEN,
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Container(height=10),
                progress_bar,
                ft.Row(controls=[progress_text], alignment=ft.MainAxisAlignment.END),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
        ),
        bgcolor=PANEL,
        border=ft.border.all(1, DARK_GREEN),
        padding=20,
        margin=ft.Margin(bottom=14, top=0, left=0, right=0),
    )

    search_row = ft.Row(
        controls=[
            search_input,
            pixel_btn("SEARCH", lambda e: refresh(search_input.value)),
            pixel_btn("RESET", lambda e: (setattr(search_input, "value", ""), refresh(""))),
        ],
        spacing=8,
    )

    add_row = ft.Row(
        controls=[
            new_input,
            pixel_btn("+ ADD", lambda e: add_item()),
        ],
        spacing=8,
    )

    page.add(
        ft.Column(
            controls=[
                header,
                search_row,
                add_row,
                ft.Container(height=4),
                grid,
                ft.Divider(height=1, color=DARK_GREEN),
                status_text,
            ],
            spacing=10,
            expand=True,
        )
    )

    refresh()


if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER)