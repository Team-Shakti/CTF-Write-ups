#Phasestream3
## Description


>> On looking at phasestream3.py, we get to know that key used for AES-CTR is reused, which makes it similar to XOR. We also have a known plaintext and the ciphertext of it, using which we find the key. The key found here is used for decrypting the flag.

Ciphertext of known plaintext:  **464851522838603926f4422a4ca6d81b02f351b454e6f968a324fcc77da30cf979eec57c8675de3bb92f6c21730607066226780a8d4539fcf67f9f5589d150a6c7867140b5a63de2971dc209f480c270882194f288167ed910b64cf627ea6392456fa1b648afd0b239b59652baedc595d4f87634cf7ec4262f8c9581d7f56dc6f836cfe696518ce434ef4616431d4d1b361c**

Ciphertext of flag: 
**4b6f25623a2d3b3833a8405557e7e83257d360a054c2ea**


<p align="left">

<img src = "../../asset/PS3.png" width = "300" height = "300" >

</p>
 
`flag = CHTB{r3u53d_k3Y_4TT4cK}`
