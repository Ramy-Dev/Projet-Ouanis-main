<script>
    import { onMount } from 'svelte';
    import { loadStripe } from '@stripe/stripe-js';
    let stripe;
    let clientSecret;
  
    const stripePromise = loadStripe('your-publishable-key-here');
  
    onMount(async () => {
      await fetchClientSecret();
    });
  
    async function fetchClientSecret() {
      const response = await fetch('http://localhost:8000/create-payment-intent/', { // Use absolute URL
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Token your-auth-token',
        },
        body: JSON.stringify({
          annonce_id: 1,  // Replace with your annonce ID
          amount: 10.00,  // Replace with your amount
          currency: 'usd'
        })
      });
      const data = await response.json();
      clientSecret = data.client_secret;
    }
  
    async function handlePayment() {
      stripe = await stripePromise;
      const { error } = await stripe.confirmCardPayment(clientSecret, {
        payment_method: {
          card: elements.create('card'),
          billing_details: {
            name: 'Jenny Rosen',
          },
        },
      });
  
      if (error) {
        console.error(error);
        // Handle error here
      } else {
        // Handle successful payment here
        alert('Payment succeeded!');
      }
    }
  </script>
  
  <button on:click="{handlePayment}">Pay Now</button>
  