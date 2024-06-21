<script>
  import { writable } from "svelte/store";
  import { onMount } from "svelte";

  let message = "";
  let passwordType = writable("password");
  let confirmPasswordType = writable("password");
  let phoneInput;
  let passportPhotoUrl = ""; // Store the image URL for preview

  async function handleSubmit(event) {
    event.preventDefault(); // Prevent the default form submission

    // Get form data
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    data.phoneNumber = phoneInput.getNumber();

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/demandes_compte_voyageur/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(data),
        }
      );

      if (response.ok) {
        const result = await response.json();
        message = "Registration successful!";
        localStorage.setItem("authToken", result.token);
        console.log("Success:", result);
        // Handle success (e.g., show a success message, clear form, etc.)
      } else {
        const error = await response.json();
        message = "Registration failed!";
        console.error("Error:", error);
        // Handle errors (e.g., show error messages)
      }
    } catch (error) {
      message = "An error occurred!";
      console.error("Error:", error);
      // Handle errors (e.g., show error messages)
    }
  }

  function togglePassword(type) {
    if (type === "password") {
      passwordType.update((value) =>
        value === "password" ? "text" : "password"
      );
    } else if (type === "confirmPassword") {
      confirmPasswordType.update((value) =>
        value === "password" ? "text" : "password"
      );
    }
  }

  function handleFileChange(event) {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function(e) {
        passportPhotoUrl = e.target.result;
      };
      reader.readAsDataURL(file);
    }
  }

  function deletePhoto() {
    passportPhotoUrl = "";
    document.getElementById("passeport-photo-user").value = ""; // Reset file input
  }

  onMount(() => {
    phoneInput = window.intlTelInput(document.querySelector("#phone-number"), {
      initialCountry: "fr",
      preferredCountries: [
        "dz",
        "fr",
        "ma",
        "tn",
        "es",
        "ch",
        "be",
        "mc",
        "ad",
        "mt",
        "it",
        "gb",
        "de",
      ],
      utilsScript:
        "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
    });
  });
</script>

