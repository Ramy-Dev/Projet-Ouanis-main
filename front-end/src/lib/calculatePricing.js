export function calculatePricing(category, max, paliers) {
  let poidsPaliers = [];
  let prixPaliers = [];

  switch (category) {
    case 'weight':
      // Génération des paliers en fonction du poids maximum entré
      poidsPaliers.push(0); // Premier palier de 0 à max
      let poidsRestant = max;
      let palierCount = paliers.length;

      // Générer les paliers à partir des données entrées par l'utilisateur
      for (let i = 0; i < palierCount; i++) {
        poidsPaliers.push(paliers[i].max);
      }

      // Calcul des prix en fonction des paliers de poids
      for (let i = 1; i < poidsPaliers.length; i++) {
        const poidsPrecedent = poidsPaliers[i - 1];
        const poidsActuel = poidsPaliers[i];
        const poidsIntervalle = poidsActuel - poidsPrecedent;
        // Logique pour calculer le prix en fonction de l'intervalle de poids
        prixPaliers.push(poidsIntervalle * 2); // Exemple basique : 2 euros par kilo
      }

      break;

    default:
      break;
  }

  return {
    poidsPaliers,
    prixPaliers
  };
}
