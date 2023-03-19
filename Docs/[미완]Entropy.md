# Entropy, Cross Entropy, KL Divergence
---

## 1. Entropy

- 본래 Entropy는 열 역학에서 사용하던 개념으로 분자의 무질서함을 측정하는 척도

- 이 개념이 인공지능 분야로 넘어오면서 불순도의 측정에 사용되었는데 이때의 Entropy는 확률 분포의 불확실성 으로 표현할 수 있다.

- 우선 확률 분포의 불확실성은 확률 분포에서 어떤 값이 나올지 확신할 수 없는 상태이다.

ex) 동전 던지기에서 앞,뒤 가 나올 확률은 각 50%로 생각하지만 실제로는 어떤 면이 나올지 확신할 수 없는 상태이기에 동전 던지기에서의 확률 분포는 불확실성을 가지고 있는 상태임.
(실생활에서의 대부분의 경우의 확률 분포는 불확실성을 가지고 있다고 생각함)

- Entropy는 0 ~ 1 사이의 값을 가지는데 정보의 무질서함 혹은 확률 분포의 불확실성이라는 지표이므로 1에 가까울수록 무질서, 불확실하며 0에 가까울수록 반대가 된다.

Entropy는 분류 문제에서 사용한다.
    - 머신러닝 : Tree 알고리즘이 Entropy를 이용한 Information Gain을 통해 분기를 생성하며 결정을 잘 내리는 방향으로 학습을 진행한다.

    - 딥러닝 : 손실함수로 Cross Entropy를 사용한다.

---
## 2. Cross Entropy






---
## 3. KL Divergence






---
Reference 

[Chat GPT](https://chat.openai.com/)
[재호아빠의 연구노트](https://dhkim9108.tistory.com/m/7)
[꾸준희](https://eehoeskrap.tistory.com/13)