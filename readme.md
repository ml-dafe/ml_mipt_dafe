# Машинное обучение на ФАЛТ 2021/2022

Курс основан на материалах: __Машинное обучение ФИВТ МФТИ__
[Видеолекции](https://www.youtube.com/playlist?list=PL4_hYwCyhAvZyW6qS58x4uElZgAkMVUvj)

[Текущие результаты](https://docs.google.com/spreadsheets/d/14OtGRIsVzB0n-rJOlq899GqIab0i5W4tswir2j9Be9o/edit#gid=0)

## Tools 

### <img src='https://github.com/ml-dafe/ml_mipt_dafe_major/blob/master/src/anaconda.png' height="20px" width="20px" align="top"> Вариант 1
- Установить [Anaconda](https://www.anaconda.com/distribution/)
- Написать в командной строке: `jupyter notebook`
- Открыть в браузере [http://localhost:8888](http://localhost:8888)
- Использовать по назначению

### <img src='https://github.com/ml-dafe/ml_mipt_dafe_major/blob/master/src/docker.png' height="20px" width="20px" align="top"> Вариант 2
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

### <img src='https://github.com/ml-dafe/ml_mipt_dafe_major/blob/master/src/colab.png' height="20px" width="20px" align="top"> Вариант 3
- Переходим в [Google colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true)
- Использовать по назначению
