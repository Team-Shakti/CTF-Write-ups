# Taxes

Solved by : Sridevi

## Description

![taxes](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/forensics/TAMUCTF22/Taxes/taxes.png)

## Solution

We are given a zip file. Unzip the file, we get an encrypted pdf file. There is a hint given in the description that the password of the pdf file is a SSN nuber, which is nine-digit number that the U.S. government issues to all U.S. citizens which basically means that the password length is 9. 

Used "crunch" ( a utility to generate wordlists using letters, numbers, and symbols for every possible combination) to create a wordlist with 9 digit numbers of all the combinations. 

![1](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/forensics/TAMUCTF22/Taxes/1.png)

Then used the tool 'pdfcrack' with the created wordlist and got the password after a few hours :P

![2](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/forensics/TAMUCTF22/Taxes/2.png)

The password was '694705124'. Opened the pdf file with this password and got the flag.

![3](https://raw.githubusercontent.com/Team-Shakti/CTF-Write-ups/master/docs/forensics/TAMUCTF22/Taxes/3.png)


**gigem{hope_you_did_your_taxes_already}**

We got the flag!
