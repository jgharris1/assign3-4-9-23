window.addEventListener("load", link_events, false);

function link_events()
{
	document.getElementById("text_input").onkeydown = HelloWorld;
	document.getElementById("text_input").onclick = HelloWorld;
}

function HelloWorld()
{
	var str = document.getElementById("text_input").value;
	var location = document.getElementById("counter");
	var len = str.length;
	var newstr = len + "/256";
	location.innerHTML = newstr;
}

function message(user1, user2)
{
	var roomName = user1 + "__" + user2;
	window.location.pathname = '/chat/' + roomName + '/';
}




function pass_chng()
{
	var boxloc = document.getElementById("chng_pass");
	if(boxloc.style.display === "none")
	{
		boxloc.style.display = "block";
	}
	else
	{
		boxloc.style.display = "none";
	}
}

function edit_fun(id, method)
{
	if(method === 0)
	{
		var poststr = "post" + id;
		var editstr = "edit" + id;
	}
	else
	{
		var poststr = "postp" + id;
		var editstr = "editp" + id;
	}
	var postloc = document.getElementById(poststr);
	var editloc = document.getElementById(editstr);
	if(postloc.style.display === "none")
	{
		postloc.style.display = "block";
		editloc.style.display = "none";
	}
	else
	{
		postloc.style.display = "none";
		editloc.style.display = "block";
	}
	
}
