<script>
  import { onMount } from 'svelte';

  let user = "";
  let username = "";
  onMount(() => {
    user = JSON.parse(localStorage.getItem('user'));
  });
  
  $: username = user && user[0] && user[0].username ? user[0].username : "";

  // Add your code here

</script>

<!-- Rest of the code -->
<!-- svelte-ignore non-top-level-reactive-declaration -->
<main>
  <nav class="navbar fixed navbar-expand-lg bg-body-tertiary fontPrimary">
    <div class="container-fluid">
      <a class="navbar-brand" href="/">
      <img class="image_nav" src="../svg/logo-navbar.svg" alt="">
    </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link text-darkPrimary" href="/recherche">Recherche</a>
          </li>
          <!-- <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="/" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  Dropdown
                </a>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="/">Action</a></li>
                  <li><a class="dropdown-item" href="/">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="/">Something else here</a></li>
                </ul>
              </li> -->
          <!-- <li class="nav-item">
                <a class="nav-link disabled" href="/" aria-disabled="true">Disabled</a>
              </li> -->
        </ul>
        <ul class="SignUp-LogIn d-flex m-0 p-0">
          <li class="text-primary fw-bold nav-link" >
           {username}
          </li>
          <li>
            <a class="LogIn fw-semibold nav-link bg-primary" href="/creation">Créer une annonce +</a>
          </li>
          <li>
            <a class="fw-semibold d-flex nav-link" href="/profil">
              <lord-icon
                src="https://cdn.lordicon.com/hrjifpbq.json"
                trigger="hover"
                colors="primary:#0D434F"
                style="width:40px;height:40px">
              </lord-icon>
            </a>
          </li>
          <li>
            <a class="SignUp fw-semibold nav-link text-primary" href="/sign-up">Sign up</a>
          </li>
          <li>
            <a class="LogIn fw-semibold nav-link bg-primary" href="/log-in">Log in</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</main>

<style>
  nav {
    padding: 10px 10px;
    z-index: 9999;
    width: 100%;
  }
  .image_nav {
    width: 200px;
  }
  .SignUp {
    background-color: transparent;
    border: 3px dashed #21A5C3;
    align-items: center;
    border-radius: 5px;
    padding: 7px 10px;
  }
  .LogIn {
    color: white;
    border-radius: 5px;
    padding: 10px;
  }
  .SignUp-LogIn {
    gap: 20px;
  }
  li {
    list-style: none;
    align-self: center;
  }
</style>
