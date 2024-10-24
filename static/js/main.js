/**
 * Function to get the screen size width and height.
 * @returns {object} - Object containing the screen width and height.
 */

function getScreenSize() {
    return {
        width: window.innerWidth,
        height: window.innerHeight
    };

}


/**
 * Auth layout function to set the height of the auth layout.
 * @param {number} windowHeight - The height of the window.
 * @param {number} windowWidth - The height of the header.
 */

function setAuthLayoutHeight(windowHeight, windowWidth) {
    const form = document.querySelector('#auth-layout__form');
    const image = document.querySelector('#auth-layout__image');

    if (!form || !image) return;

    if (windowWidth > 768) {
        form.style.width = `${windowWidth + (windowWidth / 2)}px`;
        image.style.width = `${windowWidth - (windowWidth / 2)}px`;

        form.style.height = `${windowHeight}`
        image.style.height = `${windowHeight}`
    } else {
        form.style.height = 'auto';
        image.style.height = 'auto';
    }
}


/**
 * Set the home layout height.
 * @param {number} windowHeight - The height of the window.
 * @param {number} windowWidth - The height of the header.
 */

function setHomeLayoutHeight(windowHeight, windowWidth) {
    const homeLayout = document.querySelector('#home-layout__banner');
    const homeContent = document.querySelector('#home-layout__content');

    if (!homeLayout || !homeContent) return;

    if (windowWidth > 768) {
        console.log(windowHeight);
        homeLayout.style.height = `${windowHeight}px`;
        homeContent.style.height = `${windowHeight}px`;
    } else {
        homeLayout.style.height = 'auto';
        homeContent.style.height = 'auto';
    }

}

// Invoke the function to set the height of the auth layout.
const { width, height } = getScreenSize();
setAuthLayoutHeight(height, width);
setHomeLayoutHeight(height, width);


// Invoke the function when window resize.
window.addEventListener('resize', (e) => {
    const { width, height } = getScreenSize();
    setAuthLayoutHeight(height, width);
    setHomeLayoutHeight(height, width);
})
