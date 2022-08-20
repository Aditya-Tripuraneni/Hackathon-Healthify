function imgsplit() {
    $("#splitform").append("<input type = 'file' name = 'myfile' id='myfile'>")
    $("#mos").val('1');
    $("#myfile").attr('value', '1')

}
function ammsplit() {
    $("#splitform").append('<input type="text" placeholder="Amount of bill" name="ammount">')
    $("#mos").attr('value', '2');
}
let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");

closeBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();
});

searchBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    menuBtnChange();
});

console.log(Cookies.get('csrftoken'));