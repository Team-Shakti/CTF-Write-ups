# Writeup Repo

A collection of writeups from the CTFs we have participated.

## How to build ?


This document is currently deployed in mkdocs at "to be filled" . Of course, it can also be deployed locally, as follows:

Installation dependence

    # mkdocs
    pip install mkdocs
    # extensions
    pip install pymdown-extensions
    # theme
    pip install mkdocs-material
    
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


Docs :

[1] [mkdocs](https://www.mkdocs.org/#mkdocs) 

[2] [mkdocs-meterial](https://squidfunk.github.io/mkdocs-material/)
    


    

