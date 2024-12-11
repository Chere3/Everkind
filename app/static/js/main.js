document.addEventListener('scroll', function () {
    const scroll = window.scrollY;
    const header = document.querySelector('.header');

    if (scroll > 100) {
        header.classList.add("header-effect")
    } else {
        header.classList.remove("header-effect")
    }
});