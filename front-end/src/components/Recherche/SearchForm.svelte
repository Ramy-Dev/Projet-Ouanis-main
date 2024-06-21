<script>
  import { onMount } from 'svelte';
  import TagPanel from './TagPanel.svelte';
  import TarifPanel from './TarifPanel.svelte';
  import { conditions } from '../../lib/tagList.js';
  import { clickOutside } from '../../lib/functions/clickOutside.js';

  let searchCriteria = "";
  let selectedTags = [];

  let from = '';
  let to = '';
  let date = '';
  let tariff = '';
  let critères = '';

  let poids = "";
  let quantite = "";
  let volume = "";

  let input1, input2, input3, input4, input5;
  let isFocused1 = false, isFocused2 = false, isFocused3 = false, isFocused4 = false, isFocused5 = false;
  let showPanel = false;
  let showTarifPanel = false;
  let tags = conditions; // Example tags

  let tagPanelContainer;

  function togglePanel() {
    showPanel = !showPanel;
  }

  function toggleTarifPanel() {
    showTarifPanel = !showTarifPanel;
  }

  function clearInput(ref, bindValueSetter) {
    ref.value = '';
    ref.dispatchEvent(new Event('input'));
    bindValueSetter('');
  }

  function onBlur(setter) {
    setTimeout(() => setter(false), 115);
  }

  function handleSearch() {
    // Perform search actions
    console.log({ from, to, date, tariff, critères, selectedTags });
    // For example, fetch data based on search criteria
  }

  function handleTagSelected(event) {
    // Update selected tags array
    selectedTags = [...selectedTags, event.detail];
    console.log(selectedTags);
  }

  onMount(() => {
    const inputs = document.querySelectorAll('.custom-placeholder');
    inputs.forEach(input => {
      const placeholderText = input.getAttribute('data-placeholder').split('|');
      input.addEventListener('input', () => {
        if (input.value) {
          input.setAttribute('placeholder', '');
        } else {
          input.setAttribute('placeholder', placeholderText.join(' '));
        }
      });
      input.setAttribute('placeholder', placeholderText.join(' '));
    });
  });
</script>

