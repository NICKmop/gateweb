// -----------------------------
//  custom
// -----------------------------
const btnArr = document.getElementsByTagName('button');
const navLink = document.getElementsByClassName('nav-link');

function menuBoxScroll (className) {
    console.log("className : ", className);
    return document.getElementById(className);
}

for(let i = 0; i < btnArr.length; i++){
    btnArr[i].addEventListener('click',function(e){
        if (i == 1) {
            document.getElementById('service-2-scroll').scrollLeft -= 450;
        }else{
            document.getElementById('service-2-scroll').scrollLeft += 450;
        }
});
}
for (let i = 0; i < navLink.length; i++)     {
    navLink[i].addEventListener('click', function(params) {
       console.log("click : ", this.text); 
       if (this.text == 'About Us') {
        window.scrollBy({top: menuBoxScroll('aboutUs').getBoundingClientRect().top, behavior: 'smooth'})
       }else if(this.text == '메인페이지'){
        window.scrollBy({top: menuBoxScroll('navbarDropdown').getBoundingClientRect().top, behavior: 'smooth'})
       }else if(this.text == 'Contact'){
        window.scrollBy({top: menuBoxScroll('Contact').getBoundingClientRect().top, behavior: 'smooth'})
       }

       
    });
}