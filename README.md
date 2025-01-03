# **KHRAL - Outils de Tests de Vulnérabilités Web**

KHRAL est un outil conçu pour détecter, tester et exploiter certaines des vulnérabilités web les plus courantes, en se basant sur les directives du **Top 10 OWASP**. Ce projet vise à fournir aux utilisateurs des outils personnalisés pour les tests d'intrusion, tout en offrant une meilleure compréhension des méthodologies de pentesting.

Grâce à **KHRAL**, les testeurs de sécurité et développeurs peuvent identifier les failles de sécurité présentes dans leurs applications web et améliorer la robustesse de leur code face aux attaques.

---

## **Fonctionnalités**

### 🔍 Tests de vulnérabilités OWASP 
1. **Injection SQL** : 
   - Identifie les points vulnérables aux injections SQL en analysant les paramètres d'URL ou de requête.  
   - Exploitation basique avec des chaînes SQL malveillantes.

2. **Cross-Site Scripting (XSS)** :
   - Détecte les failles XSS dans les champs de saisie utilisateur et les paramètres d'URL.
   - Teste automatiquement l'exécution de scripts JavaScript malveillants.

3. **Broken Access Control** *(En développement)* :
   - Analyse les restrictions d'accès inadéquates ou contournées.
   - Teste les autorisations manquantes ou mal configurées.

4. **Scanner Réseau** *(En développement)* :
   - Permet de cartographier les serveurs web et services actifs.
   - Identifie les points d'entrée potentiels pour d'autres tests.

---

### 🖥️ Interface Graphique Moderne

- **Navigation intuitive** : 
  - Interface utilisateur ergonomique développée avec **CustomTkinter**, permettant une navigation fluide entre les outils.
  - Possibilité de passer rapidement d'un test à un autre grâce à une interface modulaire et réactive.

- **Visualisation des résultats** : 
  - Retour clair des résultats des tests.
  - Messages détaillés en cas de succès ou d'échec des attaques simulées.

---

## **Technologies Utilisées**

- **Langage principal** : Python 3.x
- **Framework UI** : [CustomTkinter](https://customtkinter.tomschimansky.com/)
- **Bibliothèques complémentaires** :
  - `requests` : Gestion des requêtes HTTP pour les tests d'attaques.
  - `concurrent.futures` : Implémentation multithread pour accélérer les tests.
  - `itertools` : Gestion des itérations et des données.
- **Documentation** : Conforme aux standards OWASP et aux méthodologies de pentesting.

---

## **Installation**

1. **Cloner le projet** :  
   ```bash
   git clone https://github.com/votre-repo/KHRAL.git
   cd KHRAL

### Prérequis

Avant de commencer, assurez-vous d'avoir installé les outils suivants sur votre machine :

- **Python 3.x** : Ce projet utilise Python pour implémenter les outils de tests.
- **Bibliothèques Python** :
  - `requests` : pour effectuer des requêtes HTTP et tester les vulnérabilités.
  - `tkinter` : pour l'interface graphique.
  - `Pillow` : pour afficher des images dans l'interface.


## Installation

1. **Clone ce repository sur ta machine** :

```bash
git clone https://github.com/votre-utilisateur/KHRAL.git
cd KHRAL
```

2. **Crée un environnement virtuel et activez-le (optionnel mais recommandé)** :
bash

```bash
python3 -m venv env
source env/bin/activate  # Sur macOS/Linux
env\Scripts\activate     # Sur Windows
```

3. Installez les dépendances :
Copier le code
```bash
pip install -r requirements.txt
```

4. Utilisation
Pour lancer l'application et accéder aux outils de tests, exécutez le fichier principal appli.py :

Copier le code
```bash
python appli.py
```
Cela ouvrira une fenêtre graphique avec les différents outils de tests de vulnérabilités.

## Contribuer

Si vous souhaitez contribuer à ce projet, voici les étapes à suivre :

1. **Fork le repository**.
2. **Crée une branche pour tes nouvelles fonctionnalités** :
```bash
git checkout -b feature/nom_de_fonctionnalité
```
3. **Commite tes changements :**
Copier le code
```bash
git commit -am 'Ajout d'une nouvelle fonctionnalité'
```
4. **Pousse sur la branche :**
Copier le code
```bash
git push origin feature/nom_de_fonctionnalité
```
5. **Ouvre une Pull Request sur le repository principal.**
## Auteurs
- Karim ABDALLAH - @abdhkarim

## Liens utiles
- [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/v42/)
- [OWASP Top 10](https://owasp.org/Top10/fr/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [NIST CVE](https://nvd.nist.gov/vuln)
