# Entropy, Cross Entropy, KL Divergence
---



---
## 1. Entropy

---
## 2. Cross Entropy
> Cross Entropy는 머신러닝 및 딥러닝에서 매우 중요한 개념 중 하나로, 분류 문제에서 예측한 결과와 실제 결과 간의 차이를 측정하는데 사용됩니다.

Cross Entropy는 주로 분류 문제에서 두 확률 분포 간의 차이를 측정하는데 사용됩니다. 이 때 하나의 분포는 실제 분포(ground truth distribution)이고, 다른 하나는 예측 분포(predicted distribution)입니다. Cross Entropy는 두 분포 간의 차이를 측정하며, 이 값이 작을수록 예측 결과가 실제 결과에 가깝다고 판단할 수 있습니다.

분류 모델에서 Cross Entropy는 모델이 예측한 확률 분포와 실제 분포 간의 차이를 측정하여 모델을 학습시킬 때 사용됩니다. 모델이 잘못된 분류를 할 경우 Cross Entropy는 높아지고, 올바른 분류를 할 경우 Cross Entropy는 낮아집니다. 따라서 Cross Entropy를 최소화하는 방향으로 모델을 학습시키면, 더 정확한 분류 모델을 얻을 수 있습니다.

또한, Cross Entropy는 분류 문제 뿐만 아니라 다른 머신러닝 및 딥러닝 문제에서도 다양하게 활용됩니다. 예를 들어, 회귀 문제에서는 Cross Entropy 대신 Mean Squared Error(MSE) 등의 손실 함수를 사용합니다.

---
## 3. KL Divergence
