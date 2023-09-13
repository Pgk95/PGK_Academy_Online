const slideshowText = document.getElementById("typed-text");
const texts = ["Welcome", "your gateway to a world of learning.", "embrace your future",];
let charIndex = 0;
let textIndex = 0;

function type() {
    if (charIndex < texts[textIndex].length) {
        slideshowText.textContent += texts[textIndex].charAt(charIndex);
        charIndex++;
        setTimeout(type, 50);
    } else {
        setTimeout(erase, 1500);
    }
}

function erase() {
    if (charIndex > 0) {
        slideshowText.textContent = texts[textIndex].substring(0, charIndex - 1);
        charIndex--;
        setTimeout(erase, 30);
    } else {
        textIndex = (textIndex + 1) % texts.length;
        setTimeout(type, 1000);
    }
}

type();