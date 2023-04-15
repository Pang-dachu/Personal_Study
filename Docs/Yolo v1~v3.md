YOLO v1~v3 특징 정리

# YOLO v1

1. Anchor Box를 사용하지않고, Cell 단위로 Bounding Box Regressor 과정을 통해 Box를 찾으므로 Localization Error로 인해 성능이 낮다.

- 자전거(3X4)와 강아지(1X2)가 있다고 했을 때 하나의 Box(1X1)를 가지고 늘렸다 줄였다 하면서 조정해 주는 일이 쉬운 일은 아니다. 

2. 각 Grid Cell에 대해 2개의 Bounding Box를 찾지만, Classification은 한 개에 대해서만 수행한다. 따라서 겹치는 Object는 Detection하기 어렵다.

3. 작은 물체에 대해서는 성능이 좋지 않음

- layer의 size가 7by7로 매우 작아서 큰 물체는 잘 찾지만, 작은 물체에 대해서는 잘 못 찾는다는 단점
(단점만 있나? ㄴㄴ Detection 속도가 아주 빠르다고 함)

- YOLO v1 입력 특징

- YOLO v1에서는 이미지 사이즈를 224by224로 pre-train Classifier 모델을 그대로 사용하고, 실제 입력을 받을 때는 448by448 사이즈의 고해상도 이미지를 사용 (YOLO v2 에서 문제 지적 및 개선 방안 제시)


# YOLO v2

1. 속도 개선 

- BackBone으로 Darknet 19 모델을 사용하여 속도를 빠르게 유지

2. 성능 개선 

- 모든 Conv Layer 뒤에 Batch Normalization 적용

어떤 장점 ? : Vanishing Gradient 문제를 해결, Learning Rate를 키울 수 있기 때문에 더 빨리 수렴할 수 있도록 해주고, Regularization 역할을 하기때문에 Dropout 등의 기법을 사용하지 않아도 된다는 장점

[BatchNormalization에 대한 설명](https://m.youtube.com/watch?v=m61OSJfxL0U&t=440s)

* HIGH Resolution Classifier

- YOLO v2는 Classfier를 똑같이 처음에는 224by224로 학습하고, 마지막 10 epoch정도는 448by448의 고해상도 이미지로 fine tuning 과정

- 단, 최종적으로 입력하는 이미지 사이즈는 416by416이다.

이는 최종 output feature map의 크기가 홀수가 되도록 하기 위함인데, 물체의 크기가 큰 경우 보통 가운데에 물체가 존재하기 때문에 feature map 내에 중심 cell이 존재할 수 있도록 하기 위함이다. 

그래서 ? 
416by416 이미지 입력 ->  13by13의 feature map 출력

* Convolutional with Anchor Boxes

- Grid Cell에 대해 5개의 Anchor Box를 예측한다.

Box는 2개를 예측하고, Classification은 한 번만 수행했던 v1과 달리, 모든 Anchor Box에 대해 Classification을 수행

- output tensor는 13X13X{(5+C)X5}가 된다. (C는 Class 개수를 의미)

- mAP는 69.5에서 69.2로 감소 
- 대신 recall은 81에서 88로 상승

- OD 문제에서 recall이 높다는것은 모델이 실제 객체의 위치를 예측한 비율이 높다는 것을 의미

* v1과 v2의 Recall 차이 이유

v1에서 recall값이 낮은 이유는 이미지 당 상대적으로 적은 수의 bounding box를 예측하기 때문이다.

v2에서는 anchor box를 통해 더 많은 수의 bounding box를 예측하면서 실제 객체의 위치를 더 잘 예측하고, 이로인해 recall 값이 상승

* Dimension Cluster 

- Anchor Box의 개수와 크기는 고정이 아니라, 해결하고자 하는 데이터셋에 따라 GT를 가장 잘 대변할 수 있는 optimal anchor box를 탐색하여 결정
( 여기서 말하는  GT는 무엇인가? )

- GT들의 width와 height로 K-means Clustering을 수행 후 적절한 K개를 찾는다.  

- YOLO v2에서는 K를 5로 정했으며 K값이 Anchor Box의 개수가 됨.

- 각 Cluster의 center point가 Anchor Box의 사이즈가 된다.
( 이때 Cluster의 기준은 유클리디안x , IOU가 기준)
* Direct Location Prediction 

- Box에 Sigmoid함수를 적용하여 Box의 중심점이 Cell 내에 존재하도록 한다.

왜 ? Sigmoid를 적용하지 않으면 Box가 Cell을 벗어나 아무 위치에나 존재할 수 있어 학습 초기 iteration 시 모델이 불안정하기 때문.

* Fine-Grained Features

- feature map의 크기가 작을 때 큰 물체는 잘 예측하지만
작은 물체는 예측하기 어렵다는 문제가 발생.

- 해결하기 위해 Passthrogh layer를 추가

뭔데 ? High Resolution feature map은 작은 물체를 잘 예측하고, Low Resolution feature map은 큰 물체를 잘 예측한다는 특징을 활용한 layer

* Multi-Scale Training 

- YOLO v1은 마지막에 Fully Connetecd Layer를 사용했는데 
YOLO v2는 이를 CNN Layer로 변경

왜?
1.  파라미터 수를 감소시키고 속도도 빠르게 수행할 수 있도록 했으며, Input 이미지 사이즈에 변화가 가능하도록 했다.

2. 다양한 Size의 이미지에도 Robust한 Detection 성능을 내기 위함이고, 실제 10 batch 마다 random 하게 이미지 사이즈를 변경하여 학습.
( 단, 1/32로 down sampling되기 때문에 input size는 32의 배수 조건 )

* 그러나 YOLO v2 역시 작은 물체에 대해 성능이 낮았다.

# YOLO v3

1. Multilabel Classification 

- 사람 물체는 "사람"이면서 "여성"일 수 있다.
- 하나의 물체에 대해 Multi Class Label 을 가질수 있다.
- v3 부터는 이것을 진행하기 위해서 마지막 활성화 함수를 SoftMax가 아닌 모든 클래스에 대해 Sigmoid를 취하여 각 Class 별로 Binary Classification을 수행

2  Backbone으로 Darknet - 53 사용 

- 이전 v2 Darknet-19 보다 깊이가 깊어져 정확도는 상승
- 근데 속도가 떨어져부림

3. Predictions Across Scales 

- 드디어 v3 에서 작은 물체에 대한 탐지를 높이기 위해서 
Prediction Feature Map으로 3개의 Scale 을 적용함!

- 어떻게 ? 
416by416 이미지를 input으로 넣었을 때,

1. 13by13 size의 feature map에서 큰 이물을 Detection하고,
2. 26by26 size의 feature map에서 중간 크기의 이물을 Detection하고,
3. 52by52 size의 feature map에서 작은 이물을 Detection한다

- v2와 마찬가지로 FC layer가 없으므로 input size는 32의 배수

- Anchor Box는 각 Scale별로 3개씩 총 9개를 사용했으며, 개수와 크기는 v2와 동일하게 K-means를 통해 결정
( 하나의 Scale 당 output tensor는 {(5+C)X3} )

- version3에서 예측하는 BBox의 수가 version2에 비해 10배가 넘는다.

따라서 속도는 줄지만, 성능은 좋아질 수 있었다