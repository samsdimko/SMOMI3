В файле train.py записана не предобученная нейросеть на основе vgg16 
В файле train1.py -- замороженная vgg16, обученная на image.net, с обучающимся классификатором
В файле train2.py -- размороженная предыдущая сеть

Заморозка и разморозка осуществлены с сохранением весов первой модели и последующим запуском второй на их основе.



В не предобученной сети на основе vgg16 получились следующие результаты для темпов обучения:

1) lr = 1e-7

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/1e-7.png)

2) lr = 1e-8

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/1e-8.png)

3) lr = 1e-9

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/1e-9.png)

4) lr = 1e-10

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/1e-10.png)

5) lr = 1e-11

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/1e-11.png)

Таким образом получилось, что функция потерь начинает себя адекватно вести при lr = 10^(-10) и меньше

В предобученной сети при обучении классификатора получилась следующая картина, lr = 10^(-6)

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Frozen.png)

После разморозки всех слоев, lr = 10^(-11)

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Unfrozen.png)

Совместные графики до и после разморозки (синий -- до, серый -- после)

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Together.png)