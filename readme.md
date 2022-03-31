# Машинное обучение на ФАЛТ 2021/2022

Курс основан на материалах: __Машинное обучение ФПМИ МФТИ__
[Видеолекции](https://www.youtube.com/playlist?list=PL4_hYwCyhAvZyW6qS58x4uElZgAkMVUvj)

# Инстурменты окружения

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

# Программа DL курса:

1. [Введение в нейронные сети](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_01)
  - теория по методу обучения сетей - обратное распространение ошибки
  - кодирование данных
  - функции потерь
  - нейронная сеть на numpy

2. [Примитивный цикл обучения на Pytorch](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_02)
  - torch.tensor
  - Dataset, Dataloader
  - nn.Module: forward, backward
  - цикл обучения на torch

3. [Сверточная нейронная сеть](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_03)
  - загрузка данных CIFAR10
  - операции conv2d, pooling, dropout, batchnorm
  - построение примитивной CNN
  - цикл обучения
  - примеры логирования на tensorboard, wandb

4. [Сверточные нейронные сети в задачах компьютерного зрения](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_04)
  - описание задач
  - metric learning
  - self-supervision
  
5. [Практика с kaggle](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_05)
  - знакомство с площадкой Kaggle

6. [CNN для решения задачи сегментации](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_06)
  - Архитектуры для сегментации
  - метрики и функции потерь

7. [CNN для решения задачи распознавания](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_07)
  - R-CNN, Fast R-CNN, Faster R-CNN
  - two/one shot detectors

8. [Генерация изображений](https://github.com/ml-dafe/ml_mipt_dafe/tree/main/week_08)
  - deep inpainting
  - AE / VAE
  - GAN

