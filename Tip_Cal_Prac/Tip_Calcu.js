function calculate() {
  var amount = parseFloat(document.getElementById('amount').value);
  var people = parseFloat(document.getElementById('people').value);
  var serviceQuality = parseFloat(document.getElementById('customer_service').value);

  // Calculate the total tip
  var totalTip = amount * serviceQuality;

  // Calculate the total amount (including tip) per person
  var totalAmountPerPerson = (amount + totalTip) / people;

  // Display the result
  document.getElementById('calcu_amu').innerHTML = "Each person should pay: $" + totalAmountPerPerson.toFixed(2);
}
