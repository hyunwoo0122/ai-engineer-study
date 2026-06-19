import logging


def read_file(filepath: str) -> str | None:
    logging.info(f"파일 읽기 시작: {filepath}")

    try:
        with open(filepath, "r") as file:
            content = file.read()

        logging.info(f"파일 읽기 성공: {filepath}, 글자 수: {len(content)}")
        return content

    except FileNotFoundError:
        logging.error(f"파일을 찾을 수 없습니다: {filepath}")
        return None

    except PermissionError:
        logging.error(f"파일 접근 권한이 없습니다: {filepath}")
        return None

    except Exception as e:
        logging.error(
            f"예상하지 못한 에러 발생: {e}",
            exc_info=True,
        )
        return None