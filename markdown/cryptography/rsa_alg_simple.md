# <center>RSA加密算法的概述及证明</center>
 


<div style="text-align: right;">孙自翔 </div> 
<div style="text-align: right;">haichengsun123@163.com</div> 

<script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

**写在前面**: 本文简明扼要的阐述RSA算法的证明过程，只阐述必要的定理，不对定理本身做深入说明，专注于RSA算法本身。 并且在不引入中国剩余定理的情况下证明RSA算法.
   
 

 
<ol>   <!---定义有序列表 这个很重要-->


<!--
这里是注释显示不出来
{\rm 需转换的部分字符}
$$ evidence\_{i}=\sum \_{j}W\_{ij}x\_{j}+b\_{i} $$
其中，\\( W\_i \\) 和 \\( b\_i \\) 分别为类别 \\( i \\) 的权值和偏置。
\\( {\cal  K}   {\rm A}   \alpha　A　\beta　B　\gamma　\Gamma　\delta　\Delta　\epsilon　E \varepsilon　　\zeta　Z　\eta　H　\theta　\Theta　\vartheta \iota　I　\kappa　K　\lambda　\Lambda　\mu　M　\nu　N \xi　\Xi　o　O　\pi　\Pi　\varpi　　\rho　P \varrho　　\sigma　\Sigma　\varsigma　　\tau　T　\upsilon　\Upsilon \phi　\Phi　\varphi　　\chi　X　\psi　\Psi　\omega　\Omega  \\))
\\({\cal K} {\sf K}\\)
\\[\alpha\\]
--> 

## 算法概述
<ol>

### <li> RSA加密定义
\\(  RSA加密  \ \  \  \  \ 给定公钥（e,n）=k\_{pub}和明文x,则加密函数为:   \\)
$$y=e_\{k\_{pub}}(x)\equiv x^e \ mod \ n$$
\\(其中 x, y \in Z\_n\\)

### <li> RSA解密定义
\\(  RSA解密  \ \  \  \  \ 给定私钥（d,n）=k\_{pr}和密文y,则解密函数为:   \\)
$$x=d_\{k\_{pr}}(y)\equiv y^d \ mod \ n$$
\\(其中 x, y \in Z\_n\\)

### <li> 密钥生成过程
\\(  输出：公钥：k_{pub}=(e,n) 和私钥: k\_{pr}=(d,n)  \\)

\\( 1. 选择两个大素数p和q\\)     
\\( 2. 计算n=p\cdot q\\)     
\\( 3. 计算\varphi(n)=\varphi(p)\varphi(q)=(p-1)(q-1)\\)     
\\( 4. 选择满足以下条件的公钥e\in\\{1,2,....,\varphi(n)-1\\}， 使得\\)     
$$(e,\varphi(n))=1 \ \ \ \ 即e和\varphi(n)互素,下同$$
  \\(注意：实际的选择可以大于\varphi(n)\\)        
\\( 5. 计算满足以下条件的私钥d\\)  
$$d\cdot e \equiv 1 \ mod \ \varphi(n)$$    

 
### <li> 加解密实例1-较小的指数
Alice想要发送一个加密后的消息给Bob。首先，Bob执行步骤1~5计算RSA参数，并将他的公钥发给Alice。Alice然后将消息(x=4)加密，并将得到的密文y发送给Bob。最后Bob使用他自己的私钥解密y。     
**Alice有消息发送给Bob**    
>\\(消息x=4\\)
     
**Bob生成公钥和私钥**
>\\(1. 选择素数p=3和q=11\\)    
>\\(2. 计算n=p\cdot q =33\\)    
>\\(3. 计算\varphi(n)=\varphi(p)\varphi(q)=(3-1)(11-1)=20\\)    
>\\(4. 选择公钥 e =3, 使得 (e,\varphi(n))=(3,20)=1\\)    
>\\(5. 计算d=e^{-1}\ \equiv 7\ mod\ 20， 也就是d\cdot e \equiv 1\ mod\ 20\\)   
>\\(此时得到公钥(e,n)=(3,33), 私钥 (d) = 7 , 并把公钥公布于众\\) 

**Alice拿到Bob的公钥\\((e,n)=(3,33)\\)**
> \\(y=x^e\equiv4^3\equiv mod \ 33\\)    

