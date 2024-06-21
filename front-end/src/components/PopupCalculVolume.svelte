<script>
  import { createEventDispatcher } from "svelte";
  import Palier from "../components/Palier.svelte";
  import { paliersStore } from "../stores/paliersStore.js";

  const dispatch = createEventDispatcher();

  export let isOpen = false;
  export let onClose = () => {};
  export let title = "";
  export let fieldName = "";

  let lenght;
  let width;
  let height;
  $: volume = lenght * width * height ? lenght * width * height : 0;

  function addVolumeMax() {
    dispatch("volumeAdded", volume.toFixed(2));
    onClose();
  }
  // Fonction pour gérer la fermeture du popup
  function handleOverlayClick(event) {
    if (event.target.classList.contains("overlay")) {
      onClose();
    }
  }
</script>

<main>
  {#if isOpen}
    <div class="overlay" on:click={handleOverlayClick}>
      <div class="popup">
        <div class="popup-header">
          <h2 class="fw-bold fs">{title}</h2>
          <button
            class="border-0 text-primary fs-2 fw-bold fontSecondary"
            on:click={onClose}> <lord-icon
            class="animated-cross"
            src="https://cdn.lordicon.com/zxvuvcnc.json"
            colors="primary:#4FE1F9"
            style="background-color: none;"
            trigger="hover">
        </lord-icon></button
          >
        </div>
        <div class="popup-content fs-4 fontSecondary">
          <div class="blocsCalcul">
            <div class="bloc">
              <p>Lenght</p>
              <input
                type="number"
                class="notextPricing fontSecondary"
                bind:value={lenght}
                placeholder="mètres"
              />
            </div>
            <div class="bloc">
              <p>Width</p>
              <input
                type="number"
                class="notextPricing fontSecondary"
                bind:value={width}
                placeholder="mètres"
              />
            </div>
            <div class="bloc">
              <p>Height</p>
              <input
                type="number"
                class="notextPricing fontSecondary"
                bind:value={height}
                placeholder="mètres"
              />
            </div>
          </div>
          <div class="bottomPopup">
            <div class="bloc">
              <p>Volume</p>
              <div class="displayVolume notextPricing fontSecondary">
                {volume.toFixed(2)} m³
              </div>
            </div>

            <div class="ajoutBtn">
              <button
                class="notextPricing bg-light text-white fs-5 fontSecondary"
                on:click={addVolumeMax}
              >
                Add
              </button>
            </div>
          </div>
        </div>
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
    flex-direction: column;
    gap: 20px;
  }
  p {
    margin-bottom: 0 !important;
  }
  input {
    /* Styles pour le champ de saisie */
    width: 70%;
    appearance: none;
    border-radius: 10px;
    border: 3px solid #4FE1F9;
    color: #21A5C3;
  }
  input:focus {
    outline: none;
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
  .blocsCalcul {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .displayVolume {
    width: 300px;
    appearance: none;
    border-radius: 10px;
    border: 3px solid #4FE1F9;
    color: #21A5C3;
  }
  .bottomPopup {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
  }
  .animated-cross {
width: 40px;
height: 40px;
  }
</style>
