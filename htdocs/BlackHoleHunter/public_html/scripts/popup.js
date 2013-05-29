/*
function externalLinks() {
        if (!document.getElementsByTagName) return;
        var anchors = document.getElementsByTagName("a");
        for (var i=0; i<anchors.length; i++) {
                var anchor = anchors[i];
                if (anchor.getAttribute("href") &&
                anchor.getAttribute("rel") == "external")
                anchor.target = "_blank";
        }
        var anchors = document.getElementsByTagName("area");
        for (var i=0; i<anchors.length; i++) {
                var anchor = anchors[i];
                if (anchor.getAttribute("href")) 
                anchor.target = "_blank";
        }
}
window.onload = externalLinks;

function fensterOeffnen (Adresse) {
		neuesFenster = window.open(Adresse, "Zweitfenster", "width=800,height=600,left=100,top=200");
        neuesFenster.focus();
}

function openInfo(infobox) {
	document.getElementById (infobox).style.visibility = 'visible';
	document.getElementById (infobox).style.display = 'block';
	document.getElementById (infobox).style.width = '65%';
	document.getElementById (infobox).style.height = '25em';
	document.getElementById (infobox).style.backgroundColor = '#FEFDEB';
	document.getElementById (infobox).style.padding = '1em 1em 1em 1em';
	document.getElementById (infobox).style.position = 'absolute';
	document.getElementById (infobox).style.top = '30em';
	document.getElementById (infobox).style.left = '1em';
	document.getElementById (infobox).style.overflow = 'scroll';
}

function openInfo2(infobox2) {
	document.getElementById (infobox2).style.visibility = 'visible';
	document.getElementById (infobox2).style.display = 'block';
	document.getElementById (infobox2).style.width = '65%';
	document.getElementById (infobox2).style.height = '25em';
	document.getElementById (infobox2).style.backgroundColor = '#FEFDEB';
	document.getElementById (infobox2).style.padding = '1em 1em 1em 1em';
	document.getElementById (infobox2).style.position = 'absolute';
	document.getElementById (infobox2).style.top = '30em';
	document.getElementById (infobox2).style.left = '1em';
	document.getElementById (infobox2).style.overflow = 'scroll';
}
*/
function ShowThisHideRest(gravWellen){
	var alldivs = document.getElementsByTagName("div");
	for (i=0; i<alldivs.length; i++){
		if (alldivs[i].className=="infobox") alldivs[i].style.display = "none";
	}
	document.getElementById(gravWellen).style.display = "block";
	document.getElementById(gravWellen).style.width = '65%';
	document.getElementById(gravWellen).style.height = '45em';
	document.getElementById(gravWellen).style.backgroundColor = '#FEFDEB';
	document.getElementById(gravWellen).style.padding = '1em 1em 1em 1em';
	document.getElementById(gravWellen).style.position = 'absolute';
	document.getElementById(gravWellen).style.top = '30em';
	document.getElementById(gravWellen).style.left = '1em';
	document.getElementById(gravWellen).style.overflow = 'scroll';
	document.getElementById(gravWellen).style.border = "1px solid #000000";
}
