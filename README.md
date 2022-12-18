# Writeup Repo

A collection of writeups from the CTFs we have participated.

## How to build ?


This document is currently deployed in mkdocs at https://teamshakti.in/CTF-Write-ups/ . Of course, it can also be deployed locally, as follows:

Installation dependence

    MKdocs
    pip install mkdocs
    # extensions
    pip install pymdown-extensions
    
    Theme
    
    pip install mkdocs-material
    pip install mkdocs-bootswatch
    pip install mkdocs-bootstrap
    
Local deployment

    mkdocs serve

The mkdocs locally deployed website is dynamically updated, ie when you modify and save the md file, the refresh page will be dynamically updated.

<!-- Generating the site locally  -->

<!--     # generate static file in site/ -->
<!--     mkdocs build -->
    
<!-- The generated webpage will be in `site/` folder -->

<!-- ### Using Docker  -->

<!-- After installing docker on your machine  -->

<!-- Just run  -->

<!--     docker pull squidfunk/mkdocs-material -->
<!--     docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material -->
    
The site will be served on http://localhost:8000


## Contribution

    ├── CNAME
    ├── docs
    │   ├── crypto
    │   ├── forensics
    │   ├── index.md
    │   ├── pwning
    │   ├── reversing
    │   ├── _static
    │   └── web
    ├── mkdocs.yml
    └── README.md
    |__ about.md

`mkdocs.yml` : config file for mkdocs , also contains details about the structure of the contents.
`docs` : contains all the required files.
`_static` : static file for the theme.

## How to add a new writeup

- Open the docs folder
- Go to the corresponding field of the writeup (Crypto,Reversing etc)
- If you are adding a new CTF
    - Create a CTF folder and inside it add your intro.md (which has a description about the CTF and the list of challenges).
    - Also edit the intro.md with the CTF name and it’s link.
    - Add the challenge name and the link to the mardown file along with the author's name (and twitter handle).
- If the CTF is already there go to the CTF folder
	- Add the challenge name and it’s link along with the author's name (and twitter handle) under the correct CTF bullet.



Docs :

[1] [mkdocs](https://www.mkdocs.org/#mkdocs) 

[2] [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)
    


    

