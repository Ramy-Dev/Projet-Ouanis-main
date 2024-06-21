<script>
  import TagRecherche from "../../components/Recherche/TagRecherche.svelte";
  import { conditions } from "../../lib/tagList.js";

  let tags = conditions; // replace this with your actual tags
</script>

<main class="fontSecondary">
  <img class="image_bg_recherche_ads" src="../svg/bg-recherche-ads.svg" />
  <div class="containerAnnonce">
    <div class="textAnnonce">L'annonce</div>
    <div class="annonce card-shadow-gray">
      <!--  Top Annonce -->

      <div class="topAnnonce">
        <div class="imageProfile">
          <img src="../svg/image_profil.svg" alt="Photo de profile" />
        </div>
        <div class="trajet text-primary">
          <span class="leftTrajet text-white">Paris</span>
          <span>Alger</span>
        </div>
      </div>

      <!--  Mid Annonce -->

      <div class="midAnnonce">
        <div class="elementAnnonce text-primary">
          Créateur :
          <div class="dataElement text-basic">username</div>
        </div>
        <div class="elementAnnonce text-primary">
          Date :
          <div class="dataElement text-basic">xx/xx/xxxx</div>
        </div>
        <div class="elementAnnonce text-primary">
          Poids Max :
          <div class="dataElement text-basic">xx kg</div>
        </div>
        <div class="elementAnnonce text-primary">
          Volume Max :
          <div class="dataElement text-basic">x.x m³</div>
        </div>
      </div>

      <!--  Main Annonce -->

      <div class="mainAnnonce">
        <div class="leftMain">
          <div class="inputPoids">
            <label class="text-basic" for="poids">Poids du bagage :</label>
            <input
              type="number"
              id="poids"
              name="poids"
              min="0"
              placeholder="entrez le poids"
            />
          </div>
          <div class="tarif">
            <label class="text-basic" for="poids">Tarifs :</label>
            <div class="displayTarif text-white">5€ / kg</div>
          </div>
        </div>
        <div class="rightMain">
          <div class="conditions">
            <label class="text-basic" for="poids">Conditions :</label>
            <div class="displayConditions text-white">
              {#each tags as tag}
                <TagRecherche name={tag} />
              {/each}
            </div>
          </div>
        </div>
      </div>

      <!--  Bottom Annonce -->

      <div class="bottomAnnonce">
        <img class="planeImage" src="../svg/plane.svg" alt="plane" />
        <div class="prixFinal">
          <label class="text-basic" for="poids">Prix final :</label>
          <div class="displayPrix text-light">25€</div>
        </div>
        <div class="reserveButton">
          <button>reserve</button>
        </div>
      </div>
    </div>
  </div>
</main>

<style>
main {
   flex: 1;
   position: relative;
   display: flex;
   flex-direction: column;
   justify-content: space-between; /* This ensures that the footer image is pushed to the bottom */
   height: 200vh;
   width: 100vw;
  }
  label {
    font-size: 1.3rem;
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
  .containerAnnonce {
    margin: 100px;
  }
  .textAnnonce {
    font-size: 2.5rem;
    text-align: center;
  }
  .annonce {
    width: 85%;
    margin: auto;
    margin-top: 50px;
    display: flex;
    flex-direction: column;
    padding: 60px 80px;
    border-radius: 40px;
    background-color: #ffffff;
    gap: 80px;
  }

  .topAnnonce {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }

  .trajet {
    width: 55%;
    display: flex;
    justify-content: space-between;
    border: 4px solid #21a5c3;
    border-radius: 50px;
    font-size: 2rem;
    padding-right: 50px;
    align-items: center;
  }
  .leftTrajet {
    background-color: #21a5c3;
    width: 45%;
    padding: 25px 50px;
    border-top-left-radius: 40px;
    border-bottom-left-radius: 40px;
    border-top-right-radius: 50px;
    border-bottom-right-radius: 50px;
  }

  .midAnnonce {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-template-rows: repeat(2, 1fr);
    grid-column-gap: 100px;
    grid-row-gap: 30px;
  }

  .elementAnnonce {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    align-items: baseline;
    font-size: 1.5rem;
  }
  .dataElement {
    margin-left: 20px;
    font-size: 1.3rem;
  }

  .mainAnnonce {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: flex-start;
  }
  /* Left Main */

  .leftMain {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 50px;
  }

  .inputPoids {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 25px;
  }
  .inputPoids input {
    flex: 1;
    padding: 0.75rem 1rem;
    margin-left: 20px;
    width: 300px;
    font-size: 1.1rem;
    border-radius: 16px;
    text-align: center; /* Centrer le contenu */
    border: 3px solid #21a5c3;
    background: none;
    color: #21a5c3;
    transition: border 0.3s ease; /* Add this line */
  }
  .inputPoids input::placeholder {
    color: #21a5c3;
    font-size: 1.2rem;
  }
  .inputPoids input:focus {
    outline: none;
    border: 3px solid #4fe1f9;
  }
  .inputPoids input:hover {
    border: 3px solid #4fe1f9;
  }
  .tarif {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 25px;
  }
  .displayTarif {
    padding: 1.75rem 1rem;
    margin-left: 20px;
    width: 300px;
    font-size: 1.5rem;
    border-radius: 16px;
    text-align: center; /* Centrer le contenu */
    background-color: #1a849c;
    transition: background-color 0.3s ease; /* Add this line */
  }
  .displayTarif:hover {
    background-color: #4fe1f9;
  }

  /* Right Main */

  .rightMain {
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 50px;
  }
  .conditions {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 25px;
  }
  .displayConditions {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
    justify-content: flex-start;
    align-items: center;
    padding: 15px 20px 30px 20px;
    gap: 10px;
    border: 4px dashed #4fe1f9;
    border-radius: 20px;
  }

  .bottomAnnonce {
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: end;
  }
  .prixFinal {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: flex-start;
    gap: 25px;
  }
  .displayPrix {
    font-size: 2.5rem;
    padding: 0.75rem 3rem;
    margin-left: 20px;
    border: 4px dashed #4fe1f9;
    border-radius: 20px;
  }
  button {
    flex: 1;

    padding: 0.75rem 3rem;
    font-size: 1.3rem;
    border-radius: 16px;
    text-align: center; /* Centrer le contenu */
    border: 3px solid #4fe1f9;
    background-color: #4fe1f9;
    color: white;
  }
  button:hover {
    background-color: #55e3f8;
    border: 3px solid #55e3f8;
  }
  .planeImage {
    width: 12%;
    position: absolute;
    top: -70%;
    left: 30%;
  }
</style>
