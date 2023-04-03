// Get HTML elements
const donationCategory = document.querySelector('#donation-category');
const utilitiesForm = document.querySelector('#utilities-form');
const utilitiesDonationForm = document.querySelector('#utilities-donation-form');
const cart = document.querySelector('#cart');
const cartItems = document.querySelector('#cart-items');
const cartTotal = document.querySelector('#cart-total');
const cartProceedButton = document.createElement('button');
cartProceedButton.innerText = 'Proceed to Payment';
cartProceedButton.style.display = 'none'; // Hide the button by default


// Set prices for grains and books
const grainPrices = {
  rice: 50,
  wheat: 40,
  corn: 30,
};
const bookPrices = {
  textbook: 200,
  novel: 150,
  comic: 50,
};

// Set event listener for donation category select
donationCategory.addEventListener('change', function () {
  // Hide all donation forms
  utilitiesForm.classList.add('hidden');

  // Show the selected donation form
  if (donationCategory.value === 'utilities') {
    utilitiesForm.classList.remove('hidden');
  }
});

// Set event listener for utilities donation form submit
utilitiesDonationForm.addEventListener('submit', function (event) {
  event.preventDefault();

  // Get form inputs
  const moneyDonation = Number(document.querySelector('#money-donation').value);
  const grainDonation = document.querySelector('#grain-donation').value;
  const grainDonationQuantity = Number(document.querySelector('#grain-donation-quantity').value);
  const bookDonation = document.querySelector('#book-donation').value;
  const bookDonationQuantity = Number(document.querySelector('#book-donation-quantity').value);

  // Add donation items to cart
  let cartItemHTML = '';
  let total = 0;
  if (moneyDonation) {
    cartItemHTML += `<li>Money Donation: Rs. ${moneyDonation}</li>`;
    total += moneyDonation;
  }
  if (grainDonation && grainDonationQuantity) {
    const grainPrice = grainPrices[grainDonation];
    const donationAmount = grainPrice * grainDonationQuantity;
    cartItemHTML += `<li>${grainDonation} (${grainPrice}/kg) x ${grainDonationQuantity}: Rs. ${donationAmount}</li>`;
    total += donationAmount;
  }
  if (bookDonation && bookDonationQuantity) {
    const bookPrice = bookPrices[bookDonation];
    const donationAmount = bookPrice * bookDonationQuantity;
    cartItemHTML += `<li>${bookDonation} (${bookPrice}): Rs. ${donationAmount}</li>`;
    total += donationAmount;
  }

  // Update cart HTML
  cartItems.innerHTML = cartItemHTML;
  cartTotal.innerHTML = `Total: Rs. ${total}`;

  // Show cart
  cart.classList.remove('hidden');

  // Reset form
 cart.appendChild(cartProceedButton);
   
 
});
