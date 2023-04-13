# Chapter5. 고급 합성곱 신경망 구조

## intro
<details>
<summary>Intro</summary>

이번에 알아볼 내용들은 무엇일까 ?

* LeNet, 1998
    - [GradientBased Learning Applied to DocumentRecognition](http://vision.stanford.edu/cs598_spring07/papers/Lecun98.pdf)

    - [한국어 리뷰 - JJuOn's Dev](https://jjuon.tistory.com/21)

* AlexNet
* VGGNet
* Inception, 2014
* ResNet, 2015

주의 깊게 보아야 하는 것 

* 새로운 특징 : 각 구조별 이전 구조와의 차이 및 "무엇을 해결" 하려고 했는가
* 신경망 구조 : 구조, 구성 요소, 어떻게 조합하였는가
* 신경망 구현 : 어떻게 구현할 수 있는가 (사용할 수 있는가)
* 하이퍼 파라미터 설정 : 하이퍼 파라미터에 따른 개선은 얼마나 되었는가 
* 성능 : 어떤 사례에서 어떤 성능이 나왔는지

정리하자면 
* 무엇은 개선하려고 했는지, 왜 만들게 되었는지
    - 결국 기존의 어떤 문제를 해결하고 싶었기 때문

* 만든 사람은 무슨 생각을 하면서 만들었을까를 같이 생각해보자! 뇌에 불법 침입!

</details>


## 5.1 CNN의 디자인 패턴

CNN의 패턴은 무엇이었는지 다시 짚어보자.

1. 특징 추출과 분류 : 두가지 부분을 "분리"해서 사용했다.
2. 이미지의 깊이는 증가, 크기는 감소 
3. FC : 대부분의 FC는 유닛수가 같거나 점차 감소하는 패턴, 
    - 유닛수가 증가하는 패턴은 드물다


## 5.2 LeNet-5

* 5개의 가중치 (Conv 3개 + FC 2개)

* 활성화 함수로 tanh를 사용하였는데, 그 당시에는 tanh가 좋은 것으로 알려져 있었기 때문  
(당시에는 sigmoid와 tanh가 일반적이었으며 relu는 알려지지 않았다고 함)

* 3개의 Conv 층의 커널 갯수는 6, 16, 120
* 커널 사이즈는 3 by 3
* 풀링에서는 Average Pool 사용 
* 활성화 함수는 tanh 사용(당시 시대적인 분위기)
