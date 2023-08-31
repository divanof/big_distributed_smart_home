var xhr = new XMLHttpRequest();
xhr.open("POST", "/api/lightlamp/1/", true);
xhr.setRequestHeader('Content-Type', 'application/json');
var data = JSON.stringify({
  from: "user",
  value: 0
});
xhr.send(data);