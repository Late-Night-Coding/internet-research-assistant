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

let menuShown = false;
const scopes = document.querySelectorAll(".searchResult");
var menu = document.querySelector(".menu");
let selectedText = "";

for(s of scopes){
    s.addEventListener("mouseup", () => {

        let selection = document.getSelection();
        let selectedText = selection.toString();

        if (selectedText.length > 0) {

            if(selectedText.charCodeAt(0) < 31){
                console.log(selectedText.charCodeAt(0) );
                if(selectedText.charCodeAt(0) < 31){
                    menu.style.display = "none";
                }

            } else{
                menu.style.display = "block";
                updateMenuLocation();    

                var lookupbtn = document.getElementById("lookup-btn");
        
                document.addEventListener("click", function(event){
    
                    if(event.target == lookupbtn){
                        performSearch(currInputQuery + ' ' + selectedText);
                        menu.style.display = "none";
                    } 
                });
            }
    
        } else {
            menu.style.display = "none";
            console.log("Selected text length 0: " + selectedText);
        }
    });
    
}

window.addEventListener("mouseup", (e) => {

    let selectedText = window.getSelection().toString();

    if(selectedText == ""){
        menu.style.display = "none";
        window.getSelection().removeAllRanges();
    }
});

function updateMenuLocation(){
    const range = window.getSelection().getRangeAt(0);
    const rect = range.getBoundingClientRect();
    menu.style.top = rect.top + window.pageYOffset - 40 + 'px';
    menu.style.left = rect.left + window.pageXOffset + 'px';
}

window.addEventListener("resize", function(){
    updateMenuLocation();
});

const circleInfoIcon = document.querySelector('#info-icon');

circleInfoIcon.addEventListener('click', function() {
    console.log("icon clicked");
});