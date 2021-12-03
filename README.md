# OS crypto exercices

&copy; Maxence Raballand 2021

Exercices from [this source](https://vqhuy.github.io/teaching/crypto/td4)

## 1. Hashing

Simple nonce generator for brute force in [this file](hashing_1.py).

The results for the exercice are :

![Result of hashing](/media/result_hash.png)

## 2. What is an authenticated encryption?

Authenticated encryption (AE) allow you to both encrypt data (privacy) and ensure authenticity of the data.

## 3. Why should you use authenticated encryption?

If you send data unencrypted, you don't have privacy. If you don't have authentication and a middle man has access to your encryption method, he could send wrong message to the user you wanted to send a message to.

## 4. Name few authenticated encryption modes.

- Encrypt-and-Authenticate
- Authenticate-then-Encrypt
- Encrypt-then-Authenticate
