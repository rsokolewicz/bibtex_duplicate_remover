When combining different .bib files from co-authors or 
from previous projects, sometimes the same article is 
cited using different cite-keys and will 
appear multiple times in the bibliography. 

This package will go through your `.bib` file and find 
duplicate entries with different cite-keys and then update
the `.tex` file by replacing the cite keys accordingly.

### Example
Suppose your bibliography file `bibliography.bib` contains 
the following two entries:
```
@article{PhysRev.47.777,
  title = {Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?},
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
  title = {Can Quantum-Mechanical Description of Physical Reality Be Considered Complete?},
  author = {Einstein, A. and Podolsky, B. and Rosen, N.},
  journal = {Phys. Rev.},
  volume = {47},
  issue = {10},
  pages = {777--780},
  year = {1935},
  url = {https://link.aps.org/doi/10.1103/PhysRev.47.777}
}
```
which you cite with both keys inside `main.tex`. This will 
result in the following bibliography:

[1] A. Einstein, B. Podolsky, and N. Rosen, Phys. Rev. **47**, 777 (1935).

[2] A. Einstein, B. Podolsky, and N. Rosen, Phys. Rev. **47**, 777 (1935).

This package can be used to automatically replace `\cite{Einstein1935}` with `\cite{PhysRev.47.777}` in your `main.tex` 
file and remove entry `@article{Einstein1935` from your 
`bibliography.bib` file by running the following code:

```
from bibtex_duplicate_remover import ReplaceCiteKeys, RemoveDuplicatesInBibfile

ReplaceCiteKeys(bibliography.bib, main.tex)
RemoveDuplicatesInBibfile(bibliography.bib)
```
The package is compatible with nested keys such as `\cite{Einstein1901, Einstein1935, Einstein1904}` but replacing only the necessary key. 

The above code can be easily extended to process multiple 
source files as:

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
    ReplaceCiteKeys('bibliography.bib', file)
RemoveDuplicatesInBibfile('bibliography.bib')
```

In case you do not want to replace the `.bib` and `.tex` files, the functions `RemoveDuplicatesInBibfile` and `ReplaceCiteKeys` accept an optional variable `fileout` to write to:

```
ReplaceCiteKeys('bibliography.bib', 'main.tex', 'main-2.tex')
RemoveDuplicatesInBibfile('bibliography.bib', 'bibliography-2.bib')
```

### Installation
The package can be either installed as a standalone package using pip

``` pip install . ```

or one can also copy the folder `bibtex_duplicate_remover` to where your LaTeX project.

### Technical
The way the code works is by traversing the entries inside the `.bib` file and collect all duplicate `url = ` entries. One entry is kept and all `\cite{...}` keys are replaced accordingly. 

### License

bibtex_duplicate_remover is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
