<script>
  import { createEventDispatcher } from "svelte";
  import Palier from "../components/Palier.svelte";
  import { paliersStore } from "../stores/paliersStore.js";

  const dispatch = createEventDispatcher();

  export let isOpen = false;
  export let onClose = () => {};
  export let title = "";
  export let fieldName = "";
  export let valueMaxGlobal = 0;
  export let valueMin = null;
  export let valueMax = null;

  let fullVerif = false;
  let prix = null;
  let erreurMessage = "";

  // Fonction pour valider les nouveaux paliers
  function validateNewPalier() {
    erreurMessage = "";
    // Vérifier la validité des entrées
    if (valueMin === null || valueMax === null) {
      erreurMessage = "Veuillez remplir tous les champs.";
      return false;
    }
    if (valueMin >= valueMax) {
      erreurMessage = "Le poids minimum doit être inférieur au poids maximum.";
      return false;
    }

    if (valueMin < 0 || valueMax < 0) {
      erreurMessage = "Tous les champs doivent être positifs.";
      return false;
    }
    // Vérifier si le poids minimum est supérieur au maximum du palier précédent
    console.log("$paliersStore:", $paliersStore);
    console.log("valueMin:", valueMin);
    console.log("valueMax:", valueMax);
    console.log("valueMaxGlobal:", valueMaxGlobal);
    if ($paliersStore.length > 0) {
      console.log(
        "$paliersStore[$paliersStore.length - 1].valueMax:",
        $paliersStore[$paliersStore.length - 1].valueMax
      );
    }

    if (
      $paliersStore.length > 0 &&
      typeof valueMin === "number" &&
      valueMin < $paliersStore[$paliersStore.length - 1].valueMax
    ) {
      erreurMessage =
        "Le poids minimum doit être supérieur au maximum du palier précédent.";
      console.log(
        "Le poids minimum doit être supérieur au maximum du palier précédent."
      );
      return false;
    }

    if ($paliersStore.length >= 4) {
      console.log("Le nombre maximum de paliers est atteint.");
      erreurMessage = "Le nombre maximum de paliers est atteint.";
      return false; // Arrêter l'exécution si le maximum de paliers est atteint
    }
    // Vérifier si le poids maximum est valide par rapport au poids maximum global
    if (valueMax !== "et plus" && valueMax > valueMaxGlobal) {
      erreurMessage =
        "Le poids maximum ne doit pas dépasser le poids maximum global.";
      console.log(
        "Le poids maximum ne doit pas dépasser le poids maximum global."
      );
      return false;
    }

    // Autres validations nécessaires (par exemple, poids min < poids max)
    console.log(
      "Les données sont :",
      valueMin,
      valueMax,
      valueMaxGlobal,
      $paliersStore.length
    );
    return true; // Si toutes les validations passent
  }

  // Fonction pour ajouter un nouveau palier

  export function addPalier() {
    if (validateNewPalier()) {
      const valueMin =
        $paliersStore.length > 0
          ? $paliersStore[$paliersStore.length - 1].valueMax
          : 0;
      const newPalier = {
        valueMin,
        valueMax,
        prix, // Include the prix in the newPalier object
      };
      dispatch("changesSaved", { fieldName, paliersData: [newPalier] });
      onClose();
    }
  }
  function removeAllPaliers() {
    $paliersStore = [];
    dispatch("changesSaved", { fieldName, paliersData: $paliersStore }); // Pass the value of the store
    onClose(); // Fermer le popup après avoir supprimé les paliers
  }

  function handleDeletePalier(index) {
    $paliersStore.splice(index, 1);
    dispatch("changesSaved", { fieldName, paliersData: $paliersStore }); // Pass the value of the store
  }
  // Fonction pour gérer la fermeture du popup
  function handleOverlayClick(event) {
    if (event.target.classList.contains("overlay")) {
      onClose();
    }
  }
</script>

<main class="fontSecondary">
  {#if isOpen}
    <div class="overlay" on:click={handleOverlayClick}>
      <div class="popup">
        <div class="popup-header">
          <h2 class="fw-bold fs">{title}</h2>
          <button
            class="border-0 text-primary fs-2 fw-bold fontSecondary"
            on:click={onClose}>
            <lord-icon
            class="animated-cross"
            src="https://cdn.lordicon.com/zxvuvcnc.json"
            colors="primary:#4FE1F9"
            style="background-color: white; border-radius:50%;"
            trigger="hover">
          </lord-icon>
            </button
          >
        </div>
        <div class="popup-content fs-4 fontSecondary">
          <p>De</p>
          <div class="displayMinValue notextPricing fontSecondary">
            {valueMin}
        </div>
          <p>à</p>
          <input
            type="number"
            class="notextPricing fontSecondary"
            bind:value={valueMax}
          />
           {#if fieldName === "weight"}
            <p>kg</p>
             {:else if fieldName === "volume"}
            <p>m³</p>
           {/if}
          <button
            class="notextPricing bg-light text-white fs-5 fontSecondary"
            on:click={addPalier}>Add</button
          >
        </div>
        {#if erreurMessage}
          <p class="erreurMessage text-primary fs-5 fw-bold fontSecondary">
            {erreurMessage}
          </p>
        {/if}
      </div>
    </div>
  {/if}
</main>

<style>
  /* Styles CSS pour le popup */
  .overlay {
    /* Styles pour l'overlay */
  }

  .popup {
    display: flex;
    width: 40%;
    flex-direction: column;
    justify-content: center;
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 50px 50px 30px 50px;
    border-radius: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    z-index: 9999; /* Placer la popup au-dessus des autres éléments */
    gap: 50px;
  }

  .popup-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .popup-content {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
  }
  p {
    margin-bottom: 0 !important;
  }
  input {
    /* Styles pour le champ de saisie */
    width: 30%;
    appearance: none;
    border-radius: 10px;
    border: 3px solid #4FE1F9;
    color: #21A5C3;
  }
  button {
    /* Styles pour le bouton */
    padding: 5px;
    border-radius: 10px;
    margin-left: 30px;
    border: 3px solid #4FE1F9;
  }
  .notextPricing {
    padding: 1rem 1rem;
  }
  .displayMinValue {
    width: 30%;

        appearance: none;
        border-radius: 10px;
        border: 3px solid #4FE1F9;
        color: #21A5C3;
  }
</style>
