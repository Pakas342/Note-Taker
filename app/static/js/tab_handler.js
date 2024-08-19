// Add the show now class to the first tab 
function toggleTabVisibility(tab) {
    tab.classList.add("active");
    tab.setAttribute("aria-selected", "true");
    let attributeToSearch = tab.getAttribute("id");
    console.log(attributeToSearch)
    let content = document.querySelector(`[aria-labelledby="${attributeToSearch}"]`);;
    content.classList.add("show", "active");
}

let firstTabLink = document.querySelector(".nav-link");
toggleTabVisibility(firstTabLink)

