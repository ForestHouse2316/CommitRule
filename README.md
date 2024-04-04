# CommitRule
<details><summary>⚠️Notice⚠️</summary>

> - 본 Repository 는 공동개발(협업) 시 사용되는 Git 시스템의 사용 표준을 사전에 작성한 것이며 각 개발마다 Fork 또는 Clone 하여 내용을 팀에 맞게 수정하는 것을 권장한다.\
> Clone 후 아래 라이센스를 준수하는 범위 내에서 자유롭게 public/private repository에 사본을 올릴 수 있다.
> - 본 가이드라인의 궁극적인 목적은 Git 시스템을 이용하여 효율적이고 가독성이 높은 개발 이력을 남기고 팀원 간 협업이 원활하게 진행되는 것에 있다.
> - 본 가이드라인은 영리목적에 관한 제한 없이 누구든 사용할 수 있으나 본 가이드라인을 채용하여 발생한 문제의 책임은 사용한 개인 또는 단체에 있다.
> - 본 가이드라인은 <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="CC-BY-SA" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a> 라이센스 규칙을 따른다.\
> 사적인 목적으로 이용하는 경우 cc-by 조항은 준수하지 않아도 되며, 오픈소스 프로젝트 등 공공의 목적으로 이용 시에는 본문의 링크를 기재하여야 한다.\
> 이는 repository의 공개범위인 public/private 과는 별개의 내용이다.

</details>

## Branch
### Branch naming
기본적인 양식은 다음과 같다 : `[TAG] message`
- TAG는 해당 커밋이 무엇을 변경하였는지 나타낸다.
- message는 해당 커밋의 내용으로, 일종의 title 에 해당한다.
- message 에는 변경사항들에 대한 요약을, 세부적인 사항은 content 에 적는다 (content는 필요 시 선택적으로 작성한다).\
JetBrains 계열 IDE 의 경우, 엔터가 연속하여 2번 입력된 지점의 커밋 메시지부터 content 로 인식한다 :
```
[TAG] Message of the commit.
This line is still in the message section.

Here's the content section of our commit.
```

