﻿#Слот второго дня.

label day_2_slot_us:
    scene bg ext_playground_sunset
    with dissolve
    "Я огляделся."
    "Но вокруг не было ни души!"
    th "Куда она делась?!"
    "Я отстал буквально на пару метров, а ее уже не было!"
    "Как будто улетела..."
    "Я постоял еще пару минут, ожидая, не покажется ли она откуда-нибудь..."
    "Но спрятаться на голом футбольном поле было абсолютно негде."
    "Так что мне поневоле пришлось смириться."
    "Я еще погрозил на прощание кулаком куда-то в кусты, где она могла бы сидеть..."
    "И пошел было обратно в столовую..."
    "Как сзади раздался сдавленный смешок..."
    "И не узнать его было невозможно!"
    th "Не знаю, откуда она появилась, разве что с неба свалилась..."
    "Потому что, когда я развернулся, она..."
    scene cg d2_soccer
    with dissolve

    play sound sfx_football_kick

    "С задорным смехом она врезала по невесть откуда взявшемуся у нее мячу и..."
    "Он полетел прямо в меня!"
    "И скорость у него была такая бешенная, что ни уклониться, ни отскочить я не мог..."
    "Как в замедленной съемке, наблюдал я летящий ко мне снаряд..."
    "А через секунду мощным ударом уже был сбит им на землю..."
    play sound sfx_football_catch
    with vpunch
    scene bg ext_playground_sunset
    with dissolve
    th "Хорошо, что в живот, а не ниже..."
    "От удара у меня сбило дыхание..."
    "Что спасло Ульянку от потока брани в ее адрес..."
    "А она и не думала убегать..."
    th "Наивная!"
    $ us_dress = 'pioneer'
    show us std
    us "Эй, чего валяешься?"
    th "Дай только отдышаться..."
    us "Столько бежал за мной..."
    us "Хы!"
    "Она осклабилась и показала руки, все измазанные в креме."
    us "А торта и не осталось!"
    us "Опоздал! Опоздал!"
    "Она принялась носиться вокруг меня и пинать в меня мяч."
    "А я наконец смог нормально вхдознуть..."
    me "Ты что в столовой устроила?"
    me "Ольга Дмитриевна тебе завтра задаст!"
    "Ульянка надулась."
    us "Сами виноваты!"
    us "Надо было поддаваться!"
    us "Это я должна была выиграть!"
    us "Я!"
    "И она снова принялась с силой колотить мяч, теперь об землю."
    me "Ну..."
    th "Надеюсь, она не хочет повторить тот свой удар..."
    me "Может, в следующий раз повезет..."
    "Я сказал это, чтобы хоть немного успокоить ее, но она поняла это по-своему..."
    us "В следующий раз я тако-о-ое придумаю, что сразу всех обыграю!"
    me "Верю..."
    scene bg ext_playground_night
    with dissolve
    "Пока мы стояли препираясь, на площадке уже заметно стемнело, и на небе появились первые звезды."
    me "Ты просить прощения собираешься?"
    "Но Ульянка только насупилась еще больше."
    me "Пойдем, извинишься - и Ольга Дми..."
    "Но она перебила."
    us "Не собираюсь я ни перед кем извиняться!"
    "А вот теперь она здорово разозлилась!"
    play sound sfx_football_kick
    "Ульяна со всей силы пнула по мячу, и он молнией полетел куда-то в темноту..."
    th "К счастью, не в мою сторону..."

    play sound sfx_broken_glass
    with vpunch
    
    "Судя по звону бьющегося стекла, целью оказалось окно крытого физзала, стоящего неподалеку!"
    us "Ой..."
    "Она сказала это так по-детски..."
    "Что я даже немного пожалел ее..."
    th "Ольга Дмитриевна так просто это не оставит..."
    me "А теперь что будешь делать?"
    "Но Ульянка только пожала плечами и задумчиво произнесла, ковыряя пальцем свою форму."
    us "Скажу, что это ты разбил..."
    me "Что?!"
    "При этом она хлопала глазами, как будто и не понимая, почему я так недоволен..."
    us "А что такого?"
    us "Мальчик ведь должен защищать девочку..."
    us "А девочка должна все свалить на мальчика, да?"
    "Тут я вспомнил, зачем гнался за Ульяной..."
    us "Пойдем... извинишься перед Ольгой Дмитриевной и..."
    "Я попытался взять ее за руку, но она ловко увернулась и отскочила к кустам..."
    us "Ольга Дмитриевна... Ольга Дмитриевна..."
    "Передразнила она меня."
    us "Я вам завтра и не такое устрою!"
    us "Вот увидите!"
    hide us
    "И с этими словами она нырнула в темную зелень."
    th "Что за день?!"
    "Бежать за ней уже не имело никакого смысла."
    "Поэтому я еще немного постоял, а потом пошел к себе."
    "Думая, что я буду говорить, если меня обвинят еще и в разбитом стекле..."
    jump day_2_dream