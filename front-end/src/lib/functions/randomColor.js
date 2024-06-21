const colors = ['#27005D', '#5A02D4', '#BFACFE', '#84BBFF', '#FFE767'];
let lastColorIndex = -1;

// Fonction pour obtenir une couleur aléatoire parmi les couleurs disponibles sans répétition immédiate
export function getRandomColor() {
    let newIndex;
    do {
        newIndex = Math.floor(Math.random() * colors.length);
    } while (newIndex === lastColorIndex); // Vérifie si la nouvelle couleur est la même que la précédente
    lastColorIndex = newIndex;
    return colors[newIndex];
}