**Bob收到Alice发送的密文\\(y=31\\),根据私钥d恢复明文**
> \\(x=y^d=31^7\equiv4 \mod \ 33\\) 即明文为4
>
 
### <li> 加解密实例2-较大的指数
小素数并不安全，目前2048位的素数才足够安全。给出一组16bit的和一组512bit的例子

**一个16bit的例子**
>\\(1. 选择素数p=211和q= 223\\)    
>\\(2. 计算n=p\cdot q = 47053\\)    
>\\(3. 计算\varphi(n)=\varphi(p)\varphi(q)=(211-1)(223-1)=46620\\)    
>\\(4. 选择公钥 e = 65537, 使得 (e,\varphi(n))=(65537, 46620)=1\\)    
>\\(5. 计算d=e^{-1}\ \equiv 39653\ mod\ 47053， 也就是d\cdot e \equiv 1\ mod\ \varphi(n)\\)    
>  $$65537*39653\%46620=1$$ 
>\\(此时得到公钥(e,n)=(65537, 47053), 私钥 (d) = 39653 \\) 


**一个512bit的例子**

>\\(p=0x00de58f6242be479c5c10ced57e6c5c9f9eeb01eccc85933215059d48770f3e943779dde635df6c1704c62f4b608b134a64443cc7e6b94f31b282ff18dc126e0c2e4dbbdd7582cfcb421a9952d0e3393461fb0be0b1debab53dcd858ca17a302c11e5f01559bac6c92948ba21a2b6ab654d9b899f5d55a6c08b9890a34fa544049\\)
>\\(q=0x00d969fe0b298c09a3b138f55f67985177a43a6cde776840457df76d5e463dd29ce0113774ddcf0375e3c4f6593f30533a32b9d1f791ca019bcc354dcb53974740535d0388f290b7aba975c1ecddfd23aa65a4b2adf186bbbf8749a955f50d234bad203b5c86279983fe5e6b9372853ebbf58d4b7310a0f5ddd740ae9413cd3a73\\)
>\\(n=0x00bcd577c7942b037ada6c2650145979132e6923528d74c6e44c2eb1338d236b5a74bc46dea3565853f7c6d159aca57bd44cf6511c7829fc4ecb6e5912a3212376adbcd41291227f3ed545c256925862f34c66f75fc13ae2e7166fc6ee38d9433016a1659d655c72c8993ab48f2573e00c8b216c75f1e9c1fbc4d7e7521e6e4ff773ff7147ee3d240a73c1dd6f94a2e09ec508b2c5fd6f7d1449e5780f75235aa763b006e2d7704f646d0f475f46d3f0efd563c4d43bbe70b5c54b1c4f3b21514b6538735c79f81c5d5765f1f237535aaa0ef1b58c343661b40bd5a2c319ddd5d2f5f1558b460d36b79844dfe80d33f1f0b7ecc7f46a60dc4bdd8714f46fde6acb\\)
>\\(e = 0x10001 \\)
>\\(d=0x385bddec0b24eb5cf763dfeb76a75da383ee8d444e43d438bf24106f3a689fd9d78d79f968f694563b55739638190be449341af14c4bfba9e8bd7e883977e285c144e266c83a6b8fed476cc139dc776bf619a52b4718b430145a381d518a46ab4b95d02631e26dbfc13bec37ed0db0890ddd63e9afd1fcbb8ffc8065d9ff428e2d28408ddeccf40419d54ef740c1b5b7cf85805652d666bd086d2bdd397babcfec9d3b53d7320733b629b73b88f400b73d8d6f5621778e227766a39433d0d4b95df4d2c259b62ce357c29ae483484b654cd4ff15a59b786a0aa36a064020aa9d927d8b3d03baadf0e110423e7e86e42a4fddbf2fb4cc34c3972bcd1e85854681\\)




## 重要定理阐述 
<ol>

### <li>欧拉定理   
欧拉定理在RSA加密算法中处于核心地位. 用来证明RSA算法的一般情形.      
**定义** 设\\(n\\)是一个正整数，**欧拉\\(\varphi函数\varphi(n)\\)**定义为不超过\\(n\\)且与\\(n\\)互素的正整数的个数。
<center> 欧拉函数\\(\varphi(n)\\)的值， \\(1\leq n \leq 12\\)  </center>  

