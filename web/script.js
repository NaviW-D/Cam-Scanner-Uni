getData = async () => {
  response = await fetch(`http://localhost:8000/${tag.value}`)
  response = await response.json()
  console.log(response)
  if (response.status){
    alert("can pass")
  }
  else{
    alert("can't pass")
  }
    
};

tag = document.getElementById("plate_number")
btn = document.getElementById("submit");
btn.onclick = getData;