#### TAG
[TAG]란에는 다음과 같은 태그들이 들어갈 수 있다.\
emoji 의 경우 [공식 gitmoji 가이드라인](https://gitmoji.dev/)에서 간소화한 버전을 기재한다.

| TAG      | emoji                  | Use when                                   |
|----------|------------------------|--------------------------------------------|
| Feat     | ✨`:sparkels:`          | 새로운 기능의 추가                                 |
| Fix      | 🐛`:bug:`              | 버그 수정                                      |
| Patch    | 🩹`:adhesive_bandage:` | Chore 수준의 사소한 버그 수정                        |
| Refactor | ♻️`:recycle:`          | 유지보수를 위한 코드 리팩터링 _(최적화는 Opt 이용)_           |
| Opt      | ⚡`:zap:`               | 로직 및 성능 최적화 _(단순 유지보수는 Refactor 이용)_       |
| Style    | 🎨`:art:`              | 로직상 변경이 없는 코드 format, structure 변경         |
| Test     | 🧪`:test_tube:`        | Test 와 관련된 모든 작업                           |
| Docs     | 📝`:memo:`             | Readme, 코드 내 doc 관련 작업 (리소스 제외)            |
| Res      | 📦`:package:`          | 의존성 있는 모든 리소스 파일 및 빌드 (이미지, JSON, .exe 등)  |
| CI       | 🔄️                    | CI 관련 작업                                   |
| Git      | 🔀\⏪\🍒 ️              | Git 시스템 관련 작업 (merge, revert, cherry-pick) |
| Clean    | 🧹                     | Redundant 한 코드, 주석, 파일 등의 제거               |
| Chore    | ➿`:loop:`              | 기타 중요도가 ___매우 낮은___ 작업 및 변경사항              |

#### message
- 커밋메시지는 50자 이내로 작성할 것을 권장한다.
- 별도의 
- 메시지의시작은 동사 원형을 사용한다. 첫 글자는 대문자로 시작한다.
```
Make (O)
make (X)
Making (X)
Makes (X)
Made (X)
```

#### content
- 커밋의 변경사항에 대해 추가적으로 기술해야하는 내용이 있는 경우에 사용한다.
- 커밋의 content는 해당 커밋을 선택하기 전까지는 표시되지 않으며, 커밋 세부사항 조회 시 파일 변경사항과 함께 내용이 나타난다 (GitHub/로컬 모두 해당)
- 그러므로 중요한 내용은 message 단에서 보여줄 수 있도록 한다.

<details>
  <summary>Additional methods</summary>
  
#### Double Tagging
팀에 따라 선택적으로 사용가능한 `[TAG1][TAG2] Message` 형식으로 사용할 수 있으며 다음과 같이 이용할 수 있다 :\
- TAG1 을 상위 분류, TAG2 를 하위 분류로서 사용한다.
- TAG1 과 TAG2 에 해당하는 변경사항이 해당 commit 안에 모두 들어있음을 의미 (이 경우 `[TAG1][TAGn] Message` 도 가능하나, __권장하지 아니함__)
가독성 측면에서 좋지 못하므로 이중태그 방식을 사용할 경우 상위-하위 태그를 사용하는 방법으로만 이용하는 것을 권장한다.
  
#### Gitmoji
이모티콘을 사용하여 나타내는 commit message 를 gitmoji 라 한다. [gitmoji repository](https://github.com/carloscuesta/gitmoji)\
♻️, ⚡ 등의 아이콘들을 이용하여 나타내면 되며 github 상에서 `:emoji_name:` 형태로 작성이 가능하다. (Discord 와 동일한 방식)\
일반적인 서식은 TAG 위치에 이모지를 대신 넣는 것으로, `♻️ Refactor dialogue system's control method` 와 같이 사용할 수 있다.\
gitmoji 또한 [커밋별 이모지 사용 가이드라인](https://gitmoji.dev/) 이 규정되어 있으나 이를 자신의 팀에 맞게 간소화하는 것을 권장한다.\
\
단 로컬상에서는 이모티콘이 아닌 일반 텍스트 형태(e.g. `:zap:`)로 보이므로 로컬에서 사용 시 오히려 가독성이 떨어지는 문제가 있다.\
따라서 로컬에서는 실제 이모티콘을 사용하거나 태그 네이밍과 같이 사용하여야 한다.\
로컬에서 TAG + emoji 작성 예시는 다음과 같다 :
- 작성 : `[Refactor] :recycle: Refactor dialogue system's control method`
- 로컬 내 표시 : `[Refactor] :recycle: Refactor dialogue system's control method`
- GitHub 내 표시 : `[Refactor] ♻️ Refactor dialogue system's control method`

로컬에서 emoji 작성 예시는 다음과 같다 :
- 작성 : `♻️ Refactor dialogue system's control method`
- 로컬 내 표시 : `♻️ Refactor dialogue system's control method`
- GitHub 내 표시 : `♻️ Refactor dialogue system's control method`

</details>


### Kind of branches
### Dividing branch from a feature branch
### Merge & Rebase

## Commit
### Commit interval
### Commit message

## Develop
### Develop process
#### Materialization of project
#### Making class hierarchy
#### Setting root-level class (MainClass)
#### Distribute and assign works
### Default develop range of each authors
### Way to make a communication between classes with different authors
### Modifying Interface & AbstracClass


## Debug & Fix

## Log & Analyzing logs
### Default log message shape setting
#### Recommended log message shape




## Links
[📜GitHub MD Syntax](https://docs.github.com/ko/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)\
[✍️Commit message rule reference](https://junhyunny.github.io/information/github/git-commit-message-rule/)\
[⏹️GitHub shield badge site](https://shields.io/)\
[⭕SW release lifecycle](https://ko.wikipedia.org/wiki/%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EB%B0%B0%ED%8F%AC_%EC%83%9D%EB%AA%85_%EC%A3%BC%EA%B8%B0)\
[🛟GitHub server status](https://www.githubstatus.com/)
