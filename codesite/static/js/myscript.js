
function enviardados(){

  if (document.dados.name.value == "")
    {
    alert('Campo nome não pode estar vazio')
    document.dados.name.focus();
    return false;
    }

    if (document.dados.email.value == "" || document.dados.email.value.indexOf('@') == -1)
    {
    alert('O Email deve ser preenchido Corretamente')
    document.dados.email.focus();
    return false;
    }
      
    if (document.dados.textoarea.value == "")
    {
    alert('A mensagem não pode estar vazia')
    document.dados.textoarea.focus();
    return false;
    }

  return true;

  if (document.dados == true || document.button == onclick())
  {
    alert('ok')

  }
}