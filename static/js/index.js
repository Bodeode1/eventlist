/* * Modal Handling */
const selectAll = e =>document.querySelectorAll(e)
const selector = e => document.querySelector(e)
const modalCloser = selector(".modal-closer")
if(modalCloser){
    modalCloser.addEventListener("click", e => {
        const modalBox = selector(".modal")
        modalBox.setAttribute("class", "d-none")
    })
}
