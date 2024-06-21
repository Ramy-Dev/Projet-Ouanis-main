<script>
  import { redirect } from "@sveltejs/kit";
  import { onMount } from "svelte";
  import { writable } from 'svelte/store';

   let message = "";
   let passwordType = writable("password");
  let errors = writable({});


  //  onMount(() => {
  //     if (getToken()) {
  //        window.location.href = '/'
  //     }
      
  //  });
async function handleSubmit(event) {
  event.preventDefault();
  errors.set({});
  const formData = new FormData(event.target);
  const data = Object.fromEntries(formData.entries());
  console.log("Sending data:", data); // Log data to verify structure

  try {
    const response = await fetch("http://127.0.0.1:8000/login/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      const result = await response.json();
      message = "Login successful!";
      localStorage.setItem("authToken", result.token);
      console.log("Success:", result);
      window.location.href = '/';
    } else {
      const error = await response.json();
      message = "Login failed!";
      errors.set(error);
      console.error("Error:", error, message); // Enhanced error logging
    }
  } catch (error) {
    message = "An error occurred!";
    console.error("Error:", error);
    errors.set({ general: 'An unexpected error occurred. Please try again later.' });
  }
}







async function fetchUserInfo(token) {
    try {
        const response = await fetch("http://127.0.0.1:8000/utilisateurs/", {
            headers: {
                "Authorization": `Token ${token}` 
            }
        });

        if (response.ok) {
            const user = await response.json();
            localStorage.setItem("user", JSON.stringify(user));
        } else {
            console.error("Failed to fetch user info.");
        }
    } catch (error) {
        console.error("Error fetching user info:", error);
    }
}

function getToken() {
    return localStorage.getItem("authToken");
}

function getUser() {
    return JSON.parse(localStorage.getItem("user"));
}

function logout() {
    localStorage.removeItem("authToken");
    localStorage.removeItem("user");
}
async function fetchUserByUsername(username) {
   try {
      const response = await fetch(`http://127.0.0.1:8000/users/?username=${username}`, {
         headers: {
            "Authorization": `Token ${getToken()}`
         }
      });
      if (response.ok) {
         const user = await response.json();
         return user;
      } else {
         console.error("Failed to fetch user by username.");
         return null;
      }
   } catch (error) {
      console.error("Error fetching user by username:", error);
      return null;
   }
}
function togglePassword(type) {
      passwordType.update(value => value === "password" ? "text" : "password");
  }
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
         <p class="phrase-accroche text-light">Embarquez vos colis !</p>
         <img class="illustration-plane" src="../svg/plane-login.svg" alt="Illustration of a plane">
       </div>
       <div class="sign_up_user">
         <div class="top-form">
           <p class="titre-form fw-bold">Bienvenue à <span class="text-primary">bord</span></p>
           <p class="soustitre-form">Votre colis est prêt à décoller ? Connectez-vous et trouvez le vol 
             <span class="text-primary">parfait</span> pour son voyage.</p>
         </div>
         <form class="form-user" on:submit={handleSubmit}>
           <div class="input-unit username-user">
             <label class="text-basic" for="mail-user">Adresse E-mail</label>
             <input type="email" id="mail-user" name="email" required>
           </div>
           <div class="input-unit username-user">
             <label class="text-basic" for="password-user">Mot de passe</label>
             <div class="password-container">
               <input type={$passwordType} id="password-user" name="password" required>
               <span class="toggle-password" on:click={() => togglePassword('password')}>
                 {#if $passwordType === 'password'}
                 <img src="../svg/eye-off.svg" alt="Hide" class="icon">
                 {:else}
                 <img src="../svg/eye.svg" alt="Show" class="icon">
                 {/if}
               </span>
             </div>
           </div>
           <div class="bottom-form">
              <div class="links-container">
                <a href="/reset_password" class="login-redirect text-light">Mot de passe oublié ?</a>
                <a href="/sign-up" class="login-redirect text-light">Pas encore de compte ?</a>
              </div>
             <button type="submit" class="text-white">Log in</button>
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
   padding-top: 30px;
   gap: 300px;
 }

 .right-side-sign-up {
   align-self: flex-start;
   user-select: none;
   pointer-events: none;
 }

 .phrase-accroche {
   font-size: 2.5rem;
   text-shadow: 1px 2px 0 #21A5C3;
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
   border: 3px solid #21A5C3;
   border-radius: 15px;
   transition: all 0.1s ease-in-out;
 }

 .form-user input:hover {
   border: 3px solid #4FE1F9;
 }

 .form-user input:focus {
   outline: 0px solid #21a5c3;
   border: 3px solid #4FE1F9;
 }

 .input-unit {
   display: flex;
   flex-direction: column;
 }

 .input-double {
   display: flex;
   gap: 30px;
 }

 .input-double input {
   width: 100%;
 }

 .bottom-form {
   display: flex;
   justify-content: space-between;
   align-items: center;
   margin-top: 20px;
 }

 .bottom-form button {
   padding: 10px 25px;
   background-color: #4FE1F9;
   border: 3px solid #4FE1F9;
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
   text-decoration: none;
 }

 .links-container {
   display: flex;
   flex-direction: column;
   text-align: left;
 }

 .bgImage {
   position: absolute;
   top: -5%;
   width: 100%;
   height: 100vh;
   z-index: -1;
   overflow: hidden;
   user-select: none;
   pointer-events: none;
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
   border: 3px solid #21A5C3;
   border-radius: 15px;
   transition: all 0.1s ease-in-out;
 }

 .password-container input:hover {
   border: 0px solid #4FE1F9;
 }

 .password-container input:focus {
   outline: 0px solid #21a5c3;
   border: 0px solid #4FE1F9;
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
   user-select: none;
   pointer-events: none;
 }
</style>
