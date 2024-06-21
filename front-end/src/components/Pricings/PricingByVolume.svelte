<script>
  // Imports des stores nécessaires
  import PopupPricing from "../PopupPricing.svelte";
  import PopupCalculVolume from "../PopupCalculVolume.svelte";
  import { pricingDataStore } from "../../stores/pricingDataStore.js";
  import { createEventDispatcher } from "svelte";
  import { writable } from "svelte/store";

  export let valueMax = 0;
const dispatch = createEventDispatcher();

function getVolumeMax(newVolumeMax) {
  valueMax = newVolumeMax;
  updateVolumeMax(newVolumeMax); // Appeler la fonction updatePoidsMax
  dispatch('valueMaxChange', valueMax); // Émettre l'événement avec la nouvelle valeur
}
  let valueInterm = 0;
  let volumeMaxEntered = false;
  let volumePaliers = [];
  let palierMin = "";
  let palierMax = "";
  let title = "";
  let isPricingPopupOpen = false;
  let isCalculVolumePopupOpen = false;
  let erreurMessage = "";
  let firstPalierMax;

  
function openCalculVolumePopup() {
    isCalculVolumePopupOpen = true;
    title = "Calculer le volume";
  }
  function updateVolumeMax(newVolumeMax) {
    valueMax = newVolumeMax;
    volumeMaxEntered = true;
    volumePaliers = [];
    console.log("New valueMax", newVolumeMax, "ancien", valueMax);
    console.log("Paliers after reset:", volumePaliers);
  }

  $: if (volumeMaxEntered) {
  pricingDataStore.update(data => ({ ...data, pricingByVolume: valueMax }));
  console.log("Mise à jour des volumePaliers effectuée.");
}
  // $: volumePaliers = $volumePaliersStore;
</script>

<main>
  <div class="choicePricingOptions bg-white">
    <div class="colorTopAnnonce"></div>
    
    <div class="informationsPricing">
      <div class="infoMax">
        <div class="infoMaxEtage1">
          <button
          class="text-primary bg-white border-0 fs-5 fst-italic fontSecondary"
          on:click={openCalculVolumePopup}
        >
          ** calculer le volume
        </button>   
        {#if isCalculVolumePopupOpen}
          <div class="overlay"></div>
          <PopupCalculVolume
            isOpen={isCalculVolumePopupOpen}
            onClose={() => (isCalculVolumePopupOpen = false)}
            {title}
            fieldName="NomDuChamp"
            on:volumeAdded={event => updateVolumeMax(event.detail)}
            {erreurMessage}
          />
          
        {/if}     
        </div>
        <div class="infoMaxEtage2">
        <div class="textPalier text-darkPrimary fw-bold fs-3 fontSecondary">
          Volume Max :
        </div>
        <div class="inputPalier text-primary fs-5 fontSecondary">
          <input
            type="number"
            class="inputPrix fw-normal text-primary fontSecondary"
            placeholder="Volume maximum"
            bind:value={valueMax}
            on:change={getVolumeMax(valueMax)}
            required
          />
        </div>
      </div>
      </div>
    </div>
  </div>
</main>

<style>
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* Opacité réduite */
    z-index: 999; /* Assure que la superposition est au-dessus de tout */
  }
  .choicePricingOptions {
    padding: 30px 40px;
    border-radius: 40px;
    display: flex;
    flex-direction: column;
  }

  .informationsPricing {
    display: flex;
    flex-direction: column;
    gap: 30px;
  }
  .infoMax {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 10px;
  }
  .infoMaxEtage1 {
    display: flex;
    justify-content: flex-end;
  }
  .infoMaxEtage2{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .inputPalier {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
  }
  .inputPalier input {
    padding: 0.5rem 0.2rem;
    border-radius: 20px;
    border: 2px solid #b6b3b3;
    box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.25);
    text-align: center; /* Centrer le contenu */
  }
  .inputPalier input::placeholder {
    text-align: center;
  }
  .inputPalier input:focus {
    border: 2px solid transparent;
    outline: 3px solid #4FE1F9;
  }
  .colorTopAnnonce {
    height: 0;
  }
  /* Responsive Styles for Component 1 */
@media (max-width: 1200px) {
  .choicePricingOptions {
    padding: 20px 30px;
  }

  .infoMaxEtage1,
  .infoMaxEtage2 {
    flex-direction: column;
    align-items: flex-start;
  }

  .inputPalier {
    flex-direction: column;
    gap: 5px;
  }
}

@media (max-width: 768px) {
  .choicePricingOptions {
    padding: 15px 20px;
    border-radius: 20px;
  }

  .informationsPricing {
    gap: 20px;
  }

  .infoMax {
    gap: 15px;
  }

  .textPalier {
    font-size: 1.2rem;
  }

  .inputPalier input {
    padding: 0.4rem 0.1rem;
    border-radius: 15px;
  }
}

@media (max-width: 480px) {
  .choicePricingOptions {
    padding: 10px 15px;
    border-radius: 10px;
  }

  .infoMaxEtage1 button {
    font-size: 0.9rem;
  }

  .textPalier {
    font-size: 1rem;
  }

  .inputPalier input {
    padding: 0.3rem 0.1rem;
    border-radius: 10px;
  }
}

</style>
