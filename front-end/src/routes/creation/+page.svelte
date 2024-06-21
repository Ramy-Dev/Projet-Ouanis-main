<script>
  import { onMount } from "svelte";
  import TagPopup from "../../components/TagPopup.svelte";
  import PricingByWeight from "../../components/Pricings/PricingByWeight.svelte";
  import PricingByVolume from "../../components/Pricings/PricingByVolume.svelte";
  import Dropdown from "../../components/Dropdown.svelte";
  // import { conditions } from "../../lib/tagList.js";
  import { alreadySelectedConditions } from "../../stores/alreadySelectedConditions.js";
  import { calculatePricing } from "../../lib/calculatePricing.js";
  import {
    poidsPaliersStore,
    prixPaliersStore,
  } from "../../stores/pricingStore.js";
  
  let availableCondition =true;

  let isEditing = false;
  let newFieldValue = "";
  let title = "";
  let newTag = "";
  let tags = [];
  let Addedconditions = [];
  let isKgActive = true;
  let isNumberActive = false;
  let isVolumeActive = false;
  let isAirportActive = true;
  let isPortActive = false;
  let poidsMax = 0;
  let volumeMax = 0;
  let poidsPaliers = [];


  let prixPaliers = [];
  let message = "";
  let formErrors = {};

  let arrivalLocationOptions = [];

  let departurePlace = "";
  let arrivalPlace = "";
  let departureDate = "";
  let departureTime = "";
  let arrivalDate = "";
  let arrivalTime = "";

  onMount(() => {
  const poidsPaliersUnsubscribe = poidsPaliersStore.subscribe((value) => {
    poidsPaliers = value;
  });

  return poidsPaliersUnsubscribe;
  });
 onMount(() => {
    const unsubscribe = alreadySelectedConditions.subscribe((value) => {
      tags = value;
    });
    
    return unsubscribe;
  });

  async function fetchTagInfo(token) {
    try {
        const response = await fetch("http://127.0.0.1:8000/tags/", {
            headers: {
                "Authorization": `Token ${token}` 
            }
        });

        if (response.ok) {
            const tag = await response.json();
            console.log(tag);
            return tag;
        } else {
            console.error("Failed to fetch user info.");
        }
    } catch (error) {
        console.error("Error fetching user info:", error);
    }
}

  async function handleSubmit(event) {
    event.preventDefault(); // Prevent the default form submission

    // Combine date and time into a single datetime string
    const departureDateTime = `${departureDate}T${departureTime}:00Z`;
    const arrivalDateTime = `${arrivalDate}T${arrivalTime}:00Z`;

    console.log(poidsMax, volumeMax);
    // Prepare data object
    const data = {
      lieu_depart: departurePlace,
      destination: arrivalPlace,
      poids_max: parseFloat(poidsMax),
      volume_max: parseInt(volumeMax, 10),
      date_heure_depart: departureDateTime,
      date_heure_arrivee: arrivalDateTime,
      tags: tags,
      paliers : poidsPaliers
    };
    console.log(data);
    // Validation
    formErrors = {};
    if (!data.lieu_depart) {
      formErrors.departureLocation = "Departure location is required.";
      console.log(formErrors.departureLocation);
    }
    if (!departureDate || !departureTime) {
      formErrors.departureDateTime = "Departure date and time are required.";
      console.log(formErrors.departureDateTime);
    }
    if (!data.destination) {
      formErrors.arrivalLocation = "Arrival location is required.";
      console.log(formErrors.arrivalLocation);
    }
    if (!arrivalDate || !arrivalTime) {
      formErrors.arrivalDateTime = "Arrival date and time are required.";
      console.log(formErrors.arrivalDateTime);
    }
    if (data.poids_max <= 0) {
      formErrors.poidsMax = "Max weight should be greater than 0.";
      console.log(formErrors.poidsMax);
    }
    if (data.volume_max <= 0) {
      formErrors.volumeMax = "Max volume should be greater than 0.";
      console.log(formErrors.volumeMax);
    }

    if (Object.keys(formErrors).length > 0) {
      message = "Please fix the errors in the form.";
      console.log(message);
      return;
    }
    try {
      const response = await fetch("http://127.0.0.1:8000/annonces/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Token ${getToken()}`, // Use the getToken function
        },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        const result = await response.json();
        message = "Ad posted successfully!";
        console.log("Success:", result);
        // Handle success (e.g., show a success message, clear form, etc.)
      } else {
        const error = await response.json();
        message = "Failed to post ad!";
        console.error("Error:", error);
        // Handle errors (e.g., show error messages)
      }
    } catch (error) {
      message = "An error occurred!";
      console.error("Error:", error);
      // Handle errors (e.g., show error messages)
    }
  }

  function getToken() {
    return localStorage.getItem("authToken");
  }

  function handlePoidsMaxChange(event) {
    poidsMax = event.detail; // Mettre à jour poidsMax avec la nouvelle valeur
    console.log("Nouvelle valeur de poidsMax:", poidsMax);
  }

  function handleVolumeMaxChange(event) {
    volumeMax = event.detail; // Mettre à jour poidsMax avec la nouvelle valeur
    console.log("Nouvelle valeur de volumeMax:", volumeMax);
  }

  function updatePaliers (event) {

poidsPaliers = event.detail;
console.log("Nouvelle valeur de poidsPaliers:", poidsPaliers);
}
  const prixPaliersUnsubscribe = prixPaliersStore.subscribe((value) => {
    prixPaliers = value;
  });

  function toggleAirport() {
    isAirportActive = true;
    isPortActive = false;
    departurePlace = "";
    arrivalPlace = "";
    arrivalLocationOptions = [];
  }

  function togglePort() {
    isAirportActive = false;
    isPortActive = true;
    departurePlace = "";
    arrivalPlace = "";
    arrivalLocationOptions = [];
  }

  function toggleKg() {
    isKgActive = true;
    isNumberActive = false;
    isVolumeActive = false;
    console.log("Poids");
  }

  function toggleVolume() {
    isKgActive = false;
    isNumberActive = false;
    isVolumeActive = true;
    console.log("Volume");
  }

  // function updateArrivalOptions() {
  //   if (isAirportActive) {
  //     arrivalLocationOptions =
  //       dataTransport.routes.Algeria[departurePlace] || [];
  //   } else {
  //     // Add logic for ports if necessary
  //   }
  // }

  function updatePricing() {
    // Appelez la fonction pour recalculer les paliers de poids et les prix associés
    console.log("Updating pricing...");
    let { poidsPaliers, prixPaliers } = calculatePricing("weight", poidsMax);
    console.log(poidsMax, poidsPaliers, prixPaliers);
  }

  function handleTagInput(event) {
    if (event.key === "Enter" && newTag.trim() !== "") {
      if (!tags.includes(newTag.trim())) {
        tags = [...tags, newTag.trim()];
      } else {
        console.log("This condition has already been added.");
      }
      newTag = "";
    }
  }

  function removeTag(tagToRemove) {
    tags = tags.filter((tag) => {
      const notRemoved = tag !== tagToRemove;
      if (!notRemoved) {
        alreadySelectedConditions.remove(tagToRemove); // Appeler la méthode pour supprimer le tag du store
      }
      return notRemoved;
    });
  }

  function removeAllConditions() {
    alreadySelectedConditions.set([]); // Remplacez le contenu du store par un tableau vide
    tags = []; // Effacez également les tags dans le composant
  }

  function openTagPopup() {
    isEditing = true;
    title = "Add Tags";
  }

  function saveChanges() {
    if (Addedconditions.length > 0) {
      Addedconditions.forEach((condition) => {
        alreadySelectedConditions.add(condition);
      });
      Addedconditions = []; // Réinitialiser Addedconditions après l'ajout
    }
    isEditing = false; // Fermer le popup après avoir ajouté les conditions
  }

  function handleSelectedConditionsAdded(event) {
    // Stocker temporairement les éléments sélectionnés
    Addedconditions = event.detail.conditions;
  }

