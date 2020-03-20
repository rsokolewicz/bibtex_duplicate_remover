When combining different .bib files from co-authors or 
from previous projects, sometimes the same article is 
referenced using different a different cite-key and will 
appear multiple times in the bibliography. 

This package will go through your `.bib` file and find 
duplicate entries with different cite-keys and then update
the `.tex` file by replacing the cite keys accordingly.

### example
Suppose your bibliography file `bibliography.bib` contains the following two entries 
```
@article{PhysRev.47.777,
  title = {Can Quantum-Mechanical Description of Physical 
      Reality Be Considered Complete?},
  author = {Einstein, A. and Podolsky, B. and Rosen, N.},
  journal = {Phys. Rev.},
  volume = {47},
  issue = {10},
  pages = {777--780},
  year = {1935},
  publisher = {American Physical Society},
  url = {https://link.aps.org/doi/10.1103/PhysRev.47.777}
}

@article{Einstein1935,
  title = {Can Quantum-Mechanical Description of Physical 
      Reality Be Considered Complete?},
  author = {Einstein, A. and Podolsky, B. and Rosen, N.},
  journal = {Phys. Rev.},
  volume = {47},
  issue = {10},
  pages = {777--780},
  year = {1935},
  url = {https://link.aps.org/doi/10.1103/PhysRev.47.777}
}
```
which you cite with both keys inside `main.tex`. This will result in the following bibliography

![bibliography](.bibtex_duplicate_remover/img/bibliography.png)

This package can be used to automatically replace the key 
`Einstein1935` with `PhysRev.47.777` in your `main.tex` file and 
remove entry `@article{Einstein1935` from your `bibliography.bib` file by running the following code:

```
from bibtex_duplicate_remover import ReplaceCiteKeys, RemoveDuplicatesInBibfile

ReplaceCiteKeys(bibliography.bib, main.tex)
RemoveDuplicatesInBibfile(bibliography.bib)
```

This code can be easily extended to process multiple source files as:

```
from bibtex_duplicate_remover import ReplaceCiteKeys, RemoveDuplicatesInBibfile

files = ['./Chapters/Introduction.tex',
         './Chapters/Chapter01.tex',
         './Chapters/Chapter02.tex',
         './Chapters/Chapter03.tex',
         './Chapters/Chapter0A.tex',
         './Chapters/Chapter0B.tex',
         './Chapters/Chapter0C.tex',
         './Chapters/Chapter0D.tex'
        ]
for file in files:
    ReplaceCiteKeys(bibliography.bib, file)
RemoveDuplicatesInBibfile(bibliography.bib)
```


