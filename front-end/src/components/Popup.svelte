<script>
  import { createEventDispatcher } from 'svelte';

const dispatch = createEventDispatcher();

  export let isOpen = false;
  export let onClose = () => {};
  export let newFieldValue = ""; // Déclaration de newFieldValue en tant que prop
  export let title = ""; // Autres props, comme title, si nécessaire
  export let fieldName = ""; // Champ correspondant

  let name = newFieldValue;

  function handleOverlayClick(event) {
    if (event.target.classList.contains('overlay')) {
      onClose();
    }
  }

  function saveChanges() {
    onClose();
    dispatch('changesSaved', { fieldName, newValue: newFieldValue });
  }
</script>

<main>
  {#if isOpen}
    <div class="overlay" on:click={handleOverlayClick}>
      <div class="popup">
        <div class="popup-header">
          <h2 class="fw-bold fs">{title}</h2>
        </div>
        <div class="popup-content">
          <div class="EditText">
            <p class="text-secondary fw-bold fs-5 fs">Your {fieldName}</p>
            <p class="text-secondary fw-bold fs-5 fs">New {fieldName}</p>
          </div>
          <div class="EditNew">
            <p class="fw-bold text-primary fs fs-5">{name}</p>
            <div class="input-box">
              <input class="fs fs-5" bind:value={newFieldValue} />
              <button on:click={saveChanges} class="ButtonEdit btn border-0 bg-primary text-white fs-5 fs">save</button>
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
    /* Styles pour l'en-tête de la popup */
  }

  .popup-content {
    display: flex;
    justify-content: center;
    gap: 50px;
  }

  .input-box {
    /* Styles pour la boîte (carte) contenant le champ de saisie */
    display: flex;
    justify-content: center;
    gap: 20px;
  }

  input {
    /* Styles pour le champ de saisie */
    appearance: none;
    padding: 5px;
    border-radius: 10px;
    border: 2px solid #5A02D4;
  }

  button {
    /* Styles pour le bouton */
  }

  .EditText {
    display: flex;
    flex-direction: column;
    gap: 35px;
  }
  .EditNew {
    display: flex;
    flex-direction: column;
    gap: 28px;
  }
</style>
