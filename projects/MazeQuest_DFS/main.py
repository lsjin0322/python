# main.py
import flet as ft
import asyncio
from models import Theme, START, END, WALL
from solver import MazeSolver, get_maze

CELL_SIZE   = {"random": 36, "pixel": 28, "simple": 40}
CELL_RADIUS = 3

def main(page: ft.Page):
    page.title        = "Pixel Maze Quest — DFS"
    page.bgcolor      = Theme.BASE
    page.padding      = 24
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width  = 900
    page.window_height = 780

    state = {
        "mode":       "random",
        "maze":       None,
        "solver":     None,
        "running":    False,
        "speed":      0.08,
        "steps":      0,
        "backtracks": 0,
        "dead_ends":  0,
    }

    grid_cells = []

    def pixel_char(size):
        s = max(size - 12, 10)
        return ft.Container(width=s, height=s, bgcolor=Theme.POINT, border_radius=2)

    title_text  = ft.Text("PIXEL MAZE QUEST", size=26, weight="bold", color=Theme.POINT)
    status_text = ft.Text("미로 모드를 선택하고 탐색을 시작하세요", size=13, color=ft.Colors.WHITE54)

    steps_val      = ft.Text("0", size=20, weight="bold", color=Theme.POINT)
    backtracks_val = ft.Text("0", size=20, weight="bold", color="#FF4444")
    deadends_val   = ft.Text("0", size=20, weight="bold", color="#FF8844")

    def stat_card(label, ref_text):
        return ft.Container(
            width=130, height=60, bgcolor=Theme.SECONDARY, border_radius=8,
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            content=ft.Column(spacing=2, controls=[
                ft.Text(label, size=10, color=ft.Colors.WHITE38), ref_text,
            ]),
        )

    stats_row = ft.Row(
        spacing=8, alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            stat_card("탐색 스텝", steps_val),
            stat_card("백트래킹",  backtracks_val),
            stat_card("막다른 길", deadends_val),
        ],
    )

    def reset_stats():
        state["steps"] = state["backtracks"] = state["dead_ends"] = 0
        steps_val.value = backtracks_val.value = deadends_val.value = "0"

    def update_stats():
        steps_val.value      = str(state["steps"])
        backtracks_val.value = str(state["backtracks"])
        deadends_val.value   = str(state["dead_ends"])

    speed_label = ft.Text("속도", size=11, color=ft.Colors.WHITE54)
    speed_value = ft.Text("보통", size=11, color=Theme.POINT)

    def on_speed_change(e):
        v = float(e.control.value)
        if   v <= 1: state["speed"] = 0.20; speed_value.value = "느림"
        elif v <= 2: state["speed"] = 0.08; speed_value.value = "보통"
        elif v <= 3: state["speed"] = 0.03; speed_value.value = "빠름"
        else:        state["speed"] = 0.005; speed_value.value = "최고속"
        page.update()

    speed_slider = ft.Slider(
        min=1, max=4, divisions=3, value=2,
        active_color=Theme.POINT, inactive_color=Theme.SECONDARY,
        on_change=on_speed_change, width=160,
    )
    speed_row = ft.Row(
        spacing=8, alignment=ft.MainAxisAlignment.CENTER,
        controls=[speed_label, speed_slider, speed_value],
    )

    maze_board = ft.Column(spacing=2)

    def build_grid():
        maze   = state["maze"]
        solver = state["solver"]
        cs     = CELL_SIZE[state["mode"]]
        maze_board.controls.clear()
        grid_cells.clear()
        for r in range(solver.rows):
            row_ctrl = []
            for c in range(solver.cols):
                val     = maze[r][c]
                bg      = Theme.WALL_COLOR if val == WALL else Theme.PATH
                content = None
                if val == START:
                    content = pixel_char(cs)
                elif val == END:
                    content = ft.Icon(ft.Icons.FLAG_ROUNDED, color=Theme.END_COLOR, size=cs * 0.55)
                cell = ft.Container(
                    width=cs, height=cs, bgcolor=bg,
                    border_radius=CELL_RADIUS,
                    alignment=ft.Alignment(0, 0),
                    content=content,
                )
                row_ctrl.append(cell)
            grid_cells.append(row_ctrl)
            maze_board.controls.append(
                ft.Row(row_ctrl, spacing=2, alignment=ft.MainAxisAlignment.CENTER)
            )

    def mode_btn(label, mode_key, icon):
        def on_click(e):
            if state["running"]: return
            state["mode"]   = mode_key
            state["maze"]   = get_maze(mode_key)
            state["solver"] = MazeSolver(state["maze"])
            reset_stats()
            status_text.value = f"[{label}] 모드 — 탐색 시작 버튼을 누르세요"
            status_text.color = ft.Colors.WHITE54
            build_grid()
            page.update()
        return ft.ElevatedButton(
            label, icon=icon, on_click=on_click,
            bgcolor=Theme.SECONDARY, color=ft.Colors.WHITE70,
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=6)),
        )

    mode_row = ft.Row(
        spacing=8, alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            mode_btn("랜덤",      "random", ft.Icons.SHUFFLE),
            mode_btn("픽셀 아트", "pixel",  ft.Icons.GRID_ON),
            mode_btn("간단",      "simple", ft.Icons.CROP_SQUARE),
        ],
    )

    async def start_exploration(e):
        if state["running"]: return
        state["running"] = True
        if state["maze"] is None:
            state["mode"]   = "random"
            state["maze"]   = get_maze("random")
            state["solver"] = MazeSolver(state["maze"])
        reset_stats()
        build_grid()
        status_text.value = "DFS 탐색 중..."
        status_text.color = ft.Colors.WHITE70
        page.update()

        solver     = state["solver"]
        cs         = CELL_SIZE[state["mode"]]
        visited    = set()
        path_stack = []

        async def dfs(r, c):
            if (r, c) == solver.end_pos:
                path_stack.append((r, c))
                return True
            visited.add((r, c))
            path_stack.append((r, c))
            if (r, c) != solver.start_pos:
                pr, pc = path_stack[-2]
                grid_cells[pr][pc].content = None
                grid_cells[pr][pc].bgcolor = Theme.TRAIL
                grid_cells[r][c].content   = pixel_char(cs)
                state["steps"] += 1
                update_stats()
                page.update()
                await asyncio.sleep(state["speed"])
            for dr, dc in solver.directions:
                nr, nc = r+dr, c+dc
                if solver.is_valid(nr, nc, visited):
                    if await dfs(nr, nc):
                        return True
            path_stack.pop()
            if (r, c) != solver.start_pos:
                state["backtracks"] += 1
                state["dead_ends"]  += 1
                update_stats()
                grid_cells[r][c].content = None
                grid_cells[r][c].bgcolor = Theme.DEAD_FLASH
                page.update()
                await asyncio.sleep(state["speed"] * 1.5)
                grid_cells[r][c].bgcolor = Theme.DEAD_END
                page.update()
                if path_stack:
                    br, bc = path_stack[-1]
                    grid_cells[br][bc].content = pixel_char(cs)
                    page.update()
                await asyncio.sleep(state["speed"])
            return False

        success = await dfs(*solver.start_pos)
        if success:
            status_text.value = (
                f"탈출 성공!  경로 {len(path_stack)}칸  |  "
                f"총 {state['steps']}스텝  백트래킹 {state['backtracks']}회"
            )
            status_text.color = "#00C896"
            for r, c in path_stack:
                if (r, c) == solver.start_pos or (r, c) == solver.end_pos: continue
                grid_cells[r][c].bgcolor = Theme.POINT_DIM
                grid_cells[r][c].content = ft.Container(
                    width=6, height=6, bgcolor=Theme.POINT, border_radius=3)
            page.update()
        else:
            status_text.value = "탈출구가 없습니다!"
            status_text.color = "#FF4444"
        state["running"] = False
        page.update()

    async def reset(e):
        if state["running"]: return
        state["maze"]   = get_maze(state["mode"])
        state["solver"] = MazeSolver(state["maze"])
        reset_stats()
        status_text.value = "새 미로 생성 완료 — 탐색 시작 버튼을 누르세요"
        status_text.color = ft.Colors.WHITE54
        build_grid()
        page.update()

    run_btn = ft.ElevatedButton(
        "탐색 시작  (DFS)", icon=ft.Icons.PLAY_ARROW_ROUNDED,
        on_click=start_exploration, bgcolor=Theme.POINT, color=Theme.BASE,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
    )
    reset_btn = ft.OutlinedButton(
        "새 미로", icon=ft.Icons.REFRESH_ROUNDED, on_click=reset,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=8),
            side=ft.BorderSide(1, Theme.POINT), color=Theme.POINT,
        ),
    )
    btn_row = ft.Row(
        spacing=12, alignment=ft.MainAxisAlignment.CENTER,
        controls=[run_btn, reset_btn],
    )

    state["maze"]   = get_maze("random")
    state["solver"] = MazeSolver(state["maze"])
    build_grid()

    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=14,
            controls=[
                title_text, status_text, mode_row,
                ft.Container(
                    content=maze_board, padding=14,
                    bgcolor=Theme.SECONDARY, border_radius=12,
                    border=ft.border.all(1, "#2E2E3E"),
                ),
                stats_row, speed_row, btn_row,
            ],
        )
    )

if __name__ == "__main__":
    ft.app(target=main)