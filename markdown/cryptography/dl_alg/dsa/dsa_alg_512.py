#!/usr/bin/env python
# -*- coding:UTF-8

# http://www.pengshuo.me/2014/04/22/openssl%e7%bc%96%e7%a8%8b-%e7%ac%ac%e5%8d%81%e5%85%ab%e7%ab%a0-dsa/


# 平方乘算法
def square_multi(base, exp):
    init=0  #初始化设置
    result=0
    for b in str(bin(exp)[2:]):
        if (b=='1') and (init==0):
           init=1
           result=base
        elif (b=='1') and (init==1):
           result=result**2
           result=result*base
        else:
           result=result**2
    return result

priv=0x60537d11f52ac861b3b3f3bddd76ff2265ec6e56        
pub=0x0618a8426df66bbd2d2210dbd22d81ec5e1b64a912a57a8762fafd961ea96ec018f55c893ffdd7c494834ea4db353b5e30698dca121c889b2a3f0c54e7516dbd        
P=0x00b905deecc4a2ef4b3c0b6195676b3155aa43f375034c4b548cca6796ef7dd9e7dbd23040ce9fa52d08c50d7b439801f3ebc40c69ae1fa9feb1617343d2c63d19        
Q=0x00947a3831faf44c8044f1d52fdd4774cc916a1f2b         
G=0x009b2dc10e775b8bc8f67dfc8377576af4c2a985ac8d00584316707efcb8dd7c54c49fc2fd87990ae8cc9b6b9916ecca9dfbaed68757ab60e13a37439519185b10        

# 验证第一点 Q能整除P-1  Q|(P-1)
# 也就是 Q是 P-1的一个素除数

print  ((P-1)/Q)*Q==(P-1)

# G是生成元， 即G生成了拥有Q个元素的子群 
# G^Q=1 (mod P)

# 这样暴力 算不出来 需要用平方乘算法 也就是快速指数算法 P169 深入浅出密码学
#print (G**Q)%P==1

# 这个很费时  需要用c语言的大数库 瞬间计算
print square_multi(G,Q)%P

# 验证公钥私钥
print square_multi(G,priv)%P




