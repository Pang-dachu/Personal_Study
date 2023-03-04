- [Original](https://www.kaggle.com/code/yassineghouzam/titanic-top-4-with-ensemble-modeling)

- [Kaggle Desperation](https://www.kaggle.com/code/pangdar/titanic-top-4-with-ensemble-modeling)

---

* Outlier_Detection 함수 이용 
    > IQR 계산을 통해 이상치를 판단하는 과정을 사용했는데, collections의 Counter를 사용하여 일정 횟수 이상 등장하는 값에 대해서만 이상치로 판단하여 처리함

* Train Set과 Test Set을 합쳐서 전처리
    > 굉장히 의외였던 부분인데 Train과 Test데이터를 합쳐서 전처리 과정을 진행하는 과정을 사용함.

    > *"I join train and test datasets to obtain the same number of features during categorical conversion (See feature engineering)."*

    > 현재 생각으로는 점수를 뽑기 위한 방법으로는 사용해봄직한 과정인 것 같다.

* Age 결측값 채우는 과정 
    > Age 결측값을 채우는 과정에서 Heatmap을 사용한 상관계수를 이용하여 계산하는 과정이 인상적이었음. 

* pd.get_dummies의 prefix parameter
    > prefix를 사용하여 컬럼명에 지정한 단어를 접두사로 붙일 수 있다.