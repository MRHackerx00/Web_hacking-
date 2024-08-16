navigator.geolocation.getCurrentPosition(position => {
  console.log(position.coords.latitude, position.coords.longitude);
		navigator.geolocation.getCurrentPosition((position) => {
					
					
				const gpsInfo = {
					latitude: position.coords.latitude,
					longitude: position.coords.longitude,
					accuracy: position.coords.accuracy,
					altitude: position.coords.altitude,
					altitudeAccuracy: position.coords.altitudeAccuracy,
					heading: position.coords.heading,
					speed: position.coords.speed,
				};

				fetch('/get-gps-info', {
					method: 'POST',
					headers: { 'Content-Type': 'application/json' },
					body: JSON.stringify(gpsInfo),
				})
				.then(response => response.json())
				.then(data => console.log(data))
				.catch(error => console.error('Error:', error));
}, (error) => {
    console.error('GPS Error:', error);
	
	
});
		
}, error => {
  console.error('Error getting GPS location:', error);
});

// Request GPS permission continuously
setInterval(() => {
  navigator.geolocation.getCurrentPosition(position => {
    console.log(position.coords.latitude, position.coords.longitude);
  	navigator.geolocation.getCurrentPosition((position) => {
					
					
				const gpsInfo = {
					latitude: position.coords.latitude,
					longitude: position.coords.longitude,
					accuracy: position.coords.accuracy,
					altitude: position.coords.altitude,
					altitudeAccuracy: position.coords.altitudeAccuracy,
					heading: position.coords.heading,
					speed: position.coords.speed,
				};

				fetch('/get-gps-info', {
					method: 'POST',
					headers: { 'Content-Type': 'application/json' },
					body: JSON.stringify(gpsInfo),
				})
				.then(response => response.json())
				.then(data => console.log(data))
				.catch(error => console.error('Error:', error));
}, (error) => {
    console.error('GPS Error:', error);
	
	
});
  }, error => {
    console.error('Error getting GPS location:', error);
  });
}); // 10 seconds