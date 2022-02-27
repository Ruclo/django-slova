  function handleDragStart(event) {
    event.dataTransfer.setData('text', event.target.id);
    //event.target.style.opacity = 1;
  }

  function allowDrop(event) {
      event.preventDefault();
  }

  function drop(event) {
    const id = event.dataTransfer.getData('text');
    const draggableElement = document.getElementById(id);
    const prevZone = draggableElement.parentElement;
    const dropzone = event.target.parentElement;
    //alert(prevZone.id);
    const firstChild = dropzone.firstChild;
    dropzone.replaceChild(draggableElement, dropzone.firstChild);
    prevZone.appendChild(firstChild);
    draggableElement.parentElement.style.borderLeftColor = '#8300fc';
    const parId = draggableElement.parentElement.id;
    const leftpair = document.getElementById('slovicko'+parId);
    leftpair.style.borderRightColor = '#8300fc';

    //draggableElement.style.opacity = 1.0;
    //
    //dropzone.firstChild.style.backgroundColor = 'white';
   // temp.replaceWith();


}

  function handleDragEnd(event) {

  }

  function odovzdat() {
    const inputy = document.getElementsByClassName('inputy');
    const odpovede = document.getElementsByClassName('diviky');
    for (var i = 0; i < inputy.length; i++) {
        inputy[i].value = odpovede[i].innerHTML;
    }
    document.getElementById('formularikspajanie').submit();

  }
