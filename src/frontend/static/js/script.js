const input = document.querySelector('input[name="query"]');
const currInputQuery = input.value;

// Get the search form and its input element
const searchForm = document.querySelector('.searchbar form');
const searchInput = searchForm.querySelector('input[name="query"]');

// Function to perform lookup search
function performSearch(query) {
  searchInput.value = query; // set the value of the search input to the query
  searchForm.submit();
}

// global vars to keep track of menu
let menuShown = false;
const scopes = document.querySelectorAll(".searchResult");
var menu = document.querySelector(".menu");
let selectedText = "";

// Display menu when user selects text in a search result
for(s of scopes){
    s.addEventListener("mouseup", () => {

        let selection = document.getSelection();
        selectedText = selection.toString();

        // if text is selected, validate the selection and show the menu
        if (selectedText.length > 0) {

            if(selectedText.charCodeAt(0) < 31){
                console.log(selectedText.charCodeAt(0) );
                if(selectedText.charCodeAt(0) < 31){
                    menu.style.display = "none";
                }
            } else{
                menu.style.display = "block";
                updateMenuLocation();    
            }

        // if no text selected, hide menu
        } else {
            menu.style.display = "none";
        }
    });
}

// perform search when button is pressed
const lookupbtn = document.getElementById("lookup-btn");
document.addEventListener("click", function(event){

    if(event.target == lookupbtn){
        performSearch(currInputQuery + ' ' + selectedText);
        menu.style.display = "none";
    } 
});

// When the user clicks to clear the selection, hide the menu
window.addEventListener("mouseup", (e) => {

    let selectedText = window.getSelection().toString();

    if(selectedText == ""){
        menu.style.display = "none";
        window.getSelection().removeAllRanges();
    } 
});

// Set the menu's position to the position of the selection
function updateMenuLocation(){
    const range = window.getSelection().getRangeAt(0);
    const rect = range.getBoundingClientRect();
    menu.style.top = rect.top + window.pageYOffset - 40 + 'px';
    menu.style.left = rect.left + window.pageXOffset + 'px';
}

// Update the menu position when the window is resized
window.addEventListener("resize", function(){
    updateMenuLocation();
});

// Info icon
const circleInfoIcon = document.querySelector('#info-icon');
circleInfoIcon.addEventListener('click', function() {
    console.log("icon clicked");
});