|               n|   1|   2|   3|   4 |   5|   6|   7|   8|   9|  10|  11|  12|
|            :--:|:--:|:--:|:--:| :--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|\\(\varphi(n)\\)|   1|   1|   2|   2 |   4|   2|   6|   4|   6|   4|  10|   4|


**欧拉定理** 设\\(m\\)是一个正整数，\\(a\\)是一个整数且\\((a,m)=1\\),那么\\(a^{\varphi(m)}\equiv 1(mod\ m)\\)  
**证明** 参考《初等数论及其应用》

**一点说明**
> \\(这里的a和m不要求为素数，只要满足(a,m)=1\\)
> 而后面的费马小定理则要求模数是素数.
>

**举例说明**

>\\(令a = 4， m = 9，满足(a,m)=1且\varphi(9)=6\\)       
>此时有
>\\(a^{\varphi(m)} =4^{6}=4096 \equiv 1(mod \ 9)\\)


可以利用欧拉定理来找寻模m的逆，若\\(a\\)和\\(m\\)互素则，
$$a \cdot a^{\varphi(m)-1}=a^{\varphi(m)}\equiv 1(mod\ m)$$
因此，\\(a^{\varphi(m)-1}\\) 是\\(a\\)模\\(m\\)的逆。

**举例说明**
> 
> \\(7x \equiv 1(mod\ 10)，求x\\)    
> \\(令a=7，m=10，此时有(a,m)=1，\varphi(m)=\varphi(10)=4，所以\\)    
> \\(7模10的逆为7^{\varphi(10)-1}=7^{3}=343\equiv 3(mod\ 10)\\)    
> \\(所以7模10的逆x\equiv 3(mod10)\\)

**结论** 结合模的逆和欧拉定理,我们有如下结论    
> \\(若a\_{1},a\_{2}...a\_{k}...是a模m的逆，则有\\)
> \\(a^{\varphi(m)-1}\equiv \overline{a}\equiv a^{-1}\equiv a\_{1} \equiv a\_{2}\equiv...\equiv a\_{k}\equiv...(mod\ m)\\)
> \\(而且只有与\overline{a}模m同余的这些整数才是a模m的逆\\)

后面我们统一用\\(\overline{a}\\)记为\\(a模m\\)的逆。 

   
 

### <li>欧拉函数的性质  
**定理** 
\\(如果p是素数，那么\varphi(p)=p-1.反之，如果p是正整数且满足\varphi(p)=p-1，那么p是素数.\\)
> 根据欧拉函数的定义，这个是显然的.    

**定理**
\\(设m和n是互素的正整数，即(m,n)=1，那么\varphi(mn)=\varphi(m)\varphi(n)\\)

###<li> 费马小定理
**注**：书籍上会先引进并证明_费马小定理_，然后再证明_欧拉定理_，这里把_费马小定理_看成_欧拉定理_的特殊情况来证明。   
_**费马小定理**_在证明_**RSA算法**_的其中一种情况时用到。    
**定理(费马小定理)**  \\(设p是一个素数，a是一个正整数且(a,p)=1，则a^{p-1} \equiv 1(mod \ p)\\)    
> **证明**     
> \\(因为p是素数，所以有\varphi(p)=p-1\\)    
> 根据欧拉定理     
> $$a^{p-1} = a^{\varphi(p)}\equiv 1(mod\ p)$$
> 所以    
> $$a^{p-1}  \equiv 1(mod\ p)$$
> 
 

###<li> 辅助定理
此定理可以在不引入中国剩余定理的情况下证明RSA算法的特殊情形.   
定理为《初等数论及其应用》中的推论4.9.1 的一中特殊情况。   
**定理**  \\(若a\equiv b(mod \ m\_1), a\equiv b(mod\ m\_2)， 其中a，b是整数，（m\_1,m\_2）=1, 则\\)  
$$a\equiv b(mod \  m\_1m\_2)$$  
   


</ol>   <!---跟三级标题匹配--> 

