# TDD 사이클 메모

## RED — 실패하는 테스트 작성
- `tests/test_calculator.py`에 `test_add_positive_numbers`, `test_subtract_positive_numbers` 작성
- `app/calculator.py`는 `NotImplementedError` 상태 유지
- `pytest` 실행 → 2개 FAILED 확인
- 커밋: `test: add failing tests for calculator (RED)`

## GREEN — 테스트 통과하는 최소 구현
- `app/calculator.py`에 `add()`, `subtract()` 구현
- `pytest` 실행 → 2개 PASSED 확인
- 커밋: `feat: implement add and subtract functions (GREEN)`

## REFACTOR — 코드 정리 (필요 시)
- 현재 구현이 단순하여 리팩토링 불필요
- 테스트는 그대로 통과 유지 확인