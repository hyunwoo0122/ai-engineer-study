from typing import Optional


def summarize_text(text: str) -> str:
    return text[:100]


def find_user(
    users: list[dict[str, str | int]],
    user_id: int,
) -> Optional[str]:
    for user in users:
        if user["id"] == user_id:
            return user["name"]

    return None
