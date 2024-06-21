<script>
  import Popup from "../../components/Popup.svelte";
  import { onMount, tick } from "svelte";

  let userData = [];
  let isEditing = false;
  let newFieldValue = "";
  let fieldName = "";
  let title = "";
  let isProfileActive = true;
  let is_voyageur = true;
  let profileImageUrl = "../svg/image_profil.svg"; // Default profile image

  onMount(async () => {
    const token = localStorage.getItem("authToken");
    userData = await fetchUserData(token);
    // Now userData should be populated
    console.log("User data loaded:", userData);
  });

  async function fetchUserData(token) {
    try {
      const response = await fetch("http://127.0.0.1:8000/utilisateurs/", {
        headers: {
          "Authorization": `Token ${token}`
        }
      });

      if (response.ok) {
        const data = await response.json();
        console.log("Fetched user data:", data);
        return data; // Ensure to return the fetched data
      } else {
        console.error("Failed to fetch user info.");
        return {}; // Return an empty object or handle the error as needed
      }
    } catch (error) {
      console.error("Error fetching user info:", error);
      return {}; // Return an empty object or handle the error as needed
    }
  }

  function toggleProfile() {
    isProfileActive = true;
    console.log(userData, userData[0].username);
  }

  function toggleHistory() {
    isProfileActive = false;
  }

  function toggleProfileAndToggle() {
    toggleProfile();
    toggle();
  }

  function toggleHistoryAndToggle() {
    toggleHistory();
    toggle();
  }

  const toggle = (event) => {
    const clickedButton = event.target.closest("button");
    const clickedTarif = clickedButton.querySelector(".choiceProfileBtn");
    const otherTarif =
      clickedTarif.id === "c1"
        ? document.getElementById("c2")
        : document.getElementById("c1");

    if (clickedTarif.classList.contains("colorProfileOriginalSwitch")) return;

    document
      .querySelectorAll(".choiceProfileBtn.colorProfileOriginalSwitch")
      .forEach((tarif) => {
        tarif.classList.remove("colorProfileOriginalSwitch");
        tarif.classList.add("colorProfileSecondarySwitch");
      });

    clickedTarif.classList.add("colorProfileOriginalSwitch");
    clickedTarif.classList.remove("colorProfileSecondarySwitch");

    clickedButton.disabled = false;
  };

  function openPopup(field) {
    isEditing = true;
    fieldName = field;

    switch (field) {
      case "name":
        title = "Edit your Name";
        newFieldValue = userData[0].first_name;
        break;
      case "email":
        title = "Edit your Email";
        newFieldValue = userData[0].email;
        break;
      case "phone":
        title = "Edit your Phone Number";
        newFieldValue = userData[0].numero_telephone;
        break;
      case "dateOfBirth":
        title = "Edit your Date of Birth / Age";
        newFieldValue = userData[0].date_de_naissance;
        break;
      case "address":
        title = "Edit your Address";
        newFieldValue = userData[0].adresse;
        break;
      case "password":
        title = "Change your Password";
        newFieldValue = userData[0].password; // Placeholder, you might not want to display password
        break;
      case "passport":
        title = "Edit your Passport Number";
        newFieldValue = userData[0].numero_passeport;
        break;
    }
  }

  function saveChanges() {
    switch (fieldName) {
      case "name":
        userData[0].first_name = newFieldValue;
        break;
      case "email":
        userData[0].email = newFieldValue;
        break;
      case "phone":
        userData[0].numero_telephone = newFieldValue;
        break;
      case "dateOfBirth":
        userData[0].date_de_naissance = newFieldValue;
        break;
      case "address":
        userData[0].adresse = newFieldValue;
        break;
      case "password":
        userData[0].password = newFieldValue;
        break;
      case "passport":
        userData[0].numero_passeport = newFieldValue;
        break;
    }
    isEditing = false;

    tick().then(() => {
      // Optionally, you can perform additional operations here if needed
    });
  }

  function handleChangesSaved(event) {
    const { fieldName, newValue } = event.detail;
    userData[fieldName] = newValue;
  }

  function handleFileChange(event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
        profileImageUrl = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  }

  $: {
    console.log("Updated userData:", userData);
  }
</script>

