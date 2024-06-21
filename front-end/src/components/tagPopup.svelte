<script>
  import { createEventDispatcher } from "svelte";
  import { onMount } from "svelte";
  import Tag from "./Tag.svelte";
  import { alreadySelectedConditions } from "../stores/alreadySelectedConditions.js"; // Import du store
  const dispatch = createEventDispatcher();
  export let filteredConditions = []; // Initialisation des conditions filtrées avec toutes les conditions disponibles
  export let isOpen = false;
  export let onClose = () => {};
  export let selectedCondition = ""; // La condition sélectionnée
  export let availableConditions = []; // Liste des conditions disponibles

  onMount(async () => {
     const token = localStorage.getItem("authToken");
     const tags = await fetchTagInfo(token);
     availableConditions = tags.map(tag => tag.nom).filter(Boolean); // Filter out any null or undefined values
     filteredConditions = [...availableConditions];
     console.log(availableConditions);
  });

  async function fetchTagInfo(token) {
     try {
        const response = await fetch("http://127.0.0.1:8000/tags/", {
           headers: {
              Authorization: `Token ${token}`,
           },
        });

        if (response.ok) {
           const tags = await response.json();
           console.log(tags);
           return tags;
        } else {
           console.error("Failed to fetch tags.");
           return [];
        }
     } catch (error) {
        console.error("Error fetching tags:", error);
        return [];
     }
  }

  export let title = ""; // Titre du popup

  let selectedConditions = [];

  function handleOverlayClick(event) {
     if (event.target.classList.contains("overlay")) {
        onClose();
     }
  }

  function handleEscapeKey(event) {
     if (event.key === "Escape") {
        console.log("Escape key pressed");
        onClose();
     }
  }

  function handleSearch(event) {
     const searchText = event.target.value.toLowerCase();
     filteredConditions = availableConditions.filter((condition) =>
        condition.toLowerCase().includes(searchText)
     );
     filteredConditions = [...filteredConditions]; // Ensure reactivity
  }

  function toggleCondition(condition) {
     if (selectedConditions.includes(condition)) {
        selectedConditions = selectedConditions.filter((c) => c !== condition);
     } else {
        selectedConditions = [...selectedConditions, condition];
     }
  }

  // Fonction pour sélectionner une condition et l'envoyer à creation.svelte
  function handleTagClick(event) {
     console.log("Tag clicked:", event.detail);
     const { name, selected } = event.detail;
     if (selected) {
        if (!selectedConditions.includes(name)) {
           selectedConditions = [...selectedConditions, name];
        }
     } else {
        selectedConditions = selectedConditions.filter((tag) => tag !== name);
     }
  }

  function saveChanges() {
     dispatch("selectedConditionsAdded", { conditions: selectedConditions });
     onClose();
  }

  let popupRef;

  // Fonction pour attribuer le focus au popup lorsqu'il est ouvert
  function focusPopup() {
     popupRef.focus();
  }

  onMount(() => {
     const tagRemovedListener = (event) => {
        const { tag } = event.detail;
        selectedConditions = selectedConditions.filter((t) => t !== tag);
     };
     document.addEventListener("tagRemoved", tagRemovedListener);
     return () => {
        document.removeEventListener("tagRemoved", tagRemovedListener);
     };
  });
</script>

<main>
  {#if isOpen}
     <div class="overlay fontSecondary" on:click={handleOverlayClick}>
        <div
           class="popup"
           bind:this={popupRef}
           tabindex="-1"
           on:keydown={handleEscapeKey}
        >
           <div class="popup-header">
              <h2 class="fw-bold fs">{title}</h2>
              <button
                 on:click={onClose}
                 class="exitTagBtn btn border-0 text-primary fw-bolder fs-5"
              >
                 <lord-icon
                    class="animated-cross"
                    src="https://cdn.lordicon.com/zxvuvcnc.json"
                    colors="primary:#4FE1F9"
                    style="background-color: none;"
                    trigger="hover"
                 >
                 </lord-icon></button
              >
           </div>
           <div class="popup-content">
              <div class="tagSearch">
                 <div class="inputTagSearch">
                    <input
                       on:input={handleSearch}
                       class="fs-5 fw-normal text-primary fs-5 fw-bold fontSecondary"
                       type="text"
                       placeholder="Type in your search"
                    />
                 </div>
                 <button
                    class="btnTagSearch bg-primary text-white search-button border-0 fs-5 fontSecondary"
                    on:click={saveChanges}>Add</button
                 >
              </div>
           </div>
           <div class="conditionsTag">
              <p class="text-secondary fw-bold fs-5 fontSecondary">
                 Select Condition:
              </p>
              {#if filteredConditions.length > 0}
                 <div class="tag-selection">
                    <div class="textTagSearch"></div>
                    <div class="resultsTagSearch">
                       {#each filteredConditions as condition}
                          <Tag
                             name={condition}
                             selected={selectedConditions.includes(condition)}
                             on:tagClick={toggleCondition}
                          />
                       {/each}
                    </div>
                 </div>
              {:else if availableConditions.length > 0}
                 <p
                    class="noresultsTagSearch text-primary fs-4 fw-bold fontSecondary"
                 >
                    No results found
                 </p>
              {/if}
           </div>
           <div class="popup-footer"></div>
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
     min-height: 80vh;
     max-height: 80vh; /* Définir une hauteur maximale de 80% de la hauteur de la fenêtre */
     overflow-y: auto; /* Activer le défilement vertical si nécessaire */
     width: 40%;
     display: flex;
     flex-direction: column;

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
     justify-content: space-between;
  }
  .exitTagBtn {
     border-radius: 40%;
  }
  .popup-content {
     display: flex;
     justify-content: center;
     gap: 50px;
  }
  .tagSearch {
     display: flex;
     justify-content: center;
     gap: 50px;
  }
  .inputTagSearch input {
     width: 100%;
     padding: 1rem 1.5rem;
     border-radius: 20px;
     border: 3px solid #21a5c3;
     box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.25);
     text-align: center; /* Centrer le contenu */
  }
  .tagSearch button {
     padding: 1rem 1.5rem;
     border-radius: 20px;
     box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.25);
     text-align: center; /* Centrer le contenu */
  }
  .inputTagSearch input::placeholder {
     text-align: center;
  }
  .tag-item {
     /* Styles pour chaque élément de tag */
     margin-bottom: 10px;
  }

  .popup-footer {
     /* Styles pour le pied de la popup */
     display: flex;
     justify-content: flex-end;
     margin-top: 20px;
  }

  input[type="checkbox"] {
     /* Styles pour les cases à cocher */
     margin-right: 5px;
  }
  .tag-selection {
     display: flex;
     flex-direction: column;
     gap: 30px;
  }
  .resultsTagSearch {
     display: flex;
     flex-wrap: wrap;
     gap: 30px;
  }
  .conditionTag {
     display: flex;
     justify-content: center;
  }
  .conditionTagBtn {
     padding: 1.5rem 2rem;
     border-radius: 20px;
     box-shadow: 0 3px 3px 0 rgba(0, 0, 0, 0.25);
     text-align: center; /* Centrer le contenu */
  }

  .selected-conditions {
     display: flex;
     flex-direction: column;
     gap: 10px;
  }
  .selected-condition {
     display: flex;
     align-items: center;
     justify-content: space-between;
  }
  .remove-condition-btn {
     background-color: red;
     color: white;
     border: none;
     border-radius: 5px;
     padding: 5px 10px;
     cursor: pointer;
  }
  .animated-cross {
     width: 40px;
     height: 40px;
  }
</style>
