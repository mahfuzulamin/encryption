# Encryption
* This project implements following ciphers using **Object Oriented Concept** and **Design Pattern**.
  * Hexadecimal
  * AtBash Cipher
  * Caesar Cipher
  * Keyword Cipher
  * Vigenère Cipher
* Each cipher is implemented in a separate class implementing parent's **abstract methods**. Basic input validation is implemented as well.
* **Typer wrappers** are implemented on top of Cipher implementations for each Ciphers to pass additional parameters from console.
* Unit test is implemented for all the ciphers.
* Documentation is provided for the project.

## **Hexadecimal**
* The hexadecimal Cipher encodes alphanumeric characters into hexadecimal numbers and decodes hexadecimal numbers to alphanumeric characters. It uses Python's hexadecimal library for encode and decode.
  * Example:
    * Encode: python secrets.py hex encode test1
    * Decode: python secrets.py hex decode 7465737431

## **AtBash Cipher**
* The AtBash Cipher implements AtBash Cipher algorithm and handles both uppercase and lowercase alphabets together as input. It doesn't encode/decode anything other than alphabet and simply includes those in the output.
  * Example:
    * Encode: python secrets.py atbash encode "Flee at once."
    * Decode: python secrets.py atbash decode "Uovv zg lmxv."

## **Caesar Cipher**
* The Caesar Cipher implements Caesar Cipher algorithm and handles both uppercase and lowercase alphabets together as input. It doesn't encode/decode anything other than alphabet and includes only space in the output if provided in the input.
  * Example:
    * Encode: python secrets.py caesar encode 3 "Hello World"
    * Decode: python secrets.py caesar decode 3 "Khoor Zruog"

## **Keyword Cipher**
* The Keyword Cipher implements Keyword Cipher algorithm and handles both uppercase and lowercase alphabets together as input. It doesn't encode/decode anything other than alphabet. It can take space in the input but output of both encode/decode doesn’t include it. Key cannot be longer than the message.
  * Example:
    * Encode: python secrets.py keyword encode "kryptos" "Knowledge is Power"
    * Decode: python secrets.py keyword decode "kryptos" DGHVETPSTBMIHVTL

## **Vigenère Cipher**
* The Keyword Cipher implements Vigenère Cipher algorithm and handles only uppercase alphabets and outputs uppercase message. It takes both uppercase and lowercase alphabets as input and converts in uppercase before processing. It doesn't encode/decode anything other than alphabet. Key cannot be longer than the message.
  * Example:
    * Encode: python secrets.py vigenere encode "LEMONLEMONLE" "attackatdawn"
    * Decode: python secrets.py vigenere decode lemonlemonle LXFOPVEFRNHR

## **Unit Test**
* python3 -m pytest
