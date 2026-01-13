Python

PROGRAMME_SENEGAL = {
    "Élémentaire": {
        "CM2": {
            "Histoire": ["L'Empire du Djolof", "La colonisation au Sénégal", "La résistance d'Aline Sitoé Diatta"],
            "Géographie": ["Le relief du Sénégal", "Le climat et la végétation", "L'hydrographie (Fleuve Sénégal, Gambie, Casamance)"],
            "Sciences": ["Le corps humain : la respiration", "La protection de l'environnement : le péril plastique"]
        },
        "CM1": {
            "Histoire": ["Les empires du Ghana et du Mali", "L'islamisation de l'Afrique de l'Ouest"],
            "Géographie": ["Les activités économiques : la pêche et l'agriculture"]
        }
    },
    "Moyen": {
        "3ème": {
            "Histoire": ["La Seconde Guerre mondiale et l'Afrique", "La décolonisation et l'accession à l'indépendance du Sénégal"],
            "Français": ["L'étude de l'œuvre : 'Une si longue lettre' de Mariama Bâ"]
        }
    }
}
🛠️ Comment utiliser ce dictionnaire avec ton client OpenAI ?
Maintenant que tu as ton système de prompt (défini précédemment) et ton référentiel, l'interaction devient ultra-fluide pour l'utilisateur :

L'utilisateur sélectionne : "Élémentaire" -> "CM2" -> "Histoire" -> "L'Empire du Djolof".

IA FLUX construit le prompt final :

"Génère une fiche de leçon complète sur L'Empire du Djolof pour le niveau CM2 en suivant le programme sénégalais."

Ton Proxy envoie la requête : Sécurisé par ton token HF/OpenAI, il renvoie un contenu structuré, prêt à être transformé en PDF.
