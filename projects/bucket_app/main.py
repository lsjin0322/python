from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os

app = FastAPI(title="버킷리스트 API")

DATA_FILE = "bucketlist.txt"


# ── 데이터 모델 ──────────────────────────────────────────
class BucketItem(BaseModel):
    id: int
    title: str
    done: bool


class AddRequest(BaseModel):
    title: str


class UpdateRequest(BaseModel):
    id: int
    title: Optional[str] = None
    done: Optional[bool] = None


# ── 파일 I/O ─────────────────────────────────────────────
def load_items() -> List[BucketItem]:
    items = []
    if not os.path.exists(DATA_FILE):
        return items
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            if len(parts) == 2:
                title, done_str = parts
                items.append(BucketItem(id=idx, title=title, done=done_str == "True"))
    return items


def save_items(items: List[BucketItem]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for item in items:
            f.write(f"{item.title}|{item.done}\n")


def reassign_ids(items: List[BucketItem]) -> List[BucketItem]:
    for i, item in enumerate(items):
        item.id = i
    return items


# ── 라우터 ───────────────────────────────────────────────
@app.get("/bucketlist", response_model=List[BucketItem])
def get_all(search: Optional[str] = None):
    """전체 조회 / 검색"""
    items = load_items()
    if search:
        items = [i for i in items if search.lower() in i.title.lower()]
    return items


@app.post("/bucketlist", response_model=BucketItem)
def add_item(req: AddRequest):
    """항목 추가"""
    if not req.title.strip():
        raise HTTPException(status_code=400, detail="제목이 비어있습니다.")
    items = load_items()
    new_item = BucketItem(id=len(items), title=req.title.strip(), done=False)
    items.append(new_item)
    save_items(items)
    return new_item


@app.put("/bucketlist", response_model=BucketItem)
def update_item(req: UpdateRequest):
    """수정 (제목 or 완료 상태)"""
    items = load_items()
    if req.id < 0 or req.id >= len(items):
        raise HTTPException(status_code=404, detail="항목을 찾을 수 없습니다.")
    if req.title is not None:
        items[req.id].title = req.title.strip()
    if req.done is not None:
        items[req.id].done = req.done
    save_items(items)
    return items[req.id]


@app.delete("/bucketlist/{item_id}")
def delete_item(item_id: int):
    """항목 삭제"""
    items = load_items()
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="항목을 찾을 수 없습니다.")
    deleted = items.pop(item_id)
    items = reassign_ids(items)
    save_items(items)
    return {"message": f"'{deleted.title}' 삭제 완료"}


@app.get("/bucketlist/progress")
def get_progress():
    """진행률 조회"""
    items = load_items()
    total = len(items)
    done = sum(1 for i in items if i.done)
    rate = round((done / total) * 100, 1) if total > 0 else 0.0
    return {"total": total, "done": done, "rate": rate}