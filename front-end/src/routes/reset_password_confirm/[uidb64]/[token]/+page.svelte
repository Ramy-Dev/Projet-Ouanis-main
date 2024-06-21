<script>
    import axios from 'axios';
    import { onMount } from 'svelte';
    import { page } from '$app/stores';

// Get the query parameters from the $page store
const { uidb64, token } = $page.params;

// Display the query parameters
    let new_password = '';
    let confirm_password = '';
    let message = '';
  
    const resetPassword = async () => {
      if (new_password !== confirm_password) {
        message = 'Passwords do not match';
        return;
      }
  
      try {
        const response = await axios.post(`http://127.0.0.1:8000/reset_password_confirm/${uidb64}/${token}/`, {
          new_password,
          confirm_password
        });
        message = response.data.message;
      } catch (error) {
        message = error.response?.data || 'An error occurred';
      }
    };
  

  </script>
  
  <main>
    <img class="image_bg_recherche_ads" src="../../svg/bg-recherche-ads.svg" alt="" />
    <div class="password-reset fontSecondary ">
    <h1 class="mb-4">Set
       <span class="new-span">New</span>
       Password</h1>
    <input class="text-basic" type="password" bind:value={new_password} placeholder="New Password" />
    <input class="text-basic mb-4" type="password" bind:value={confirm_password} placeholder="Confirm Password" />
    <button on:click={resetPassword}>Reset Password</button>
    <p>{message}</p>
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
  .new-span{
    color: white;
    background-color: #21A5C3;
    padding : 0.5rem;
    border-radius: 20px;
  }
  .new-span:hover{
    background-color: #4fe1f9;
  }
   h1 {
        margin-bottom: 1rem;
    }

    input {
      background: none;
        margin-bottom: 1rem;
        padding: 0.75rem;
        width: 100%;
        max-width: 300px;
        border: 3px solid #21A5C3;
        border-radius: 12px;
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
  </style>
  