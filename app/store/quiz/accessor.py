from typing import Optional

from app.base.base_accessor import BaseAccessor
from app.quiz.models import (
    Answer,
    Question,
    Theme,
)


class QuizAccessor(BaseAccessor):
    async def create_theme(self, title: str) -> Theme:
        raise NotImplemented

    async def get_theme_by_title(self, title: str) -> Optional[Theme]:
        raise NotImplemented

    async def get_theme_by_id(self, id_: int) -> Optional[Theme]:
        raise NotImplemented

    async def list_themes(self) -> list[Theme]:
        raise NotImplemented

    async def create_answers(
        self, question_id: int, answers: list[Answer]
    ) -> list[Answer]:
        raise NotImplemented

    async def create_question(
        self, title: str, theme_id: int, answers: list[Answer]
    ) -> Question:
        raise NotImplemented

    async def get_question_by_title(self, title: str) -> Optional[Question]:
        raise NotImplemented

    async def list_questions(self, theme_id: Optional[int] = None) -> list[Question]:
        raise NotImplemented
