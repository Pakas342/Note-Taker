// Add the show now class to the first tab 

function toggleTabVisibility(tabToShow) {
    document.querySelectorAll(".nav-link").forEach(tab => {
        tab.classList.remove("active");
        tab.setAttribute("aria-selected", "false");
        let searchContentBy = tab.getAttribute("id");
        document.querySelector(`[aria-labelledby="${searchContentBy}"]`).classList.remove("show", "active");
    })
    tabToShow.classList.add("active");
    tabToShow.setAttribute("aria-selected", "true");
    let ariaToSearch = tabToShow.getAttribute("id");
    let content = document.querySelector(`[aria-labelledby="${ariaToSearch}"]`);
    content.classList.add("show", "active");
}

let firstTabLink = document.querySelector(".nav-link");
toggleTabVisibility(firstTabLink)

let tabs = document.querySelectorAll(".nav-link");
tabs.forEach(tab => {
    tab.addEventListener('click', (event) => {
        toggleTabVisibility(event.target);
    })
});