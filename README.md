# Publications de VML   

Dans ce dépôt, on trouve un fichier csv contenant une liste des publications où l'association *Vaincre les maladies lysosomales* a été citée. Il a été construit de manière semie-automatique en janvier 2020 grâce au moteur de recherche *google scholar*. On trouve également un fichier bib contenant les entrées BibTeX correspondant aux publications listées (toutes ne sont pas encore présentes).

On trouve également un fichier python permettant d'intégrer depuis les fichiers BibTeX les informations manquantes dans le fichier csv, notamment la liste des auteurs. Pour que cela fonctionne, il faut ajouter dans la colonne "bibtex" du fichier csv l'identifiant de l'entrée BibTeX.

## Plusieurs choses restent à faire

* récupérer les entrées bibtex manquantes
* repérer dans les publications où ça n'a pas été fait la raison de la référence à VML. En particulier, on souhaite avoir confirmation qu'il s'agit d'un financement. Dans ce cas, on indiquera "bourse" dans la colonne "type" du fichier csv.
* générer des statistiques d'évolution suivant les années
* croiser ces informations avec les informations de l'association en terme de soutien aux activités de recherche

## Outils

On peut utiliser avec avantage:

* [Google scholar](https://scholar.google.com/), ou [Semantic Scholar](https://www.semanticscholar.org/)
* jabref, ou un logiciel équivalent, pour éditer le fichier au format BibTeX
