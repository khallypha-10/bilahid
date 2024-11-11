const toLocationData = document.getElementById("toLocationData");

function handleToLocation() {
  let locationEl = "";
  const toInput = document.getElementById("to").value;
  
  if (toInput.length > 1) {
    fetch(`select_destination/${toInput}`)
      .then((response) => response.json())
      .then((data) => {
        const toLocationArray = data.data;

        if (toLocationArray && toLocationArray.length > 0) {
          toLocationData.style.display = "block";
          
          // Iterate through the locations and build the HTML structure
          toLocationArray.map((location) => {
            locationEl += `
              <div class="card mb-3 mt-3" onclick="getToLocation('${location.iataCode}')">
                <div class="card-header"><b>Name:</b> ${location.name}</div>
                <div class="card-body">
                  City Name: ${location.address.cityName}<br />
                  Country Name: ${location.address.countryName}
                </div>
                <div class="card-footer">
                  <b>SubType:</b> ${location.subType}
                </div>
              </div>`;
          });
          
          // Update the innerHTML of the toLocationData element
          toLocationData.innerHTML = locationEl;
        } else {
          // Hide the location data if no results are found
          toLocationData.style.display = "none";
        }
      })
      .catch((error) => {
        console.error("Error fetching location data:", error);
        toLocationData.style.display = "none"; // Hide the location data on error
      });
  } else {
    toLocationData.style.display = "none"; // Hide the location data if input is too short
  }
}


function getToLocation(regionCode) {
    // Set the selected location code
    const destinationCode = regionCode;

    // Perform any action you want with the destinationCode
    // For example, display a message or redirect to another page
    console.log('Selected location code:', destinationCode);

    // Optionally hide the location data
    toLocationData.style.display = "none";

    // Display a message or redirect (example)
    alert(`You selected location with code: ${destinationCode}`);
    // or
    // window.location.href = `/some/path?destination=${destinationCode}`;
}

const flightData = document.getElementById("flightData");

// Function to handle flight search and display
function handleFindFlight() {
  const departureDate = document.getElementById("date").value;
  let flightEl = "";

  // Fetch flight data from the backend
  fetch(`search_offers/?originCode=${originCode}&destinationCode=${destinationCode}&departureDate=${departureDate}`)
    .then(response => response.json())
    .then(data => {
      const flights = data.data;

      if (flights && flights.length > 0) {
        flights.forEach(flight => {
          flightEl += `
            <div class="card mb-3 mt-3">
              <div class="card-header">
                <b>Price:</b> ${flight.price.total} (${flight.price.currency})
              </div>
              <div class="card-body">
                Number of Seats Available: ${flight.numberOfBookableSeats}
                <br />
                Last Ticketing Date: ${flight.lastTicketingDate}
                <hr />
                <h5>Itineraries</h5>
                Duration: ${flight.itineraries[0].duration}
                <hr />
                <h5>Enter your details:</h5>
                <input type="text" id="first" placeholder="Your First Name" class="form-control"/>
                <br />
                <input type="text" id="last" placeholder="Your Last Name" class="form-control"/>
              </div>
              <div class="card-footer">
                <button class="btn btn-warning" onclick='BookFlight(${JSON.stringify(flight)})'>Book Flight</button>
              </div>
            </div>
          `;
        });

        // Update the innerHTML of flightData
        flightData.innerHTML = flightEl;
      } else {
        flightData.innerHTML = "<p>No flight data found</p>";
      }
    })
    .catch(error => {
      console.error("Error fetching flight data:", error);
      flightData.innerHTML = "<p>There was an error fetching flight data.</p>";
    });
}

// Function to handle booking logic
function BookFlight(flight) {
  // Implement booking logic here
  console.log('Booking flight:', flight);
}
