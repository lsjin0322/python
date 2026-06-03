# 📦 자료구조 직접 구현

> 리스트, 스택, 집합 ADT를 Python으로 직접 구현한 자료구조 프로젝트

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![DataStructure](https://img.shields.io/badge/DataStructure-ADT-7C3AED?style=flat-square)

---

## 📌 프로젝트 소개

Python 내장 자료구조(`list`, `set` 등)를 사용하지 않고, 각 자료구조의 동작 원리를 **배열 기반으로 직접 구현**한 프로젝트입니다.

각 파일은 독립적으로 실행 가능하며, 하단에 동작 테스트 코드가 포함되어 있습니다.

---

## 🗂️ 파일 구조

```
자료구조/
├── list.py    # 배열 기반 리스트 (ArrayList) 구현
├── stack.py   # 배열 기반 스택 (ArrayStack) 구현
└── set.py     # 배열 기반 집합 (ArraySet) 구현
```

---

## 📋 구현 내용

### 1. ArrayList (`list.py`)

배열을 이용한 순서 있는 리스트 자료구조

| 메서드 | 설명 |
|--------|------|
| `insert(pos, e)` | 지정 위치에 요소 삽입 |
| `delete(pos)` | 지정 위치 요소 삭제 |
| `Append(e)` | 맨 끝에 요소 추가 |
| `getEntry(pos)` | 지정 위치 요소 반환 |
| `Replace(pos, e)` | 지정 위치 요소 교체 |
| `Find(item)` | 요소 위치 탐색 |
| `Sort()` | 오름차순 정렬 (버블 정렬) |
| `isEmpty()` / `isFull()` | 공백 / 포화 상태 확인 |
| `Size()` / `Clear()` | 크기 반환 / 초기화 |

---

### 2. ArrayStack (`stack.py`)

배열을 이용한 LIFO(후입선출) 스택 자료구조  
**괄호 검사 알고리즘** 응용 포함

| 메서드 | 설명 |
|--------|------|
| `push(e)` | 스택 맨 위에 요소 추가 |
| `pop()` | 맨 위 요소 꺼내서 반환 |
| `peek()` | 맨 위 요소 확인 (삭제 없음) |
| `isEmpty()` / `isFull()` | 공백 / 포화 상태 확인 |
| `size()` / `clear()` | 크기 반환 / 초기화 |

**응용 — 괄호 검사**

```python
check_brackets("{ A [ B + C ] }")  # True  ✓
check_brackets("{ ( a + b }")       # False ✗
```

---

### 3. ArraySet (`set.py`)

배열을 이용한 중복 없는 집합 자료구조

| 메서드 | 설명 |
|--------|------|
| `insert(e)` | 원소 삽입 (중복 불가) |
| `delete(e)` | 원소 삭제 |
| `contains(e)` | 원소 포함 여부 확인 |
| `union(setB)` | 합집합 (A ∪ B) |
| `intersect(setB)` | 교집합 (A ∩ B) |
| `difference(setB)` | 차집합 (A - B) |
| `equals(setB)` | 동등 비교 |
| `isEmpty()` / `isFull()` | 공백 / 포화 상태 확인 |

---

## 🚀 실행 방법

각 파일을 독립적으로 실행하면 하단 테스트 코드가 동작합니다.

```bash
python list.py
python stack.py
python set.py
```

---

## 💡 구현 포인트

- Python 내장 메서드 사용 최소화 — 알고리즘 직접 구현
- 각 파일 상단 주석에 내장 방식과 직접 구현 방식 비교 병기
- `__main__` 가드로 독립 실행 / 모듈 임포트 구분

---

## 📚 사용 기술

- **Python 3.10+**
- 배열 기반 ADT (Abstract Data Type) 설계
- 버블 정렬, 선형 탐색 직접 구현

---

## 🔗 관련 프로젝트

> 함께 진행한 다른 프로젝트들입니다.

- [Pixel Maze Quest](../MazeQuest_DFS) — DFS 알고리즘 시각화
- [버킷리스트 앱](../bucket_app) — FastAPI + Flet CRUD 앱
- [수식 계산기](../calculator_app) — 스택 기반 후위표기식 계산기
