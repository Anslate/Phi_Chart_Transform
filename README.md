# Phi Chart Transform

Phigros官谱Json至rpe json以及pec的转换  
简称PCT  
版本v0.1  
先来句名言辟邪
> 爬  
> —— lchzh3473

## 本项目基本被弃坑，可能会有以下要素  

屎山代码  
依靠bug运行  
重构不能  
注释失踪  

## 言归正传  

由于官谱json中的运动是以线性方式存储的  
所有的非线性运动也是分割成一小段一小段的线性运动  
所以转换完成的谱面可能会有上万甚至数十万个动作，pe及rpe也会因此崩溃  
~~pe和rpe被玩坏了，绝对不是Anslate的错，绝对不是！~~  
所以保护制谱器，从我做起，不要滥用，仅供参考  
也欢迎大家提Issues以及Pull requests来改进代码，十分感谢！

## 使用方法

安装好python3，建议最新版，理论上只要是py3都可以，不用第三方库

### 首先是Json To Pec  

字面意思，官谱json转为pec  
打开`Json2Pec.py`，在第3、4行会看到a和b的赋值，这是源官谱json和目标pec的绝对地址  
a是源官谱json绝对地址  
b是目标pec绝对地址  
直接更改掉然后运行就行了  
~~不会有人连Python赋值都不会吧，不会吧不会吧~~

### 其次是Json To Rpe

为了方便，以下rpe Json简称rpej  
字面意思，官谱json转为rpej  
将`Json2Rpe.py`与你的官谱Json，音频，曲绘放在同一目录下，三个都不能少  
demo目录中有一张1920x1080的空白图片，有需要的可以取用  
然后直接运行`Json2Rpe.py`，他会提示怎么操作  
填名称需要后缀名  
举个例子

```
官谱json名称:
Chart_IN.json
希望导出的rpe json名称:
Chart_IN_rpe.json
名称:WATER
音频名称:music.wav
曲绘名称:Illustration.png
谱师:乱流に巻き込まれ
曲师: A-39/沙包P
难度:IN Lv.13
```

输完这些后就会开始转换了  
转换完后将rpej，曲绘，音频，info.txt压缩为一个zip  
并将zip后缀改为pez  
在rpe中导入就行啦  
默认id是00000000，可以在代码第18行更改

## 题外话  

用来举例的WATER在我的rpe中是打不开的，毕竟那判定线表演，没有数十万个动作搞不定  
于是，炸内存了  
Rrhar'il的AT也有bug，但我没找出来问题在哪  
在线等个大佬Pull requests  

**请随意使用，本作品已无版权限制**  
**注意：此项目与厦门鸽游网络有限公司(Xiamen Pigeon Games Network Co., Ltd.)没有任何关系**  
若有侵权，请联系删除
