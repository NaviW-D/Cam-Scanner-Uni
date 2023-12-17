getData = async () => {
  response = await fetch(`http://localhost:8000/${tag.value}`)
  response = await response.json()
  console.log(response)
  if (response.status){
    notif.classList.add("success")
    notif.classList.remove("d-none")
    notif.classList.remove("error")
    notif.textContent = "can pass"
  }
  else{
    notif.classList.add("error")
    notif.classList.remove("d-none")
    notif.classList.remove("success")
    notif.textContent = "can't pass"
  }
    
};

tag = document.getElementById("plate_number")
btn = document.getElementById("submit");
notif = document.getElementById("notif")
btn.onclick = getData;
