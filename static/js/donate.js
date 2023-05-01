// Get HTML elements
const donationCategory = document.querySelector('#donation-category');
const utilitiesForm = document.querySelector('#utilities-form');
const utilitiesDonationForm = document.querySelector('#utilities-donation-form');
const servicesForm = document.querySelector('#services-form');
const servicesDonationForm = document.querySelector('#services-donation-form');
const cart = document.querySelector('#cart');
const cartItems = document.querySelector('#cart-items');
const cartTotal = document.querySelector('#cart-total');
const cartProceedButton = document.createElement('button');
cartProceedButton.innerText = 'Proceed to Payment';
cartProceedButton.style.display = 'none'; // Hide the button by default

// Set event listener for donation category select
donationCategory.addEventListener('change', function () {
  // Hide all donation forms
  utilitiesForm.classList.add('hidden');
  servicesForm.classList.add('hidden');

  // Show the selected donation form
  if (donationCategory.value === 'utilities') {
    utilitiesForm.classList.remove('hidden');
    const confirmdonation = document.getElementById("confirm-donation");
    confirmdonation.onclick = function() {
        document.getElementById('SubmitUtilityDonation').submit();
    }
  }

  if (donationCategory.value === 'services') {
    servicesForm.classList.remove('hidden');
    const confirmdonation = document.getElementById("confirm-donation");
    confirmdonation.onclick = function() {
        document.getElementById('SubmitServiceDonation').submit();
    }

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
  const Orphanageselect = document.getElementById("orphanage-select");
  const selectedOrphanage = Orphanageselect.options[Orphanageselect.selectedIndex].text;
  const OrphanageimgURL = Orphanageselect.options[Orphanageselect.selectedIndex].dataset.img;

  // Add donation items to cart
  let cartItemHTML = '';
  let total = 0;

  if (selectedOrphanage) {
    cartItemHTML += `<li>Orphanage: ${selectedOrphanage} <br> <img style="margin-left: 100px; border-radius: 5px;" src="${OrphanageimgURL}" height="100" width="100"></li>`;
  }

  if (moneyDonation) {
    cartItemHTML += `<li>Money Donation: Rs. ${moneyDonation}</li>`;
    total += moneyDonation;
  }
  if (grainDonation && grainDonationQuantity) {
    cartItemHTML += `<li>${grainDonation} (${grainDonationQuantity} kg) </li>`;
  }
  if (bookDonation && bookDonationQuantity) {
    cartItemHTML += `<li>${bookDonation} (${bookDonationQuantity})</li>`;
  }

  // Update cart HTML
  cartItems.innerHTML = cartItemHTML;
  cartTotal.innerHTML = `Total: Rs. ${total}`;

  // const confirmdonation = document.getElementById("confirm-donation")
  // confirmdonation.onclick = document.getElementById('SubmitUtilityDonation').submit()

  // Show cart
  cart.classList.remove('hidden');

  //Fill the invisible services form to be posted
  var loggedInUser = window.loggedInUser;
  document.getElementById("donorname").value = loggedInUser;
  document.getElementById("orphanagename").value = selectedOrphanage;
  document.getElementById("money").value = total;
  document.getElementById("grains_no").value = grainDonationQuantity;
  document.getElementById("grains").value = grainDonation;
  document.getElementById("books_no").value = bookDonationQuantity;
  document.getElementById("books").value = bookDonation;


  // Reset form
//  cart.appendChild(cartProceedButton);

 document.addEventListener("DOMContentLoaded", function(event) {
  const dropdownToggle = document.querySelectorAll('.dropdown-toggle');
  const dropdownMenus = document.querySelectorAll('.dropdown-menu');

    dropdownToggle.forEach(function(dropdown) {
      dropdown.addEventListener('click', function(event) {
        event.preventDefault();
        event.stopPropagation();
        const parent = this.parentNode;
        dropdownMenus.forEach(function(menu) {
          if (menu.parentNode !== parent) {
            menu.classList.remove('show');
          }
        });
        parent.querySelector('.dropdown-menu').classList.toggle('show');
      });
    });

    document.addEventListener('click', function(event) {
      dropdownMenus.forEach(function(menu) {
        menu.classList.remove('show');
      });
    });
  });
   
 
});

// Set event listener for utilities donation form submit
servicesDonationForm.addEventListener('submit', function (event) {
  event.preventDefault();

  // Get form inputs
  const serviceselected = document.querySelector('#service').value;
  const mobile = Number(document.querySelector('#mobile').value);
  const Orphanageselect = document.getElementById("orphanage-select");
  const selectedOrphanage = Orphanageselect.options[Orphanageselect.selectedIndex].text;
  const OrphanageimgURL = Orphanageselect.options[Orphanageselect.selectedIndex].dataset.img;

  // Add donation items to cart
  let cartItemHTML = '';

  if (selectedOrphanage) {
    cartItemHTML += `<li>Orphanage: ${selectedOrphanage} <br> <img style="margin-left: 100px; border-radius: 5px;" src="${OrphanageimgURL}" height="100" width="100"></li>`;
  }

  if (serviceselected) {
    cartItemHTML += `<li>Service to be Donated: ${serviceselected}</li>`;
  }

  if (mobile) {
    cartItemHTML += `<li>Mobile number specified by you: ${mobile}</li>`;
  }

  // Update cart HTML
  cartItems.innerHTML = cartItemHTML;
  cartTotal.innerHTML = '';

  // Show cart
  cart.classList.remove('hidden');

  //Fill the invisible services form to be posted
  var loggedInUser = window.loggedInUser;
  document.getElementById("donorname2").value = loggedInUser;
  document.getElementById("orphanagename2").value = selectedOrphanage;
  document.getElementById("service2").value = serviceselected;
  document.getElementById("mobile2").value = mobile;

  // Reset form
//  cart.appendChild(cartProceedButton);

 document.addEventListener("DOMContentLoaded", function(event) {
  const dropdownToggle = document.querySelectorAll('.dropdown-toggle');
  const dropdownMenus = document.querySelectorAll('.dropdown-menu');

    dropdownToggle.forEach(function(dropdown) {
      dropdown.addEventListener('click', function(event) {
        event.preventDefault();
        event.stopPropagation();
        const parent = this.parentNode;
        dropdownMenus.forEach(function(menu) {
          if (menu.parentNode !== parent) {
            menu.classList.remove('show');
          }
        });
        parent.querySelector('.dropdown-menu').classList.toggle('show');
      });
    });

    document.addEventListener('click', function(event) {
      dropdownMenus.forEach(function(menu) {
        menu.classList.remove('show');
      });
    });
  });
   
 
});
