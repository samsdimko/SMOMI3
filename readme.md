В файле train.py записана не предобученная нейросеть на основе vgg16 
В файле train1.py -- замороженная vgg16, обученная на image.net, с обучающимся классификатором
В файле train2.py -- размороженная предыдущая сеть

Заморозка и разморозка осуществлены с сохранением весов первой модели и последующим запуском второй на их основе.



В не предобученной сети на основе vgg16 прежде чем нейросеть уходила в nan получились следующие результаты:

1)

Функции потерь 

Train

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Train_loss_1.png)

Test

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Test_loss_1.png)

Метрики точности

Train

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Train_acc_1.png)

Test

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Test_acc_1.png)

2)

Функции потерь 

Train

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Train_loss_2.png)

Test

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Test_loss_2.png)

Метрики точности

Train

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Train_acc_2.png)

Test

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Test_acc_2.png)

3)

Функции потерь 

Train

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Train_loss_3.png)

Test

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Test_loss_3.png)

Метрики точности

Train

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Train_acc_3.png)

Test

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Test_acc_3.png)



В предобученной сети при обучении классификатора получилась следующая картина

Функции потерь 

Train

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Train_loss_4.png)

Test

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Test_loss_4.png)

Метрики точности

Train

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Train_acc_4.png)

Test

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Test_acc_4.png)

После разморозки всех слоев

Train

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Train_loss_5.png)

Test

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Test_loss_5.png)

Метрики точности

Train

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Train_acc_5.png)

Test

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Test_acc_5.png)

Совместные графики до и после зраморозки (зеленый -- до, серый -- после)

Train

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Train_loss_6.png)

Test

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Test_loss_6.png)

Метрики точности

Train

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Train_acc_6.png)

Test

![Image alt](https://github.com/samsdimko/SMOMI3/blob/master/Test_acc_6.png)