<main>
  {#if isEditing}
    <div class="overlay"></div>
    <Popup
      {title}
      isOpen={isEditing}
      onClose={() => (isEditing = false)}
      bind:newFieldValue
      {fieldName}
      on:changesSaved={handleChangesSaved}
    >
      <input
        class={fieldName === "phone" || fieldName === "dateOfBirth"
          ? "numberInput"
          : ""}
        bind:value={newFieldValue}
      />
      <button
        on:click={saveChanges}
        class="ButtonEdit btn border-0 bg-primary text-white">save</button
      >
    </Popup>
  {/if}

  <div class="Profile fontSecondary">
    <div class="Profile-background bg-primary">
      <div class="ProfileTopCard">
        <p class="text-white fw-semibold fs-2 fontPrimary">
          {#if isProfileActive}
            {userData[0]?.username || 'N/A'}'s profile
          {:else}
            {userData[0]?.username || 'N/A'}'s history
          {/if}
        </p>
        <img src="../svg/VerifStar.svg" alt="Verif Star" />
      </div>

      <div class="choiceProfile" id="tarifs">
        <button
          class="border-0"
          type="button"
          on:click={toggleProfileAndToggle}
        >
          <div
            class="choiceProfileBtn {isProfileActive
              ? 'colorProfileOriginalSwitch'
              : 'colorProfileSecondarySwitch'} fw-bold fs-5"
            id="c1"
          >
            Profile
          </div>
        </button>
        <button
          class="border-0"
          type="button"
          on:click={toggleHistoryAndToggle}
        >
          <div
            class="choiceProfileBtn {!isProfileActive
              ? 'colorProfileOriginalSwitch'
              : 'colorProfileSecondarySwitch'} fw-bold fs-5"
            id="c2"
          >
            History
          </div>
        </button>
      </div>

      {#if isProfileActive}
        <div class="ProfileDisplay card-shadow-gray">
          <div class="ProfileDisplayTopCard mb-4">
            <div class="profile-image-container">
              <img src={profileImageUrl} alt="Photo de profile" />
            </div>
            <input type="file" id="file-input" accept="image/*" on:change={handleFileChange} style="display: none;" />
            <button class="ImageEdit btn text-light fontSecondary" on:click={() => document.getElementById('file-input').click()}>
              upload image
            </button>
          </div>
          {#if is_voyageur}
          <div class="demande_compte_voyageur fontSecondary">
            <div class="ProfileContainerDisplay ProfileContainerDisplayVoyageur">
              <p class="text-basic fs-2 mb-5">Demande de compte <span class="text-primary">voyageur</span></p>
              <div class="container_infos">
                <p class="text-secondary fs-5 mb-4">
                  Vous n'êtes pas encore un voyageur, pour devenir un voyageur veuillez remplir le formulaire suivant
                </p>
                <button
                  id="edit-name"
                  class="ButtonEdit btn border-0 text-white">
                  <a href="/demande-voyageur" class="fw-semibold">
                    Remplir le formulaire
                  </a>
                </button>
              </div>
            </div>
          </div>
          {/if}
          <div class="ProfileContainerDisplay fontSecondary">
            <p class="text-basic fs-2 mb-5">Important information</p>
            <div class="ProfileInfo fs-5">
              <p class="text-secondary">Your Name</p>
              <div class="ProfileEditInfo">
                <span id="info-name" class="fw-bold">{userData[0]?.first_name}</span>
                <button
                  id="edit-name"
                  class="ButtonEdit btn border-0 bg-light text-white"
                  on:click={() => openPopup("name")}>edit</button>
              </div>
            </div>
            <div class="ProfileInfo fs-5">
              <p class="text-secondary">Email</p>
              <div class="ProfileEditInfo">
                <span class="fw-bold">{userData[0]?.email}</span>
                <button
                  class="ButtonEdit btn border-0 bg-light text-white"
                  on:click={() => openPopup("email")}>edit</button>
              </div>
            </div>
            <div class="ProfileInfo fs-5">
              <p class="text-secondary">Phone Number</p>
              <div class="ProfileEditInfo">
                <span class="fw-bold">{userData[0]?.numero_telephone}</span>
                <button
                  class="ButtonEdit btn border-0 bg-light text-white"
                  on:click={() => openPopup("phone")}>edit</button>
              </div>
            </div>
          </div>
          <div class="ProfileContainerDisplay fontSecondary">
            <p class="fs-3 mb-5">
              About <span class="text-primary">{userData[0]?.first_name}</span>
              <span class="text-muted">(optional)</span>
            </p>
            <div class="ProfileInfo fs-5">
              <p class="text-secondary">Date of birth / Age</p>
              <div class="ProfileEditInfo">
                <span class="fw-bold">{userData[0]?.date_de_naissance}</span>
                <button
                  class="ButtonEdit btn border-0 bg-light text-white"
                  on:click={() => openPopup("dateOfBirth")}>edit</button>
              </div>
            </div>
            <div class="ProfileInfo fs-5">
              <p class="text-secondary">Address</p>
              <div class="ProfileEditInfo">
                <span class="fw-bold">{userData[0]?.adresse}</span>
                <button
                  class="ButtonEdit btn border-0 bg-light text-white"
                  on:click={() => openPopup("address")}>edit</button>
              </div>
            </div>
            <div class="ProfileInfo fs-5">
              <p class="text-secondary">Password</p>
              <div class="ProfileEditInfo">
                <span class="fw-bold">********</span>
                <button
                  class="ButtonEdit btn border-0 bg-light text-white"
                  on:click={() => openPopup("password")}>edit</button>
              </div>
            </div>

            {#if userData[0]?.is_voyageur}
              <div class="ProfileInfo fs-5">
                <p class="text-secondary">Passport Number</p>
                <div class="ProfileEditInfo">
                  <span class="fw-bold">{userData[0]?.numero_passeport}</span>
                  <button
                    class="ButtonEdit btn border-0 bg-primary text-white"
                    on:click={() => openPopup("passport")}>edit</button>
                </div>
              </div>
            {/if}
          </div>
        </div>

      {:else}
        <!-- Afficher le contenu de le partie history -->

        <div class="ProfileDisplay card-shadow-gray fontSecondary">
          <p class="profileTitle text-primary fs-2 fw-bold mb-2">My Ads</p>
          <div class="album py-5">
            <div class="container containerAnnonces">
               <div
                  class="row row-cols-1 row-cols-md-2 g-5 px-5"
                  id="cardsContainer"
               >
                  
               </div>
            </div>
          </div>
        </div>
      {/if}
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

 

  .ProfileDisplay {
    width: 80%;
    margin: auto;
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
    padding: 0px 90px 0 60px;
  }
  .ProfileDisplayTopCard .profile-image-container {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    overflow: hidden;
    position: relative;
  }

  .ProfileDisplayTopCard .profile-image-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    top: 0;
    left: 0;
  }

  .ProfileDisplayTopCard .ImageEdit {
    margin-top: 10px;
  }

  .ProfileDisplayTopCard img {
    max-width: 150px; /* Adjust the size as needed */
    border-radius: 50%;
  }
  .ButtonEdit {
    padding: 0.5rem 2.5rem;
    border-radius: 20px;
    font-size: 1.25rem;
  }
  .ImageEdit {
    border: 2px dashed #4FE1F9;
    padding: 0.5rem 2.5rem;
    border-radius: 20px;
    font-size: 1.25rem;
  }
  .ProfileContainerDisplay {
    padding: 40px 60px;
    border: 2px solid #b6b3b3;
    border-radius: 40px;
    box-shadow: 0 4px 4px 0 rgba(0, 0, 0, 0.25);
  }

  .ProfileInfo {
    margin: 0 30px 20px 30px;
  }
  .container_infos {
  margin: 0 30px 20px 30px;
  }
  .container_infos button{
  align-items: center;
  }
  .container_infos a{
  text-decoration: none;
  color: #ffffff;
  }
  .ProfileEditInfo {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
  
  p {
    margin-bottom: 0;
  }
  .profileTitle {
    display: flex;
    justify-content: center;
  }
  .card {
      border: none;
      border-radius: 20px;
   }
   .colorTopAnnonce {
      height: 30px;
   }
   .topCard {
      display: flex;
      flex-direction: row;
      padding: 0 50px 30px 50px;
      align-items: center;
      justify-content: space-between;
   }
   .demande_compte_voyageur button{
      background-color: #4FE1F9;
   }
   .demande_compte_voyageur button:hover{
      background-color: #24e2ff;
   }
</style>
