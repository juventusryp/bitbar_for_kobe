#!/usr/bin/env python
# coding=utf-8
# <bitbar.title>Do Not Disturb</bitbar.title>
# <bitbar.author>BlackRun</bitbar.author>
# <bitbar.author.github>BlackRun</bitbar.author.github>
# <bitbar.desc>KobeBryant---passionate、obsessive、relentless、resilient、fearless</bitbar.desc>
# <bitbar.dependencies>python3</bitbar.dependencies>
# <bitbar.version>v1.0</bitbar.version>
import random
import sys
kobe_en = ""
mamba_mentality_en = "Mamba Mentality:passionate、obsessive、relentless、resilient、fearless"
quoations_en = [
        'Mamba out',
        'Friends always come and go, but a champion flag will never fall',
        'Second place means you’re the first loser',
        'If you\'re afraid to fail then you\'re probably going to fail',
        'I know that the appearance of Los Angeles at four o \'clock in the morning every day',
        'What I’m doing right now, I’m chasing perfection',
        'Somebody has to win, so why not be me?',
        'Boos do not block dunks',
        'I would go 0-30 before I would go 0-9. 0-9 means you beat yourself, you psyched yourself out of the game',
        'The only thing I\'m afraid of is bees',
        'I feel like killing everybody every time I go to the arena',
        'I don\'t want to be the next Michael Jordan, I only want to be Kobe Bryant',
        'Love me or hate me，it\'s one or the other。Always has been。Hate my game，my swagger。Hate my fadeaway，my hunger。Hate that I\'m a veteran。A champion。Hate that。Hate it with all your heart。And hate that I\'m loved，for the exact same reasons',
        'Bowed their heads and not give up, it is to see his own way; Please not proud, is to see their own sky',
        'If the lakers are now the Titanic, I\'ll sink together with him',
        'When I retire, I want to look back the way I walked past, every day, I have paid my all',
        'Hate me, because I desire your great, great, need at all costs',
        'Heros come and go,but legends are forever',
        'Should seize every opportunity to prove to everyone that you, prove that you are able to meet the challenge',
        'I know I played like crap, but you don\'t know me in order to let oneself have less like shit, how much effort',
        'If you love a thing you will overcome all difficulties',
        'I can\'t relate to lazy people. We don\'t speak the same language. I don\'t understand you. I don\'t want to understand you',
        'Eight hours of training, pain is only the body, but if the loss, you pain is the heart',
        'Everything negative — pressure, challenges — is all an opportunity for me to rise',
        'The last time I was intimidated was when I was 6 years old in karate class',
        'Losing is losing, there aren\'t different degrees of losing. You either win a championship or you\'re s---. It\'s very black & white to me',
        'The moment you give up, is the moment you let someone else win',
        'The important thing is that your teammates have to know you\'re pulling for them and you really want them to be successful',
        'My hearing is getting worse, hear boos in each stadium',
        'I’ll do whatever it takes to win games, whether it’s sitting on a bench waving a towel, handing a cup of water to a teammate, or hitting the game-winning shot',
        'I just go. I just go. I just keep going until it feels right to me,” Kobe says of his habits. “If something doesn’t feel right, I’m gonna stay there until I get it right. I just continue to keep pushing and pushing and pushing. That’s all I’ve known. That’s how my parents raised me. If you’re going to be focused on something, if you want to do something, you can’t, you can’t go about it in a half-assed way. You really gotta dedicate yourself to it, try to be the best at it. That’s the only way',
        'I do what I do',
        'Some of life, you have to go to the great challenges',
        ' I have self-doubt. I have insecurity. I have nights when I show up at the arena and I’m like, ‘My back hurts, my feet hurt, my knees hurt. But, I just want to chill.’ We all have self-doubt. You don’t deny it, but you also don’t capitulate to it. You embrace it',
        'My brain cannot process failure ... It WILL not process failure',
        'If you do not believe in yourself, no one else will',
        'As far as carrying the torch for the years to come, I don’t know. I just want to be the best basketball player I can be',
        'I just got one more than Shaq. You can take that to the bank',
        'I focus on one thing and one thing only – that’s trying to win as many championships as I can',
        'I,Kobe Bryant...have decided to skip college and take my talents to the NBA',
    ]

