# solver.py
import random
from models import WALL, EMPTY, START, END, SIMPLE_MAZE, PIXEL_MAZE

class MazeSolver:
    """DFS 탐색 엔진 + 랜덤 미로 생성기"""

    def __init__(self, maze_map):
        self.maze      = [row[:] for row in maze_map]
        self.rows      = len(maze_map)
        self.cols      = len(maze_map[0])
        self.start_pos = self._find_pos(START)
        self.end_pos   = self._find_pos(END)
        # 탐색 우선순위: 우 → 하 → 좌 → 상
        self.directions = [(0,1),(1,0),(0,-1),(-1,0)]

    def _find_pos(self, target):
        for r in range(self.rows):
            for c in range(self.cols):
                if self.maze[r][c] == target:
                    return (r, c)
        return (0, 0)

    def is_valid(self, r, c, visited):
        return (
            0 <= r < self.rows and
            0 <= c < self.cols and
            self.maze[r][c] != WALL and
            (r, c) not in visited
        )


class RandomMazeGenerator:
    """재귀적 백트래킹 알고리즘으로 랜덤 미로 생성"""

    def __init__(self, rows=15, cols=19):
        # 홀수 크기 보장 (벽/길 격자 구조)
        self.rows = rows if rows % 2 == 1 else rows + 1
        self.cols = cols if cols % 2 == 1 else cols + 1

    def generate(self):
        # 전부 벽으로 초기화
        maze = [[WALL] * self.cols for _ in range(self.rows)]

        # 재귀 백트래킹으로 길 뚫기
        def carve(r, c):
            dirs = [(0,2),(2,0),(0,-2),(-2,0)]
            random.shuffle(dirs)
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 1 <= nr < self.rows-1 and 1 <= nc < self.cols-1 and maze[nr][nc] == WALL:
                    maze[r+dr//2][c+dc//2] = EMPTY
                    maze[nr][nc] = EMPTY
                    carve(nr, nc)

        # (1,1) 시작점에서 길 뚫기
        maze[1][1] = EMPTY
        carve(1, 1)

        # 막다른 길 추가 (일부 벽 제거해 복잡도 증가)
        self._add_dead_ends(maze)

        # START / END 배치
        maze[1][1] = START
        maze[self.rows-2][self.cols-2] = END

        return maze

    def _add_dead_ends(self, maze):
        """내부 벽 일부를 무작위로 제거해 막다른 곁길 생성"""
        extra = (self.rows * self.cols) // 20
        for _ in range(extra):
            r = random.randrange(1, self.rows-1)
            c = random.randrange(1, self.cols-1)
            if maze[r][c] == WALL:
                # 상하좌우 중 빈 칸이 2개 이상이면 제거 (순환 방지 완화)
                neighbors = 0
                for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols and maze[nr][nc] != WALL:
                        neighbors += 1
                if neighbors >= 2:
                    maze[r][c] = EMPTY


def get_maze(mode="random"):
    """모드에 따라 미로 반환: 'random' / 'pixel' / 'simple'"""
    if mode == "random":
        gen = RandomMazeGenerator(rows=15, cols=19)
        return gen.generate()
    elif mode == "pixel":
        return [row[:] for row in PIXEL_MAZE]
    else:
        return [row[:] for row in SIMPLE_MAZE]