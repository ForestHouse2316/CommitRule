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

### Types of branches in Git-Flow
Git-Flow 방식의 이력관리에서는 다음과 같은 5가지 브랜치가 존재한다.\

#### Ⓜ️ main
`master` 로도 불리는 브랜치로 배포와 직접적으로 연결된다.
- ⚠️ __반드시 배포 가능한 상태의 커밋만이 존재하여야 한다.__\
  즉 `main` 의 각 커밋은 프로그램의 버전을 나타낸다고 볼 수 있다.

#### 🛠️ develop
`feature`에서 개발한 기능들이 통합된다.
- ⚠️ __`feature` 브랜치 merge 시 반드시 `--no-ff` 옵션을 통하여 `develop` 브랜치가 `feature` 브랜치에 대해 fast-forward 하지 않도록 한다.__
- `develop` 브랜치에 이번 버전에 필요한 `feature` 브랜치들이 모두 merge 되고 버그를 고쳤다면 `release` 브랜치로 merge 시킨다.

#### ✨ feature/_name_
기능과 관련된 개발이 이루어진다.\
일반적으로 `develop` 브랜치에서 분기되어진다.\
`feature/garbage-collection` 과 같이 기능의 이름을 적는다.
- 새로운 기능, 버그 수정이 필요할 때마다 분기한다.
- 각각의 기능별로 각각의 `feature` 브랜치를 만든다.
- ℹ️ 일반적으로 공유가 필요하지 않으므로 로컬에서 브랜치를 관리하고 팀원과의 내용 공유는 `develop` 에 완성된 기능을 merge 함으로써 할 수 있다.\
팀에 따라 `feature` 브랜치를 push 해도 무방하다. 

#### ➡️ release/_version_
`develop` 브랜치에서 배포 시점으로 삼고자 하는 커밋에서 분기하여 배포를 위한 일련의 작업을 거친다.\
최종 테스트, 버그수정, 버전 관련 문서작성(업데이트 로그 등) 과 같은 작업들이 포함된다.\
버전은 배포 버전을 적는다. (`release/1.0`)

- `release` 브랜치에 커밋되는 시점부터 배포 사이클이 시작된다.\
작업이 끝나면 `main` 브랜치에 merge 하고 배포가 이뤄진다.
- 배포 준비 과정에서 이루어진 버그수정 등의 변경사항은 배포 후 다시 `develop` 브랜치로 meger 하여 업데이트 한다.
- ⚠️ __`develop` 에서 분기 이후에는 해당 배포와 관련되지 않은 작업은 `release` 브랜치로 merge 하지 않는다.__

#### 🚨 hotfix/_version_
배포한 버전에 대하여 __긴급한__ 버그 수정이 필요한 경우에만 이용한다.\
버전은 분기된 배포 버전의 다음 버전을 적는다. (`0.1` 버전에서 문제 발생 시 `hotfix/0.2` 와 같이 작성)

- `main` 에서 분기하여 수정을 요하는 부분만 수정 후 다시 merge 시킨다.\
이후 바로 `develop` 브랜치에도 merge 시킨다.
- ℹ️ 긴급하지 않은 버그 수정은 다음 버전에서 처리할 수 있도록 한다.

### Cleaning branches
항시 유지되는 브랜치인 `main` 과 `develop` 을 제외한 나머지 브랜치는 merge 이후 필요가 없으므로 삭제하게 된다.\
단 혹시 모를 상황에 대비하여 merge 후 다음 버전, 또는 팀이 정한 기간 이후에 삭제하는 것을 권장한다.

