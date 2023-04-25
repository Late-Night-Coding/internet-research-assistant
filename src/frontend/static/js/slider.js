let sentenceLength = 3;

// Retrieve the sentence length browser cookie
const SENTENCE_LENGTH_KEY = "sentence-length";
let storedSentenceLength = localStorage.getItem(SENTENCE_LENGTH_KEY);
if(storedSentenceLength){
    sentenceLength = parseInt(storedSentenceLength);
}

// When the body loads, register an event listener for the slider
addEventListener('load', ()=>{
    const slider = document.getElementById('summary-len');
    const sentLengthLabel = document.getElementById('sentence-length-label');

    // initialize the slider with stored value
    slider.value = sentenceLength;

    // when the slider value changes, display the new summary length
    function update(){
        sentenceLength = parseInt(slider.value);
        sentLengthLabel.innerText = `${sentenceLength} sentence`;
        if(sentenceLength > 1)
            sentLengthLabel.innerText += 's';
        
        // save the value
        window.localStorage.setItem(SENTENCE_LENGTH_KEY, sentenceLength+"");
    }
    slider.addEventListener('input', update);
    update();

    // update the slider's position when the mouse moves
    addEventListener('mousemove', (e)=>{
        sentLengthLabel.style.left = e.pageX + "px";
        sentLengthLabel.style.top = (e.pageY + 15) + "px";
    });

});
