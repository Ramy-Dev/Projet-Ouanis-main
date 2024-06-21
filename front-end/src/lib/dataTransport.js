// Données des aéroports et ports
const airportsAlgeria = [
    "Alger (Houari Boumediene)",
    "Oran (Ahmed Ben Bella)",
    "Constantine (Mohamed Boudiaf)",
    "Béjaïa (Abane Ramdane)",
    "Annaba (Rabah Bitat)",
    "Tlemcen (Zenata – Messali El Hadj)"
];

const airportsFrance = [
    "Paris (Charles de Gaulle)",
    "Paris (Orly)",
    "Marseille",
    "Lyon",
    "Nice",
    "Toulouse",
    "Bordeaux"
];

const portsAlgeria = [
    "Port d'Alger",
    "Port d'Oran",
    "Port de Béjaïa",
    "Port de Skikda",
    "Port d'Annaba",
    "Port de Mostaganem",
    "Port de Ghazaouet"
];

const portsFrance = [
    "Port de Marseille",
    "Port de Sète",
    "Port de Toulon",
    "Port de Nice"
];

// Itinéraires aériens internationaux entre l'Algérie et la France
const internationalFlights = {
    "Alger (Houari Boumediene)": ["Paris (Charles de Gaulle)", "Paris (Orly)", "Marseille", "Lyon", "Nice", "Toulouse", "Bordeaux"],
    "Oran (Ahmed Ben Bella)": ["Paris (Charles de Gaulle)", "Paris (Orly)", "Marseille", "Lyon", "Nice", "Toulouse"],
    "Constantine (Mohamed Boudiaf)": ["Paris (Charles de Gaulle)", "Marseille"],
    "Béjaïa (Abane Ramdane)": ["Paris (Charles de Gaulle)"],
    "Annaba (Rabah Bitat)": ["Paris (Charles de Gaulle)", "Marseille"],
    "Tlemcen (Zenata – Messali El Hadj)": ["Paris (Charles de Gaulle)", "Marseille"]
};

// Itinéraires aériens internes en Algérie
const domesticFlightsAlgeria = {
    "Alger (Houari Boumediene)": ["Oran (Ahmed Ben Bella)", "Constantine (Mohamed Boudiaf)", "Béjaïa (Abane Ramdane)", "Annaba (Rabah Bitat)", "Tlemcen (Zenata – Messali El Hadj)"],
    "Oran (Ahmed Ben Bella)": ["Constantine (Mohamed Boudiaf)", "Annaba (Rabah Bitat)", "Tlemcen (Zenata – Messali El Hadj)"],
    "Constantine (Mohamed Boudiaf)": ["Annaba (Rabah Bitat)"]
};

// Itinéraires aériens internes en France
const domesticFlightsFrance = {
    "Paris (Charles de Gaulle)": ["Marseille", "Lyon", "Nice", "Toulouse", "Bordeaux"],
    "Paris (Orly)": ["Marseille", "Lyon", "Nice", "Toulouse", "Bordeaux"],
    "Marseille": ["Lyon", "Nice", "Toulouse", "Bordeaux"],
    "Lyon": ["Nice", "Toulouse", "Bordeaux"],
    "Nice": ["Toulouse", "Bordeaux"],
    "Toulouse": ["Bordeaux"]
};

// Itinéraires maritimes internationaux entre l'Algérie et la France
const internationalSeaRoutes = {
    "Port d'Alger": ["Port de Marseille", "Port de Sète"],
    "Port d'Oran": ["Port de Marseille", "Port de Sète"],
    "Port de Béjaïa": ["Port de Marseille"],
    "Port de Skikda": ["Port de Marseille"],
    "Port d'Annaba": ["Port de Marseille"],
    "Port de Mostaganem": ["Port de Marseille", "Port de Sète"],
    "Port de Ghazaouet": ["Port de Marseille"]
};

// Itinéraires maritimes internes en Algérie
const domesticSeaRoutesAlgeria = {
    "Port d'Alger": ["Port d'Oran", "Port de Béjaïa", "Port de Skikda", "Port d'Annaba", "Port de Mostaganem", "Port de Ghazaouet"]
};

// Fonction pour mettre à jour les options de la deuxième liste déroulante en fonction de la sélection de la première
function updateSecondInput(firstInput, secondInput, data) {
    const selectedValue = firstInput.value;
    const options = data[selectedValue] || [];
    secondInput.innerHTML = "";

    options.forEach(option => {
        const opt = document.createElement('option');
        opt.value = option;
        opt.innerHTML = option;
        secondInput.appendChild(opt);
    });
}

