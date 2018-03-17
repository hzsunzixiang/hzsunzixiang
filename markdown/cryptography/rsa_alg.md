# <center>RSA加密算法的数学原理


<div style="text-align: right;">孙自翔 haichengsun123@163.com</div> 

<script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

说明: 本文从数学的角度，阐述RSA算法所涉及的数论方面的各个知识点，文章首先简要介绍RSA加密算法,然后分述各数学知识点,最后以一个实际例子结束。

## 密码学术语介绍

<!--
这里是注释显示不出来
{\rm 需转换的部分字符}
$$ evidence\_{i}=\sum \_{j}W\_{ij}x\_{j}+b\_{i} $$
其中，\\( W\_i \\) 和 \\( b\_i \\) 分别为类别 \\( i \\) 的权值和偏置。
\\( {\cal  K}   {\rm A}   \alpha　A　\beta　B　\gamma　\Gamma　\delta　\Delta　\epsilon　E \varepsilon　　\zeta　Z　\eta　H　\theta　\Theta　\vartheta \iota　I　\kappa　K　\lambda　\Lambda　\mu　M　\nu　N \xi　\Xi　o　O　\pi　\Pi　\varpi　　\rho　P \varrho　　\sigma　\Sigma　\varsigma　　\tau　T　\upsilon　\Upsilon \phi　\Phi　\varphi　　\chi　X　\psi　\Psi　\omega　\Omega  \\))
\\({\cal K} {\sf K}\\)
-->

密码系统是指包含可能的明文信息的有限集合 \\({\cal P}\\)，可能的密文信息的有限集合\\({\cal L}\\)，可能的密钥的密钥空间\\({\cal K}\\)，以及对于密钥空间\\({\cal K}\\)里的每一个密钥\\({k}\\)，存在加密函数\\(E\_k\\)和对应的解密函数\\(D\_k\\)，使得任意的明文信息\\(x\\)满足\\(D\_k(E\_k(x))=x\\)。


## 数论概念及定理阐述 
### 整除 
<!--摘自书籍--> 

一个整数可以被另一个整数整除的概念在数论中处于中心地位.

**定义** 如果\\(a\\)和\\(b\\)为整数且\\(a \neq 0\\), 我们说\\(a\\)整除\\(b\\)是指存在整数\\(c\\)使得\\(b=ac\\).如果\\(a\\)整除\\(b\\)，我们还称\\(a\\)是\\(b\\)的一个因子,且称\\(b\\)是\\(a\\)的倍数.

如果\\(a\\)整除\\(b\\),则将其记为\\(a \mid b\\),如果\\(a\\)不能整除\\(a\\),则将其记为 \\(a \nmid b\\)

比如：\\(13 \mid 182\\)，\\(-5\mid30\\)，\\(6 \nmid 44\\)，\\(7 \nmid 50\\)

### 模除  
<!--摘自wiki百科-->
**定义** 模除是一种不具交换性的二元运算。在C语言中用 \\(\%\\)表示。



> 当 \\(a = bq + r\\)， \\(q\\)是整数，并使其达到最大，此时我们说\\(a\\)模除\\(b\\)等于\\(r\\)。(\\(r\\)为非负数)。

> 以数学式子表示：\\(a模除b = a-\left\lfloor \frac{a}{b}\right\rfloor \times b\\)。

> 例如要计算\\(100模除16\\)，由于\\(100\div16\\)是一个大于6且不大于7的数，取\\(q=6\\)。结果为\\(100-16\times6=4\\)。



### 同余  
<!--\cite{WEBSITE:congruence_modulo}-->
同余的语言使得人们能用类似于处理等式的方式来处理整数关系。

 
**定义** 设m是正整数. 若\\(a和b\\)是整数,且 \\(m \mid (a-b)\\)
 

同余（英语：congruence modulo，符号：\\(\equiv\\))是数论中的一种等价关系。当两个整数除以同一个正整数，若得相同余数，则二整数同余。同余是抽象代数中的同余关系的原型。最先引用同余的概念与“≡”符号者为德国数学家高斯。


### 辗转相除法  
### 扩展欧几里得算法   
### 模逆元(模反元素)   
### 欧拉定理   
### 欧拉函数   
### 费马小定理   
### RSA算法   
