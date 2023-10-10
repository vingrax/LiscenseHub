// Store the cache object globally
var searchCache = {};
var debounce = function(fn, t) {
  let timeout;
  return function(...args) {
      clearTimeout(timeout);
      timeout = setTimeout(()=>fn(...args),t);
  };
};

const debouncedSearch = debounce(search,750);
function fetchall() {  
  var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/manage/search/', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.setRequestHeader('X-CSRFToken', csrfToken);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var devices = JSON.parse(xhr.responseText);
      displayDevices(devices); // Call a function to display the devices
     
    }
  };
  
  var requestData = JSON.stringify({
    'searchInput': '',
    'searchType': ''
  });
  xhr.send(requestData);
}
fetchall()
function search() {
  var searchInput = document.getElementById('input').value;
  var searchType = document.querySelector('input[name="btn"]:checked').value;
  var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  var screen = document.getElementById('main')
  screen.innerHTML =  ''
  // Check if the result is already cached
  if (searchCache[searchInput + searchType]) {
    var devices = searchCache[searchInput + searchType];
    displayDevices(devices); // Use the cached result
   
    return;
  }
  
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/manage/search/', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.setRequestHeader('X-CSRFToken', csrfToken);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var devices = JSON.parse(xhr.responseText);
      searchCache[searchInput + searchType] = devices; // Cache the result
      displayDevices(devices); // Call a function to display the devices
      
    }
  };
  
  var requestData = JSON.stringify({
    'searchInput': searchInput,
    'searchType': searchType
  });
  xhr.send(requestData);
}

function displayDevices(devices) {
  var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
  var devicesContainer = document.getElementById('screen');
  devicesContainer.innerHTML = ''; // Clear the container before updating with new devices

  for (var i = 0; i < devices.length; i++) {
    var device = devices[i];
    var deviceElement = document.createElement('div');
    deviceElement.className = 'container';

    var boxElement = document.createElement('div');
    boxElement.className = 'box';
    
    var dnsNameElement = document.createElement('span');
    dnsNameElement.innerHTML = device.dns_name;
    dnsNameElement.className = 'title'
    
    var ipElement = document.createElement('strong');
    var deviceIP = document.createElement('input');
    deviceIP.className = "deviceIP";
    deviceIP.hidden = "true";
    deviceIP.value = device.ip;

    ipElement.innerHTML = device.ip;
    ipElement.id = device.ip;
    deviceElement.appendChild(boxElement);
    deviceElement.appendChild(deviceIP);

    boxElement.appendChild(dnsNameElement);
    boxElement.appendChild(ipElement);
    deviceElement.addEventListener('click',function() {
      var IP = this.getElementsByClassName('deviceIP')[0].value;     
      window.location.href='/manage/device/'+String(IP)+'/manage_license/'          
    });
    devicesContainer.appendChild(deviceElement);
  }
}


