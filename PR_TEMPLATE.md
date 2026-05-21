# 샘플 1 PR 템플릿 (minimal)

## 변경 사항
- `app/greeting.py` 파일 수정
- `get_greeting(name)` 함수 구현
- 이름이 비어있으면 "Hello, Guest!", 아니면 "Hello, {name}!" 반환

## 테스트
- 로컬에서 함수 직접 호출로 확인: `get_greeting("student")` → `"Hello, student!"` ✓

## 롤백 계획
- 문제 발생 시 이전 커밋으로 git revert

## 체크리스트
- [x] 코드 동작 확인
- [x] 자체 리뷰 완료
- [x] 문서 또는 설명 보강