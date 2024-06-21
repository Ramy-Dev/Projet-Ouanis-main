<script>
    import { onMount } from "svelte";
  
    // Define your data
    const dataTransport = {
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
  };// Données des aéroports et ports
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

  
    let firstInput;
    let secondInput;
  
    // Function to update second input options based on the first input selection
    function updateSecondInput() {
        const selectedValue = firstInput.value;
        let data;
  
        if (airportsAlgeria.includes(selectedValue)) {
            data = internationalFlights;
        } else if (airportsFrance.includes(selectedValue)) {
            data = domesticFlightsFrance;
        } else if (portsAlgeria.includes(selectedValue)) {
            data = domesticSeaRoutesAlgeria;
        } else if (portsFrance.includes(selectedValue)) {
            data = internationalSeaRoutes;
        }
  
        secondInput.innerHTML = "";
        (data[selectedValue] || []).forEach(option => {
            const opt = document.createElement('option');
            opt.value = option;
            opt.innerHTML = option;
            secondInput.appendChild(opt);
        });
    }
  
    onMount(() => {
        firstInput = document.getElementById('firstInput');
        secondInput = document.getElementById('secondInput');
        firstInput.addEventListener('change', updateSecondInput);
    });
  </script>
  
  <!-- Define your HTML structure -->
  <div>
    <select id="firstInput">
      <option value="">Select...</option>
      {#each [...airportsAlgeria, ...airportsFrance, ...portsAlgeria, ...portsFrance] as option}
        <option value={option}>{option}</option>
      {/each}
    </select>
    <select id="secondInput">
      <option value="">Select...</option>
    </select>
  </div>
  