## RSA算法证明
有了以上这些结论，我们可以推导出RSA加密算法.

 
### 重述：公钥和私钥的的生成步骤
> **RSA公钥和密钥生成**    
> **输出** : 公钥\\((e,n)和私钥d\\)    
> 1. 选择两个大素数\\(p和q\\)，则一定有\\((p,q)=1\\)  
> 2. 计算 \\(n=pq\\)    
> 3. 计算\\(\varphi(n)=\varphi(pq)=\varphi(p)\varphi(q)=(p-1)(q-1)\\)    
> 4. 选择整数\\(e\\)，使得\\((e,\varphi(n))=1\\)    
> 5. 计算满足以下条件的私钥\\(d\\)    
> $$d \cdot e \equiv 1 \ \ mod(\varphi(n))$$
>
>其中,第3步是依据欧拉函数的性质可得   
>第4步的要求可以保证\\(e模\varphi(n)的模逆元d\\)存在，      
>在选择\\(e的过程中，如果(e,\varphi(n)) \not= 1\\),则选择一个新的\\(e\\)值，并重复此过程.       



>加密报文X 属于[0,n) 
>两种情况 \\((x,n)=1, (x,n)\not=1\\)
>第一种情况用欧拉定理证明
>第二种情况用费马小定理结合以上的辅助定理得出结论
>


### RSA算法的证明
有了以上铺垫，RSA算法的证明水到渠成

RSA算法即是要证明以下等式成立    
$$  d\_{k\_{pr}} (y) = d_{k\_{pr}}(e\_{k\_{pub}}(x))\equiv(x^e)^d\equiv x^{de} \equiv x (mod \ n) $$

 
**证明**

由公钥和私钥的生成规则可知
$$d \cdot e \equiv 1 (mod \ \varphi(n))$$, 此表达式等价于    
$$d \cdot e \equiv 1 + t\cdot\varphi(n) \ 其中t \in Z_{n}$$
代入等式可得

$$  d\_{k\_{pr}} (y) \equiv x^{de} \equiv x^{1+t\dot\varphi(n)}  \equiv x^{t\dot\varphi(n)}\cdot x^1 \equiv (x^{\varphi(n)})^t  \cdot x (mod \ n)$$


**分两种情况证明**

**第一种情况**  
$$若(x,n)=1$$
根据欧拉定理   立即可得
$$x^{\varphi(n)} \equiv 1  $$ 继而

$$(x^{\varphi(n)})^{t} \equiv 1  $$
所以
$$  d\_{k\_{pr}} (y) \equiv x^{de} \equiv x^{1+t\dot\varphi(n)}  \equiv x^{t\dot\varphi(n)}\cdot x^1 \equiv (x^{\varphi(n)})^t  \cdot x \equiv x (mod \ n)$$




**第二种情况** 
 $$若(x,n) = (x, p\cdot q) \not=1$$
 分别证明 
$$  d\_{k\_{pr}} (y) \equiv  x (mod \ p)$$
$$  d\_{k\_{pr}} (y) \equiv  x (mod \ q)$$
由辅助定理可得
 $$ d\_{k\_{pr}} (y) \equiv  x \ (mod \ p\cdot q)$$
即
 $$ d\_{k\_{pr}} (y) \equiv  x \ (mod \ n)$$
只要证明其中之一即可,首先证明 \not  
>$$  d\_{k\_{pr}} (y) \equiv  x (mod \ p)$$

此时亦分两种情况    
*情况一 使用费马小定理* 
>$$x \not \equiv 0 (mod\ p) \Rightarrow (x,p) =1$$
此时有
$$  d\_{k\_{pr}} (y)  \equiv x^{t\dot\varphi(n)}\cdot x^1  \equiv x^{t(p-1)(q-1)}  \cdot x \equiv (x^{p-1})^{t(q-1)} \cdot x(mod \ p)$$
由费马小定理    
$$(x,p)=1，则x^{p-1} \equiv 1(mod \ p)$$
可得
$$  d\_{k\_{pr}} (y)  \equiv (x^{p-1})^{t(q-1)} \cdot x \equiv x(mod \ p)$$


*情况二*
>$$x  \equiv 0 (mod\ p)$$
>可得
 $$d\_{k\_{pr}} (y)  \equiv x^{ed} \equiv 0  \equiv x(mod\ p)$$

算法得证