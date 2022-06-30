// -----------------------------
//  custom
// -----------------------------
const btnArr = document.getElementsByTagName('button');

for(let i = 0; i < btnArr.length; i++){
    btnArr[i].addEventListener('click',function(e){
        if (i == 1) {
            document.getElementById('service-2-scroll').scrollLeft -= 450;
        }else{
            document.getElementById('service-2-scroll').scrollLeft += 450;
        }
});
}