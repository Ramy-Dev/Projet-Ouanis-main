<script context="module">
  export async function load({ params }) {
    const { id } = params;
    console.log(`Fetching ad details for ID: ${id}`); // Log the ID being fetched

    try {
      const response = await fetch(`http://127.0.0.1:8000/annonces/${id}`);

      if (!response.ok) {
        console.error(`Failed to fetch ad details: ${response.statusText}`);
        return {
          props: {
            ad: null,
            error: `Failed to fetch ad details: ${response.statusText}`
          }
        };
      }

      const ad = await response.json();
      console.log('Fetched ad:', ad); // Log the fetched ad details

      return {
        props: {
          ad
        }
      };
    } catch (error) {
      console.error('An error occurred while fetching ad details:', error);
      return {
        props: {
          ad: null,
          error: 'An error occurred while fetching ad details'
        }
      };
    }
  }
</script>

<script>
  export let ad;
  export let error;
</script>

<main>
  {#if error}
    <div class="error-message">
      <p>{error}</p>
    </div>
  {:else if ad}
    <div class="ad-details">
      <h1>{ad.name}</h1>
      <p>DOB: {ad.dob}</p>
      <p>From: {ad.from}</p>
      <p>To: {ad.to}</p>
      <p>Date: {ad.date}</p>
      <p>Last Updated: {ad.updated}</p>
      <!-- Add more details as needed -->
    </div>
  {:else}
    <div class="loading-message">
      <p>Loading ad details...</p>
    </div>
  {/if}
</main>

<style>
  /* Add some styles for the details page */
  .ad-details {
    padding: 20px;
  }
  .error-message {
    color: red;
  }
  .loading-message {
    color: blue;
  }
</style>
