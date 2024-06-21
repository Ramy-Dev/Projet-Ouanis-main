<script>
    export let poidsMin;
    export let poidsMax;
    export let onDelete;

    console.log("dans Palier.svelte", poidsMin, poidsMax)
  </script>
  
  <main>
  <div class="palierPricing">
    <div class="textPalier text-darkPrimary fw-bold fs-3 fontSecondary">
      {poidsMin} Kg - {poidsMax} Kg
    </div>
    <div class="inputPalier">
      <button class="deleteButton" on:click={onDelete}>x</button>

    </div>
  </div>
</main>
  <style>
   
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
    border: 2px solid transparent ;
    outline: 3px solid #5a02d4 ;
  }
  .palierPricing {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  </style>