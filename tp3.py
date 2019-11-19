### Travail Pratique 3 - Alexandre Binette

import sys
import pandas as pd
import matplotlib.pyplot as plt

#Importe le fichier au argv[1] et attrape les erreurs de filepath
try:
    file = sys.argv[1]
except (IOError, IndexError):
    error_message = """Error : sequence file missing at argv[1],
    please specify filepath"""
    print(error_message, file=sys.stderr)
    exit()

# Lis le fichier CSV et établit un RF
data = pd.read_csv(file)

# Double boucle for pour cycler entre les SNP et les génotypes
for snp in data.groupby(["snp"]):

    fa = []
    for geno in snp[1].groupby("geno"):
        # Calcule la fréquence des allèles
        fa.append(geno[1].shape[0])
        # Établit les variables propres au scatter
        x=geno[1]["x"]
        y=geno[1]["y"]
        # Dessine le scatter du geno correspondant
        plt.scatter(x,y,s=1,label=geno[0])

    # Détermine le MAF et le nombre de samples par snp
    MAF = min(fa) / sum(fa)
    nb_samples = snp[1].shape[0]

    # Établit les règles du plot et sauvegarde le fichier
    plt.xlabel("x intensity")
    plt.ylabel("y intensity")
    plt.title("{} ({:,d} samples, MAF={:.3f})".format(snp[0],nb_samples,MAF))
    plt.legend(loc="best", numpoints=1, markerscale=5)
    plt.savefig(fname="{}.png".format(snp[0]))
    #plt.show()
    plt.close()