</script>

<main>
  <div class="Profile">
    <div class="Profile-background">
      <div class="ProfileTopCard">
        <p class="text-primary fw-semibold fs-2 fontPrimary">
          Publiez votre annonce
          <span class="text-white bg-primary rounded px-2">Ramy</span>
        </p>
      </div>

      <div class="choiceProfile bg-primary">
        <div class="ProfileDisplay card-shadow-gray">
          <div class="pt-5 ProfileDisplayTopCard">
            <p class="fs-1 fw-bold text-darkPrimary fontPrimary">
              Informations generals
            </p>
          </div>

          <form on:submit={handleSubmit}>
            <div class="placeCreationTransport">
              <div class="choiceTranspor">
                <p class="fs-3 fw-bold text-primary fontPrimary my-4">
                  Transport :
                </p>
                <div class="choiceTransportToggle">
                  <button
                    class="border-0"
                    type="button"
                    on:click={toggleAirport}
                  >
                    <div
                      class="{isAirportActive
                        ? 'colorTransportOriginalSwitch'
                        : 'colorTransportSecondarySwitch'} choiceTransportBtn fw-bold fs-3 fontSecondary"
                      id="c1"
                    >
                      Airport
                    </div>
                  </button>

                  <button class="border-0" type="button" on:click={togglePort}>
                    <div
                      class="{isPortActive
                        ? 'colorTransportOriginalSwitch'
                        : 'colorTransportSecondarySwitch'} choiceTransportBtn fw-bold fs-3 fontSecondary"
                      id="c2"
                    >
                      Port
                    </div>
                  </button>
                </div>
              </div>
              <div class="placeCreation">
                <div class="departureCreation cardCreation">
                  <p class="titreCreation fs-3 fw-bold text-primary fontPrimary my-4">
                    Depart :
                  </p>
                  <div class="placeCreationContainer">
                    <div class="parentGridCreation">
                      <div class="airportDepartureCreation">
                        <div class="airportDepartureCreation">
                          <p class="fs-5 fw-bold text-darkPrimary fontPrimary">
                            {#if isAirportActive}
                              Airport :
                            {:else}
                              Port :
                            {/if}
                          </p>
                        </div>
                      </div>
                      <div class="airportDepartureCreationInput">
                        <div class="input-box-creation">
                          <!-- Departure Inputs -->
                          <input
                            id="departure-location"
                            class="fw-normal text-primary fontSecondary"
                            type="text"
                            placeholder={`choisissez un ${isAirportActive ? "airport" : "port"}`}
                            bind:value={departurePlace}
                            required
                          />
                        </div>
                      </div>
                      <div class="dateDepartureCreation">
                        <div class="dateDepartureCreation">
                          <p class="fs-5 fw-bold text-darkPrimary fontPrimary">
                            Date :
                          </p>
                        </div>
                      </div>
                      <div class="DateDepartureCreationInput">
                        <div class="input-box-date-creation">
                          <input
                            id="departure-date"
                            class="DateInput fw-normal text-primary fontSecondary"
                            bind:value={departureDate}
                            type="date"
                            required
                          />
                        </div>
                      </div>
                      <div class="hoursMinutesDateDepartureCreationInput">
                        <div class="input-box-date-creation">
                          <input
                            id="departure-time"
                            class="DateInput fw-normal text-primary fontSecondary"
                            bind:value={departureTime}
                            type="time"
                            required
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="arrivalCreation cardCreation">
                  <p class="titreCreation fs-3 fw-bold text-primary fontPrimary my-4">
                    Arrivée :
                  </p>
                  <div class="placeCreationContainer">
                    <div class="parentGridCreation">
                      <div class="airportDepartureCreation">
                        <div class="airportDepartureCreation">
                          <p class="fs-5 fw-bold text-darkPrimary fontPrimary">
                            {#if isAirportActive}
                              Airport :
                            {:else}
                              Port :
                            {/if}
                          </p>
                        </div>
                      </div>
                      <div class="airportDepartureCreationInput">
                        <div class="input-box-creation">
                          <!-- Arrival Inputs -->
                          <input
                            id="arrival-location"
                            class="fw-normal text-primary fontSecondary"
                            type="text"
                            placeholder={`choisissez un ${isAirportActive ? "airport" : "port"}`}
                            bind:value={arrivalPlace}
                            required
                          />
                        </div>
                      </div>
                      <div class="dateDepartureCreation">
                        <div class="dateDepartureCreation">
                          <p class="fs-5 fw-bold text-darkPrimary fontPrimary">
                            Date :
                          </p>
                        </div>
                      </div>
                      <div class="DateDepartureCreationInput">
                        <div class="input-box-date-creation">
                          <input
                            id="arrival-date"
                            class="DateInput fw-normal text-primary fontSecondary"
                            bind:value={arrivalDate}
                            type="date"
                            required
                          />
                        </div>
                      </div>
                      <div class="hoursMinutesDateDepartureCreationInput">
                        <div class="input-box-date-creation">
                          <input
                            id="arrival-time"
                            class="DateInput fw-normal text-primary fontSecondary"
                            bind:value={arrivalTime}
                            type="time"
                            required
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="conditionCreation">
              <p class="fs-3 fw-bold text-primary fontPrimary my-4">
                Conditions :
              </p>
              <div class="ProfileContainerDisplay">
                <!-- Bouton pour ouvrir le tagPopup -->

                <!-- TagPopup -->
                {#if isEditing}
                  <div class="overlay"></div>
                  <TagPopup
                    isOpen={isEditing}
                    onClose={() => (isEditing = false)}
                    {availableCondition}
                    on:selectedConditionsAdded={handleSelectedConditionsAdded}
                    {title}
                    on:addClick={saveChanges}
                  />
                {/if}

                <!-- Affichage des tags sélectionnés -->
                <div class="tagContainer">
                  {#each tags as tag}
                    <div
                      class="tagItem bg-primary text-white fs-5 fontSecondary"
                      key={tag}
                    >
                      <p class="m-0">{tag}</p>
                      <button
                        class="removeTagBtn"
                        on:click={() => removeTag(tag)}
                      >
                        <lord-icon
                          class="animated-cross"
                          src="https://cdn.lordicon.com/zxvuvcnc.json"
                          colors="primary:#4FE1F9"
                          style="background-color: none;"
                          trigger="hover"
                        >
                        </lord-icon>
                      </button>
                    </div>
                  {/each}
                </div>
                <div class="buttonsCreationConditions">
                  <div class="buttonAddTag">
                    <button
                      class="ButtonEdit btn border-0 bg-primary text-white fs-5 fontSecondary"
                      on:click={openTagPopup}
                    >
                      Ajouter une condition +
                    </button>
                  </div>
                  {#if tags.length >= 2}
                    <div class="buttonAddTag">
                      <button
                        class="ButtonEdit btn border-0 bg-primary text-white fs-5 fontSecondary"
                        on:click={removeAllConditions}
                      >
                        Tout retirer
                      </button>
                    </div>
                  {/if}
                </div>
              </div>
            </div>
            <div class="pt-5 ProfileDisplayTopCard">
              <p class="fs-1 fw-bold text-darkPrimary fontPrimary">
                Infomartions des tarifs
              </p>
            </div>
            <div class="pricingCreation">
              <p class="fs-3 fw-bold text-primary fontPrimary my-4">
                Pricing :
              </p>
              <div class="pricingCreationDisplay">
                <div class="choicePricing" id="tarifs">
                  <button class="border-0" type="button" on:click={toggleKg}>
                    <div
                      class="{isKgActive
                        ? 'colorProfileOriginalSwitch'
                        : 'colorProfileSecondarySwitch'} choiceProfileBtn fw-bold fs-5 fontSecondary"
                      id="c1"
                    >
                      Poids
                    </div>
                  </button>
                  <button
                    class="border-0"
                    type="button"
                    on:click={toggleVolume}
                  >
                    <div
                      class="{isVolumeActive
                        ? 'colorProfileOriginalSwitch'
                        : 'colorProfileSecondarySwitch'} choiceProfileBtn fw-bold fs-5 fontSecondary"
                      id="c3"
                    >
                      Volume
                    </div>
                  </button>
                </div>
                <div class={isKgActive ? "active" : "inactive"}>
                  <PricingByWeight on:valueMaxChange={handlePoidsMaxChange} on:paliersMaxChange={updatePaliers} />
                </div>
                <div class={isVolumeActive ? "active" : "inactive"}>
                  <PricingByVolume on:valueMaxChange={handleVolumeMaxChange} />
                </div>
              </div>
            </div>
            <div class="postCreation">
              <button
                class="PostBtn ButtonEdit btn border-0 text-white fw-bold fs-3 fontSecondary"
                type="submit"
                on:click={handleSubmit}
              >
                Publier
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</main>

<style>
  @import "./responsive.css";

  p{
    margin-bottom: 0!important;
  }
  .overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* Opacité réduite */
    z-index: 999; /* Assure que la superposition est au-dessus de tout */
  }
  .ProfileTopCard {
    padding: 40px 50px 50px 0;
  }

  .choiceProfile {
    border-radius: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 60px 0px 186px 0px;
    height: 20px;
    background-color: #007bff; /* Couleur de fond */
  }

  .ProfileDisplay {
    width: 80%;
    margin: auto;
    margin-top: 70px;
    display: flex;
    flex-direction: column;
    padding: 60px 150px;
    border-radius: 40px;
    background-color: #ffffff;
    gap: 50px;
  }

  .ProfileDisplayTopCard {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .ProfileContainerDisplay {
    padding: 30px 40px;
    border: 2px solid #b6b3b3;
    border-radius: 40px;
    box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
    display: flex;
    flex-direction: column;
  }
  .pricingCreationDisplay {
    padding: 40px 160px;
    background-color: #21a5c3;
    border-radius: 40px;
    box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
    display: flex;
    flex-direction: column;
    gap: 40px;
  }
  .titreCreation {
    padding-bottom: 5px;
  }
  .placeCreation {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .placeCreationTransport {
    display: flex;
    flex-direction: column;
  }
  .choiceTransportToggle {
    padding-inline: 20%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
  }
  .cardCreation {
    width: 47%;
  }
  .placeCreationContainer {
    padding: 30px 40px;
    border: 2px solid #b6b3b3;
    border-radius: 40px;
    box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
    display: flex;
    flex-direction: column;
  }

  .input-box-creation input {
    padding: 1rem 0.5rem;
    width: 100%;
    border-radius: 20px;
    border: 2px solid #b6b3b3;
    box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.25);
    text-align: center; /* Centrer le contenu */
  }
  .input-box-creation input::placeholder {
    text-align: center;
  }
  .input-box-creation input:focus {
    border: 2px solid transparent;
    outline: 3px solid #21a5c3;
  }

  .input-box-date-creation {
    display: flex;
    justify-content: center; /* Centrer horizontalement */
    align-items: center; /* Centrer verticalement */
  }
  .input-box-date-creation input {
    padding: 1rem 0.5rem;
    width: 50%;
    border-radius: 20px;
    border: 2px solid #b6b3b3;
    box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.25);
  }
  .input-box-date-creation input::placeholder {
    text-align: center;
  }
  .input-box-date-creation input:focus {
    border: 2px solid transparent;
    outline: 3px solid #21a5c3;
  }
  .airportDepartureCreation {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .dateDepartureCreation {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .DateInput {
    display: flex;
    justify-content: center;
    text-align: center;
  }
  .parentGridCreation {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 20px;
    grid-row-gap: 40px;
  }

  .airportDepartureCreation {
    grid-area: 1 / 1 / 2 / 2;
  }
  .airportDepartureCreationInput {
    grid-area: 1 / 2 / 2 / 4;
  }
  .dateDepartureCreation {
    grid-area: 2 / 1 / 3 / 2;
  }
  .DateDepartureCreationInput {
    grid-area: 2 / 2 / 3 / 3;
  }
  .DateDepartureCreationInput input {
    width: 100%;
  }
  .hoursMinutesDateDepartureCreationInput {
    grid-area: 2 / 3 / 3 / 4;
  }
  .hoursMinutesDateDepartureCreationInput input {
    width: 100%;
  }
  .tagInputBox {
    margin-bottom: 20px;
  }
  .tagItem {
    display: flex;
    padding: 1rem 1.5rem;
    border-radius: 20px;
    box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.25);
    text-align: center; /* Centrer le contenu */
    margin-bottom: 30px;
    transition: 0.2 ease;
  }
  .tagContainer {
    display: flex;
    flex-wrap: wrap;
    column-gap: 30px;
  }

  .removeTagBtn {
    background-color: transparent;
    border: none;
    color: white;
    margin-left: 5px;
    cursor: pointer;
  }
  .buttonsCreationConditions {
    display: flex;
  }
  .buttonAddTag {
    display: flex;
    justify-content: center;
    width: 100%;
  }
  .buttonAddTag button {
    border-radius: 20px;
    width: 50%;
  }
  .choicePricing {
    display: flex;
  justify-content: space-evenly;
  gap: 10px;
  }
  .choiceProfileBtn {
    width: 200px;
  }
  .postCreation {
    display: flex;
    justify-content: flex-end;
    margin-top: 30px;
  }
  .PostBtn {
    border-radius: 40px;
    padding: 1rem 4rem;
    background-color: #4fe1f9;
    transition: background-color 0.2s ease-in-out;
  }
  .PostBtn:hover {
    background-color: #21a5c3;
  }
  .active {
    display: block;
  }

  .inactive {
    display: none;
  }
  .animated-cross {
    width: 28px;
    height: 28px;
  }
  /* Responsive styles */
@media (max-width: 1800px) {
    .ProfileDisplay {
        padding: 40px 100px;
    }

    .pricingCreationDisplay {
        padding: 30px 100px;
    }

    .placeCreationContainer {
        padding: 20px 30px;
    } 
      .parentGridCreation {
        grid-template-columns: 1fr;
        grid-template-rows: repeat(5, auto);
        grid-column-gap: 0;
        grid-row-gap: 20px;
    }


    .airportDepartureCreation {
    grid-area: 1 / 1 / 2 / 2;
    
  }
  .airportDepartureCreationInput {
    grid-area: 1 / 2 / 2 / 4;
  }
  .dateDepartureCreation {
    grid-area: 3 / 1 / 3 / 2;

  }
  .DateDepartureCreationInput {
    grid-area: 2 / 2 / 3 / 3;
    
  }
  .DateDepartureCreationInput input {
    width: 100%;
  }
  .hoursMinutesDateDepartureCreationInput {
    grid-area: 2 / 3 / 3 / 4;
  }
  .hoursMinutesDateDepartureCreationInput input {
    width: 100%;
  }

    .airportDepartureCreationInput,
    .DateDepartureCreationInput,
    .hoursMinutesDateDepartureCreationInput {
        grid-area: auto / auto / auto / auto;
    }

    
}

@media (max-width: 992px) {
    .ProfileDisplay {
        padding: 30px 80px;
    }

    .pricingCreationDisplay {
        padding: 20px 80px;
    }

    .placeCreationContainer {
        padding: 15px 80px;
        
    }
    .departureCreation.cardCreation, 
    .arrivalCreation.cardCreation
    {
        width: calc(100% - 50px);
    }
    .ProfileDisplay {
      width: 90%;
    }
    .placeCreation {
        flex-direction: column;
        gap: 20px;
    }

}

@media (max-width: 768px) {
    .ProfileDisplay {
        padding: 20px 50px;
    }

    .pricingCreationDisplay {
        padding: 15px 50px;
    }

    .placeCreation {
        flex-direction: column;
        gap: 20px;
    }

    .choiceTransportToggle {
        gap: 15px;
    }

    .choicePricing {
        grid-template-columns: 1fr;
        grid-row-gap: 20px;
    }
}

@media (max-width: 576px) {
    .ProfileDisplay {
        padding: 10px 30px;
    }

    .pricingCreationDisplay {
        padding: 10px 30px;
    }

    .placeCreationContainer {
        padding: 10px 15px;
    }
}
</style>
