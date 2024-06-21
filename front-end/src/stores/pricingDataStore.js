// stores.js
import { writable } from 'svelte/store';

export const pricingDataStore = writable({
  pricingByWeight: [],
  pricingByVolume: []
});