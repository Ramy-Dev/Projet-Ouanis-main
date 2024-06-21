<script>
        import axios from 'axios';
        let email = '';
        let message = '';
    
        const resetPassword = async () => {
            try {
                const response = await axios.post('http://127.0.0.1:8000/reset_password/', { email });
                message = response.data.message;
            } catch (error) {
                message = error.response.data.detail || 'An error occurred';
            }
        };
    </script>
    
    <main>
       
        <img class="image_bg_recherche_ads" src="../svg/bg-recherche-ads.svg" alt="" />
        <div class="password-reset fontSecondary">
        <h1 class="mb-4">Réinitialisation du mot de passe</h1>
        <input class="mb-4" type="email" bind:value={email} placeholder="Entrer votre E-mail" />
        <button on:click={resetPassword}>Envoyer un lien de réinitialisation</button>
        <button class="mt-2"><a class="text-white" href="/">Accueil</a></button>
        <p class="">{message}</p>
    </div>
    </main>
    
<style>

main {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh;
    }
   
    .image_bg_recherche_ads {
    width: 100%;
    height: 120%;
    object-fit: cover;
    position: absolute;
    top: -10%;
    z-index: -2;
    transition: transform 0.5s ease;
  }
  .password-reset {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
   h1 {
        margin-bottom: 1rem;
    }

    input {
        background: none;
        margin-bottom: 1rem;
        padding: 0.75rem;
        width: 100%;
        max-width: 350px;
        border: 3px solid #21A5C3;
        border-radius: 12px;
        transition: all 0.2s ease;
    }
    input:hover {
      outline: none;
    border: 3px solid #4fe1f9;
    }
    input:focus {
      outline: none;
    border: 3px solid #4fe1f9;
    }
    button {
        padding: 0.5rem 1rem;
        background-color: #21A5C3;
        color: white;
        border: none;
        border-radius: 12px;
        cursor: pointer;
        transition: background-color 0.2s ease;
    }

    button:hover {
        background-color: #4fe1f9;
    }

    p {
        margin-top: 1rem;
        color: #21A5C3;
    }

    p:hover {
      color: #4fe1f9;
    }
    a{
        text-decoration: none;
    }
</style>