// Invoke Functions Call on Document Loaded
document.addEventListener('DOMContentLoaded', function () {
  hljs.highlightAll();
});


let alertWrapper = document.querySelector('.alert')
let alertClose = document.querySelector('.alert__close')
console.log('loko');
if (alertWrapper) {
  console.log('click me');
  alertClose.addEventListener('click', () =>
    alertWrapper.style.display = 'none'
  )
}