<main>
  <div class="bd">
    <b>{message}</b>
    <div class="bgImage">
      <img class="image_hexa" src="../svg/hexaMotif.svg" alt="bgImage" />
    </div>
    <section>
      <header class="fontSecondary">
        <div class="right-side-sign-up">
          <p class="phrase-accroche text-light">Gagnez en voyageant !</p>
          <img
            class="illustration-plane"
            src="../svg/illustration_plane.svg"
            alt="Illustration of a plane"
          />
        </div>
        <div class="sign_up_user">
          <div class="top-form">
            <p class="titre-form fw-bold">
              Prêt à <span class="text-primary">voyager</span> ?
            </p>
            <p class="soustitre-form">
              trouvez les colis a transporter sur votre
              <span class="text-primary">itinéraire</span> !
            </p>
          </div>
          <form class="form-user" on:submit={handleSubmit}>
            <div class="input-unit username-user">
              <label class="text-basic" for="dob-user">Date de naissance</label>
              <input type="date" id="dob-user" name="dob"  required/>
            </div>
            <div class="input-unit phone-number-user">
              <label class="text-basic" for="phone-number"
                >Numéro de téléphone</label
              >
              <input type="tel" id="phone-number" name="phone-number"  required/>
            </div>
            <div class="input-unit username-user">
              <label class="text-basic" for="adresse-user">Adresse</label>
              <input type="email" id="adresse-user" name="email"  required/>
            </div>
            <div class="input-unit username-user">
              <label class="text-basic" for="passeport-user"
                >Numéro de passeport</label
              >
              <div class="password-container">
                <input
                  type={$passwordType}
                  id="passeport-user"
                  name="password"
                  required
                />
                <span
                  class="toggle-password"
                  on:click={() => togglePassword("password")}
                >
                  {#if $passwordType === "password"}
                    <img src="../svg/eye-off.svg" alt="Hide" class="icon" />
                  {:else}
                    <img src="../svg/eye.svg" alt="Show" class="icon" />
                  {/if}
                </span>
              </div>
            </div>
            <div class="input-unit username-user passeport-user">
              <label class="text-basic" for="passeport-photo-user"
                >Photo de votre passeport</label
              >
              <input
                type="file"
                id="passeport-photo-user"
                name="passport-photo"
                on:change={handleFileChange}
                required
              />
              <img
                class="photo-passeport"
                src="../svg/photo_passeport.svg"
                alt=""
              />
            </div>
            {#if passportPhotoUrl}
            <div class="photo-preview">
              <img src={passportPhotoUrl} alt="Passport Preview" />
              <button type="button" class="delete-photo" on:click={deletePhoto}>
                <lord-icon
                  class="animated-cross"
                  src="https://cdn.lordicon.com/zxvuvcnc.json"
                  colors="primary:#4FE1F9"
                  style="background-color: transparent;"
                  trigger="hover">
                </lord-icon>
              </button>
            </div>
            {/if}
            <div class="bottom-form">
              <a href="/log-in" class="login-redirect text-light">
                Vous avez déjà un compte ?
              </a>
              <button type="submit" class="text-white"> confirmer </button>
            </div>
          </form>
        </div>
      </header>
    </section>
  </div>
</main>


<style>
  @import "./responsive.css";

  .bd {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    position: relative;
    z-index: 1;
  }

  header {
    display: flex;
    flex-direction: row-reverse;
    justify-content: center;
    align-items: center;
    position: relative;
    padding-top: 0px;
    gap: 300px;
    height:85vh;
  }
  .image_hexa {
    user-select: none; /* Prevents selection of the image */
    pointer-events: none; /* Disables all mouse events, including dragging */
  }
  .right-side-sign-up {
    align-self: flex-start;
    user-select: none; /* Prevents selection of the image */
    pointer-events: none; /* Disables all mouse events, including dragging */
  }

  .phrase-accroche {
    font-size: 2.5rem;
    text-shadow: 1px 2px 0 #21a5c3;
  }

  .illustration-plane {
    position: absolute;
    width: 70%;
    top: 50%;
    left: 80%;
    transform: translate(-50%, -50%);
    z-index: -1;
    
  }

  .sign_up_user {
    background: white;
    padding: 20px 30px;
    border-radius: 30px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 420px;
    display: flex;
    flex-direction: column;
    gap: 30px;
  }

  .titre-form {
    font-size: 1.7rem;
    margin-bottom: 5px !important;
  }

  .soustitre-form {
    font-size: 0.9rem;
    margin-bottom: 5px !important;
  }

  .form-user {
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .form-user input {
    appearance: none;
    padding: 10px 15px !important;
    border: 3px solid #21a5c3;
    border-radius: 15px;
    transition: all 0.1s ease-in-out;
  }

  .form-user input:hover {
    border: 3px solid #4fe1f9;
  }

  .form-user input:focus {
    outline: 0px solid #21a5c3;
    border: 3px solid #4fe1f9;
  }

  .input-unit {
    display: flex;
    flex-direction: column;
  }

  .phone-number-user input {
    width: 100%;
    padding: 10px 50px !important;
  }

  .bottom-form {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 20px;
  }

  .bottom-form button {
    margin-top: 10px;
    padding: 10px 25px;
    background-color: #4fe1f9;
    border: 3px solid #4fe1f9;
    border-radius: 15px;
    font-size: 1.2rem;
    transition: all 0.1s ease-in-out;
  }

  .bottom-form button:hover {
    background-color: #24e2ff;
  }

  .login-redirect {
    padding: 5px 0;
    font-size: 0.9rem;
    align-self: flex-end;
    text-decoration: none;
  }

  .bgImage {
    position: absolute;
    top: -5%;
    width: 100%;
    height: 100vh;
    z-index: -1;
    overflow: hidden;
  }

  .bgImage img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0.1;
  }

  .bgImage::after {
    content: "";
    display: block;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
      to top,
      rgba(255, 255, 255, 1) 5%,
      rgba(255, 255, 255, 0) 50%,
      rgba(255, 255, 255, 0) 100%
    );
    pointer-events: none;
  }

  .password-container {
    position: relative;
    border: 3px solid #21a5c3;
    border-radius: 15px;
    transition: all 0.1s ease-in-out;
  }
  .password-container input:hover {
    border: 0px solid #4fe1f9;
  }

  .password-container input:focus {
    outline: 0px solid #21a5c3;
    border: 0px solid #4fe1f9;
  }

  .password-container input {
    border: 0;
  }

  .toggle-password {
    position: absolute;
    right: 10px;
    top: 50%;
    transform: translateY(-50%);
    cursor: pointer;
  }

  .icon {
    width: 25px;
    height: 25px;
    user-select: none; /* Prevents selection of the image */
    pointer-events: none; /* Disables all mouse events, including dragging */
  }
  .passeport-user {
    position: relative;
    margin-bottom: 30px;
  }
  .passeport-user input {
    border: 3px dashed #4fe1f9;
    appearance: none;
    padding: 10px 15px !important;
    padding-right: 60px!important;
    border-radius: 15px;
    transition: all 0.1s ease-in-out;
  }
  .passeport-user input::placeholder {
    color: #4fe1f9;
  }
  .passeport-user input:hover {
    border: 3px dashed #24e2ff;
  }

  .passeport-user input:focus {
    outline: 0px dashed #21a5c3;
    border: 3px dashed #4fe1f9;
  }
  .photo-passeport {
    position: absolute;
    width: 75px;
    right: 0;
    top: 50%;
    user-select: none; /* Prevents selection of the image */
    pointer-events: none; /* Disables all mouse events, including dragging */
  }
  .photo-preview {
  position: relative;
  display: inline-block;
}

.photo-preview img {
  width: 100px; /* Adjust the size as needed */
  height: auto;
  border: 1px solid #ccc;
  border-radius: 15px;
}

.delete-photo {
  position: absolute;
  top: 0; /* Align with the top of the image */
  right: calc(100% - 100px); /* Align with the right side of the image */
  transform: translate(50%, -50%); /* Slight adjustment to place button correctly */
  border: none;
  cursor: pointer;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%; /* Optional: make it circular */
}
</style>
