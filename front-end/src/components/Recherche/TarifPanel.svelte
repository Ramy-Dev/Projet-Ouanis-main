<script>
    export let visible = false;
    export let poids = "";
    export let quantite = "";
    export let volume = "";
  
    function handleAdd(type) {
      if (type === 'poids') {
        console.log(`Poids ajouté: ${poids} kg`);
        poids = ""; // Reset the input field
      } else if (type === 'quantite') {
        console.log(`Quantité ajoutée: ${quantite}`);
        quantite = ""; // Reset the input field
      } else if (type === 'volume') {
        console.log(`Volume ajouté: ${volume} m³`);
        volume = ""; // Reset the input field
      }
    }
  </script>
  
  <main>
    <div class="tarifContainer fontSecondary" style="display: {visible ? 'flex' : 'none'}">
        <div class="textTagPanel fs-5 fontSecondary">Sélectionnez des tarifs</div>

    <div class="sectionInputs">
        <div class="containerInputs">
        <p class="textPreInput">Poids</p>
      <div class="inputGroup">
        <input bind:value={poids} placeholder="poids kg" type="number" />
        <button on:click={() => handleAdd('poids')}>add</button>
      </div>
    </div>
      <div class="containerInputs">
        <p class="textPreInput">Volume</p>
      <div class="inputGroup">
        <input bind:value={volume} placeholder="volume m³" type="number" />
        <button on:click={() => handleAdd('volume')}>add</button>
      </div>
    </div>

      <div class="note">*calculez votre volume</div>
    </div>
    </div>
  </main>
  
  <style>
    .tarifContainer {
        border: 0;
    position: absolute;
    top: 100%; /* Position below the input */
    left: 0;
    width: 450px; /* Full width of the parent tarifContainer */
    height: 400px;
    background: white;
    box-shadow: 0 4px 30px 0 rgba(0, 0, 0, 0.29);
    z-index: 1000;
    display: flex;
    flex-direction: column;
    border-radius: 20px;
    gap: 10px;
    overflow-y: auto; /* Add this line */
    padding: 0px 30px;
    }

    .textTagPanel {
    position: sticky;
    top: 0;
    padding: 20px 0px;
    color: #434343;
    background-color: white;
    z-index: 1; /* Ensure it stays on top */
  }
  .sectionInputs {
    display :flex;
    flex-direction: column;
    gap: 20px;
  }
  .conatinerInputs {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .textPreInput {
        font-size: 1.2rem;
        color: #1F1F1F;
        opacity: 0.7;
    }
    .inputGroup {
      display: flex;
      align-items: center;
      gap: 30px;
    }
    input {
      flex: 1;
    padding: 0.75rem 1rem;
    font-size: 1.1rem;
    border-radius: 16px;
    text-align: center; /* Centrer le contenu */
    border: 3px solid #21A5C3;
    background-color: white; 
    color: #21A5C3; 
    }
    input::placeholder {
      color: #21A5C3;
      font-size: 1.2rem;
    }
    input:focus {
      outline: none;
    }
    button {
        flex: 1;

padding: 0.75rem 1rem;
font-size: 1.1rem;
border-radius: 16px;
text-align: center; /* Centrer le contenu */
border: 3px solid #4FE1F9;
background-color: #4FE1F9; 
color: white; 
    }
    button:hover {
      background-color: #4FE1F9;
    }
    .note {
      font-size: 1em;
      margin-left: 5px;
      color: #4FE1F9;
    }
  </style>
  