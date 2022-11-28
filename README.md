# lost-punks

### Dead Punks

How many punks are lost forever? This question comes up often. I've heard numbers as high as 2,000 but without a source. This script is a starting point to help answer that question. 

Roughly 192, or 2% of CryptoPunks are lost. "Lost" is defined as a wallet or related wallet having no transactions for 4 years.

Interestingly, 155 of the 192 are concentrated in two wallets: [0x717](https://cryptopunks.app/cryptopunks/accountinfo?account=0x7174039818a41e1ae40fdcfa3e293b0f41592af2) which has 89 punks and [0x776](0x7760E0243cA9BAA630412865DF7b39AfbA42Ff0f) which has 66 punks. See screenshots below for the punks lost to the ether. 

![image](https://user-images.githubusercontent.com/90461460/204386278-05edee1b-131a-4c12-84f0-c3d52981d77a.png)
![image](https://user-images.githubusercontent.com/90461460/204386354-8a4d4ce8-027d-4e99-9795-a2e4972df5d9.png)


### Running the script
* set `years_dormant` (default = 4)
* run `python3 script.py`

### Depedencies
* Python 3
* Etherscan API
* Infura API 

### Changing parameters 

Surprisingly, changing how many years a wallet has been dormant doesn't move the needle. 

* 4 years - 192 lost
* 3 years - 223 lost
* 2 years - 241 lost

### 4 year wallet data 

192 / 10,000 punks lost: ~2%

| Address | Total Lost |
| --- | --- |
| 0x7174039818a41E1ae40FDcFA3E293b0f41592AF2 | 89 |
| 0x7760E0243cA9BAA630412865DF7b39AfbA42Ff0f | 66 |
| 0xc8c115dcB2910eE8F3dbAC4056B5448C4f624bde | 5 |
| 0x09BdF0eFDfFDb841fAF667CBc4f9c9B09fd6b909 | 4 |
| 0x8A873b31646dF1F4de3e28c2f608Bc37f21fE4D7 | 2 |
| 0x96cdA18688cB93F0578CE9DFA35014c877624f1F | 2 |
| 0xDe03D31d4EAf058497C7B27CA74E8110014FbF6d | 2 |
| 0xe675218BbA7eC17b0E2231bcAcfe41C07667cbe8 | 2 |
| 0x01c59869B44F3Fc5420dbB9166a735CdC020E9Ae | 1 |
| 0x03FbbFE27FAe9bd53dBc5B5c7fC0504c9B3DD0B1 | 1 |
| 0x12945660aAaB3fB97F46E18fCee02959C2d13bc5 | 1 |
| 0x147A3aaA88c451F97D95684aBFBCc846c22262Ab | 1 |
| 0x18F4F933F8773c5BfbDF1a675F5Fe667bc2020a1 | 1 |
| 0x28c89718f4daB5Cf853E37e96735a3cAD85C41d5 | 1 |
| 0x2a15cAfb85096027179B5568334a812b13BF268c | 1 |
| 0x4B674e70f6B36801d3bcA071628Cd6759dD3d039 | 1 |
| 0x4Ef1aB9a3330C1d7d0A039CDC47eDEB41254E39e | 1 |
| 0x582b2164D8C0AD22E0777275d646F29FD18D27c4 | 1 |
| 0x729FbdD2c5662FC11f62104D298BAf06a47b1245 | 1 |
| 0x77F713b00cA5f1B258A47Be34d947ABE5617154b | 1 |
| 0x7C892fE9cD3545b2dD30C045555D82f3b76C839a | 1 |
| 0x871f66E0C9C77141d25FB52222AcE830B584F209 | 1 |
| 0xbFc586A34128D14ECf29d1aAEB71E08AAE5827CC | 1 |
| 0xC52641D393C78Bc70C25a0ABc99B32A26f38D890 | 1 |
| 0xF21E5f7B79FDC4E5695c7349eaFD5bD5981c68b7 | 1 |
| 0xF7b33567153e20cDc811e0FE02bD37E0B6893688 | 1 |
| 0xf892D9Fa129bD7abA89f29361Fe6C0e749F8935a | 1 |
| 0xFBb0658c4796f66e3376ea9E7CC200C428F217DD | 1 |

