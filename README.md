# Publications de VML   

Dans ce dépôt, on trouve un fichier csv contenant une liste des publications où l'association *Vaincre les maladies lysosomales* a été citée. Il a été construit de manière semie-automatique en janvier 2020 grâce au moteur de recherche *google scholar*, puis traité à la main en février 2020. On trouve également un fichier bib contenant les entrées BibTeX correspondant aux publications listées (toutes ne sont pas encore présentes).

On trouve également un fichier python permettant d'intégrer depuis les fichiers BibTeX les informations manquantes dans le fichier csv, notamment la liste des auteurs. Pour que cela fonctionne, il faut ajouter dans la colonne "bibtex" du fichier csv l'identifiant de l'entrée BibTeX. En ajoutant à ce script le paramètre "--filter", on trie les colonnes dans un ordre pratique;

Enfin, un deuxième script python permet de filtrer les entrées bibtex pour ne garder que celle présentes dans le fichier csv.

## Plusieurs choses restent à faire

* repérer dans les publications où ça n'a pas été fait la raison de la référence à VML. En particulier, on souhaite avoir confirmation qu'il s'agit d'un financement. Dans ce cas, on indiquera "bourse" dans la colonne "type" du fichier csv.
* supprimer les références bibliographiques qui ne sont pas présentes dans le fichier csv
* croiser ces informations avec les informations de l'association en terme de soutien aux activités de recherche


## Outils

On peut utiliser avec avantage:

* [Google scholar](https://scholar.google.com/), ou [Semantic Scholar](https://www.semanticscholar.org/)
* jabref, ou un logiciel équivalent, pour éditer le fichier au format BibTeX
