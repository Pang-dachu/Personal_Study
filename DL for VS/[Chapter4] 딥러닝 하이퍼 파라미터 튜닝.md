# Chapter4. 딥러닝 프로젝트 시동 걸기와 하이퍼파라미터 튜닝

## intro
<details>
<summary>Intro</summary>

* 딥러닝 개발은 경험에 의존하는 바가 크다. 

* 고려할 것들에 대한 내용은 아래와 같다.
    - 신경망 구조는 무엇으로
    - 은닉층의 갯수 설정
    - 층의 유닛과 필터의 수
    - 학습률의 설정
    - 활성화 함수 종류
    - 데이터 수집 vs 하이퍼 파라미터 튜닝

</details>

## 4.1 성능 지표 
<details>

* 모델의 평가지표에는 정확도, 재현율, 정밀도, F1-Score등이 존재한다. 
어떤 평가지표가 정답이 아닌 상황에 따라 평가지표를 취사 선택해야 한다.

* Confusion Matrix의 사용 

* F1-Score는 정밀도와 재현율의 조화평균, 서로 Trade-off의 관계 

</details>

## 4.2 BaseLine Model 선택 
<details>

* 베이스 라인 선택시 고려해야할 부분은 다음과 같다.
    - 신경망 유형 선택 (MLP, CNN, RNN ... )
    - 혹시 Object Detection 인가 ?
    - 신경망의 층수, 활성화 함수, 최적화 알고리즘의 선택
    - 드롭아웃, 배치정규화, L2 규제 유형의 모델 규제 선택 

* 전이학습 모델이 무엇을 학습했는지를 알고 있다면 내가 직면한 문제와 유사한 전이학습 모델의 사용을 고려해봄직 하다.

* AlexNet (구조 알아둘 것)
    - 5개의 합성곱층 + 2개의 전결합층 
    - 층의 깊이(필터 수) : 합성곱층 96, 256, 384, 385, 256
    - 필터 크기 : 11, 5, 3, 3
    - 은닉층 : Relu
    - 합성곱 층에서는 MaxPool 적용
    - 전결합층(출력층 이전)의 뉴런은 4096
    - 출력층 뉴런 갯수 1000개, softmax 사용 

* AlexNet, ResNet, Inception의 구조는 익혀둘것 (특히, skip connection)

</details>

## 4.3 학습 데이터 준비 
<details>

* train, valid, test 데이터의 분할에 대한 내용

* 하나의 epoch 마다 loss, acc가 출력 

</details>