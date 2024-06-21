<script>
  import TagRecherche from '../Recherche/TagRecherche.svelte'; // Assuming Tag.svelte is in the same directory
  export let tags = [];
  export let visible = false;
  export let searchCriteria = "";

  let filteredTags = [];
  let selectedTags = [];

  $: filteredTags = tags.filter(tag => tag.toLowerCase().includes(searchCriteria.toLowerCase()));

  function handleTagClick(event) {
    const { name, isSelected } = event.detail;
    if (isSelected) {
      if (!selectedTags.includes(name)) {
        selectedTags = [...selectedTags, name];
      }
    } else {
      selectedTags = selectedTags.filter(selectedTag => selectedTag !== name);
    }
  }
</script>

<main>
  <div class="tag-panel" style="display: {visible ? 'flex' : 'none'}">
    <div class="textTagPanel fs-5 fontSecondary">Choisissez vos conditions ({selectedTags.length} sélectionnés)</div>
    <div class="tagList">
      {#each filteredTags as tag}
        <TagRecherche name={tag} selected={selectedTags.includes(tag)} on:tagClick={handleTagClick} />
      {/each}
    </div>
  </div>
</main>

<style>
  .tagList {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    padding: 10px 30px 30px 30px;
  }
  .textTagPanel {
    position: sticky;
    top: 0;
    padding: 20px 30px;
    color: #434343;
    background-color: white;
    z-index: 1; /* Ensure it stays on top */
  }
  .tag-panel {
    border: 0;
    position: absolute;
    top: 100%; /* Position below the input */
    right: 0;
    width: 450px; /* Full width of the parent container */
    height: 500px;
    background: white;
    box-shadow: 0 4px 30px 0 rgba(0, 0, 0, 0.29);
    z-index: 1000;
    display: flex;
    flex-direction: column;
    border-radius: 20px;
    gap: 10px;
    overflow-y: auto; /* Add this line */
  }
  /* Style the scrollbar track */
  .tag-panel::-webkit-scrollbar {
    width: 10px;
    border-radius: 20px;
  }
  /* Style the scrollbar handle */
  .tag-panel::-webkit-scrollbar-thumb {
    background: #21A5C3;
    border-radius: 20px;
  }
  /* Handle on hover */
  .tag-panel::-webkit-scrollbar-thumb:hover {
    background: #4FE1F9;
  }
</style>
