# SEO — Voisin D'abord

## Priorité 1 : Schema.org LocalBusiness (impact fort, rapide à faire)

Ajouter ce bloc dans le `<head>` de `index.html`. C'est le levier SEO local le plus impactant pour apparaître dans les résultats Google Maps et "services proches de moi".

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Voisin D'abord",
  "description": "Services à domicile dans les Yvelines : baby-sitting, pet-sitting, jardinage, nettoyage Karcher, voiture et gouttières.",
  "url": "https://voisindabord.fr",
  "email": "contact@voisindabord.fr",
  "areaServed": {
    "@type": "AdministrativeArea",
    "name": "Yvelines (78)"
  },
  "serviceType": ["Baby-sitting", "Pet-sitting", "Jardinage", "Nettoyage Karcher", "Nettoyage voiture", "Nettoyage gouttières"],
  "priceRange": "€"
}
</script>
```
→ Compléter avec `"telephone"` et `"address"` dès que le SIRET est obtenu.

## Priorité 2 : Open Graph / partage social

Sans ces balises, un partage WhatsApp ou Facebook n'affiche aucune prévisualisation. À ajouter dans le `<head>` de chaque page :

```html
<meta property="og:title" content="Voisin D'abord — Services à domicile, Yvelines (78)" />
<meta property="og:description" content="Baby-sitting, jardinage, nettoyage Karcher… Un jeune sérieux se déplace chez vous dans les Yvelines." />
<meta property="og:image" content="https://voisindabord.fr/img-jardinage.jpg" />
<meta property="og:url" content="https://voisindabord.fr" />
<meta property="og:type" content="website" />
```

## Priorité 3 : Balises title — renforcer la géolocalisation

Les titres actuels sont corrects mais peuvent être plus précis pour les recherches locales :

| Page          | Titre actuel                                   | Titre suggéré                                              |
|---------------|------------------------------------------------|------------------------------------------------------------|
| index.html    | Voisin D'abord — Services à domicile, Yvelines | Services à domicile Yvelines 78 — Voisin D'abord           |
| services.html | Services — Voisin D'abord · Yvelines (78)      | Baby-sitting, jardinage, Karcher — Yvelines · Voisin D'abord |
| contact.html  | Contact — Voisin D'abord · Yvelines (78)       | Demander un devis — Services à domicile 78 · Voisin D'abord |

## Priorité 4 : Images — attributs `width` et `height`

Google pénalise les pages avec Cumulative Layout Shift élevé. Toutes les images manquent de dimensions déclarées. Exemple à appliquer sur chaque `<img>` :

```html
<!-- Avant -->
<img src="img-jardinage.jpg" alt="Jardin soigné dans les Yvelines" loading="eager" />

<!-- Après -->
<img src="img-jardinage.jpg" alt="Jardin soigné dans les Yvelines" loading="eager" width="800" height="1000" />
```

## À faire plus tard (non bloquant au lancement)

- **`/sitemap.xml`** : générer un sitemap simple avec les 5 URLs. GitHub Pages peut servir un fichier statique.
- **`/robots.txt`** : fichier minimal `User-agent: * / Allow: /`.
- **Google Search Console** : vérifier le site dès la mise en ligne pour indexation et suivi des requêtes.
- **Google Business Profile** : créer une fiche Google Maps pour "Voisin D'abord" (gratuit, essentiel pour le SEO local).
- **Mentions légales** : compléter avec le SIRET dès immatriculation — obligatoire légalement, et un signal de confiance pour Google.

## État actuel des meta descriptions

Toutes les pages ont une meta description. Elles sont correctes et dans la limite de 155 caractères. Rien à changer pour le lancement.