kobe_zh = "如果哪天你忘记了努力，我把科比讲给你听"
mamba_mentality_zh = "曼巴精神:热情、执着、严厉、回击、无惧"
quoations_zh = [
        '曼走',
        '朋友来了又走，冠军旗帜永不朽',
        '第二名只能说明你是头号输家',
        '如果你害怕失败，那意味着你已经输了',
        '我见过每天凌晨四点的洛杉矶',
        '24，意味着24小时全力以赴',
        '我现在所做的一切，都是为了追求更加完美',
        '总有一个人要赢，那为什么不能是我？',
        '嘘声又不能盖掉我',
        '我宁愿30投0中，也不愿意9投0中。9投0中意味着你被自己打败了，被比赛吓得不知所措……唯一的解释就是，你已经对自己丧失信心',
        '除了蜜蜂，我无所畏惧',
        '每一次走上球场，我都觉得自己可以击败每一个人',
        '我不想做下一个迈克尔-乔丹，我只想做科比-布莱恩特',
        '爱我或者恨我，两者必有其一，这就是生活。有许多人恨我，恨我的偏执，恨我对比赛的专注，恨我的后仰跳投。但也有许多人爱我，理由却和恨我的人一样',
        '低头不是认输,是要看清自己的路。仰头不是骄傲,是看见自己的天空',
        '如果现在湖人是泰坦尼克，我会和他一起沉下去',
        '当我退役的时候，我希望回头看我走过的路，每一天，我都付出了我的全部',
        '恨我，因为我渴望你伟大，而伟大，需要不惜一切代价',
        '英雄是一时的，但传奇是一世的',
        '要抓住一切机会，向所有人证明你自己，证明你能够迎接挑战',
        '我知道我自己打得像坨屎一样，但你们不知道我为了让自己打得不那么像坨屎，付出了多少努力',
        '如果你热爱一件事时，你就会为它克服一切困难',
        '我没法和懒人相处，我们讲的不是同一种语言，我不了解懒人，也不想去了解',
        '八小时的训练,痛的只是身体,但如果输球,你痛的是心',
        '每件负面的事 – 压力、挑战 – 都是一个让我提升的良机',
        '我最后一次被吓到还是6岁时学空手道',
        '输球就是输球，没有什么遗憾告负。赢得冠军或者两手空空，就这么简单',
        '你放弃的那一刻，就是你让对手赢的那刻',
        '重要的是，你的队友必须知道你是站在他们这边的，你是真心希望他们成功的',
        '我的听力越来越差了，每个球场都听不见嘘声',
        '为了取得比赛的胜利，要我做什么都可以，不管是坐在板凳席上给队友递毛巾、递水，还是上场执行致胜一投',
        '我只是不停地训练，不停地训练，直到我满意为止。如果我感觉一些东西不对，我会呆在那不停地训练，直到我做到对为止。我只是不停地激励自己，不停地激励自己。这是我很了解自己的地方，也是父母教育我的东西。如果你要专注于某些事情，如果你想要做某些事情，你可不能半途而废，你得倾注你全部精力去完成那些事，尽力去完美地完成那些事。这就是事情解决的唯一途径',
        '做我该做的事',
        '有些时候你必须去挑战伟大',
        '我会自我怀疑，我会缺乏安全感。很多夜晚，当我出现在比赛场时，我心里却嘀咕：“我的背好疼，我的脚好疼，我的膝盖好疼。但是我不会那么紧张。我们都会有缺乏自信的时候。你不应该否认这一事实，但是你不要向它屈服，你要敢于面对它',
        '我的大脑没法处理失败，它不会',
        '如果你都不相信自己，没人会相信你',
        '我不知道需要多长时间才能取得辉煌，我只是想尽我所能去成为最出色的篮球运动员',
        '现在我比奥尼尔多了一个总冠军，你们可以把这句话写在报纸上',
        '我专注于一件事，而且只有这件事 ，那就是尽我所能地赢到越多冠军',
        '嗨，我是科比-布莱恩特，我已经决定把我的天赋带到......额，我决定跳过大学，把我的天赋带到NBA',
        '那些你早起努力的时光，那些你熬夜奋斗的日子,那些你多疲惫,却依然在坚持的时候,那就是梦想的力量'
    ]


articles = [
    '一个科蜜最甜美的梦——科比的“名人堂演讲”' + '| href=' + 'https://news.zhibo8.cc/nba/2020-01-28/5e30449eb6a85.htm',
    '绝对巨星科比 送君别离千里 曼巴精神永存' + '| href=' + 'https://news.zhibo8.cc/nba/2020-01-27/5e2ec343a6dfb.htm',
    '英雄一时 传奇一世！盘点科比生前41条经典语录' + '| href=' + 'https://news.zhibo8.cc/nba/2020-01-27/5e2ea09917e69.htm',
    '科比的传奇职业生涯' + '| href=' + 'https://news.zhibo8.cc/nba/2020-01-27/5e2e93dbc8a75.htm',
    '科比-布莱恩特——你与凌晨四点永生同在' + '| href=' + 'https://news.zhibo8.cc/nba/2020-01-27/5e2e82af10909.htm',
    '最长的电影——致科比' + '| href=' + 'https://news.zhibo8.cc/nba/2020-01-29/5e30e76de67a6.htm'
]

movies = [
    '历历在目！重温科比职业生涯最后一战' + '| href=' + 'https://weibo.com/tv/v/Irs4EeeeN?fid=1034:4465425539334155&sudaref=www.zhibo8.cc&display=0&retcode=6102',
    '23&24最后一次对决！' + '| href=' + 'https://weibo.com/tv/v/IrVlahKtZ?fid=1034:4466549394964482',
    'Remembering Kobe Bryant！' + '| href=' + 'https://weibo.com/tv/v/IrVAHgJuf?fid=1034:4466557376462879',
    '能否重启2020？让时光倒回这甜蜜的一刻！' + '| href=' + 'http://1251542705.vod2.myqcloud.com/vod-player/1251542705/5285890798173826396/tcplayer/console/vod-player.html?autoplay=false&width=960&height=540',
    '如果你永不畏惧！科比当年在《开讲啦》励志演讲' + '| href=' + 'http://1251542705.vod2.myqcloud.com/vod-player/1251542705/5285890798119901101/tcplayer/console/vod-player.html?autoplay=false&width=960&height=540',
    '[中字]曼巴OUT！科比球衣退役演讲' + '| href=' + 'https://weibo.com/tv/v/IrtPXmrHY?fid=1034:4465467083915321',
]

def show_articles():
    for i in articles:
        print('--' + i)

def show_movies():
    for i in movies:
        print('--' + i)

def mamba_en():
    print(random.choice(quoations_en)+ "| color = #441571")
    print('---')
    print(kobe_en + "| color = #441571")
    print(mamba_mentality_en + "| color = #441571")

def mamba_zh():
    print(random.choice(quoations_zh)+ "| color = #441571")
    print('---')
    print(kobe_zh + "| color = #441571")
    show_articles()
    print(mamba_mentality_zh + "| color = #441571")
    show_movies()







if __name__ == "__main__":
    mamba_zh()