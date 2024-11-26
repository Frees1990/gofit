/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

// Extract Stripe public key and client secret from the template
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

// Log the public key and client secret for debugging
console.log("Stripe Public Key:", stripe_public_key);
console.log("Client Secret:", client_secret);

// Initialize Stripe with the public key
var stripe = Stripe(stripe_public_key);
console.log("Stripe initialized:", stripe);

// Create an instance of Stripe Elements
var elements = stripe.elements();
console.log("Stripe Elements instance created:", elements);

// Define styles for the card element
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

// Create the card element with styles
var card = elements.create('card', { style: style });
console.log("Card Element created:", card);

// Mount the card element to the DOM
try {
    card.mount('#card-element');
    console.log("Card Element mounted successfully.");
} catch (error) {
    console.error("Error mounting Card Element:", error);
}
