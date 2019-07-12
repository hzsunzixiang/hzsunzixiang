
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <assert.h>
#include "gmp.h"
int main()
{
	mpz_t P;    // 素数
	mpz_t Q;    // Q个元素的子群 
	mpz_t G;    // 生成元
	mpz_t pub;  // 公钥
	mpz_t priv; // 私钥
	mpz_t tmp;  // 临时值
	mpz_t phi_P;    //P的欧拉phi函数为P-1 
	mpz_inits (P ,Q, G, pub, priv, tmp, phi_P, NULL);
	mpz_set_str (P, "0x00b905deecc4a2ef4b3c0b6195676b3155aa43f375034c4b548cca6796ef7dd9e7dbd23040ce9fa52d08c50d7b439801f3ebc40c69ae1fa9feb1617343d2c63d19", 0); //  初始化素数
	mpz_set_str (Q, "0x00947a3831faf44c8044f1d52fdd4774cc916a1f2b", 0); // 初始化子群个数
	mpz_set_str (G, "0x009b2dc10e775b8bc8f67dfc8377576af4c2a985ac8d00584316707efcb8dd7c54c49fc2fd87990ae8cc9b6b9916ecca9dfbaed68757ab60e13a37439519185b10", 0);
	mpz_set_str (priv, "0x60537d11f52ac861b3b3f3bddd76ff2265ec6e56", 0);
	mpz_set_str (pub, "0x0618a8426df66bbd2d2210dbd22d81ec5e1b64a912a57a8762fafd961ea96ec018f55c893ffdd7c494834ea4db353b5e30698dca121c889b2a3f0c54e7516dbd", 0);
	mpz_set_str (phi_P, "0x00b905deecc4a2ef4b3c0b6195676b3155aa43f375034c4b548cca6796ef7dd9e7dbd23040ce9fa52d08c50d7b439801f3ebc40c69ae1fa9feb1617343d2c63d18", 0); //  初始化素数
// 验证 (G**Q)%P==1
	mpz_powm(tmp, G, Q, P);
    printf("modulus G^Q % P =  : ");
	mpz_out_str(stdout, 10, tmp);
	printf("\n");

// # 验证公钥私钥
// G^priv)%P=pub
	mpz_powm(tmp, G, priv, P);
// 验证和公钥相等
	int result = mpz_cmp(tmp, pub);
    printf("G^priv \%P = pub|result = : %d\n", result);

//# 验证第一点 Q能整除P-1  Q|(P-1)
// 也就是证明 (P-1)%Q=0
	mpz_mod (tmp, phi_P, Q);
    printf("(P-1)%Q result = : ");
	mpz_out_str(stdout, 10, tmp);
	printf("\n");
}
