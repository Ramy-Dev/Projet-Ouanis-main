// Imports nécessaires
import { writable } from 'svelte/store';


// Store pour les paliers et les prix pour Pricing byWeight
export const poidsPaliersStore = writable([]);
export const prixPaliersStore = writable([]);

// Store pour les paliers et les prix pour Pricing byNumber
export const numberPaliersStore = writable([]);
export const numberPrixPaliersStore = writable([]);

// Store pour les paliers et les prix pour Pricing byVolume
export const volumePaliersStore = writable([]);
export const volumePrixPaliersStore = writable([]);


