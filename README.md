# NAAS: Not Another AI System
### Empathic State Machine for Gentle Consultation

## 概要
NAASは、作業改善やアイデア創出に関する相談を、より簡単でストレスの少ないものにするために設計されたシステムです。
ユーザーがためらったり迷ったりすると優しく反応し、必要に応じて再試行やスキップを提案します。
相談内容は段階的に整理され、完全に記録されるため、後でレビューや分析が可能です。
たとえ答えが曖昧であっても共感を受け、システムは次に何を尋ねるべきかを調整します。

**English Summary:**  
NAAS is designed to make consultations for workflow improvement or idea generation easier and less stressful.  
It responds gently when users hesitate or are unsure, offering retries or the option to skip questions.  
Consultation content is structured step by step and fully recorded for later review and analysis.  
Even ambiguous answers are treated with empathy, and the system adjusts what to ask next.

## 特徴 / Features
- 段階的な質問
- スキップオプション付きの穏やかなリトライ
- 回答は整理され、レビューのために記録されます
- 答えが曖昧であっても共感的な反応を示す

- Step-by-step questioning
- Gentle retries with the option to skip
- Answers are organized and recorded for review
- Empathetic responses even to ambiguous answers

## ユースケース / Use Cases
- 病院での待機時間改善
- チーム課題の整理と分析
- 新しいプロジェクトのアイデア開発
曖昧な考えでも徐々に明確化でき、心理的に安全な環境で相談可能です。

- Reducing waiting times in hospitals
- Organizing and analyzing team challenges
- Developing ideas for new projects
Even vague ideas can gradually become clearer, allowing consultations in a psychologically safe environment.

## 使い方 / Usage
1. リポジトリをクローンするか、コードをダウンロード
2. 質問やプロンプトをまとめたフロー構成辞書を用意
3. `EmpathicStateMachine` クラスでフローを実行
4. プロンプトに従い、ステップごとに答える
5. 回答は後日分析のために `naas_memory.json` に保存

1. Clone the repository or download the code
2. Prepare a flow configuration dictionary with questions and prompts
3. Run the flow using the `EmpathicStateMachine` class
4. Respond step by step according to the prompts
5. Responses are saved in `naas_memory.json` for later analysis

## 設置 / Setup
- Python 3.7+
- 標準ライブラリ以外に外部依存関係は不要

- Python 3.7+
- No external dependencies beyond the standard library

## コメント欄例 / Example Comment
※コードはGitHubで公開しています。興味のある方はぜひご覧ください。  
*The code is available on GitHub. Feel free to check it out if you are interested.*
