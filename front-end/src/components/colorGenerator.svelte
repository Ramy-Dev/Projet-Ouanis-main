<script>
    import { onMount } from 'svelte';
    import { getRandomColor } from '../lib/functions/randomColor.js'; // Importer la fonction de génération de couleurs aléatoires
  
    // Fonction exécutée après le rendu du composant
    onMount(() => {
      const cards = document.querySelectorAll('.cardAnnonce');
      cards.forEach(card => {
        const cardColor = getRandomColor();
        const url = `/details?color=${encodeURIComponent(cardColor)}`;
        card.setAttribute('href', url);
      });
    });
  </script>