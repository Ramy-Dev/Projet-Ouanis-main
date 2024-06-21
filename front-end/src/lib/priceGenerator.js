// priceGenerator.js

export function generatePrices(paliers) {
  let prixPaliers = [];
  let price = 10; // Initial price

  for (let i = 0; i < paliers.length; i++) {
    const poidsPrecedent = paliers[i - 1] ? paliers[i - 1].max : 0;
    const poidsActuel = paliers[i].max;
    const poidsIntervalle = poidsActuel - poidsPrecedent;
    const prix = poidsIntervalle * price; // Calculate the price for the current palier
    prixPaliers.push(prix);
    price += 10; // Increase the price by 10 for each palier
  }

  return prixPaliers;
}