<script>
   import { onMount } from "svelte";
   import ColorGenerator from "../../components/colorGenerator.svelte";
   import { getRandomColor } from "../../lib/functions/randomColor.js";
   import SearchForm from "../../components/Recherche/SearchForm.svelte";
   import AdCard from "../../components/AdCard.svelte";
   import { fakeUsers } from "../../lib/generatedUsers.js";

   let ads = fakeUsers;
   let annonces = [];
   let currentPage = 1;
   const itemsPerPage = 12; // 3 rows of 3 ads
   let totalPages = Math.ceil(ads.length / itemsPerPage);

   async function get_annonce() {
      try {
         const response = await fetch("http://127.0.0.1:8000/recherche/", {
            method: "GET",
            headers: {
               "Content-Type": "application/json",
            },
         });

         if (!response.ok) {
            throw new Error(`An error has occurred: ${response.status}`);
         }

         annonces = await response.json();
         annonces = annonces.map(annonce => ({
            ...annonce,
            created_at: annonce.created_at.split('T')[0],
            updated_at: annonce.updated_at.split('T')[0]
         }));
         totalPages = Math.ceil(annonces.length / itemsPerPage);
      } catch (error) {
         console.error("Error:", error);
      }
   }

   function nextPage() {
      if (currentPage < totalPages) {
         currentPage += 1;
         // scrollToAnnonces();
         animateSVG(false, -1);
      }
   }

   function prevPage() {
      if (currentPage > 1) {
         currentPage -= 1;
         // scrollToAnnonces();
         animateSVG(false, 1);
      }
   }

   function scrollToAnnonces() {
      document.querySelector('.search-container').scrollIntoView({ behavior: 'smooth' });
   }

   $: paginatedAds = ads.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);

   onMount(() => {
      get_annonce();
      const cards = document.querySelectorAll(".cardAnnonce");
      cards.forEach((card) => {
         const cardColor = getRandomColor();
         const colorTopElement = card.querySelector(".colorTopAnnonce");
         colorTopElement.style.backgroundColor = cardColor;
      });
   });

   // SVG animation function
   function animateSVG(reset = true, side) {
      const svgContainer = document.getElementById('svg-bg');
      let currentTransform = svgContainer.style.transform.match(/translateX\((-?\d+)px\)/);
      let currentX = currentTransform ? parseInt(currentTransform[1], 10) : 0;
   
      if (side === 1) {
          currentX -= 50; // Move the SVG to the right
      } else if (side === -1) {
          currentX += 50; // Move the SVG to the left
      }
   
      svgContainer.style.transform = `translateX(${currentX}px)`;
   
      if (reset) {
          setTimeout(() => {
               // Reset the SVG position after a short delay for visual effect
               svgContainer.style.transform = '';
          }, 1000); // Match this duration with the CSS transition duration
      }
   }
</script>

<main class="bg-main">
   <img id="svg-bg" class="image_bg_recherche_ads" src="../svg/bg-recherche-ads.svg">
   <div class="header">
      <div class="recherche_cover">
         <img class="image_bg_recherche" src="../svg/bg_recherche.svg">
         <div class="textIntro text-white fontSecondary">
            Explorez des milliers d'annonces en toute <span class="simpl-text">simplicité</span>
         </div>
         <div class="search-container">
            <SearchForm />
         </div>
      </div>
   </div>
   <section class="section-annonces">
      <div class="textAnnonces text-secondary fontSecondary">
         annonces trouvées
      </div>
      <div class="ads-container">
         {#each paginatedAds as ad}
            <AdCard {ad} />
         {/each}
      </div>
      <div class="pagination fontSecondary">
         <button class="btnPage fontPrimary" on:click={() => { prevPage(); }} disabled={currentPage === 1}>
            <lord-icon
               class="animated-arrow animated-arrow-left"
               src="https://cdn.lordicon.com/vduvxizq.json"
               colors="primary:white"
               style="background-color: none;"
               trigger="hover">
            </lord-icon>
         </button>
         <span>Page <span class="text-primary">{currentPage}</span> sur {totalPages}</span>
         <button id="nextPageBtn" class="btnPage fs-3 fontPrimary" on:click={() => { nextPage();}} disabled={currentPage === totalPages}>
            <lord-icon
               class="animated-arrow"
               src="https://cdn.lordicon.com/vduvxizq.json"
               colors="primary:white"
               style="background-color: none;"
               trigger="hover">
            </lord-icon>
         </button>      
      </div>
   </section>
   <img class="image_bottom" src="../svg/bottom_recherche.svg">
</main>

<style>
   html, body {
   height: 100%;
   margin: 0;
   padding: 0;
}

body {
   display: flex;
   flex-direction: column;
}

main {
   flex: 1;
   position: relative;
   display: flex;
   flex-direction: column;
   justify-content: space-between; /* This ensures that the footer image is pushed to the bottom */
}

#svg-bg {
   transition: transform 2s ease;
}

.bg-main {
   position: relative;
   overflow: hidden;
   margin: 0;
}

.header {
   margin-top: 0;
   position: relative;
   height: 50vh;
}

.recherche_cover {
   position: relative;
   width: 100%;
   height: 100%;
   display: flex;
   flex-direction: column;
   justify-content: center;
   align-items: center;
   padding: 100px;
   gap: 30px;
}

.image_bg_recherche {
   width: 100%;
   height: 100%;
   object-fit: cover;
   position: absolute;
   top: 0;
   left: 0;
   z-index: -1;
}

.image_bg_recherche_ads {
   margin-top: 20%;
   width: 120%;
   height: 100%;
   object-fit: cover;
   position: absolute;
   top: -10%;
   left: -10%;
   z-index: -2;
   transition: transform 0.5s ease;
}

.image_bottom {
   width: 100%;
   z-index: -1;
}

.textIntro {
   margin-top: 90px;
   font-size: 3rem;
   font-weight: 700;
   text-align: center;
}

.textAnnonces {
   margin-top: 50px;
   font-size: 3rem;
   font-weight: 700;
   text-align: center;
}

.simpl-text {
   font-size: 3rem;
   font-weight: 700;
   color: #FFFFFF;
   text-shadow: 
      -1px -7px 0 #4FE1F9,
      1px -1px 0 #40c5de,
      -1px 1px 0 #40c5de,
      1px 7px 0 #4FE1F9;
}

.search-container {
   position: relative;
   display: flex;
   flex-direction: column;
   align-items: center;
}

.section-annonces {
   padding: 0 80px;
   position: relative;
   flex: 1;
}

.ads-container {
   display: flex;
   flex-wrap: wrap;
   justify-content: center;
   margin-top: 10px;
}

.pagination {
   display: flex;
   justify-content: center;
   align-items: center;
   gap: 10px;
   margin-top: 20px;
}

.pagination button {
   appearance: none;
   border: 0;
   border-radius: 12px;
   background-color: #21A5C3;
   color: white;
   padding: 0px 20px;
   font-size: 1rem;
   cursor: pointer;
   box-shadow: 0 7px 4px 0 rgba(0, 0, 0, 0.29);
   transition: background-color 0.3s ease;
}

.pagination button:hover {
   background-color: #4FE1F9;
}

.pagination button:disabled {
   background-color: #0D434F;
   cursor: not-allowed;
}

.pagination button:disabled:hover {
   background-color: #0D434F;
}

.btnPage {
   display: flex;
}

.pagination span {
   font-size: 1.2rem;
   font-weight: 600;
}

.animated-arrow-left {
   transform: rotate(180deg);
}

</style>
