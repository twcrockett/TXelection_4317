/* index.js */

// Initialize and add the map
function initMap() {
  // The location of Texas
  const texas = { lat: 31.9686, lng: -99.9018 };
  // The map, centered at Texas
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 3,
    center: texas,
  });
}

window.initMap = initMap;

function clickGo()
	{
	document.getElementById('go').onclick=function(){
		document.getElementById('infopane').style.display='block';
	};
	

document.getElementById('infopane').style.display = 'none';

document.getElementById('go').onclick=function(){
	document.getElementById('infopane').style.display='block';
};

document.getElementById('info').innerHTML = Date()