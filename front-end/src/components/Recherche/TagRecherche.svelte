<!-- Tag.svelte -->
<script>
  import { createEventDispatcher } from "svelte";
  import { alreadySelectedConditions } from "../../stores/alreadySelectedConditions.js"; // Import du store

  const dispatch = createEventDispatcher();

  export let name;
  export let isSelected;


  function handleClick() {
    isSelected = !isSelected; // Inverser l'état actuel du tag
    dispatch("tagClick", { name, isSelected }); // Émettre un événement avec le nouvel état du tag
  }
</script>

<main>
  <button
    class="{isSelected ? 'selected conditionTagBtn' : 'conditionTagBtn'} fontSecondary"
    on:click={handleClick}
  >
    <p class="m-0">{name}</p>
  </button>
</main>

<style>
   .conditionTagBtn {
    transition: 0.2s ease;
  }
  .selected {
 
    border: 3px solid transparent !important;
    box-shadow: 0 3px 3px 1px rgba(0, 0, 0, 0.25) !important;
    background-color: #21A5C3 !important; /* Couleur de fond par défaut */
    color: white !important;
  }
  .selected:hover {
    background-color: #4FE1F9 !important;
  }

  .conditionTagBtn {
    padding: 0.75rem 1rem;
    font-size: 1.1rem;
    border-radius: 20px;
    text-align: center; /* Centrer le contenu */
    box-shadow: 0px 5px 0px 0px #21A5C3;
    border: 3px solid #21A5C3;
    background-color: white; 
    color: #21A5C3; 
  }
  .conditionTagBtn:hover {
    box-shadow: 0px 5px 0px 0px #4FE1F9;
    border: 3px solid #4FE1F9;
  }
</style>
