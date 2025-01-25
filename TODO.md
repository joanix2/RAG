# Moteur basé sur GPT

---

## Objectifs Fonctionnels

### 1. Buffer de Requêtes

- Implémenter un système de file d'attente pour gérer et prioriser les requêtes utilisateurs.
- Gérer les débordements de requêtes en cas de surcharge.

### 2. Gestion des Limites (Rate Limiting)

- Mettre en place un mécanisme pour limiter les appels par utilisateur ou système.
- Ajouter des alertes ou des réponses en cas de dépassement des quotas.

### 3. Suivi des Conversations

- Assurer la persistance des sessions et du contexte conversationnel.
- Lier chaque session utilisateur à un identifiant unique.

### 4. Gestion Multi-GPTs

- Permettre l'orchestration entre différents modèles GPT (ex. GPT-4, GPT-3.5).
- Configurer des préférences ou des routes spécifiques en fonction des types de requêtes.

### 5. Génération de Fichiers

- Ajouter des fonctionnalités pour produire des fichiers (PDF, CSV, JSON, etc.) à partir des réponses générées.
- Implémenter des templates pour les formats courants.

### 6. Calcul d'Embeddings

- Générer des embeddings pour les données utilisateurs.
- Utiliser les embeddings pour effectuer des recherches sémantiques rapides.

### 7. Ajout d'une Mémoire Sémantique

- Intégrer une mémoire persistante pour stocker et récupérer des informations clés issues des conversations.
- Utiliser un moteur vectoriel (comme Milvus) pour effectuer des recherches contextuelles basées sur les embeddings.

### 8. Function Calling

- Implémenter des appels à des fonctions externes pour exécuter des tâches spécifiques (ex. recherche d'informations, calculs, etc.).
- Définir un protocole clair pour les entrées/sorties des appels.

---

## Technologies Utilisées

### 1. Milvus

- Stockage et recherche d'embeddings.
- Gestion de la mémoire vectorielle pour les recherches sémantiques.

### 2. LangChain

- Orchestration des modèles GPT et gestion des chaînes de prompts.
- Intégration avec des outils externes pour enrichir les fonctionnalités (ex. appels d'API, recherches de connaissances).

---

## Étapes à Prioriser

### 1. Infrastructure de Base

- Définir la structure du projet et choisir un environnement (Docker, Kubernetes, etc.).
- Configurer Milvus et intégrer LangChain pour les appels GPT.

### 2. Gestion des Utilisateurs et des Sessions

- Implémenter un système de suivi des utilisateurs et de leurs sessions (via une base relationnelle ou NoSQL).

### 3. Calcul et Stockage des Embeddings

- Intégrer Milvus avec LangChain pour calculer et stocker des embeddings.
- Ajouter un mécanisme pour lier les embeddings aux conversations.

### 4. Ajout des Fonctionnalités Étendues

- Buffer de requêtes avec gestion des priorités.
- Génération de fichiers et appel des fonctions.

### 5. Tests et Optimisation

- Tester les performances sur des scénarios réels.
- Optimiser la mémoire vectorielle et la gestion des taux de requêtes.
