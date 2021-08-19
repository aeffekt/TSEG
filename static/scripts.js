//código javascript para TSEG 2021, 

//validacion login
function validate()
{	
	var form = document.getElementById("login");
	if(!form.name.value)
	{
		alert("Debe ingresar un nombre");
		return false;
	}
	else if(!form.password.value)
	{
		alert("Debe ingresar contraseña");
		return false;
	}
	else if(form.name.value=="admin" && form.password.value=="admin"){
		alert("login correcto");
		return false;	
	}
}