<main>
  <form on:submit|preventDefault={handleSearch}>
    <div class="search-form fontSecondary">
      <div class="input-container container1">
        <label class="custom-label">De<br></label>
        <input
        required
          bind:this={input1}
          class="custom-placeholder input1"
          type="text"
          bind:value={from}
          data-placeholder="ville, aéroport, port"
          on:focus={() => isFocused1 = true}
          on:blur={() => onBlur(value => isFocused1 = value)} />
        {#if from}
          <button type="button" class="clear-button" on:click={() => clearInput(input1, value => from = value)}>
            <lord-icon
              class="animated-cross"
              src="https://cdn.lordicon.com/zxvuvcnc.json"
              colors="primary:#4FE1F9"
              style="background-color: white;"
              trigger="hover">
            </lord-icon>
          </button>
        {/if}
      </div>
      <div class="input-container container2">
        <label class="custom-label">Vers<br></label>
        <input
        required
          bind:this={input2}
          class="custom-placeholder input2"
          type="text"
          bind:value={to}
          data-placeholder="ville, aéroport, port"
          on:focus={() => isFocused2 = true}
          on:blur={() => onBlur(value => isFocused2 = value)} />
        {#if to}
          <button type="button" class="clear-button" on:click={() => clearInput(input2, value => to = value)}>
            <lord-icon
              class="animated-cross"
              src="https://cdn.lordicon.com/zxvuvcnc.json"
              colors="primary:#4FE1F9"
              style="background-color: white;"
              trigger="hover">
            </lord-icon>
          </button>
        {/if}
      </div>
      <div class="input-container container3">
        <label class="custom-label">Date<br></label>
        <input
        required
          bind:this={input3}
          class="custom-placeholder input3"
          type="date"
          bind:value={date}
          data-placeholder="jj/mm/aaaa"
          on:focus={() => isFocused3 = true}
          on:blur={() => onBlur(value => isFocused3 = value)} />
        {#if date}
          <button type="button" class="clear-button" on:click={() => clearInput(input3, value => date = value)}>
            <lord-icon
              class="animated-cross"
              src="https://cdn.lordicon.com/zxvuvcnc.json"
              colors="primary:#4FE1F9"
              style="background-color: white;"
              trigger="hover">
            </lord-icon>
          </button>
        {/if}
      </div>
      <div class="input-container container4">
        <label class="custom-label">Tarifs<br></label>
        <input
        required
          bind:this={input4}
          class="custom-placeholder input4"
          type="text"
          bind:value={tariff}
          data-placeholder="poids, volume, quantité"
          on:focus={() => { isFocused5 = true; toggleTarifPanel(); }} />
        <TarifPanel {poids} {quantite} {volume} visible={showTarifPanel} />
        {#if tariff}
          <button type="button" class="clear-button" on:click={() => clearInput(input4, value => tariff = value)}>
            <lord-icon
              class="animated-cross"
              src="https://cdn.lordicon.com/zxvuvcnc.json"
              colors="primary:#4FE1F9"
              style="background-color: white;"
              trigger="hover">
            </lord-icon>
          </button>
        {/if}
      </div>
      <div class="input-container container5">
        <label class="custom-label">Conditions<br></label>
        <input
        required
          bind:this={input5}
          class="custom-placeholder input5"
          type="text"
          bind:value={critères}
          data-placeholder="pick from the list"
          on:focus={() => { isFocused5 = true; togglePanel(); }} />
        <TagPanel {tags} searchCriteria={critères} visible={showPanel} on:tagSelected={handleTagSelected} />
        {#if critères}
          <button type="button" class="clear-button" on:click={() => clearInput(input5, value => critères = value)}>
            <lord-icon
              class="animated-cross"
              src="https://cdn.lordicon.com/zxvuvcnc.json"
              colors="primary:#4FE1F9"
              style="background-color: white;"
              trigger="hover">
            </lord-icon>
          </button>
        {/if}
      </div>
      <div class="search-button-container">
        <button class="searchButton" type="submit">Search</button>
        <div class="arrow">
          <svg
            class="arrowSVG"
            fill="#4FE1F9"
            height="347"
            viewBox="0 0 198 347"
            xmlns="http://www.w3.org/2000/svg">
            <path d="M191.36 137.224L197.302 138.06L191.36 137.224ZM30.402 346.498C27.3654 347.825 23.8283 346.439 22.5017 343.402L0.883889 293.918C-0.44269 290.881 0.943544 287.344 3.98013 286.018C7.01671 284.691 10.5538 286.077 11.8803 289.114L31.0962 333.1L75.082 313.884C78.1186 312.557 81.6556 313.944 82.9822 316.98C84.3088 320.017 82.9226 323.554 79.886 324.88L30.402 346.498ZM54.2748 0.140731C56.056 3.42689 58.2611 6.59445 60.8525 9.6692L51.6767 17.4025C48.6316 13.7894 45.9442 9.95333 43.725 5.85927L54.2748 0.140731ZM78.7967 25.8217C85.2231 30.4903 92.3572 34.9216 99.9037 39.2694L93.9132 49.6671C86.1706 45.2064 78.6406 40.5405 71.7438 35.5304L78.7967 25.8217ZM122.232 51.5547C129.839 55.6513 137.517 59.7965 144.862 64.0812L138.816 74.4466C131.674 70.2806 124.171 66.2285 116.542 62.1201L122.232 51.5547ZM166.921 78.4814C174.47 84.1764 181.242 90.4144 186.514 97.4448L176.914 104.644C172.53 98.7987 166.68 93.3313 159.694 88.0609L166.921 78.4814ZM197.485 123.684C198.049 128.278 198.005 133.066 197.302 138.06L185.419 136.388C185.983 132.383 186.005 128.65 185.575 125.147L197.485 123.684ZM197.302 138.06C196.626 142.863 195.693 147.461 194.524 151.876L182.924 148.803C183.969 144.858 184.808 140.727 185.419 136.388L197.302 138.06ZM183.935 177.922C179.299 186.156 173.757 193.617 167.596 200.559L158.621 192.594C164.319 186.174 169.331 179.401 173.479 172.034L183.935 177.922ZM147.942 219.734C141.234 225.558 134.171 231.182 127.004 236.78L119.618 227.323C126.745 221.756 133.609 216.286 140.074 210.673L147.942 219.734ZM106.025 253.191C99.2238 258.623 92.4752 264.221 85.9115 270.17L77.8534 261.278C84.6674 255.103 91.6246 249.334 98.5369 243.814L106.025 253.191ZM67.4889 288.597C61.8516 294.902 56.5018 301.647 51.5558 308.967L41.6126 302.249C46.8934 294.433 52.5845 287.264 58.5432 280.599L67.4889 288.597ZM38.7419 331.319C36.9191 335.127 35.1968 339.08 33.5863 343.189L22.4137 338.811C24.1311 334.429 25.9698 330.208 27.918 326.138L38.7419 331.319Z"/>
          </svg>
        </div>
      </div>
    </div>
  </form>
</main>

<style>

  .search-form {
      display: flex;
      flex-direction: row;
      gap: 12px;
      align-items: center;
      padding: 10px;
  }
  .input-container {
      position: relative;
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      background-color: #ffffff;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.35);
      padding: 20px 10px;
      border-radius: 20px;
      width: 200px;
  }
  .custom-label {
      font-weight: bold;
      color: #434343;
      text-align: center;
      font-size: 14px;
  }
  .custom-label span {
      font-weight: normal;
      color: #aaaaaa;
      font-size: 12px;
  }
  .search-form label {
    padding-left: 10px;
  }
  .search-form input {
      padding: 5px 10px;
      border: none;
      border-radius: 20px;
      background-color: transparent;
      font-size: 14px;
      text-align: left;
      width: 100%;
  }
  .search-form .input3 {
    color: #aaaaaa;
  }
  .search-form .container3 {
    color: #aaaaaa;
    width: 160px;
  }
  .search-form .container4 {
      width: 220px;

  }
  .search-form .container5 {
      width: 180px;
  }
  .search-form .searchButton {
      padding: 35px 30px;
      border: none;
      border-radius: 20px;
      background-color: #4FE1F9;
      color: white;
      font-size: 14px;
      cursor: pointer;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.35);
      transition: background-color 0.3s ease;
      position: relative;
  }
  .search-form .searchButton:hover {
      background-color: #3bc7d7;
  }
  .search-form input:focus {
      text-align: left;
      outline: none;
  }
  .search-form input::placeholder {
      text-align: left;
      color: #aaaaaa;
      font-weight: 600;
  }
  .clear-button {
      position: absolute;
      top: 20%;
      right: 10px;
      transform: translateY(-50%);
      background: none;
      border: none;
      border-radius: 50%;
      padding: 0;
      margin: 0;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
  }
  .clear-button:hover {
      color: #333;
  }
  .animated-cross {
width: 28px;
height: 28px;
  }
  .search-button-container {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    
  }
  .arrow {
   position: absolute;
   bottom: -250%;
   left: 40%;
   transform: translateX(-50%);
   z-index: -1;
   
}

.arrowSVG {
   width: 280px;
   height: 280px;
   transform: rotate(20deg);
   transition: transform 0.3s ease;
}
.searchButton:hover ~ .arrow .arrowSVG {
    transform: translateX(5px);
    fill: #3bc7d7;
  }
</style>
