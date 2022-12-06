/* script.js */

function clickGo()
	{
	document.getElementById('go').onclick=function(){
		document.getElementById('infopane').style.display='block';
	};
	

document.getElementById('infopane').style.display = 'none';

document.getElementById('go').onclick=function(){
	document.getElementById('infopane').style.display='block';
};

document.getElementById('info').innerHTML = Date()