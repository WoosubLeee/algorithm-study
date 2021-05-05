# SSAFY 5th SEOUL3 APS_HUB

> The only tool that everlast

SW 업계에서 일한다면 언어, 프레임워크, OS, 분야 등 모든게 바뀌어도 git 과 git remote는 사용합니다.



## 1. Intro

**해당 `README.md`와 `.gitignore` 등 공동 문서는 절대 수정하지 않습니다.** :x:

- 조별 폴더 및 파일만 수정합니다.

  


## 2. 사용 방법 (**반드시 지킬것!**)

> 반드시 **현재 브랜치**를 확인하는 습관이 매우 중요합니다. (내가 어디에 있는지를 아는 것)
>
> 아래 내용이 매우 복잡해 보일 수 있지만, 여기까지가 협업에서의 **최소 능력 조건**입니다.



### 2.1. 로컬에서 작업하기

1. https://lab.ssafy.com/tony/computational_thinking 로 이동하여 해당 repo clone합니다.

   ```bash
   $ git clone https://lab.ssafy.com/tony/computational_thinking.git
   ```
   
2. `$ git switch -c <브랜치이름>` 으로 새로운 브랜치 생성 후 이동합니다.(매번 `생성=>삭제`를 반복)

   - `master` 에서 `group*` 로 변경된 내용을 확인합니다.
   - 다음은 `1조` 의 예시입니다. (ex. 2조의 경우 : `group2`)

   ```bash
   tony@tony MINGW64 ~/Desktop/SSAFY/computational_thinking (master)
   $ git switch -c group1
   Switched to a new branch 'group1'
   
   tony@tony MINGW64 ~/Desktop/SSAFY/computational_thinking (group1)
   ```

3. 아래와 같이 폴더 구조를 확인합니다.

   - 폴더 및 파일은 미리 구성되어 있습니다.
   - 작업은 해당 조별 폴더에서만 진행합니다. (:x:다른 조의 파일 및 폴더 수정 금지 :x:)

   ```
   1조/
   	이미지파일폴더/
   	1_논리와 증명.md
   	2_수와 표현.md
   	...
   	7_시간복잡도.md
   2조/
   	이미지파일폴더/
   	1_논리와 증명.md
   	2_수와 표현.md
   	...
   	7_시간복잡도.md
   ...
   ```

4. 매 문제 풀이 완료 이후 add, commit을 진행합니다.

   ```bash
   tony@tony MINGW64 ~/Desktop/SSAFY/computational_thinking (group1)
   $ git add .
   tony@tony MINGW64 ~/Desktop/SSAFY/computational_thinking (group1)
   $ git commit -m "1. 논리와 증명 완료" 
   ```

5. 하루의 마무리에 `$ git push origin <브랜치 이름>` 으로 push합니다.

   ```
   tony@tony MINGW64 ~/Desktop/SSAFY/computational_thinking (group1)
   $ git push origin group1
   ```



---

### 2.2 Merge Request

