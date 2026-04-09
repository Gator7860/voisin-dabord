# Audit UI/UX — Voisin D'abord MVP

## Problèmes critiques (bloquants avant mise en ligne)

### 1. Navigation mobile cassée
**Pages concernées : toutes**
Le menu `.nav-links` est masqué (`display: none`) sous 768px via un simple `@media`, mais **aucun hamburger n'est implémenté** dans les fichiers HTML. L'utilisateur mobile n'a donc aucune navigation — uniquement le bouton CTA "Demander un devis".
→ Ajouter un menu hamburger minimal, ou au minimum exposer les liens essentiels (Accueil, Services, Contact) en version mobile.

### 2. Aucune preuve sociale (zéro avis, zéro témoignage)
C'est le problème de conversion le plus sérieux. Le service est proposé par un inconnu qui entre chez les gens. Sans un seul avis client, la barrière de confiance est très haute.
→ Même 2 ou 3 témoignages inventoriés dès les premières prestations seraient décisifs. Prévoir l'emplacement maintenant.

### 3. Pas de numéro de téléphone
La page contact affiche uniquement l'e-mail. Pour la cible (familles, adultes 35-60 ans en zone péri-urbaine), l'absence de téléphone est un frein fort.
→ Ajouter un numéro, même si le callback se fait à l'initiative du prestataire.

### 4. Pas de favicon
Le site n'a aucun favicon. Basique mais visible immédiatement dans un onglet navigateur.

### 5. Formulaire : aucune gestion d'erreur
`contact.html` ligne 313 : le `fetch` vers Formspree gère uniquement `response.ok`. Si le réseau échoue ou si Formspree renvoie une erreur, l'utilisateur voit... rien. Le formulaire ne se cache pas, aucun message d'erreur ne s'affiche.
→ Ajouter un bloc erreur affiché en cas de `!response.ok` ou d'exception dans le catch.

---

## Problèmes importants (améliorer rapidement)

### 6. Pas de CTA WhatsApp
Pour des services locaux en France, WhatsApp est le canal de contact dominant. Un bouton flottant `wa.me/33XXXXXXXXX` multiplierait les conversions mobiles.

### 7. Images sans dimensions `width`/`height`
Aucune image ne déclare ses dimensions. Cela cause des Layout Shifts (CLS) mesurables dans les Core Web Vitals.
→ Ajouter `width` et `height` sur toutes les balises `<img>`.

### 8. Section hero : les "stats" ne sont pas de la preuve sociale
Les trois chiffres (6, 24h, 78) sont des caractéristiques produit, pas de la réassurance. Ce slot serait plus puissant avec un premier avis client ou un compteur de prestations réalisées.

### 9. Carte Leaflet sans fallback
`index.html` — si JavaScript est désactivé ou si le CDN Leaflet est indisponible, le `<div id="map">` reste vide et invisible. Ajouter un `<noscript>` ou un texte de fallback dans le div.

### 10. `style.css` orphelin
`style.css` utilise des variables et polices différentes (Cormorant Garamond, `--texte`, `--or`) et n'est référencé par aucune page HTML. Il crée de la confusion lors des modifications. À supprimer ou documenter comme archive.

---

## Points positifs à conserver

- Ton authentique (première personne, direct, honnête) — ne pas le "corporatiser"
- La mise en avant du crédit d'impôt 50 % est bien placée et répétée (homepage + services + contact) — garder cette logique
- Carte Leaflet interactive sur la homepage : différenciante et utile pour la zone géo
- Design cohérent sur toutes les pages (palette, typographie, espacements) malgré l'absence de fichier CSS partagé
- Formspree avec honeypot (`_gotcha`) : bonne pratique anti-spam déjà en place
