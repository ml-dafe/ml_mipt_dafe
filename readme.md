# Машинное обучение на ФАЛТ 2021/2022

Курс основан на материалах: __Машинное обучение ФПМИ МФТИ__
[Видеолекции](https://www.youtube.com/playlist?list=PL4_hYwCyhAvZyW6qS58x4uElZgAkMVUvj)

# Tools 

## <img src='https://github.com/ml-dafe/ml_mipt_dafe_major/blob/master/src/anaconda.png' height="20px" width="20px" align="top"> Вариант 1
- Установить [Anaconda](https://www.anaconda.com/distribution/)
- Написать в командной строке: `jupyter notebook`
- Открыть в браузере [http://localhost:8888](http://localhost:8888)
- Использовать по назначению

## <img src='https://github.com/ml-dafe/ml_mipt_dafe_major/blob/master/src/docker.png' height="20px" width="20px" align="top"> Вариант 2
- Устанавливаем Docker с [официального сайта](https://www.docker.com/products/docker-desktop)
- Перейдите в терминале в директорию, где хотите запускать юпитер ноутбуки и используйте команду
```
docker run -d -p 4545:4545 -v $PWD:/home/user vlasoff/ml jupyter notebook 
``` 
- Заходим через браузер на [http://localhost:4545](http://localhost:4545)
- Использовать по назначению (Для остановки напишите в терминале`docker ps` and `docker stop`)
- Образ включает в себя:
  - Python 3.7
  - Julia 1.3.1 

> :warning: Unsecure! 
> Close port 4545 on your local machine while container is running  

## <img src='https://github.com/ml-dafe/ml_mipt_dafe_major/blob/master/src/colab.png' height="20px" width="20px" align="top"> Вариант 3
- Переходим в [Google colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true)
- Использовать по назначению

# Программа курса:

0. [Вводное занятие](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_00)

1. [Naive Bayes, kNN](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_01)
  - kNN
  - градиентный спуск
  - теорема Гаусса Маркова

2. [Linear Models](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_02)
  - численное и аналитическое решение
  - метрики
  - регуляризация

3. [Logistic Regression](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_03)
  - задача классификации
  - метрики
  - модель логистической регрессии
  - torch

4. [SVM & PCA](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_04)
  - PCA
  - SVD
  - SVM on torch

5. [Kaggle](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_05)
  

6. [Decision Trees](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_06)
  - Деревья решений

7. [Ensembles](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_07)
  - Bias-Variance decomposition
  - Bootstrap
  - Bagging
  - Random forest

8. [Boosting](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_08)
  - градиентный бустинг
  - AdaBoost
  - Catboost, LightGBM, XGboost

9. [Clustering](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_09)
  - Agglomerative clustering 
  - Mean-shift clustering
  - DBSCAN
  - Визуализация кластеров: t-SNE & PCA
  