## Workflow
[git 사이트](https://git-scm.com/book/ko/v2/%EB%B6%84%EC%82%B0-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C%EC%9D%98-Git-%EB%B6%84%EC%82%B0-%ED%99%98%EA%B2%BD%EC%97%90%EC%84%9C%EC%9D%98-%EC%9B%8C%ED%81%AC%ED%94%8C%EB%A1%9C)에서 소개하는 3가지 방식의 workflow 가 있다.

### Centralized Workflow
![](https://git-scm.com/book/en/v2/images/centralized_workflow.png)\
하나의 repository 를 각 개발자가 clone 하여 사용, 작업은 브랜치를 기준으로 분리하여 사용한다.

### Integration-Manager Workflow
![](https://git-scm.com/book/en/v2/images/integration-manager.png)\
프로젝트 규모가 커지는 경우, 각 개발자의 작업이 다른 개발자와 겹치지 아니할 때 사용 가능한 방법.\
상위 repository 를 각각의 개발자가 fork 하여 private repository 를 만들고,\
이를 clone 하여 local repository 를 만든다.\
기본적으로 Centralized Workflow 와 동일한 브랜치 구조를 가져가며, 개인별 

### Dictator and Lieutenants Workflow
![](https://git-scm.com/book/en/v2/images/benevolent-dictator.png)\
GitHub-flow 기반의 공개 repository 와 오픈소스 프로젝트에서 유용한 방식.\
초대형 프로젝트에서 사용할 수 있다.

## Commit

### Commit interval

### Commit message
기본적인 양식은 다음과 같다 : `TAG: message` 또는 `[TAG] message` 또는 `✨ message`\
팀에 맞는 사용법을 골라 사용하도록 한다.

- TAG는 해당 커밋의 타입으로, 변경사항이 무엇과 관련된 것인지 나타낸다.
- message는 해당 커밋의 내용으로, 일종의 title 에 해당한다.
- message 에는 변경사항들에 대한 요약을, 세부적인 사항은 content 에 적는다 (content는 필요 시 선택적으로 작성한다).\

> ℹ️ JetBrains 계열 IDE 의 경우, 엔터가 연속하여 2번 입력된 지점의 커밋 메시지부터 content 로 인식합니다 :
> ```
> [TAG] Message of the commit.
> This line is still in the message section.
>
> Here's the content section of our commit.
> ```

#### TAG (emoji)
TAG 위치에는 다음과 같은 태그들이 들어갈 수 있다.

|   TAG    | emoji | Use when                                  |
|:--------:|:-----:|-------------------------------------------|
|   Feat   |   ✨   | 새로운 기능의 추가                                |
|   Fix    |  🐛   | 버그 수정                                     |
|  Patch   |  🩹   | 사소한 버그, 밸런스, 계산식, 상수값 수정                  |
| Refactor |  ♻️   | 유지보수를 위한 코드 리팩터링 (_최적화는 Opt 이용_)          |
|   Opt    |   ⚡   | 로직 및 성능 최적화 (_단순 유지보수는 Refactor 이용_)      |
|  Style   |  🎨   | 로직상 변경이 없는 코드 format, structure, 변수명 변경   |
|   Test   |  🧪   | Test 와 관련된 모든 작업                          |
|   Docs   |  📝   | Readme, 코드 내 doc 관련 작업 (리소스 제외)           |
|   Res    |  📦   | 의존성 있는 모든 리소스 파일 및 빌드 (이미지, JSON, .exe 등) |
|    CI    |  🔃️  | CI 관련 작업                                  |
|  Merge   |  🔀️  | Merge 관련 작업                               |
|  Revert  |   ⏪   | 변경사항 Revert                               |
|  Cherry  |  🍒️  | Cherry-pick 수행                            |
|   Git    | ️🐈‍⬛ | 기타 Git 관련 작업                              |                            
|  Rename  |  ✏️   | 파일, 폴더명 변경                                |
|  Clean   |  🧹   | Redundant 한 코드, 주석, 파일 등의 제거              |
|  Chore   |   ➿   | 기타 중요도가 ___낮은___ 작업 및 변경사항 (typo, )       |
> ℹ️ TAG 와 대응되는 emoji 는 [carloscuesta의 gitmoji 가이드라인](https://gitmoji.dev/)에서 간소화하여 만들어졌습니다.

> ⚠️ 본 repository 의 내용은 git hook 을 사용하여 상기한 emoji를 사용하는 방식을 기준으로 적혀있습니다.\
> carloscuesta 의 gitmoji 방식은 하단의 Additional methods 에 추가되어있습니다.

본 repository 에 있는 커스텀 prepare-commit-msg hook 을 이용하는 경우, :tag_name: 형태로 message 작성 시 자동으로 변환된다.\
TAG와 달리 tag_name 은 소문자로 시작한다 :
```c++
// example 1
//// Commit Message
:refactor: Refactor dialogue system

//// Ouput (on git log)
♻️ Refactor dialogue system

// example 2
//// Commit Message
:opt::patch: :Fix: [fix]

//// Ouput (on git log)
⚡🩹 :Fix: [fix]
```



<details>
  <summary>Additional methods</summary>

#### Double tagging _(not recommended)_
팀에 따라 선택적으로 사용가능한 `[TAG1][TAG2] Message` 형식으로 사용할 수 있으며 다음과 같이 이용할 수 있다 :\
- TAG1 을 상위 분류, TAG2 를 하위 분류로서 사용한다.
- TAG1 과 TAG2 에 해당하는 변경사항이 해당 commit 안에 모두 들어있음을 의미 (이 경우 `[TAG1][TAGn] Message` 도 가능하나, __권장하지 아니함__)
  가독성 측면에서 좋지 못하므로 이중태그 방식을 사용할 경우 상위-하위 태그를 사용하는 방법으로만 이용하는 것을 권장한다.

#### Gitmoji by carloscuesta
♻️, ⚡ 등의 아이콘들을 이용하여 커밋 유형을 나타내며 github 상에서 이모티콘의 작성이 `:emoji_name:` 형태로 가능한 점을 이용한다. (Discord 와 동일한 방식)\
서식은 앞서 소개한 git hook 버전의 gitmoji 양식과 같이 TAG 위치에 이모지를 대신 넣는 것으로, `♻️ Refactor dialogue system's control method` 와 같이 사용할 수 있다.\
[carloscuesta의 gitmoji 가이드라인](https://gitmoji.dev/)이 존재하고, 이를 자신의 팀에 맞게 간소화하는 것을 권장한다.\
\
로컬상에서는 이모티콘이 아닌 일반 텍스트 형태(e.g. `:zap:`)로 보이므로 로컬에서 사용 시 오히려 가독성이 떨어지는 문제가 있다.\
따라서 로컬에서는 **본 repository의 gitmoji 버전을 이용**하거나 아래의 예시와 같이 사용하는 것을 권장한다 :
1. TAG + emoji 작성 예시 :
- 작성 : `[Refactor] :recycle: Refactor dialogue system's control method`
- 로컬 내 표시 : `[Refactor] :recycle: Refactor dialogue system's control method`
- GitHub 내 표시 : `[Refactor] ♻️ Refactor dialogue system's control method`

2. emoji 작성 예시 :
- 작성 : `♻️ Refactor dialogue system's control method`
- 로컬 내 표시 : `♻️ Refactor dialogue system's control method`
- GitHub 내 표시 : `♻️ Refactor dialogue system's control method`

> ℹ️ JetBrains 사의 IDE 에서 사용가능한 [gitmoji plugin](https://plugins.jetbrains.com/plugin/12383-gitmoji-plus-commit-button) 의 옵션을 통해\
[carloscuesta의 gitmoji 가이드라인](https://gitmoji.dev/) 상의 원하는 이모지를 `:emoji_name:` 또는 `😎` 형태로 바로 삽입할 수 있다.
</details>


#### message
- 커밋메시지는 50자 이내로 작성할 것을 권장한다.
- 별도의 세부 내용은 content 에 따로 적도록 한다.
- 첫 글자는 대문자로 시작한다. 메시지의 시작은 동사 원형을 사용한다.\
  동사 make 를 사용하고자 하는 경우, `[TAG] Make...` 가 올바른 표기법이다.\
  `make`, `Making`, `Makes`, `Made` 모두 잘못된 표기법이다.

#### content
- 커밋의 변경사항에 대해 추가적으로 기술해야하는 내용이 있는 경우에 사용한다.
- 커밋의 content는 해당 커밋을 선택하기 전까지는 표시되지 않으며, 커밋 세부사항 조회 시 파일 변경사항과 함께 내용이 나타난다 (GitHub/로컬 모두 해당)
- 그러므로 중요한 내용은 message 단에서 보여줄 수 있도록 한다.




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
### Development
[✍️Commit message rule reference](https://junhyunny.github.io/information/github/git-commit-message-rule/)\
[⭕Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)\
[♾️SW release lifecycle](https://ko.wikipedia.org/wiki/%EC%86%8C%ED%94%84%ED%8A%B8%EC%9B%A8%EC%96%B4_%EB%B0%B0%ED%8F%AC_%EC%83%9D%EB%AA%85_%EC%A3%BC%EA%B8%B0)\
[😎Gitmoji by carloscuesta](https://github.com/carloscuesta/gitmoji)\
[🌳Kinds of branches](https://gmlwjd9405.github.io/2018/05/11/types-of-git-branch.html)

### GitHub MarkDown
[📜GitHub MD Syntax](https://docs.github.com/ko/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)\
[⏹️GitHub shield badge site](https://shields.io/)\

### Utils
[🛟GitHub server status](https://www.githubstatus.com/)\
