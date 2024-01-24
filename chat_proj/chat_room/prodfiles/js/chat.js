const modal = document.getElementById("postModal");

const openbtn = document.getElementById("openCreatorBtn");

const closespan = document.getElementsByClassName("close")[0];

openbtn.onclick = function() {
    console.log("Hello")
    modal.style.display = "block";
}

closespan.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}