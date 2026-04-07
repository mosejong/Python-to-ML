---
## Git 브랜치 병합 단계별 정리 (team1, team2 → master)
1. master에서 e.py 생성
   - master 브랜치에서 e.py 파일을 만들고 커밋.
      ```bash
      git add e.py
      git commit -m "master에서 e.py 생성"
      ```

2. team1 브랜치에서 e.py 수정
    - team1 브랜치로 이동 후 e.py 수정.
    - 수정만하고 gi checkout master 혹은 team2로 이동하려하면 오류발생 함
      <div style="border:2px solid #1A237E; border-radius:12px; padding:14px; background-color:#E8EAF6;">
      "message " : error: Your local changes to the following files would be overwritten by checkout </div>

       ```bash
        Samsung@OK-NoteBook MINGW64 /c/kok/git_exam (team1)
        $ vi e.py
        Samsung@OK-NoteBook MINGW64 /c/kok/git_exam (team1)
        $ git checkout master
        error: Your local changes to the following files would be overwritten by checkout:
                git_exam/e.py
        Please commit your changes or stash them before you switch branches.
        Aborting
        ```
    - 해결 : 수정한 내용을 반드시 커밋 하거나 `git stash`로 임시 저장후 브랜치 이동
       ```bash
        git add e.py
        git commit -m "team1에서 e.py 수정"
        ```

3. team2 브랜치에서 e.py 수정
      ```bash
      git checkout team2
      vi e.py   # 다른 코드 추가/수정
      git add e.py
      git commit -m "team2에서 e.py 수정"
      ```

4. master에서 team1 병합
   ```bash
   git checkout master
   git merge team1
   ```
   **오류발생** : `e.py` 충돌 발생 → Git이 충돌 마커 삽입
   **해결** : 
   1. e.py 열어 충돌 마커(<<<<<<< HEAD, =======, >>>>>>> team1) 제거

   2. 원하는 최종 코드 작성

   3. 완료 표시:
   ```bash
   git add e.py
   git commit -m "merge team1 into master"
   ```
5. master에서 team2 병합
   ```bash
   git merge team2
   ```
   ***오류발생*** : 다시 `e.py` 충돌발생
   ***해결*** : 
   1. `e.py` 열어 충돌 마커 제거
   2. 최종 코드 작성
   3. 완료 표시:
   ```bash
   git add e.py
   git commit -m "merge team2 into master"
   ```

## 전체 요약
- 오류 1: team1에서 수정 후 커밋하지 않고 브랜치 이동 → checkout 오류
→ 해결: 커밋하거나 stash 후 이동

- 오류 2: master에서 team1 병합 시 충돌 발생
→ 해결: 충돌 마커 제거 후 git add → git commit

- 오류 3: master에서 team2 병합 시 충돌 발생
→ 해결: 동일하게 충돌 수정 후 전체 커밋

👉 핵심은 각 브랜치에서 작업할 때는 반드시 전체 커밋을 하고,
master에서 병합할 때 충돌이 생기면 
: 충돌 마커를 직접 수정 (vi) → git add → git commit으로 병합을 완료해야 한다는 점임.