// Exemple d'utilisation avec des éléments HTML
document.addEventListener('DOMContentLoaded', () => {
    const firstInput = document.getElementById('firstInput');
    const secondInput = document.getElementById('secondInput');

    firstInput.addEventListener('change', () => {
        let data;
        if (airportsAlgeria.includes(firstInput.value)) {
            data = internationalFlights;
        } else if (airportsFrance.includes(firstInput.value)) {
            data = domesticFlightsFrance;
        } else if (portsAlgeria.includes(firstInput.value)) {
            data = domesticSeaRoutesAlgeria;
        } else if (portsFrance.includes(firstInput.value)) {
            data = internationalSeaRoutes;
        }
        updateSecondInput(firstInput, secondInput, data);
    });
});
// dataTransport.js
export const dataTransport = {
  airports: {
    Algeria: [
      "Aéroport Houari Boumediene (Alger)",
      "Aéroport Ahmed Ben Bella (Oran)",
      "Aéroport Mohamed Boudiaf (Constantine)",
      "Aéroport Abane Ramdane (Béjaïa)",
      "Aéroport Rabah Bitat (Annaba)",
      "Aéroport de Tlemcen (Tlemcen)",
      "Aéroport Es Sénia (Oran)"
    ],
    France: [
      "Aéroport Paris-Charles de Gaulle (Paris)",
      "Aéroport Paris-Orly (Paris)",
      "Aéroport de Marseille-Provence (Marseille)",
      "Aéroport de Lyon-Saint Exupéry (Lyon)",
      "Aéroport Nice Côte d'Azur (Nice)",
      "Aéroport de Toulouse-Blagnac (Toulouse)",
      "Aéroport de Bordeaux-Mérignac (Bordeaux)"
    ]
  },
  routes: {
    Algeria: {
      "Aéroport Houari Boumediene (Alger)": ["Aéroport Paris-Charles de Gaulle (Paris)", "Aéroport Paris-Orly (Paris)", "Aéroport de Marseille-Provence (Marseille)", "Aéroport de Lyon-Saint Exupéry (Lyon)", "Aéroport Nice Côte d'Azur (Nice)", "Aéroport de Toulouse-Blagnac (Toulouse)", "Aéroport de Bordeaux-Mérignac (Bordeaux)"],
      "Aéroport Ahmed Ben Bella (Oran)": ["Aéroport Paris-Charles de Gaulle (Paris)", "Aéroport Paris-Orly (Paris)", "Aéroport de Marseille-Provence (Marseille)", "Aéroport de Lyon-Saint Exupéry (Lyon)", "Aéroport Nice Côte d'Azur (Nice)", "Aéroport de Toulouse-Blagnac (Toulouse)"],
      "Aéroport Mohamed Boudiaf (Constantine)": ["Aéroport Paris-Charles de Gaulle (Paris)", "Aéroport Paris-Orly (Paris)", "Aéroport de Marseille-Provence (Marseille)"],
      "Aéroport Abane Ramdane (Béjaïa)": ["Aéroport Paris-Charles de Gaulle (Paris)", "Aéroport Paris-Orly (Paris)"],
      "Aéroport Rabah Bitat (Annaba)": ["Aéroport Paris-Charles de Gaulle (Paris)", "Aéroport Paris-Orly (Paris)", "Aéroport de Marseille-Provence (Marseille)"],
      "Aéroport de Tlemcen (Tlemcen)": ["Aéroport Paris-Charles de Gaulle (Paris)", "Aéroport Paris-Orly (Paris)", "Aéroport de Marseille-Provence (Marseille)"]
    },
    France: {
      "Aéroport Paris-Charles de Gaulle (Paris)": ["Aéroport Houari Boumediene (Alger)", "Aéroport Ahmed Ben Bella (Oran)", "Aéroport Mohamed Boudiaf (Constantine)", "Aéroport Abane Ramdane (Béjaïa)", "Aéroport Rabah Bitat (Annaba)", "Aéroport de Tlemcen (Tlemcen)"],
      "Aéroport Paris-Orly (Paris)": ["Aéroport Houari Boumediene (Alger)", "Aéroport Ahmed Ben Bella (Oran)", "Aéroport Mohamed Boudiaf (Constantine)", "Aéroport Abane Ramdane (Béjaïa)", "Aéroport Rabah Bitat (Annaba)", "Aéroport de Tlemcen (Tlemcen)"],
      "Aéroport de Marseille-Provence (Marseille)": ["Aéroport Houari Boumediene (Alger)", "Aéroport Ahmed Ben Bella (Oran)", "Aéroport Mohamed Boudiaf (Constantine)", "Aéroport Rabah Bitat (Annaba)", "Aéroport de Tlemcen (Tlemcen)"],
      "Aéroport de Lyon-Saint Exupéry (Lyon)": ["Aéroport Houari Boumediene (Alger)", "Aéroport Ahmed Ben Bella (Oran)"],
      "Aéroport Nice Côte d'Azur (Nice)": ["Aéroport Houari Boumediene (Alger)", "Aéroport Ahmed Ben Bella (Oran)"],
      "Aéroport de Toulouse-Blagnac (Toulouse)": ["Aéroport Houari Boumediene (Alger)", "Aéroport Ahmed Ben Bella (Oran)"],
      "Aéroport de Bordeaux-Mérignac (Bordeaux)": ["Aéroport Houari Boumediene (Alger)"]
    }
  }
};
